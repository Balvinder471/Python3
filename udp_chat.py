import threading
import socket
import os


def send (sock) :
  while True :
    mssg = input().encode()
    if mssg.decode().casefold() == "exit" :
      print("\nShutting Down!!")
      os._exit(1)
    sock.sendto(mssg,("192.168.1.6",1030))
    mssg = "YOU : {}".format(mssg.decode())
    print("\n{}".format(mssg.rjust(50 + len(mssg))))


pro = socket.SOCK_DGRAM
af = socket.AF_INET

ip = "192.168.1.10"
port = 1040

with socket.socket(af,pro) as sock :
  sock.bind((ip,port))
  sender = threading.Thread(target=send,args=(sock,))
  sender.start()
  print("Listning On port 1040/udp\n")
  while True :
    data = sock.recvfrom(1024)
    print("\nMssg From {}:{} : {}".format(data[1][0],data[1][1],data[0].decode()))

