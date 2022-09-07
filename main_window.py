# coding = utf-8

import os

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QPushButton, QGroupBox, QStyleFactory, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTimer

import time


class AudioPlayer(QWidget):

    def __init__(self):
        super(AudioPlayer, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("电话会议")
        self.setFixedSize(800, 500)
        self.setWindowIcon(QIcon("./images/win_title.jpeg"))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)
