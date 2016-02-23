# lcd
Sample program to control a serial LCD on the Intel Galileo Gen 2

This has been tested on a Galileo Gen 2 using the EGlibC image. 
And with the following Serial LCDs from Sparkfun:

 https://www.sparkfun.com/products/9393

 https://www.sparkfun.com/products/9067
        
You will need to install PySerial

    pip install pyserial


Usage:
    
    #Send the message Hello World
    root@galileo:~# ./lcd.py "Hello World"
    Setting up GPIO Pins
    Sending your message to /dev/ttyS0

    #Display help
    root@galileo:~# ./lcd.py --help
    usage: lcd.py [-h] [--version] message
    
    Simple LCD Display Script for Galileo
    
    positional arguments:
      message     The message you want to display on the LCD
    
    optional arguments:
      -h, --help  show this help message and exit
      --version   show program's version number and exit

Example, reading a TMP36 using analog.py and printing the temperature on the display. 

    root@galileo:~# ./analog.py 1 --quiet --count=1 --temp | xargs ./lcd.py 
    Setting up GPIO Pins
    Sending your message to /dev/ttyS0

