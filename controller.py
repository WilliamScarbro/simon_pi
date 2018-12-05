import pygame
import joystick
import time

class item:
  def __init__(self,val,time):
    self.val = valn #0,1,2,3
    self.time = time #timestamp used for program syncing
  def __str__:
    return "{},{}".format(self.val,self.time)
    

while true:
  sleep(0.1)
  events = joystick.get_events
  for event in events:
    if event.val == 5 or not event.down:
      exit()
    i = item(event.val, time.time())
    f = open("userimput.txt","w")
    f.write(i)
    
    
  
  
  
