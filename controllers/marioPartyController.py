# imports
import time
import random
import asyncio
from libraries import chatPlays
timeSinceLastMessage = time.time()

# makes inputs when no one has typed in chat for a while
async def idleBot():

    # checks if idle bot is supposed to be on and if no one has chatted
    while chatPlays.idleBotPlaying:
        if timeSinceLastMessage <= (time.time() - 5 * 60):

            # tell obs to show idle bot is active
            if not chatPlays.idleBotStatus:
                chatPlays.idleBotStatus = True
                await chatPlays.updateSnatus()

            # time between inputs
            await asyncio.sleep(random.randint(1, 10) / 10)

            # 25% chance of non directionals
            dice = random.randint(1, 4)
            if dice == 1:
                dice = random.randint(1, 9)
                match dice:
                    case 1:
                        await a(True if random.randint(1, 2) == 1 else False)
                    case 2:
                        await b(True if random.randint(1, 2) == 1 else False)
                    case 3:
                        await x(True if random.randint(1, 2) == 1 else False)
                    case 4:
                        await start(True if random.randint(1, 2) == 1 else False)
                    case 5:
                        await mashB(True if random.randint(1, 2) == 1 else False)
                    case 6:
                        await mashA(True if random.randint(1, 2) == 1 else False)
                    case 7:
                        await x(True if random.randint(1, 2) == 1 else False)
                    case 8:
                        await l(True if random.randint(1, 2) == 1 else False)
                    case 9:
                        await r(True if random.randint(1, 2) == 1 else False)

            # 75% chance of directionals
            else:
                dice = random.randint(1, 4)
                match dice:
                    case 1:
                        await up(True if random.randint(1, 2) == 1 else False)
                    case 2:
                        await down(True if random.randint(1, 2) == 1 else False)
                    case 3:
                        await left(True if random.randint(1, 2) == 1 else False)
                    case 4:
                        await right(True if random.randint(1, 2) == 1 else False)

        # tell obs idle bot is inactive
        else:
            if chatPlays.idleBotStatus:
                chatPlays.idleBotStatus = False
                await chatPlays.updateSnatus()
            await asyncio.sleep(5)

# makes inputs every so often
async def inputBot():

    # checks if conditions are right
    while chatPlays.inputBotPlaying:
        if not chatPlays.snackShot or chatPlays.snackHealed:

            # sleepy snack controls
            if chatPlays.currentSnack == "sleepy":

                # time between inputs
                await asyncio.sleep(random.randint(60, 720))

                # 5% chance of no action
                dice = random.randint(1, 100)
                if dice < 96:
                    dice = random.randint(1, 6)
                    match dice:
                        case 1:
                            await up(True if random.randint(1, 2) == 1 else False)
                        case 2:
                            await down(True if random.randint(1, 2) == 1 else False)
                        case 3:
                            await left(True if random.randint(1, 2) == 1 else False)
                        case 4:
                            await right(True if random.randint(1, 2) == 1 else False)
                        case 5:
                            await a(True if random.randint(1, 2) == 1 else False)
                        case 6:
                            await b(True if random.randint(1, 2) == 1 else False)

            # chris snack controls
            elif chatPlays.currentSnack == "chris":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 13)
                    match dice:
                        case 1:
                            await up(True if random.randint(1, 2) == 1 else False)
                        case 2:
                            await down(True if random.randint(1, 2) == 1 else False)
                        case 3:
                            await left(True if random.randint(1, 2) == 1 else False)
                        case 4:
                            await right(True if random.randint(1, 2) == 1 else False)
                        case 5:
                            await a(True if random.randint(1, 2) == 1 else False)
                        case 6:
                            await x(True if random.randint(1, 2) == 1 else False)
                        case 7:
                            await b(True if random.randint(1, 2) == 1 else False)
                        case 8:
                            await start(True if random.randint(1, 2) == 1 else False)
                        case 9:
                            await mashA(True if random.randint(1, 2) == 1 else False)
                        case 10:
                            await mashB(True if random.randint(1, 2) == 1 else False)
                        case 11:
                            await y(True if random.randint(1, 2) == 1 else False)
                        case 12:
                            await l(True if random.randint(1, 2) == 1 else False)
                        case 13:
                            await r(True if random.randint(1, 2) == 1 else False)

            # burst snack controls
            elif chatPlays.currentSnack == "burst":

                # time between inputs
                await asyncio.sleep(random.randint(300, 900))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    for i in range(5):
                        dice = random.randint(1, 5)
                        match dice:
                            case 1:
                                await up(True if random.randint(1, 2) == 1 else False)
                            case 2:
                                await down(True if random.randint(1, 2) == 1 else False)
                            case 3:
                                await left(True if random.randint(1, 2) == 1 else False)
                            case 4:
                                await right(True if random.randint(1, 2) == 1 else False)
                            case 5:
                                await a(True if random.randint(1, 2) == 1 else False)

            # silly snack controls
            elif chatPlays.currentSnack == "silly":

                # time between inputs
                await asyncio.sleep(random.randint(10, 80))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 4)
                    match dice:
                        case 1:
                            await up(True if random.randint(1, 2) == 1 else False)
                        case 2:
                            await down(True if random.randint(1, 2) == 1 else False)
                        case 3:
                            await left(True if random.randint(1, 2) == 1 else False)
                        case 4:
                            await right(True if random.randint(1, 2) == 1 else False)

            # cautious snack controls
            elif chatPlays.currentSnack == "cautious":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 20% chance of no action
                dice = random.randint(1, 5)
                if dice != 1:
                    dice = random.randint(1, 4)
                    match dice:
                        case 1:
                            await b(True if random.randint(1, 2) == 1 else False)
                        case 2:
                            await x(True if random.randint(1, 2) == 1 else False)
                        case 3:
                            await down(True if random.randint(1, 2) == 1 else False)
                        case 4:
                            await mashA(True if random.randint(1, 2) == 1 else False)

            # sonic snack controls
            elif chatPlays.currentSnack == "sonic":

                # time between inputs
                await asyncio.sleep(random.randint(20, 60))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    dice = random.randint(1, 6)
                    match dice:
                        case 1:
                            await up(True if random.randint(1, 2) == 1 else False)
                        case 2:
                            await down(True if random.randint(1, 2) == 1 else False)
                        case 3:
                            await left(True if random.randint(1, 2) == 1 else False)
                        case 4:
                            await right(True if random.randint(1, 2) == 1 else False)
                        case 5:
                            await mashB(True if random.randint(1, 2) == 1 else False)
                        case 6:
                            await mashA(True if random.randint(1, 2) == 1 else False)
        else:
            await asyncio.sleep(5)

