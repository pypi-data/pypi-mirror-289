## 切片推理

此代码 Fork [obss/sahi](https://github.com/obss/sahi), 添加如下功能
- 添加rknn支持
```python
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8rknn',
    model_path=yolov8_onnx_model_path,
    confidence_threshold=0.3,
    category_mapping=category_mapping,
    device="cpu", # or 'cuda:0'
)
```
- 添加yolov10 导出 onnx 支持
```python
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov10onnx',
    model_path=yolov8_onnx_model_path,
    confidence_threshold=0.3,
    category_mapping=category_mapping,
)
```
- 添加参数 EP_LIST, 使用onnx推理时直接传递
```python
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov10onnx',
    model_path=yolov8_onnx_model_path,
    confidence_threshold=0.3,
    category_mapping=category_mapping,
    ep_list=['CUDAExecutionProvider', 'CPUExecutionProvider']
)
```