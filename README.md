<h1 align="center">
  <br>
  <a href="#"><img src="https://via.placeholder.com/200x200/000000/00ffea?text=GV" alt="Guardian Vision" width="200"></a>
  <br>
  Guardian Vision
  <br>
</h1>

<h4 align="center">A real-time crowd detection and monitoring system with a cyberpunk-themed HUD interface built on top of <a href="https://www.python.org/" target="_blank">Python</a> and <a href="https://pyqt.info/" target="_blank">PyQt5</a>.</h4>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg"
         alt="Python Version">
  </a>
  <a href="https://github.com/microsoft/onnxruntime">
    <img src="https://img.shields.io/badge/ONNX-Runtime-orange.svg">
  </a>
  <a href="https://opencv.org/">
      <img src="https://img.shields.io/badge/OpenCV-4.0+-green.svg">
  </a>
  <a href="https://pyqt.info/">
    <img src="https://img.shields.io/badge/PyQt5-5.15+-red.svg">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#installation">Installation</a> •
  <a href="#system-requirements">System Requirements</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://via.placeholder.com/800x600/000000/00ffea?text=Guardian+Vision+HUD)

## Key Features

* **Real-time Crowd Detection** - Advanced ONNX model inference for accurate person detection
  - High-performance computer vision processing with customizable confidence thresholds
* **Cyberpunk HUD Interface** - Futuristic neon-themed user interface
  - Frameless window design with custom title bar and draggable interface
* **Live Video Feed** - Real-time webcam integration with pulsing detection boxes
  - Dynamic visual feedback with animated bounding boxes and safety alerts
* **Multi-tab Dashboard** 
  - Live Feed: Real-time detection with side panel statistics
  - Settings: Configurable danger thresholds and model switching
  - Graph: Historical crowd density visualization with CSV export
* **Intelligent Safety System** - Configurable danger threshold alerts
  - Automatic safety warnings when crowd density exceeds set limits
* **Data Logging & Visualization**
  - Real-time graph plotting of crowd density over time
  - CSV export functionality for data analysis
* **Model Flexibility** - Support for custom ONNX models
  - Easy model switching through file dialog interface
* **Performance Optimized**
  - Threaded model inference with mutex locks for thread safety
  - Efficient frame processing with configurable update rates

## How To Use

To clone and run this application, you'll need [Python 3.7+](https://www.python.org/downloads/) and the required dependencies installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/yourusername/guardian-vision

# Go into the repository
$ cd guardian-vision

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python main.py
```

> **Note**
> Make sure you have a webcam connected and an ONNX model file ready. The default model path is set to `b1.onnx` in the project directory.

## Installation

### Prerequisites

- Python 3.7 or higher
- Webcam or video input device
- ONNX model file for person detection

### Required Dependencies

```bash
pip install PyQt5
pip install opencv-python
pip install onnxruntime
pip install matplotlib
pip install numpy
```

### Quick Setup

1. **Download or train an ONNX model** for person detection
2. **Place the model file** in your project directory
3. **Update the model path** in `app.py` if necessary:
   ```python
   current_model_path = r"path/to/your/model.onnx"
   ```
4. **Run the application**:
   ```bash
   python main.py
   ```

## System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.14, or Linux (Ubuntu 18.04+)
- **Python**: 3.7+
- **RAM**: 4GB
- **CPU**: Intel i5 or equivalent
- **Webcam**: Any USB webcam or built-in camera

### Recommended Requirements
- **RAM**: 8GB or more
- **CPU**: Intel i7 or equivalent with multiple cores
- **GPU**: NVIDIA GPU with CUDA support (for faster inference)

## Configuration

### Model Configuration
- Modify `current_model_path` in `app.py` to point to your ONNX model
- Adjust detection parameters in `processing.py`:
  - `conf_threshold`: Confidence threshold for detections (default: 0.3)
  - `iou_threshold`: IoU threshold for Non-Maximum Suppression (default: 0.5)
  - `input_width`, `input_height`: Model input dimensions (default: 512x512)

### UI Customization
- Danger threshold can be adjusted in the Settings tab
- Window size is set to 1440x900 (modifiable in `app.py`)
- Color scheme uses neon cyan (#00ffea) and can be customized in the stylesheet sections

### Data Export
- Detection counts are automatically saved to `crowd_counts.csv`
- Graph data includes timestamps and crowd counts for analysis

## Architecture

The project is structured with modular components:

- **`app.py`**: Main application with PyQt5 GUI and webcam integration
- **`model.py`**: ONNX model loading and inference management
- **`processing.py`**: Image preprocessing and post-processing pipeline
- **`visuals.py`**: Custom bounding box rendering with cyberpunk aesthetics
- **`graph.py`**: Real-time data visualization and CSV logging
- **`widgets.py`**: Custom UI components including draggable title bar
- **`main.py`**: Application entry point

## Credits

This software uses the following open source packages:

- [PyQt5](https://pyqt.info/) - Cross-platform GUI toolkit
- [OpenCV](https://opencv.org/) - Computer vision library
- [ONNX Runtime](https://github.com/microsoft/onnxruntime) - High-performance ML inference
- [Matplotlib](https://matplotlib.org/) - Data visualization library
- [NumPy](https://numpy.org/) - Numerical computing library

## Related

- [YOLO Object Detection](https://github.com/ultralytics/yolov5) - Popular object detection framework
- [OpenVINO](https://github.com/openvinotoolkit/openvino) - Alternative inference engine

## Support

If you find this project useful for crowd monitoring, security applications, or computer vision research, consider starring the repository!

## You may also like...

- [Real-time Face Recognition](https://github.com/example/face-recognition) - Face detection and recognition system
- [Security Camera AI](https://github.com/example/security-ai) - AI-powered security monitoring

## License

MIT

---

> **Guardian Vision** - Real-time crowd detection for safer environments
> GitHub saranyan18 (https://github.com/yourusername) &nbsp;&middot;&nbsp;
> Built with ❤️ and cutting-edge AI technology
