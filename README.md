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
--__main__() --simple demonstration of how to use the inerface, prints button contents, exits on R1</br>
</br>
led.h:</br>
--provides interface to the led display</br>
--classes:</br>
----Image:</br>
------Image(unsigned char* val) //creates a writable image for the 8x8 led screen, val contains 8 chars representing each line, each char looks like ('0x' + two hex chars), see led.cc for examples</br>
------Image CROSS() //predefined CROSS image</br>
------Image SQUARE() //predefined SQUARE image</br>
------Image CIRCLE() // ''    ''</br>
------Image TRIANGLE() //  ''   ''</br>
------Image FULL()  //all pixels on</br>
------Image BLANK() //all pixels off</br>
----Led_Writer:</br>
------Led_Writer() //starts the interface</br>
------void write(const Image&, const Image&) //writes two Images, one to each of the two 8x8 screens. </br>
------void write(int valL, int valR) //writes predefined images (-2 = FULL, -1 = BLANK, 0=square, 1=cross,2=circle,3=triangle) (these match the button values for the controller, you're welcome)</br>
