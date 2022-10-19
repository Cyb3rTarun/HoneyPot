import socket
from pyfiglet import figlet_format
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_address = "linux.tarun1@gmail.com"
to_address = "starun.py@gmail.com"

msg = MIMEMultipart()

msg['FROM'] = from_address

msg['TO'] = to_address

msg['Subject'] = "About Activity Login"

body = "Here is the Intruders list with their Ip Address."

msg.attach(MIMEText(body,'plain'))

file_name = 'Intruders.txt'
attachment = open(file_name, 'rb')

p = MIMEBase('application', 'octet-stream')

p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition',f"attachment; filename = {file_name}")

msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(from_address, 'mizmtbbzdtmgeyds')
text = msg.as_string()
s.sendmail(from_address, to_address, text)
s.quit()

#for viewing the banner.
ascii_banner = figlet_format('HoneyPot',font='ntgreek')
print('\33[33m'+ascii_banner+'\33[0m')

#intializing the socket.
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket Successfully Created!!!")
#if socket is not successfully created.
except socket.error as s:
	print("An error has occured while creating the socket.")

#asking for the port number.
port_number = int(input("Port Number to monitor: "))
#listening on the local ip address and the port number.
s.bind(('',port_number))
no_connections = int(input("Listening Connections for: "))
#Starts listening for the connections.
s.listen(no_connections)

file = open('Intruders.txt','a')

while True:
	conn,addr = s.accept()
	print(f"{addr} has been logged an activity.")
	file.write(f'{addr} is trying to connect\n')	
	conn.send(b'Your activity has been logged.')
	conn.close()



