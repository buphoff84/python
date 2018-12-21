import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('cls', shell=True)

remoteServer = raw_input("Enter host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

startPort = int(raw_input("starting port: "))
endPort = int(raw_input("ending port: "))

print("-" * 60)
print("Scanning ... ")
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(startPort,endPort):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:    Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("hostname not resolvable")
    sys.exit()

except socket.error:
    print("Unable to connect")
    sys.exit()

t2 = datetime.now()
total = t2 - t1

print("Scan completed in: ", total)