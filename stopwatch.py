#Python PyQt5 Stopwatch
import sys #handles system variables for your Python interpreter
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
#Widgets are building blocks for a PyQt5 application
from PyQt5.QtCore import QTimer, QTime, Qt 
#QTimer admits a signal after a given interval
#QTime keeps track of time
#Qt for alignment

class StopWatch(QWidget):
  def __init__(self):
    super().__init__()
    self.time = QTime(0, 0, 0, 0)#hrs, min, sec, millisec
    self.time_label = QLabel("00:00:00.00", self)
    self.start_button = QPushButton("Start", self)
    self.stop_button = QPushButton("Stop", self)
    self.reset_button = QPushButton("Reset", self)
    self.timer = QTimer(self)

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Stopwatch")

    vbox = QVBoxLayout()
    vbox.addWidget(self.time_label)

    self.setLayout(vbox)

    self.time_label.setAlignment(Qt.AlignCenter)

    hbox = QHBoxLayout()
    hbox.addWidget(self.start_button)
    hbox.addWidget(self.stop_button)
    hbox.addWidget(self.reset_button)

    vbox.addLayout(hbox)

    self.setStyleSheet("""
      QPushButton, QLabel{
        padding: 20px;
        font-weight: bold;
        font-family: calibri;
      }
      QPushButton{
        font-size: 50px;
      }
      QLabel{
        font-size: 120px;
        background-color: hsl(217, 67%, 49%);
        border-radius: 20px;
      }
    """)

    self.start_button.clicked.connect(self.start)
    self.stop_button.clicked.connect(self.stop)
    self.reset_button.clicked.connect(self.reset)
    self.timer.timeout.connect(self.update_display)

  def start(self):
    self.timer.start(10)

  def stop(self):
    self.timer.stop()

  def reset(self):
    self.timer.stop()
    self.time = QTime(0,0,0,0)
    self.time_label.setText(self.format_time(self.time))
    
  def format_time(self, time):
    hours = time.hour()#returns hour
    minutes = time.minute()#returns minutes
    seconds = time.second()#returns seconds
    milliseconds = time.msec() // 10 #returns milliseconds in 2 digits
    return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

  def update_display(self):
    self.time = self.time.addMSecs(10)#updates the time with 10 milliseconds
    self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
  app = QApplication(sys.argv)#sys.argv is if we are using command_line arguments
  stopwatch = StopWatch()
  stopwatch.show()
  sys.exit(app.exec_())#app.exec_() starts the main event loop and handles events