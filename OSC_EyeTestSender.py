import random
import time

from pythonosc import udp_client

PORT = 9000
IP = "127.0.0.1"

def functionLoop():

  Random = random.random()

  print("Forward")
  sendData(0.0,
           0.0,
           Random,
           Random)
  time.sleep(0.5)

  print("Up")
  sendData(0.0,
           1.0,
           1.0,
           1.0)
  time.sleep(0.5)

  print("Down")
  sendData(0.0,
           -1.0,
           1.0,
           1.0)
  time.sleep(0.5)

  print("Left")
  sendData(1.0,
           0.0,
           1.0,
           1.0)
  time.sleep(0.5)

  print("Right")
  sendData(-1.0,
           0.0,
           1.0,
           1.0)
  time.sleep(0.5)

  print("Blink")
  sendData(0.0,
           0.0,
           0.0,
           0.0)
  time.sleep(0.35)

def sendData(X,Y,LeftBlink,RightBlink):

  print(f"\tEyeX: {X}")
  print(f"\tEyeY: {Y}")
  print(f"\tLeftEyeLid: {LeftBlink}")
  print(f"\tRightEyeLid: {RightBlink}")

  client.send_message("/avatar/parameters/LeftEyeX", X)
  client.send_message("/avatar/parameters/LeftEyeY", Y)
  client.send_message("/avatar/parameters/RightEyeX", X)
  client.send_message("/avatar/parameters/RightEyeY", Y)

  client.send_message("/avatar/parameters/LeftEyeLid", LeftBlink)
  client.send_message("/avatar/parameters/RightEyeLid", RightBlink)

if __name__ == "__main__":

  client = udp_client.SimpleUDPClient(IP, PORT)

  for x in range(10000):
    functionLoop()
