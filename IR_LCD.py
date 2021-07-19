import LCD1602
import time
import pylirc
import RPi.GPIO as GPIO
#LCD1602.init(0x27,1)
blocking = 0
def setup():
# LCD1602.init(0x27, 1)  # init(slave address, background light)
# LCD1602.write(0, 0, 'Greetings!!')
# LCD1602.write(1, 1, 'from SunFounder')
# time.sleep(2)
# LCD1602.write(0, 0, 'Hello!!')
# LCD1602.write(1, 1, 'Everyone')
 time.sleep(2)




def loop():
 space = '                '
 ERR = 15.86
 t = 0.00
 kp = 17.55
 kd = 12.11
 
 err = pylirc.init("ircontrol", "./lircrc", blocking)
 print(err)
# init(slave address, background light)
 while True:
  space = '                '
  s = pylirc.nextcode(1)
  while(s):
   for (code) in s:
    print ("Command: ", code["config"])
   if(not blocking):
    s = pylirc.nextcode(1)
   else:
    s = []
   if code["config"]== 'KEY_NUMERIC_1':
    kp = kp + .01
   if code["config"]== 'KEY_NUMERIC_2':
    kp = kp - .01
   if code["config"]== 'KEY_NUMERIC_3':
    kd = kd + .01
   if code["config"]== 'KEY_NUMERIC_4':
    kd = kd - .01
  
  
  format(ERR, ".1f")
  format(t, ".1f")
  t=t+.01
  LCD1602.write(8, 1, 'ERR:' + str('{:.1f}'.format(ERR)))
  LCD1602.write(0, 1, 't: ' + str('{:.2f}'.format(t)))
  LCD1602.write(0, 0, 'kp:' + str('{:.2f}'.format(kp)))
  LCD1602.write(8, 0, 'kd:' + str('{:.2f}'.format(kd)))
#  ERR = ERR / 2
#  t = t + 1 
#  kp = kp + 1
#  kd = kd - 1
  time.sleep(.1)
#  LCD1602.clear()
                 
#  print(ERR)
#  print(t)


def destroy():
#    GPIO.cleanup()
    LCD1602.clear()
    pylirc.exit()
    GPIO.cleanup()
    pass    

if __name__ == "__main__":
    try:
#        setup()
        LCD1602.init(0x27,1)# init(slave address, background light)
        loop()
        while True:
            pass
    except KeyboardInterrupt:
        destroy()