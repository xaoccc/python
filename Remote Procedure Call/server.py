def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def test():
    return "It Works!!!"

from rpc import RPCServer

server = RPCServer()

server.registerMethod(add)
server.registerMethod(sub)
server.registerMethod(test)

server.run()