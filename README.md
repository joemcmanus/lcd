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
    usage: lcd.py [-h] [--version] lineOne [lineTwo]
    
    Simple LCD Display Script for Galileo
    
    positional arguments:
      lineOne     The message you want to display on line 1 of the LCD
      lineTwo     The message you want to display on line 2 of the LCD
    
    optional arguments:
      -h, --help  show this help message and exit
      --version   show program's version number and exit

Example, reading a TMP36 using analog.py and printing the temperature on the display. 

    root@galileo:~# ./analog.py 1 --quiet --count=1 --temp | xargs ./lcd.py 
    Setting up GPIO Pins
    Sending your message to /dev/ttyS0

Example, reading a TMP36 using analog.py, then printing the data on the display every 30 seconds.
    
    root@galileo:~# while [ 1 ]
    > do
    >   ./lcd.py `./analog.py 1 --quiet --count=1 --temp` "`date +'%b %d %H:%M %p'`"
    >   sleep 30
    > done

Image of the Sparkfun 2 Line x 16 char LCD. 

