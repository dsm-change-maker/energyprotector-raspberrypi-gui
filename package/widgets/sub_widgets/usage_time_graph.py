# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *


class UsageTimeGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(502, 331)
        self.labels = ["-4", "-3", "-2", "-1", "0"]
        self.day_times = [10.2, 5.2, 4.2, 9.2, 14.8]
        self.week_times = [80.2, 60.4, 49.8, 50.6, 89]
        self.month_times = [320.4, 200.3, 331.5, 425.90, 302.34]

        self.x = np.arange(len(self.labels))
        self.width = 0.20

        self.fig, self.ax = plt.subplots()
        self.rects1 = self.ax.bar(self.x - self.width, self.day_times, self.width, label='Day', color='darkorange')
        self.rects2 = self.ax.bar(self.x, self.week_times, self.width, label='Week', color='lightgreen')
        self.rects3 = self.ax.bar(self.x + self.width, self.month_times, self.width, label='Month',
                                  color='cornflowerblue')

        self.ax.set_xticks(self.x)
        self.ax.set_xticklabels(self.labels)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.ax.get_xaxis().set_visible(False)
        self.ax.legend(loc='upper left')
        self.fig.tight_layout()

        self.auto_label(self.rects1, "grey")
        self.auto_label(self.rects2, "grey")
        self.auto_label(self.rects3, "grey")

        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        lay = QHBoxLayout()
        self.setLayout(lay)
        lay.addWidget(self.canvas)
        self.setStyleSheet("background-color:white;")
        self.canvas.show()

    def auto_label(self, rects, annotate_color):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            self.ax.annotate('{}'.format(height),
                             xy=(rect.get_x() + rect.get_width() / 3, height),
                             xytext=(0, 0),  # 3 points vertical offset
                             textcoords="offset points",
                             ha='center', va='bottom',
                             color=annotate_color)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    usageTimeGraph = UsageTimeGraph()
    usageTimeGraph.show()
    sys.exit(app.exec_())
