import socket

SERVER_IP = "10.0.0.4"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, PORT))

reader = client.makefile("r")
writer = client.makefile("w")

print(reader.readline().strip())

for i in range(3):

    question = reader.readline().strip()

    print("\n" + question)

    answer = input("Your answer: ")

    writer.write(answer + "\n")
    writer.flush()

    result = reader.readline().strip()

    print(result)

result = reader.readline().strip()
print("\n" + result)

reader.close()
writer.close()
client.close()
