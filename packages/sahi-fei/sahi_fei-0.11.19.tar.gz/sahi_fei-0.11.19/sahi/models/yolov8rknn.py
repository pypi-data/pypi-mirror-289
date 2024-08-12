# OBSS SAHI Tool
# Code written by Karl-Joan Alesma and Michael García, 2023.

import logging
from typing import Any, Dict, List, Optional, Tuple

import cv2
import numpy as np
import torch

logger = logging.getLogger(__name__)

from sahi.models.base import DetectionModel
from sahi.prediction import ObjectPrediction
from sahi.utils.compatibility import fix_full_shape_list, fix_shift_amount_list
from sahi.utils.import_utils import check_requirements
from sahi.utils.yolov8rknn import post_process
from sahi.utils.rknn_utils import COCO_test_helper
from sahi.utils.yolov8onnx import non_max_supression


class Yolov8RknnDetectionModel(DetectionModel):
    def __init__(self, *args, iou_threshold: float = 0.7, **kwargs):
        """
        Args:
            iou_threshold: float
                IOU threshold for non-max supression, defaults to 0.7.
        """
        super().__init__(*args, **kwargs)
        self.iou_threshold = iou_threshold

    def check_dependencies(self) -> None:
        check_requirements(["rknn-toolkit-lite2"])

    def load_model(self, ort_session_kwargs: Optional[dict] = {}) -> None:
        """Detection model is initialized and set to self.model.

        Options for RKNNLite sessions can be passed as keyword arguments.
        """
        from rknnlite.api import RKNNLite

        try:
            # 创建RKNN对象
            rknn_lite = RKNNLite(verbose=False)

            # 加载RKNN模型
            logging.info('--> Load RKNN model')
            ret = rknn_lite.load_rknn(self.model_path)
            if ret != 0:
                logging.info('Load RKNN model failed')
                exit(ret)
            logging.info('done')

            # 初始化 runtime 环境
            logging.info('--> Init runtime environment')
            # run on RK356x/RK3588 with Debian OS, do not need specify target.
            ret = rknn_lite.init_runtime(core_mask=RKNNLite.NPU_CORE_0_1_2)
            if ret != 0:
                logging.info('Init runtime environment failed!')
                exit(ret)
            logging.info('done')

            self.set_model(rknn_lite)

        except Exception as e:
            raise TypeError("model_path is not a valid rknn model path: ", e)

    def set_model(self, model: Any) -> None:
        """
        Sets the underlying rknn model.

        Args:
            model: Any
                A rknn model
        """

        self.model = model

        # set category_mapping
        if not self.category_mapping:
            raise TypeError("Category mapping values are required")

    def _preprocess_image(self, image: np.ndarray, input_shape: Tuple[int, int]) -> np.ndarray:
        """Prepapre image for inference by resizing, normalizing and changing dimensions.

        Args:
            image: np.ndarray
                Input image with color channel order RGB.
        """
        input_image = cv2.resize(image, input_shape)

        input_image = input_image / 255.0
        input_image = input_image.transpose(2, 0, 1)
        image_tensor = input_image[np.newaxis, :, :, :].astype(np.float32)

        return image_tensor

    def _post_process(self, outputs: np.ndarray) -> List[torch.Tensor]:

        boxes, classes, scores = post_process(outputs)
        # Format the results
        prediction_result = []

        if boxes is not None and len(boxes) > 0:
            indices = non_max_supression(boxes, scores, self.iou_threshold)
            boxes = boxes.round().astype(np.int32)

            for bbox, score, label in zip(boxes[indices], scores[indices], classes[indices]):
                bbox = bbox.tolist()
                cls_id = int(label)

                if score >= self.iou_threshold:
                    prediction_result.append([bbox[0], bbox[1], bbox[2], bbox[3], score, cls_id])

        prediction_result = [torch.tensor(prediction_result)]
        # prediction_result = [prediction_result]

        return prediction_result

    def perform_inference(self, image: np.ndarray):
        """
        Prediction is performed using self.model and the prediction result is set to self._original_predictions.
        Args:
            image: np.ndarray
                A numpy array that contains the image to be predicted. 3 channel image should be in RGB order.
        """

        # Confirm model is loaded
        if self.model is None:
            raise ValueError("Model is not loaded, load it by calling .load_model()")

        image_shape = image.shape[:2]
        co_helper = COCO_test_helper(enable_letter_box=True)

        img = co_helper.letter_box(im=image, new_shape=image_shape, pad_color=(0, 0, 0))
        inputs = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        outputs = self.model.inference(inputs=[inputs])
        self._original_predictions = self._post_process(outputs)

    @property
    def category_names(self):
        return list(self.category_mapping.values())

    @property
    def num_categories(self):
        """
        Returns number of categories
        """
        return len(self.category_mapping)

    @property
    def has_mask(self):
        """
        Returns if model output contains segmentation mask
        """
        return False

    def _create_object_prediction_list_from_original_predictions(
            self,
            shift_amount_list: Optional[List[List[int]]] = [[0, 0]],
            full_shape_list: Optional[List[List[int]]] = None,
    ):
        """
        self._original_predictions is converted to a list of prediction.ObjectPrediction and set to
        self._object_prediction_list_per_image.
        Args:
            shift_amount_list: list of list
                To shift the box and mask predictions from sliced image to full sized image, should
                be in the form of List[[shift_x, shift_y],[shift_x, shift_y],...]
            full_shape_list: list of list
                Size of the full image after shifting, should be in the form of
                List[[height, width],[height, width],...]
        """
        """
        self._original_predictions is converted to a list of prediction.ObjectPrediction and set to
        self._object_prediction_list_per_image.
        Args:
            shift_amount_list: list of list
                To shift the box and mask predictions from sliced image to full sized image, should
                be in the form of List[[shift_x, shift_y],[shift_x, shift_y],...]
            full_shape_list: list of list
                Size of the full image after shifting, should be in the form of
                List[[height, width],[height, width],...]
        """
        original_predictions = self._original_predictions

        # compatilibty for sahi v0.8.15
        shift_amount_list = fix_shift_amount_list(shift_amount_list)
        full_shape_list = fix_full_shape_list(full_shape_list)

        # handle all predictions
        object_prediction_list_per_image = []
        for image_ind, image_predictions_in_xyxy_format in enumerate(original_predictions):
            shift_amount = shift_amount_list[image_ind]
            full_shape = None if full_shape_list is None else full_shape_list[image_ind]
            object_prediction_list = []

            # process predictions
            for prediction in image_predictions_in_xyxy_format.cpu().detach().numpy():
                x1 = prediction[0]
                y1 = prediction[1]
                x2 = prediction[2]
                y2 = prediction[3]
                bbox = [x1, y1, x2, y2]
                score = prediction[4]
                category_id = int(prediction[5])
                category_name = self.category_mapping[str(category_id)]

                # fix negative box coords
                bbox[0] = max(0, bbox[0])
                bbox[1] = max(0, bbox[1])
                bbox[2] = max(0, bbox[2])
                bbox[3] = max(0, bbox[3])

                # fix out of image box coords
                if full_shape is not None:
                    bbox[0] = min(full_shape[1], bbox[0])
                    bbox[1] = min(full_shape[0], bbox[1])
                    bbox[2] = min(full_shape[1], bbox[2])
                    bbox[3] = min(full_shape[0], bbox[3])

                # ignore invalid predictions
                if not (bbox[0] < bbox[2]) or not (bbox[1] < bbox[3]):
                    logger.warning(f"ignoring invalid prediction with bbox: {bbox}")
                    continue

                object_prediction = ObjectPrediction(
                    bbox=bbox,
                    category_id=category_id,
                    score=score,
                    segmentation=None,
                    category_name=category_name,
                    shift_amount=shift_amount,
                    full_shape=full_shape,
                )
                object_prediction_list.append(object_prediction)
            object_prediction_list_per_image.append(object_prediction_list)

        self._object_prediction_list_per_image = object_prediction_list_per_image
