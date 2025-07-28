import cv2
import math
import sys
import time
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QFileDialog,
    QHBoxLayout, QVBoxLayout, QApplication, QTabWidget,
    QSpinBox, QFormLayout
)
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtCore import QTimer, Qt
from model import load_model, run_inference
from processing import preprocess, postprocess
from visuals import fancy_box
from graph import GraphWidget
from widgets import TitleBar

current_model_path = r"C:\Users\siron\OneDrive\Desktop\projects\guardian vision\b1.onnx"


class WebcamApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(1440,900)  # Increased window size
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)

        self.danger_threshold = 5  # Default threshold

        # Title bar
        self.title_bar = TitleBar(self)

        # Tabs with consistent neon/dark theme
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #00ffea;
                background: #000000;
                border-radius: 8px;
                margin: 0px;
            }
            QTabBar::tab {
                background: #111111;
                color: #00ffea;
                font-family: 'OCR A Extended';
                font-size: 16px;
                border: 1px solid #00ffea;
                border-bottom: none;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                min-width: 140px;
                min-height: 36px;
                margin-right: 2px;
                padding: 6px 18px;
            }
            QTabBar::tab:selected, QTabBar::tab:hover {
                background: #00ffea;
                color: #000000;
                font-weight: bold;
                border: 2px solid #00ffea;
            }
            QTabBar::tab:!selected {
                margin-top: 2px;
            }
        """)
        self.live_tab = self.create_live_tab()
        self.settings_tab = self.create_settings_tab()
        self.graph_tab = self.create_graph_tab()
        self.tabs.addTab(self.live_tab, "Live Feed")
        self.tabs.addTab(self.settings_tab, "Settings")
        self.tabs.addTab(self.graph_tab, "Graph")

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(self.tabs)

        # Video capture + timer
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.pulse_frame = 0
        load_model(current_model_path)

        self.tabs.currentChanged.connect(self.on_tab_changed)
        self.graph_tab_index = self.tabs.indexOf(self.graph_tab)
        self._graph_active = False

    def create_live_tab(self):
        live_tab = QWidget()
        layout = QVBoxLayout(live_tab)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Video + overlays container
        container = QWidget(live_tab)
        container.setFixedSize(1180, 750)
        container.setStyleSheet("background-color: #000000;")
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        # Video feed
        self.image_label = QLabel(container)
        self.image_label.setGeometry(0, 0, 900, 750)
        self.image_label.setScaledContents(True)
        self.image_label.setStyleSheet("border: 2px solid #00ffea;")
        container_layout.addWidget(self.image_label)

        # Side panel
        side_panel = QWidget(container)
        side_panel.setFixedSize(260, 750)
        side_panel.setStyleSheet("background-color: #000000; border: 2px solid #00ffea;")
        side_layout = QVBoxLayout(side_panel)
        side_layout.setContentsMargins(10, 10, 10, 10)
        side_layout.setSpacing(10)

        # Time display
        self.time_label = QLabel("Time: 00:00:00", side_panel)
        self.time_label.setFont(QFont("OCR A Extended", 13))
        self.time_label.setStyleSheet("""
            color: #00ffea;
            background-color: rgba(0, 0, 0, 150);
            border: 1px solid #00ffea;
            border-radius: 8px;
            padding: 8px;
        """)
        self.time_label.setFixedHeight(38)
        side_layout.addWidget(self.time_label)

        # Target/Location display
        self.location_label_panel = QLabel("Target: NIL", side_panel)
        self.location_label_panel.setFont(QFont("OCR A Extended", 13))
        self.location_label_panel.setStyleSheet("""
            color: #00ffea;
            background-color: rgba(0, 0, 0, 150);
            border: 1px solid #00ffea;
            border-radius: 8px;
            padding: 8px 12px;
        """)
        self.location_label_panel.setFixedHeight(38)
        side_layout.addWidget(self.location_label_panel)

        # Detection Logger
        self.detection_logger = QLabel("Live: 0", side_panel)
        self.detection_logger.setFont(QFont("OCR A Extended", 13))
        self.detection_logger.setStyleSheet("""
            color: #00ff00;
            background-color: rgba(0, 0, 0, 150);
            border: 1px solid #00ff00;
            border-radius: 8px;
            padding: 8px 12px;
        """)
        self.detection_logger.setFixedHeight(38)
        side_layout.addWidget(self.detection_logger)

        side_layout.addStretch()
        container_layout.addWidget(side_panel)

        layout.addWidget(container)

        # Safety Alert Label (initially hidden, positioned lower)
        self.safety_label = QLabel("", live_tab)
        self.safety_label.setFont(QFont("OCR A Extended", 18))
        self.safety_label.setStyleSheet("""
            QLabel {
                color: #ff0000;
                background-color: rgba(255, 0, 0, 80);
                border: 3px solid #ff0000;
                border-radius: 10px;
                padding: 8px 12px;
            }
        """)
        self.safety_label.setFixedSize(260, 50)
        self.safety_label.move(470, 700)
        self.safety_label.hide()

        # Detection Count Label (bottom-left)
        self.log_label = QLabel("Total: 0", live_tab)
        self.log_label.setFont(QFont("OCR A Extended", 13))
        self.log_label.setStyleSheet("""
            color: #00ffea;
            background-color: rgba(0, 0, 0, 150);
            border: 1px solid #00ffea;
            border-radius: 8px;
            padding: 8px 12px;
        """)
        self.log_label.setFixedSize(220, 38)
        self.log_label.move(20, 700)

        # Switch Model Button (bottom right)
        self.switch_button = QPushButton("⟳", live_tab)
        self.switch_button.setFont(QFont("OCR A Extended", 22))
        self.switch_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 150);
                color: #00ffea;
                border: 2px solid #00ffea;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgba(0, 255, 255, 120);
                color: #000000;
            }
        """)
        self.switch_button.setFixedSize(80, 60)
        self.switch_button.move(1080, 700)
        self.switch_button.clicked.connect(self.switch_model)

        # Add overlays to live_tab
        self.safety_label.setParent(live_tab)
        self.log_label.setParent(live_tab)
        self.switch_button.setParent(live_tab)

        return live_tab

    def create_settings_tab(self):
        settings_tab = QWidget()
        layout = QFormLayout(settings_tab)

        # Danger threshold input
        threshold_spin = QSpinBox()
        threshold_spin.setRange(1, 50)
        threshold_spin.setValue(self.danger_threshold)
        threshold_spin.setStyleSheet("""
            background-color: #111111;
            color: #00ffea;
            border: 1px solid #00ffea;
            border-radius: 8px;
            padding: 6px 10px;
        """)
        threshold_spin.valueChanged.connect(self.update_danger_threshold)
        layout.addRow("Danger Threshold:", threshold_spin)

        # Switch Model button
        switch_btn = QPushButton("Switch Model")
        switch_btn.setStyleSheet("""
            background-color: #111111;
            color: #00ffea;
            border: 1px solid #00ffea;
            border-radius: 8px;
            padding: 6px 10px;
        """)
        switch_btn.clicked.connect(self.switch_model)
        layout.addRow(switch_btn)

        return settings_tab

    def create_graph_tab(self):
        graph_tab = QWidget()
        layout = QVBoxLayout(graph_tab)
        self.graph_widget = GraphWidget()
        layout.addWidget(self.graph_widget)
        return graph_tab

    def update_danger_threshold(self, value):
        self.danger_threshold = value

    def switch_model(self):
        model_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select ONNX Model",
            "",
            "ONNX Files (*.onnx)"
        )
        if model_path:
            global current_model_path
            current_model_path = model_path
            load_model(current_model_path)
            print(f"Switched to model: {current_model_path}")

    def on_tab_changed(self, idx):
        self._graph_active = (idx == self.graph_tab_index)
        if self._graph_active and hasattr(self, "graph_widget"):
            self.graph_widget.redraw()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        img = cv2.flip(frame, 1)
        input_tensor = preprocess(img)
        outputs = run_inference(input_tensor)
        boxes, scores = postprocess(outputs, img.shape)

        # Update detection count (in side panel and bottom left)
        num_detections = len(boxes)
        self.log_label.setText(f"Total: {num_detections}")
        self.detection_logger.setText(f"Live: {num_detections}")

        # Update time (now inside side panel)
        current_time = time.strftime("%H:%M:%S")
        self.time_label.setText(f"Time: {current_time}")

        # Safety check: trigger DANGER when number of detections exceeds threshold
        if num_detections >= self.danger_threshold:
            self.safety_label.setText("DANGER!")
            self.safety_label.show()
        else:
            self.safety_label.hide()

        # Pulsing bounding boxes
        self.pulse_frame += 1
        pulse = (math.sin(self.pulse_frame * 0.3) + 1) / 2
        thickness = int(2 + 4 * pulse)
        intensity = int(128 + 127 * pulse)
        color = (0, intensity, 0)
        scale = 1.0 + 0.10 * pulse

        for box, score in zip(boxes, scores):
            x1, y1, x2, y2 = box
            cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
            w_box, h_box = (x2 - x1) * scale, (y2 - y1) * scale
            new_box = (
                int(cx - w_box / 2),
                int(cy - h_box / 2),
                int(cx + w_box / 2),
                int(cy + h_box / 2)
            )
            fancy_box(img, new_box, round(score, 2), color, thickness)

        # Update the graph with the current detection count only if graph tab is active
        if hasattr(self, "graph_widget") and getattr(self, "_graph_active", False):
            self.graph_widget.update_graph(num_detections)

        # Convert to QImage and display
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qimg = QImage(
            img_rgb.data,
            img_rgb.shape[1],
            img_rgb.shape[0],
            QImage.Format_RGB888
        )
        self.image_label.setPixmap(QPixmap.fromImage(qimg))

    def closeEvent(self, event):
        self.cap.release()
        event.accept()


def main():
    """Main function to run the Guardian Vision HUD application"""
    app = QApplication(sys.argv)
    window = WebcamApp()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
