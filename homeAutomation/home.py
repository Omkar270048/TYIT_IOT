# pip install Flask
from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

led1 = 2
led2 = 3
led3 = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)


print("Done")

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/A')
def led1on():
    GPIO.output(led1, 1)
    return render_template('home.html')

@app.route('/a')
def led1off():
    GPIO.output(led1, 0)
    return render_template('home.html')

@app.route('/B')
def led2on():
    GPIO.output(led2, 1)
    return render_template('home.html')

@app.route('/b')
def led2off():
    GPIO.output(led2, 0)
    return render_template('home.html')

@app.route('/C')
def led3on():
    GPIO.output(led3, 1)
    return render_template('home.html')

@app.route('/c')
def led3off():
    GPIO.output(led3, 0)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='192.168.0.7', port=5010)
