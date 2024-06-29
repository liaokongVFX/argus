import os
import sys

import importlib.util

from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore


class OutlinedLabel(QtWidgets.QLabel):
    double_clicked = QtCore.Signal()

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.setStyleSheet('background: rgba(0, 0, 0, 0);')
        self.setFixedHeight(26)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.TextAntialiasing)

        text = self.text()
        rect = event.rect()

        pen = QtGui.QPen(
            QtGui.QColor(0, 0, 0), 2,
            QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
        painter.setPen(pen)
        for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            painter.drawText(
                rect.adjusted(dx, dy, dx, dy), QtCore.Qt.AlignCenter, text)

        pen.setColor(QtGui.QColor(255, 255, 255))
        painter.setPen(pen)
        painter.drawText(rect, QtCore.Qt.AlignCenter, text)

    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.double_clicked.emit()


class SystemMonitor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_tray()
        self.dragging = False

    def import_modules_from_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.py'):
                module_name = filename[:-3]
            else:
                module_name = filename
            module = importlib.import_module(f'plugins.{module_name}')

            if hasattr(module, 'register'):
                label = OutlinedLabel()
                module.register(label, self)

                if hasattr(module, 'double_click_handler'):
                    label.double_clicked.connect(
                        module.double_click_handler)

                self.container_layout.addWidget(label)

    def init_ui(self):
        self.setWindowTitle('System Monitor')
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: rgba(0, 0, 0, 10); color: white;")

        self.container_layout = QtWidgets.QVBoxLayout()
        self.container_layout.setAlignment(QtCore.Qt.AlignTop)
        self.container_layout.setSpacing(0)

        container = QtWidgets.QWidget()
        container.setStyleSheet('border-radius: 10px')
        container.setLayout(self.container_layout)
        self.setCentralWidget(container)

        self.import_modules_from_folder('plugins')

    def init_tray(self):
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon('icon.png'))

        show_action = QtGui.QAction('Show', self)
        quit_action = QtGui.QAction('Quit', self)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(QtWidgets.QApplication.instance().quit)

        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.drag_start_position = event.globalPosition().toPoint()
            self.window_start_position = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.dragging:
            current_position = event.globalPosition().toPoint()
            delta = current_position - self.drag_start_position
            self.move(self.window_start_position + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    monitor = SystemMonitor()
    monitor.show()
    sys.exit(app.exec())
