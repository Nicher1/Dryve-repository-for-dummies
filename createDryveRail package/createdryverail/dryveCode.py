import socket
import time
read = 0
write = 1
profileAcceleration = 300
profileDeceleration = 300
HOST = "172.31.1.101"
PORT = 503



# Create TCP/IP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Variables
def establishConnection():
    s.connect((HOST, PORT))

# Commands/arrays -------------------------------------------

status = [0, 0, 0, 0, 0, 13, 0, 43, 13, read, 0, 0, 96, 65, 0, 0, 0, 0, 2]
statusArray = bytearray(status)

shutdown = [0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 96, 64, 0, 0, 0, 0, 2, 6, 0]
shutdownArray = bytearray(shutdown)

switchOn = [0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 96, 64, 0, 0, 0, 0, 2, 7, 0]
switchOnArray = bytearray(switchOn)

enableOperation = [0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0x40, 0, 0, 0, 0, 2, 15, 0]
enableOperationArray = bytearray(enableOperation)

def extractBytes(integer):
    return divmod(integer, 0x100)[::-1]

# Function for shutdown
def setShdn():
    sendCommand(shutdownArray)
    while (sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 33, 6]
           and sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 33, 22]
           and sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 33, 2]):
        print("wait for shutdown")

        # 1 Sekunde Verzoegerung
        # 1 second delay
        time.sleep(1)


# Function for switching on
def setSwon():
    sendCommand(switchOnArray)
    while (sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 35, 6]
           and sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 35, 22]
           and sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 35, 2]):
        print("wait for switch on")

        # 1 Sekunde Verzoegerung
        # 1 second delay
        time.sleep(1)


# Function for enabling operation
def setOpEn():
    sendCommand(enableOperationArray)
    while (sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 39, 6]
           and sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 39, 22]
           and sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 96, 65, 0, 0, 0, 0, 2, 39, 2]):
        print("wait for op en")

        # 1 Sekunde Verzoegerung
        # 1 second delay
        time.sleep(1)


def setMode(mode):
    # Set operation modes in object 6060h Modes of Operation
    sendCommand(bytearray([0, 0, 0, 0, 0, 14, 0, 43, 13, 1, 0, 0, 96, 96, 0, 0, 0, 0, 1, mode]))
    while (sendCommand(bytearray([0, 0, 0, 0, 0, 13, 0, 43, 13, 0, 0, 0, 96, 97, 0, 0, 0, 0, 1])) != [0, 0, 0, 0, 0, 14,
                                                                                                      0, 43, 13, 0, 0,
                                                                                                      0, 96, 97, 0, 0,
                                                                                                      0, 0, 1, mode]):
        # 1 second delay
        time.sleep(1)


def startProcedure():
    reset = [0, 0, 0, 0, 0, 15, 0, 43, 13, write, 0, 0, 96, 64, 0, 0, 0, 0, 2, 0, 1]
    resetArray = bytearray(reset)
    sendCommand(resetArray)

    sendCommand(statusArray)

    setShdn()
    setSwon()
    setOpEn()
    setMode(1)
    # set velocity and acceleration of profile
    sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0x81, 0, 0, 0, 0, 2, 0x2c, 0x1]))
    # Profile acceleration set below
    sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0x83, 0, 0, 0, 0, 2, extractBytes(profileAcceleration)[0], extractBytes(profileAcceleration)[1]]))
    # Profile deacceleration set below
    sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0x84, 0, 0, 0, 0, 2, extractBytes(profileDeceleration)[0], extractBytes(profileDeceleration)[1]]))


def targetPosition(target, rw=1):
    setMode(1)

    # Check if target datavalue is within range
    if target > 0xffff:
        print("Invalid target specified")
    else:
        if target > 255:  # If the target is over 2 bytes large, split the data correctly into two seperate bytes.
            target2Byt = extractBytes(target)
            targetPos = [0, 0, 0, 0, 0, 15, 0, 43, 13, rw, 0, 0, 0x60, 0x7a, 0, 0, 0, 0, 2, target2Byt[0],
                         target2Byt[1]]
        elif target <= 255:
            targetPos = [0, 0, 0, 0, 0, 14, 0, 43, 13, rw, 0, 0, 0x60, 0x7a, 0, 0, 0, 0, 1, target]
        targetPosArray = bytearray(targetPos)
        sendCommand(targetPosArray)


        # Execute command
        sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, rw, 0, 0, 0x60, 0x40, 0, 0, 0, 0, 2, 0x1f, 0x0]))

        time.sleep(0.01)

        # Check Statusword for target reached
        while (sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 0x60, 0x41, 0, 0, 0, 0, 2, 39, 22]):
            # 1 second delay
            time.sleep(0.01)

        sendCommand(enableOperationArray)


