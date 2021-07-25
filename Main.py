import time
import board
import busio
import adafruit_bmp3xx
import csv

i2c = busio.I2C(board.SCL, board.SDA)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bmp.sea_level_pressure = int(bmp.pressure)

temp = 7

def sensor_write(Stemp, Dtime):
  with open ('Readings/temp.csv', 'a') as log:
        log_writer = csv.writer(log)
        log_writer.writerow('{Stemp}')
        log_writer.writerow('{Dtime}')

file = open("Readings/temp.csv", "r+")
file.truncate
file.close

start = dt.datetime.now()
while (dt.datetime.now() - start).seconds < 120:
    temp = int((bmp.temperature * 1.8) + 32)
    
    sensor_write(temp, start)
