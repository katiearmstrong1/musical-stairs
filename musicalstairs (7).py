#!/usr/local/lib/python2.7/sitepackages
import mysql.connector as mariadb # connect to mysql
import RPi.GPIO as GPIO # GPIO
import pygame.mixer # To make sound
pygame.mixer.pre_init(44100, -16, 2, 2048) # reduce latency in sound
pygame.mixer.init()
pygame.init()
import time

#variables to determine if note has been played when beam is broken
pin4played = False
pin17played = False
pin27played = False
pin22played = False
pin23played = False
pin16played = False
pin26played = False
pin20played = False

#play a note
def playSound(soundFile):
  print soundFile
  note = pygame.mixer.Sound(soundFile)
  note.play()

#determine what instrument has been selected and play the sound
def selectInstrument(id, pianoFile, drumFile, xyFile):
  if(id==1):
    playSound(pianoFile)

  if(id==2):
    playSound(drumFile)

  if(id==3):
    playSound(xyFile)

#GPIO setup
GPIO.setmode(GPIO.BCM) # GPIO set mode
GPIO.setwarnings(False)

#Motion sensor setup
GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, GPIO.PUD_UP)

while True:
  
  #Connect to database
  mariadb_connection = mariadb.connect(user='newuser', password='password', database='stairs')
  cursor = mariadb_connection.cursor()
  cursor.execute("SELECT id FROM settings WHERE active = 'true'")
  settings = cursor.fetchall()
  
  if not settings:
    pass

  else:
  
    for id in settings:

      instrument = id[0]

      """if beam is broken and a note has not already been played, the selectInstrument()
      function can be called to play a note. This sets pin4played=True, meaning the note
      can't play again until the object blocking the beam has moved"""
      input_state = GPIO.input(4)
      if not input_state and not pin4played:
        pin4played = True
        selectInstrument(instrument, "piano/C1.wav", "drum/Drumc1.wav", "xylophone/X1.wav")

      """only when the beam is no longer blocked (input_state == True) the note is
      available to be played agani"""             
      if input_state == True:
        pin4played = False

                             
      input_state = GPIO.input(17)
      if not input_state and not pin17played:
        pin17played = True
        selectInstrument(instrument, "piano/D.wav", "drum/Drumd.wav", "xylophone/X2.wav")

      if input_state == True:
        pin17played = False


      input_state = GPIO.input(27)
      if not input_state and not pin27played:
        pin27played = True
        selectInstrument(instrument, "piano/E.wav", "drum/Drume.wav", "xylophone/X3.wav")

      if input_state == True:
        pin27played = False
              

      input_state = GPIO.input(22)
      if not input_state and not pin22played:
        pin22played = True
        selectInstrument(instrument, "piano/F.wav", "drum/Drumf.wav", "xylophone/X4.wav")

      if input_state == True:
        pin22played = False      


      input_state = GPIO.input(23)
      if not input_state and not pin23played:
        pin23played = True
        selectInstrument(instrument, "piano/G.wav", "drum/Drumg.wav", "xylophone/X5.wav")

      if input_state == True:
        pin23played = False

          

      input_state = GPIO.input(16)
      if not input_state and not pin16played:
        pin16played = True
        selectInstrument(instrument, "piano/A.wav", "drum/Druma.wav", "xylophone/X6.wav")

      if input_state == True:
        pin16played = False
          

      input_state = GPIO.input(26)
      if not input_state and not pin26played:
        pin26played = True
        selectInstrument(instrument, "piano/B.wav", "drum/Drumb.wav", "xylophone/X7.wav")
          
      if input_state == True:
        pin26played = False

                    
      input_state = GPIO.input(20)
      if not input_state and not pin20played:
        pin20played = True
        selectInstrument(instrument, "piano/C2.wav", "drum/Drumc2.wav", "xylophone/X8.wav")

      if input_state == True:
        pin20played = False

    
      # close connection to database
      cursor.close()
      mariadb_connection.close()
      
      # Stress testing - fried if didn't free up processing time
      time.sleep(0.0001)

GPIO.cleanup()
