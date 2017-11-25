from pyrad.server import Server, RemoteHost
from netaddr import *


#Testing, testing
print("Hello!")
ip = IPNetwork("192.168.0.1/24")
print("version: ", ip.version)
print("IP:", ip.ip)
print(ip.broadcast)
print(ip.netmask)
print(ip.secret)


#if (IPAddress("192.168.1.1") in IPNetwork("192.168.0.0/24")):
#	print("Ip is within subnet")
#else:
#	print("Ip is not within subnet")

remoteHost = RemoteHost("69.69.69.69", "pwd", "host")
server = Server(hosts={"192.168.0.0/24": remoteHost})
