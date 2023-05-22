import telnetlib
import time

#sales switch
host = '172.16.20.3'
port = '23'
user = 'service'
password = 'password'

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"save configuration\n")
tn.write(b"y\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#HR switch
host = "172.16.30.3"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"save configuration\n")
tn.write(b"y\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#it switch
host = "172.16.40.3"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"save configuration\n")
tn.write(b"y\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#guest switch
host = "172.16.50.3"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"save configuration\n")
tn.write(b"y\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

#local switch
host = "172.16.40.2"

tn = telnetlib.Telnet(host=host, port=port)
tn.read_until(b'login: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'password: ')
tn.write(password.encode() + b'\n')

tn.write(b"save configuration\n")
tn.write(b"y\n")
tn.write(b"exit\n")
tn.write(b"y\n")
time.sleep(1)

tn.close()