from rpc import RPCClient

client = RPCClient()

client.connect()

# Here we call functions, which are on the server:
print(client.add(5, 6))
print(client.sub(5, 6))

client.disconnect()