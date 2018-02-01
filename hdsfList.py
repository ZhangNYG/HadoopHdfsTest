from hdfs import *
client = Client("http://192.168.1.160:50070",root="/",timeout=100,session=False)
print(client.list("/"))
print(dir(client))
print(client.status("/"))

print(client.list("/",status=False))
print(client.list("/",status=True))

client.makedirs("/test")
print(client.list("/"))
with client.read("/usr/111.txt") as reader:
    print(reader.read())
