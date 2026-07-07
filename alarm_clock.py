import time
import datetime
import pygame #works with sound effects

def set_alarm(alarm_time):
  print(f"Alarm set for {alarm_time}")
  sound_file = "alarm.wav"
  is_running = True #clock is running

  while is_running:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)

    if current_time == alarm_time:
      print("WAKE UP! 😫")

      pygame.mixer.init() #module for loading and playing sounds
      #init() initialises mixer
      #init() is another way to call the constructor
      pygame.mixer.music.load(sound_file) #load sound file
      pygame.mixer.music.play() #plays music

      #sound stops playing when program terminates
      #we want to continue playing sound_file while that sound_file is busy/still playimg

      while pygame.mixer.music.get_busy():
        time.sleep(1)#Instead of checking every tiny fraction of a second, 
        #the program waits for 1 second,then checks again if the music is still playing.

      is_running = False

    time.sleep(1)

if __name__ == "__main__":
  alarm_time = input("Enter the alarm time (HH:MM:SS): ")
  set_alarm(alarm_time)