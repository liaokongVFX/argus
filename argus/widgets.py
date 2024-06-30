from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets


class StatusLabel(QtWidgets.QLabel):
    double_clicked = QtCore.Signal()

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.is_checked = False

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.setStyleSheet('background: rgba(0, 0, 0, 0);')
        self.setFixedHeight(26)

    def set_status(self, is_changed=True):
        self.is_checked = is_changed

        if is_changed:
            self.setStyleSheet('background: rgba(255, 0, 0, 188);')
        else:
            self.setStyleSheet('background: rgba(0, 0, 0, 0);')

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
