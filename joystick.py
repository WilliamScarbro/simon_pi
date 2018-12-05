import pygame
import time
class ButtonEvent:
    def __init__(self,down,val):
        self.down=down
        self.val=val #0,1,2,3
    def __str__(self):
        return "Down? {} button: {}".format(self.down,self.val)

class Joystick_Listener:
    def __init__(self):
        pygame.joystick.init()
        pygame.init()
   
    #Returns true if it can find the controller (and only one controller)
    #false otherwise
    def findController(self):    
        if (pygame.joystick.get_count()!=1):
           return False
        joystick=pygame.joystick.Joystick(0)
        joystick.init()
        return True
    
    #returns list of all ButtonEvents since last checked or cleared
    def get_events(self):
        ret=[]
        for event in pygame.event.get():
            #print("found event")
            if event.type==pygame.JOYBUTTONDOWN:
                #print(event)
                ret.append(ButtonEvent(True,event.button))
            if event.type==pygame.JOYBUTTONUP:
                #print(event)
                ret.append(ButtonEvent(False,event.button))
        return ret

    #clears ButtonEvent buffer
    #(not necessary because events get flushed out of buffer really fast)
    def clear_events(self):
        pygame.event.get()

if __name__=="__main__":
    ps=Joystick_Listener()
    if (ps.findController()):
        print("initialized controller")
    while True:
        evs = ps.get_events()
        if (len(evs)!=0):
            for be in evs:
                if be.val==5 and not be.down: #exit if R1 is hit
                    exit()
                print(be)

