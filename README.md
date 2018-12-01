# simon_pi
joystick.py:</br>
--provides interface to ps4 controller</br>
--contains classes:</br>
----Joystick_Listener:</br>
------__init__() --initialized the listener</br>
------findController() --finds the controller, returns false if number of controllers connected !=1</br>
------get_event() --returns list of ButtonEvent, needs to be polled often or events will get flushed from buffer (not my design)</br>
----ButtonEvent:</br>
------down --bool, was button pressed down? (rather than released)</br>
------val --int, button number (0 - square, 1 - 'X', 2 - 'O', 3 - triangle)</br>
------__init__(down,val) -- initializes values</br>
------__str__() --helpful print for debugging (equivalent to toString)</br>
