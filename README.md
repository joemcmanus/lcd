# lcd
Sample program to control a serial LCD on the Intel Galileo Gen 2


Usage:
    ./lcd.py "Hello World"
    Setting up GPIO Pins
    Sending your message to /dev/ttyS0

    root@galileo:~# ./lcd.py --help
    usage: lcd.py [-h] [--version] message
    
    Simple LCD Display Script for Galileo
    
    positional arguments:
      message     The message you want to display on the LCD
    
    optional arguments:
      -h, --help  show this help message and exit
      --version   show program's version number and exit