# Definition of the function to send and receive data
def sendCommand(data):
    # Create socket and send request
    s.send(data)
    res = s.recv(24)
    # #Print response telegram
    # print(list(res))
    return list(res)

def getPosition():
    getPositionFromDryve = bytearray([0, 0, 0, 0, 0, 13, 0, 43, 13, read, 0, 0, 0x60, 0x64, 0, 0, 0, 0, 4])
    positionRaw = sendCommand(getPositionFromDryve)
    position = 0
    for i in range(4):
        position = position + positionRaw[i+19] * 256 ** i
    return position

def homing():
    setMode(6)

    setHomingMethodLSN = [0, 0, 0, 0, 0, 14, 0, 43, 13, write, 0, 0, 96, 152, 0, 0, 0, 0, 1, 17]
    setHomingMethodLSNArray = bytearray(setHomingMethodLSN)
    sendCommand(setHomingMethodLSNArray)

    # Set homing speeds 6099h
    sendCommand(bytearray([0, 0, 0, 0, 0, 14, 0, 43, 13, 1, 0, 0, 0x60, 0x99, 0, 0, 0, 0, 1, 200]))
    sendCommand(bytearray([0, 0, 0, 0, 0, 14, 0, 43, 13, 1, 0, 0, 0x60, 0x99, 1, 0, 0, 0, 1, 200]))
    sendCommand(bytearray([0, 0, 0, 0, 0, 14, 0, 43, 13, 1, 0, 0, 0x60, 0x99, 2, 0, 0, 0, 1, 200]))

    # Set acceleration 609Ah
    sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0x9a, 0, 0, 0, 0, 2, 0xe8, 0x3]))

    time.sleep(0.1)

    print("Begin Homing")
    # Start Homing 6040h
    sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0x40, 0, 0, 0, 0, 2, 0x1f, 0]))

    while (sendCommand(statusArray) != [0, 0, 0, 0, 0, 15, 0, 43, 13, 0, 0, 0, 0x60, 0x41, 0, 0, 0, 0, 2, 39, 22]):
        # 1 second delay
        time.sleep(0.1)

    print("Homing complete")

    sendCommand(enableOperationArray)


# Definition of the function to send velocity data and convert decimal to 1/2-byte.
def targetVelocity(target):
    setMode(3)
    def extractBytes(integer):
        return divmod(integer, 0x100)[::-1]
    if target > 0xffff:
        print("Invalid target velocity specified")
    else:
        if target > 255:  # If the target is over 2 bytes large, split the data correctly into two seperate bytes.
            targetVel2Byt = extractBytes(target)
            # set velocity and acceleration of profile
            sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0xFF, 0, 0, 0, 0, 2, targetVel2Byt[0], targetVel2Byt[1]]))
        elif target <= 255:
            # set velocity and acceleration of profile
            sendCommand(bytearray(
                [0, 0, 0, 0, 0, 14, 0, 43, 13, 1, 0, 0, 0x60, 0xFF, 0, 0, 0, 0, 1, target]))

def profileVelocity(target):
    def extractBytes(integer):
        return divmod(integer, 0x100)[::-1]
    if target > 0xffff or target == 0:
        print("Invalid target velocity specified")
    else:
        if target > 255:  # If the target is over 2 bytes large, split the data correctly into two seperate bytes.
            targetVel2Byt = extractBytes(target)
            # set velocity and acceleration of profile
            sendCommand(bytearray([0, 0, 0, 0, 0, 15, 0, 43, 13, 1, 0, 0, 0x60, 0x81, 0, 0, 0, 0, 2, targetVel2Byt[0], targetVel2Byt[1]]))
        elif target <= 255:
            # set velocity and acceleration of profile
            sendCommand(bytearray(
                [0, 0, 0, 0, 0, 14, 0, 43, 13, 1, 0, 0, 0x60, 0x81, 0, 0, 0, 0, 1, target]))


def dryveInit():
    establishConnection()
    startProcedure()
    homing()
    setMode(1)

# Never input target position lower than 1. It will trigger the limit switch.
