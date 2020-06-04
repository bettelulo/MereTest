import socket
server_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverName = 'localhost'
serverPort = 10000
runSystem = True
runClient = False

def handshake():
    conCount = 0
    server_connection.connect((serverName, serverPort))
    while conCount <= 1:
        if conCount == 0:
            Message = "com-0"
            server_connection.send(Message.encode())
####fix.

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


def sendMessage(message, counter):
    runSystem, runClient = quit(message)
    counter += 1
    currentMessage = "msg-" + str(counter) + ": " + message ##msg-0: den ønskede tekst. (Syntaks)
    clientCon.send(currentMessage.encode())
    return runSystem, runClient


# Systemet
while runSystem:
    # Running if client is connected
    if runClient:
        if firstCon:
            message = input("Write to the server: ")
            counter = -1 #skulle gerne lave den første besked om til 0.
            runSystem, runClient = sendMessage(message, counter)
            firstCon = False

    else:
        run, clientCon = handshake()

# #et eller andet fejlfosøg.
# #Opretter udp  socket (DGRAM) (#TODONE: oprette en udp socket)
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print('Client: Socket oprettet')
# #TODO sende en SYN ("Jeg vil gerne kommunikerer med dig!")
#     #TODO 1. printline der siger  "Hvor er serveren?
#
# #Forbinder socket til port hvor serveren er
# print('Hvor er serveren?')
# host = input(str('Indtast ip adresse: '))
# port = 10000
# client_socket.connect((host, port))
# print('forbundet til server')
#     #TODO Indtaste din IP(localhost i dette tilfælde)
#     #TODO - server vil checke om det stemmer overens.
#
# #TODO ACK ( "Fedt! Nu kan vi snakke sammen!"
# #TODO client, er nu accepteret til at kunne chatte med serveren.  ("JOIN OK" reposonse evt)
#     #TODO client skal kunne skrive besked
#     #TODO at kunne modtage den automatiske besked fra server
#
#
# message = 'Madkasse'
# try:
#     #Sender
#     print('Client sender: ' + message)
#     client_socket.sendto(message.encode(), server_address)
#
#     #Modtager
#     data, server = client_socket.recvfrom(4096)
#     data = data.decode()
#     print('Client modtaget: ' + data)
#
#
# finally:
#     print('Client: closing socket')
#     client_socket.close()
# #endregion