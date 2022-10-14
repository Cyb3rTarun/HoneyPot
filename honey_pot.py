import socket
from pyfiglet import figlet_format


ascii_banner = figlet_format('HoneyPot',font='ntgreek')
print('\33[33m'+ascii_banner+'\33[0m')

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket Successfully Created!!!")
except socket.error as s:
	print("An error has occured while creating the socket.")

port_number = int(input("Port Number to monitor: "))
s.bind(('',port_number))
no_connections = int(input("Listening Connections for: "))

s.listen(no_connections)

while True:
	conn,addr = s.accept()
	print(f"{addr} has been logged an activity.")
	conn.send(b'Your activity has been logged.')
	conn.close()
