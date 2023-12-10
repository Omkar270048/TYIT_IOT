# TYIT_IOT
![image](https://github.com/Omkar270048/TYIT_IOT/assets/69665958/cd870b36-0c9a-4978-920f-9023e01039a9)

RFID
```py
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader=SimpleMFRC522()
try:
    id,text=reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()
```


Oscilloscope
```cmd
pip install numpy
```

```cmd
sudo apt-get install libopenblas-base
```

LED pattern
```py
import RPi.GPIO as GPIO 
from time import sleep
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
while True: # Run forever
 GPIO.output(8, GPIO.HIGH)
 sleep(1)
 GPIO.output(8, GPIO.LOW)
 sleep(1)
```

Starting Raspbian OS, Familiarising with Raspberry Pi Components and interface, Connecting to ethernet, Monitor, USB : 
```
Raspberry Pi, 
MicroSD card with Rasbian OS installed, 
Power adapter for Raspberry PI, 
HDMI cable and monitor, 
Ethernet cable, 
USB keyboard and mouse, 
USB flash drive
```
