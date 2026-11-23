#building a clock widget using PyQt5
import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):#QWidget is a base class to create our own widgets
  def __init__(self):
    super().__init__()
    self.time_label = QLabel(self)
    self.timer = QTimer(self)
    self.initUI()

    #here we will construct all the different entities of the clock

  def initUI(self):
    # designing the layout of our clock will be handled here
    self.setWindowTitle("Digital Clock")
    self.setGeometry(400,400,300,100)

    vbox = QVBoxLayout()
    vbox.addWidget(self.time_label)

    self.setLayout(vbox)

    self.time_label.setAlignment(Qt.AlignCenter)
    self.time_label.setStyleSheet("font-size: 150px;"
                                  "color: hsl(111, 100%, 50%)")#remove ° in hsl values
    self.setStyleSheet("background-color: black")

    # when working with imported fonts, can be found in ds digital
    font_id = QFontDatabase.addApplicationFont("DS-DIGIB.TTF")# for managing and quering fonts available to the application
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]#returns a list of font names
    my_font = QFont(font_family, 150)
    self.time_label.setFont(my_font)

    # to get our clock to update after every second, we need to connect our timer to a slot of update time
    self.timer.timeout.connect(self.update_time)
    # to trigger a timeout signal every 1 second;
    self.timer.start(1000)

    self.update_time()

  def update_time(self):
    current_time = QTime.currentTime().toString("hh:mm:ss AP") #to get current time
    # to add am/pm we use AP
    #A stands for Ante Meridiem (before midday).
    #P stands for Post Meridiem(after midday).
    self.time_label.setText(current_time)


if __name__ == "__main__":
  app = QApplication(sys.argv)#argv means arguments
  clock = DigitalClock()
  clock.show()
  sys.exit(app.exec())#app.exec() keeps your application running.