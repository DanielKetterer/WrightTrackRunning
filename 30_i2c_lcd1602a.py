#!/usr/bin/env python3
import LCD1602
import time
LCD1602.init(0x27,1)
def setup():
 LCD1602.init(0x27, 1)	# init(slave address, background light)
 LCD1602.write(0, 0, 'Greetings!!')
 LCD1602.write(1, 1, 'from SunFounder')
 time.sleep(2)
 LCD1602.write(0, 0, 'Hello!!')
 LCD1602.write(1, 1, 'Everyone')
 time.sleep(2)

def loop():
 space = '                '
 ERR = 15.8658433358433485
 t = 1.22
 kp = 17.5554515
 kd = 12.11
# init(slave address, background light)
 while True:
  #LCD1602.init(0x27, 1)	# init(slave address, background light)
  space = '                '
    # init(slave address, background light)
  format(ERR, ".1f")
  format(t, ".1f")
  LCD1602.write(8, 1, 'ERR: ' + str('{:.2f}'.format(ERR)))
  LCD1602.write(0, 1, 't: ' + str('{:.2f}'.format(t)))
  LCD1602.write(0, 0, 'kp: ' + str(kp))
  LCD1602.write(8, 0, 'kd: ' + str(kd))
  ERR = ERR + 1
  t = t - 1
  kp = kp + 1
  kd = kd - 1
  print(ERR)
  print(t)


def destroy():
	pass	

if __name__ == "__main__":
	try:
		#setup()
        #LCD1602.init(0x27,1)# init(slave address, background light)
		loop()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()