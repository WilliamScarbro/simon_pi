# simon_pi
joystick.py:
  provides interface to ps4 controller
  contains classes:
    Joystick_Listener:
      __init__() --initialized the listener
      findController() --finds the controller, returns false if number of controllers connected !=1
      get_event() --returns list of ButtonEvent, needs to be polled often or events will get flushed from buffer (not my design)
    ButtonEvent:
      down --bool, was button pressed down? (rather than released)
      val --int, button number (0 - square, 1 - 'X', 2 - 'O', 3 - triangle)
      __init__(down,val) -- initializes values
      __str__() --helpful print for debugging (equivalent to toString)
