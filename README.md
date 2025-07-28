<p align="center">
<pre>
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
</p>


# 🛡️ Guardian Vision

<div align="center">
  
  **A cutting-edge real-time crowd detection and monitoring system with a cyberpunk-themed HUD interface**
  
  *Powered by Python, PyQt5, and advanced AI detection models*

  <br>

  ![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
  ![ONNX Runtime](https://img.shields.io/badge/ONNX-Runtime-orange.svg?style=for-the-badge)
  ![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg?style=for-the-badge&logo=opencv&logoColor=white)
  ![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-red.svg?style=for-the-badge)
  ![License](https://img.shields.io/badge/license-MIT-purple.svg?style=for-the-badge)

  <br>

  [🚀 **Quick Start**](#-quick-start) • 
  [✨ **Features**](#-key-features) • 
  [⚙️ **Installation**](#%EF%B8%8F-installation) • 
  [🎯 **Configuration**](#-configuration) • 
  [📊 **Architecture**](#-architecture)

  <br>

</div>

---

## 🌟 Why Guardian Vision?

Guardian Vision transforms ordinary security monitoring into an advanced AI-powered surveillance system. Whether you're managing public spaces, monitoring events, or enhancing security protocols, our cyberpunk-themed interface makes crowd detection both powerful and visually stunning.

## ✨ Key Features

### 🎯 **Advanced Detection Engine**
- **Real-time Crowd Detection** with high-performance ONNX model inference
- **Customizable Confidence Thresholds** for precision tuning
- **Multi-threaded Processing** with mutex locks for optimal performance

### 🎨 **Cyberpunk HUD Interface**
- **Futuristic Neon Design** with animated visual elements
- **Frameless Window** with custom draggable title bar
- **Pulsing Detection Boxes** for dynamic visual feedback

### 📊 **Smart Dashboard System**
- **Live Feed Tab**: Real-time detection with comprehensive statistics
- **Settings Panel**: Configurable danger thresholds and model switching
- **Analytics Graph**: Historical crowd density with CSV export capabilities

### 🚨 **Intelligent Safety Features**
- **Automated Alert System** when crowd density exceeds safety limits
- **Real-time Notifications** with visual and audio warnings
- **Customizable Danger Thresholds** for different environments

### 📈 **Data Analytics & Export**
- **Live Graph Plotting** of crowd density over time
- **CSV Export Functionality** for detailed analysis
- **Historical Data Tracking** with timestamp logging

---

## 🚀 Quick Start

Get Guardian Vision running in under 5 minutes:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/saranyan18/guardian-vision.git

# 2️⃣ Navigate to project directory
cd guardian-vision

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Launch Guardian Vision
python main.py
```

> 💡 **Pro Tip**: Ensure your webcam is connected and you have an ONNX model file ready before launching!

---

## ⚙️ Installation

### 📋 Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.7+ | Core runtime |
| **Webcam** | Any USB/Built-in | Video input |
| **ONNX Model** | Person detection | AI inference |

### 🔧 Dependency Installation

```bash
# Core GUI and Computer Vision
pip install PyQt5 opencv-python

# AI Inference Engine
pip install onnxruntime

# Data Visualization and Processing
pip install matplotlib numpy
```

### 🎯 Quick Setup Guide

1. **📥 Download ONNX Model**
   ```bash
   # Place your person detection model in the project directory
   # Default expected: b1.onnx
   ```

2. **🔧 Configure Model Path**
   ```python
   # In app.py, update the model path:
   current_model_path = r"path/to/your/model.onnx"
   ```

3. **🚀 Launch Application**
   ```bash
   python main.py
   ```

---

## 💻 System Requirements

<table>
<tr>
<td valign="top">

### Minimum Specs
- **OS**: Windows 10 / macOS 10.14 / Ubuntu 18.04+
- **Python**: 3.7+
- **RAM**: 4GB
- **CPU**: Intel i5 equivalent
- **Camera**: Any USB webcam

</td>
<td valign="top">

### Recommended Specs
- **RAM**: 8GB+
- **CPU**: Intel i7+ (multi-core)
- **GPU**: NVIDIA CUDA-compatible
- **Storage**: 2GB free space
- **Internet**: For model downloads

</td>
</tr>
</table>

---

## 🎯 Configuration

### 🤖 AI Model Settings
```python
# Detection Parameters (processing.py)
conf_threshold = 0.3    # Confidence threshold
iou_threshold = 0.5     # IoU threshold for NMS
input_width = 512       # Model input width
input_height = 512      # Model input height
```

### 🎨 UI Customization
- **Danger Threshold**: Adjustable via Settings tab
- **Window Size**: 1440x900 (customizable in `app.py`)
- **Color Scheme**: Neon cyan (`#00ffea`) theme
- **Animation Speed**: Configurable pulsing effects

### 📊 Data Export
- **Auto-save**: Detection counts → `crowd_counts.csv`
- **Graph Export**: Timestamps + crowd density data
- **Real-time Logging**: Continuous data capture

---

## 🏗️ Architecture

Guardian Vision is built with a modular, scalable architecture:

```
📁 guardian-vision/
├── 🎮 main.py          # Application entry point
├── 🖥️ app.py           # Main GUI & webcam integration
├── 🧠 model.py         # ONNX model management
├── 🔄 processing.py    # Image preprocessing pipeline
├── 🎨 visuals.py       # Cyberpunk bounding box rendering
├── 📊 graph.py         # Real-time data visualization
├── 🧩 widgets.py       # Custom UI components
└── 📋 requirements.txt # Dependencies
```

### 🔧 Core Components

| Component | Responsibility | Key Features |
|-----------|---------------|--------------|
| **App** | Main application logic | PyQt5 GUI, webcam integration |
| **Model** | AI inference | ONNX runtime, model loading |
| **Processing** | Image pipeline | Preprocessing, post-processing |
| **Visuals** | UI rendering | Custom bounding boxes, animations |
| **Graph** | Data analytics | Real-time plotting, CSV export |

---

## 🛠️ Built With

<div align="center">

| Technology | Purpose | Version |
|------------|---------|---------|
| **PyQt5** | Cross-platform GUI Framework | 5.15+ |
| **OpenCV** | Computer Vision & Image Processing | 4.0+ |
| **ONNX Runtime** | High-performance ML Inference | Latest |
| **Matplotlib** | Data Visualization & Plotting | Latest |
| **NumPy** | Numerical Computing & Arrays | Latest |

</div>

---

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **💾 Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **📤 Push** to the branch (`git push origin feature/AmazingFeature`)
5. **🔄 Open** a Pull Request

---

## 🐛 Issues & Support

Found a bug or need help? We're here for you!

- 🐛 **Bug Reports**: [Open an issue](https://github.com/saranyan18/guardian-vision/issues)
- 💡 **Feature Requests**: [Request a feature](https://github.com/saranyan18/guardian-vision/issues)
- 📧 **Direct Support**: Contact the maintainer

---

## 🎯 Roadmap

- [ ] 🔄 Real-time model switching
- [ ] 📱 Mobile app companion
- [ ] ☁️ Cloud integration
- [ ] 🎵 Audio alerts system
- [ ] 📧 Email notifications
- [ ] 🌐 Web dashboard
- [ ] 🔐 Multi-user authentication

---

## 🌟 Related Projects

- **[Real-time Face Recognition](https://github.com/example/face-recognition)** - Advanced facial detection system
- **[Security Camera AI](https://github.com/example/security-ai)** - Comprehensive security monitoring
- **[YOLO Object Detection](https://github.com/ultralytics/yolov5)** - Popular object detection framework

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ Show Your Support

If Guardian Vision helps secure your environment, please consider giving it a star!

**Made with ❤️ by [Saranyan](https://github.com/saranyan18)**

*Transforming security monitoring with cutting-edge AI*

---

[![GitHub stars](https://img.shields.io/github/stars/saranyan18/guardian-vision?style=social)](https://github.com/saranyan18/guardian-vision/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/saranyan18/guardian-vision?style=social)](https://github.com/saranyan18/guardian-vision/network)
[![GitHub issues](https://img.shields.io/github/issues/saranyan18/guardian-vision)](https://github.com/saranyan18/guardian-vision/issues)

</div>
