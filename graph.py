# graph.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import deque
import time
import numpy as np
import os
import csv

class GraphWidget(QWidget):
    def __init__(self, max_points=120, parent=None):
        super().__init__(parent)
        self.setMinimumSize(1100, 500)  # Back to single plot size
        self.max_points = max_points
        self.timestamps = deque(maxlen=max_points)
        self.detection_history = deque(maxlen=max_points)

        self.figure = Figure(facecolor='#000000')
        self.canvas = FigureCanvas(self.figure)
        self.ax_line = self.figure.add_subplot(111)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def update_graph(self, count, redraw=True):
        timestamp = time.strftime("%H:%M:%S")
        self.timestamps.append(timestamp)
        self.detection_history.append(count)
        # Save to CSV
        csv_path = os.path.join(os.path.dirname(__file__), 'crowd_counts.csv')
        file_exists = os.path.isfile(csv_path)
        with open(csv_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(['time', 'crowd count'])
            writer.writerow([timestamp, count])
        if redraw:
            self.redraw()

    def redraw(self):
        self.ax_line.clear()
        self.ax_line.set_facecolor('#000000')
        n = len(self.timestamps)
        x = list(range(n))
        y = list(self.detection_history)
        self.ax_line.plot(x, y, color="#00ffea", linewidth=2)
        self.ax_line.set_title("Crowd Density Over Time", color="#00ffea")
        self.ax_line.set_xlabel("Time", color="#00ffea")
        self.ax_line.set_ylabel("Detections", color="#00ffea")
        self.ax_line.tick_params(colors="#00ffea")
        self.ax_line.spines['bottom'].set_color('#00ffea')
        self.ax_line.spines['left'].set_color('#00ffea')
        # Show only a subset of x-ticks to avoid overlap
        if n > 0:
            if n > 12:
                step = max(1, n // 12)
                xtick_locs = list(range(0, n, step))
                if xtick_locs[-1] != n-1:
                    xtick_locs.append(n-1)
                xtick_labels = [self.timestamps[i] for i in xtick_locs]
                self.ax_line.set_xticks(xtick_locs)
                self.ax_line.set_xticklabels(xtick_labels, rotation=45, ha='right', fontsize=9, color="#00ffea")
            else:
                self.ax_line.set_xticks(list(range(n)))
                self.ax_line.set_xticklabels(list(self.timestamps), rotation=30, ha='right', fontsize=10, color="#00ffea")
            self.ax_line.set_xlim(-0.5, max(n-0.5, 11.5))
            if y:
                ymin = min(y)
                ymax = max(y)
                if ymin == ymax:
                    ymin -= 1
                    ymax += 1
                self.ax_line.set_ylim(ymin-1, ymax+1)
            else:
                self.ax_line.set_ylim(0, 10)
        self.ax_line.grid(True, linestyle='--', alpha=0.3)
        self.canvas.draw()
