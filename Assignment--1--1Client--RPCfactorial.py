import xmlrpc.client

n = int(input("Enter an integer value: "))
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')
result = proxy.factorial(n)
print(f"The factorial of {n} is {result}")
#Remote Procedure Call is a software communication protocol that one program can use to request a service from a program located in another computer on a network without having to understand the network's details. RPC is used to call other processes on the remote systems like a local system.
