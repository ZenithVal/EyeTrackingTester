import random
import time

from pythonosc import udp_client

PORT = 9000
IP = "127.0.0.1"

def sendData():
  
  LeftBlink = random.random()
  # RightBlink = random.random()

  if LeftBlink > 0.1:
    LeftBlink = 1.0
    RightBlink = 1.0
  else:
    LeftBlink = 0.0
    RightBlink = 0.0

  DirectionalRandom = random.random()
  X = 0.0
  Y = 0.0
  
  if DirectionalRandom > .75:    # Up
    X = 0.0
    Y = 1.0
  elif DirectionalRandom > .50:  # Down
    X = 0.0
    Y = -1.0
  elif DirectionalRandom > .25:   # Left
    X = -1.0
    Y = 0.0
  else:                     # Right
    X = 0.0
    Y = 1.0


  print(f"Sending information:\n\tX: {X}\n\tY: {Y}\n\tLeftEyeLid: {LeftBlink}\n\tRightEyeLid: {RightBlink}")

  client.send_message("/avatar/parameters/LeftEyeX", X)
  client.send_message("/avatar/parameters/LeftEyeY", Y)
  client.send_message("/avatar/parameters/RightEyeX", X)
  client.send_message("/avatar/parameters/RightEyeY", Y)

  client.send_message("/avatar/parameters/LeftEyeLid", LeftBlink)
  client.send_message("/avatar/parameters/RightEyeLid", RightBlink)

  print("")

  time.sleep(0.5)

if __name__ == "__main__":

  client = udp_client.SimpleUDPClient(IP, PORT)

  for x in range(10000):
    sendData()
