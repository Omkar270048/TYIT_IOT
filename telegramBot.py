import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

RELAY1=20
RELAY2=16

FAN=RELAY1
LIGHT=RELAY2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(RELAY1,GPIO.OUT)
GPIO.setup(RELAY2,GPIO.OUT)
telegramBotToken='6559879878:AAHorplrEBd7Y5NVkxShwx_MqYSFyIZ1R8U' #BilluVermaBot aka Ok Sir
def on(pin):
    GPIO.output(pin,GPIO.LOW)
    return "off"

def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return "off"

def handle(msg):
    chat_id=msg['chat']['id']
    print (str(chat_id))
    command=str(msg['text'])

    print ('Receive message from Telegram: %s'%command)
    if'Fan' in command or 'fan' in command:
        if'on' in command:
            bot.sendMessgae(chat_id,str("Fan"+on(FAN)))

        elif'off' in command:
            bot.sendMessage(chat_id,str("Fan"+off(FAN)))

    elif'Light' in command or 'light' in command:
        if'on' in command:
            bot.sendMessgae(chat_id,str("Light"+on(LIGHT)))

        elif'off' in command:
            bot.sendMessgae(chat_id,str("Light"+on(LIGHT)))

bot=telepot.Bot(telegramBotToken)
bot.message_loop(handle)
print('I am listening...')
while 1:
    time.sleep(10)
