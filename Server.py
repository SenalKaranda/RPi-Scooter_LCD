import time
import bluetooth
from RPLCD import CharLCD

#Server Vars
hostMACAddress = 'AA:AA:AA:AA:AA:AA' # The MAC address of a Bluetooth adapter on the server, in this case, My Phone's MAC address
port = 27371 #Port must match between client/server
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

#LCD Vars
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

x = 0
y = 16
sunChar = (
	0b00000,
	0b10101,
	0b01110,
	0b11111,
	0b01110,
	0b10101,
	0b00000,
	0b00000
)
rainChar = (
	0b10101,
	0b01010,
	0b00000,
	0b10101,
	0b01010,
	0b00000,
	0b10101,
	0b01010
)

#Setup Cursor & Custom Characters
lcd.cursor_mode = CursorMode.hide
lcd.create_char(0, sunChar)
lcd.create_char(1, rainChar)

#Intro Loop
for x in range(15):
    lcd.cursor_pos = (0,x)
    lcd.write_string(u'Tesselex')
    lcd.cursor_pos = (1,y-x)
    lcd.write_string(u'Studios')
    time.sleep(1)
    lcd.clear()
#Info Display Loop
while True:
	#Communicate with client & recieve info
	try:
    	client, clientInfo = s.accept()
    	while 1:
        	data = client.recv(size).decode('utf-8')
        	if data:
            	#I need to extract all my info from 'data' and push them into my own variables.
            	client.send(data) # Echo back to client
	except:
    	print("Closing socket")
    	client.close()
    	s.close()

	#Display info to LCD
    lcd.cursor_pos = (0,1);
    lcd.write_string(%time.strftime("%H:%M"))
    lcd.cursor_pos = (0, 10)
    lcd.write_string(unichr(0) + ' 00°')
    time.sleep(1)
    lcd.clear()