# chat controls
async def controller(message):

    # makes sure chat is playing
    if chatPlays.chatPlaying is True:
        global timeSinceLastMessage
        timeSinceLastMessage = time.time()

        # making inputs
        if message.content.lower() == "a":
            await a("a" <= message.author.name[0] <= "m")
        elif message.content.lower() == "b":
            await b("a" <= message.author.name[0] <= "m")
        elif message.content.lower() == "x":
            await x("a" <= message.author.name[0] <= "m")
        elif message.content.lower() == "y":
            await x("a" <= message.author.name[0] <= "m")
        elif message.content.lower() == "l":
            await x("a" <= message.author.name[0] <= "m")
        elif message.content.lower() == "r":
            await x("a" <= message.author.name[0] <= "m")
        elif "start" in message.content.lower():
            await start("a" <= message.author.name[0] <= "m")
        elif "mash a" in message.content.lower():
            await mashA("a" <= message.author.name[0] <= "m")
        elif "mash b" in message.content.lower():
            await mashB("a" <= message.author.name[0] <= "m")
        elif "up" in message.content.lower():
            await up("a" <= message.author.name[0] <= "m")
        elif "down" in message.content.lower():
            await down("a" <= message.author.name[0] <= "m")
        elif "left" in message.content.lower():
            await left("a" <= message.author.name[0] <= "m")
        elif "right" in message.content.lower():
            await right("a" <= message.author.name[0] <= "m")

async def a(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("X"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("N"), .2)

async def mashA(aCrew):
    mashTime = 0
    while mashTime <= 5:
        if aCrew:
            await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("X"), .2)
        else:
            await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("N"), .2)
        mashTime += .2 + .3
        await asyncio.sleep(.3)

async def b(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("Z"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("M"), .2)

async def mashB(aCrew):
    mashTime = 0
    while mashTime <= 5:
        if aCrew:
            await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("Z"), .2)
        else:
            await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("M"), .2)
        mashTime += .2 + .3
        await asyncio.sleep(.3)

async def x(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("C"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("B"), .2)

async def y(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("H"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("G"), .2)
    
async def l(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("T"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("E"), .2)

async def r(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("Y"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("R"), .2)

async def start(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("Q"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("O"), .2)

async def up(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("I"), .2)

async def down(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("K"), .2)

async def left(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("J"), .2)

async def right(aCrew):
    if aCrew:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), .2)
    else:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("L"), .2)
