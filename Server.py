import socket

runProgram = True
runClient = False

def server():
    serverName = 'localhost'
    serverPort = 10000
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.bind((serverName, serverPort))


def quit(message):
    # Client disconnection
    if message.lower() == "luk":
        print("clukker")
        return True, False

    # System og client disconnection
    elif message.lower() == "låk":
        print("LUKKKEETETET")
        return False, False
    else:
        return True, True



def handshake():
    count = 0
    tempConn = server()
    while count <= 1:
        FirstStep, tempClient = tempConn.recvfrom(2048)
        connTry = FirstStep.decode()

        runProgram, runClient = count(connTry)
        if runProgram and runClient:
            if connTry == "com-0":
                serverAnswer = "com-0 accept"
                tempConn.sendto(serverAnswer.encode(), tempClient)

            elif connTry == "com-0 accept":
                print("Server Accepted client")
                print(f"Connection to {tempClient} has been made!")
                tempConn.sendto(str(runClient).encode(), tempClient)
                serverConn = tempConn
                client = tempClient

                ###Fiixxxxxxxxxxxxxxxxxxxxxx

        count += 1

while runProgram:
# at kører programmet.

# # opretter upd socket (DGRAM)
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print('Server: socket oprettet')
#
# # Bind socket
# server_address = ('localhost', 10000)
# print('Server: Socket connected to {} port {}'.format(*server_address))
# server_socket.bind(server_address)
#
# # TODO - få din hjerne til at tænke, køb en over ebay.
#
# '''# Bind socket
# host = 'localhost'
# print('server vil starte på ip: ' + host)
# port = 10000
# # print('Server: Socket connected to {} port {}'.format(*server_address))
# server_socket.bind((host, port))
# server_socket.listen(1)
# conn, adress = server_socket.accept()
# print(adress, "har forbundet")'''
#
# # TODO SYN + ACK (Modtager request og accepterer "Okay lad os snakke sammen!")
# # -IP adresse bliver tastet ind
# # Server accepterer at ip'erne stemmer overens.
# # sender en "join ok" tilbage til clienten
# # når clienten sender en besked, skal serveren sende en automatisk besked.
# message = 'Test message'
#
# while True:
#     data, address = server_socket.recvfrom(4096)
#     data = data.decode()
#     print('Modtaget fra client ' + data)
#
#     if data:
#         print('Server sender: ' + message)
#         server_socket.sendto(message.encode(), address)