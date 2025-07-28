<h1 align="center">
  <br>
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guardian Vision Animated Logo</title>
    <style>
        body {
            background: #000;
            color: #00ffea;
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        .logo-container {
            text-align: center;
            margin: 20px 0;
        }

        /* Version 1: Glowing Pulse */
        .glow-pulse {
            animation: glowPulse 2s ease-in-out infinite;
            text-shadow: 0 0 10px #00ffea, 0 0 20px #00ffea, 0 0 30px #00ffea;
        }

        @keyframes glowPulse {
            0%, 100% { 
                text-shadow: 0 0 10px #00ffea, 0 0 20px #00ffea, 0 0 30px #00ffea;
                opacity: 1;
            }
            50% { 
                text-shadow: 0 0 20px #00ffea, 0 0 30px #00ffea, 0 0 40px #00ffea, 0 0 50px #00ffea;
                opacity: 0.8;
            }
        }

        /* Version 2: Typewriter Effect */
        .typewriter {
            overflow: hidden;
            border-right: 3px solid #00ffea;
            white-space: nowrap;
            animation: typing 4s steps(40, end), blink-caret 0.75s step-end infinite;
        }

        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: #00ffea }
        }

        /* Version 3: Matrix Rain Effect */
        .matrix-rain {
            position: relative;
            overflow: hidden;
        }

        .matrix-rain::before {
            content: '';
            position: absolute;
            top: -100%;
            left: 0;
            width: 100%;
            height: 200%;
            background: linear-gradient(transparent, #00ffea, transparent);
            animation: matrixRain 3s linear infinite;
            opacity: 0.3;
        }

        @keyframes matrixRain {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(100%); }
        }

        /* Version 4: Scan Line Effect */
        .scan-line {
            position: relative;
            overflow: hidden;
        }

        .scan-line::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: #00ffea;
            box-shadow: 0 0 10px #00ffea;
            animation: scanLine 3s linear infinite;
        }

        @keyframes scanLine {
            0% { transform: translateY(-10px); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(400px); opacity: 0; }
        }

        /* Version 5: Flicker Effect */
        .flicker {
            animation: flicker 0.15s infinite linear alternate;
        }

        @keyframes flicker {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }

        .title {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            animation: titleGlow 2s ease-in-out infinite alternate;
        }

        @keyframes titleGlow {
            0% { 
                text-shadow: 0 0 5px #00ffea;
                color: #00ffea;
            }
            100% { 
                text-shadow: 0 0 15px #00ffea, 0 0 25px #00ffea;
                color: #ffffff;
            }
        }

        pre {
            font-size: 12px;
            line-height: 1;
            margin: 0;
        }

        .separator {
            width: 80%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00ffea, transparent);
            margin: 30px 0;
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .demo-label {
            color: #00ffea;
            font-size: 18px;
            margin: 20px 0 10px 0;
            text-shadow: 0 0 10px #00ffea;
        }
    </style>
</head>
<body>
    <div class="demo-label">Version 1: Glowing Pulse</div>
    <div class="logo-container">
        <pre class="glow-pulse">
   ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ █████╗ ███╗   ██╗
  ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║
  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║██║███████║██╔██╗ ██║
  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██║██╔══██║██║╚██╗██║
  ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║
   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                    ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
                    ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
                    ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
                    ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
                     ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
                      ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        </pre>
        <div class="title">Guardian Vision</div>
    </div>

    <div class="separator"></div>

    <div class="demo-label">Version 2: Scan Line Effect</div>
    <div class="logo-container">
        <pre class="scan-line">
   ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ █████╗ ███╗   ██╗
  ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║
  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║██║███████║██╔██╗ ██║
  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██║██╔══██║██║╚██╗██║
  ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║
   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                    ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
                    ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
                    ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
                    ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
                     ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
                      ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        </pre>
        <div class="title">Guardian Vision</div>
    </div>

    <div class="separator"></div>

    <div class="demo-label">Version 3: Matrix Rain Effect</div>
    <div class="logo-container">
        <pre class="matrix-rain">
   ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ █████╗ ███╗   ██╗
  ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║
  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║██║███████║██╔██╗ ██║
  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██║██╔══██║██║╚██╗██║
  ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║
   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                    ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
                    ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
                    ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
                    ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
                     ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
                      ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        </pre>
        <div class="title">Guardian Vision</div>
    </div>

    <div class="separator"></div>

    <div class="demo-label">Version 4: Subtle Flicker</div>  
    <div class="logo-container">
        <pre class="flicker">
   ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ █████╗ ███╗   ██╗
  ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║
  ██║  ███╗██║   ██║███████║██████╔╝██║  ██║██║███████║██╔██╗ ██║
  ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██║██╔══██║██║╚██╗██║
  ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║
   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                    ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
                    ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
                    ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
                    ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
                     ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
                      ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        </pre>
        <div class="title">Guardian Vision</div>
    </div>
</body>
</html>
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
> GitHub saranyan18 (https://github.com/saranyan18)) &nbsp;&middot;&nbsp;
> Built with ❤️ and cutting-edge AI technology
