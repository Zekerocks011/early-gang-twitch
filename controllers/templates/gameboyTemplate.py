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
                dice = random.randint(1, 6)
                match dice:
                    case 1:
                        await a()
                    case 2:
                        await b()
                    case 3:
                        await select()
                    case 4:
                        await start()
                    case 5:
                        await l()
                    case 6:
                        await r()

            # 75% chance of directionals
            else:
                dice = random.randint(1, 4)
                match dice:
                    case 1:
                        await up()
                    case 2:
                        await down()
                    case 3:
                        await left()
                    case 4:
                        await right()

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
                    dice = random.randint(1, 5)
                    match dice:
                        case 1:
                            await up()
                        case 2:
                            await down()
                        case 3:
                            await left()
                        case 4:
                            await right()
                        case 5:
                            await b()

            # chris snack controls
            elif chatPlays.currentSnack == "chris":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 10)
                    match dice:
                        case 1:
                            await up()
                        case 2:
                            await down()
                        case 3:
                            await left()
                        case 4:
                            await right()
                        case 5:
                            await a()
                        case 6:
                            await b()
                        case 7:
                            await select()
                        case 8:
                            await start()
                        case 9:
                            await l()
                        case 10:
                            await r()

            # burst snack controls
            elif chatPlays.currentSnack == "burst":

                # time between inputs
                await asyncio.sleep(random.randint(300, 900))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    for i in range(5):
                        dice = random.randint(1, 10)
                        match dice:
                            case 1:
                                await up()
                            case 2:
                                await down()
                            case 3:
                                await left()
                            case 4:
                                await right()
                            case 5:
                                await a()
                            case 6:
                                await b()
                            case 7:
                                await select()
                            case 8:
                                await start()
                            case 9:
                                await l()
                            case 10:
                                await r()

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
                            await up()
                        case 2:
                            await down()
                        case 3:
                            await left()
                        case 4:
                            await right()

            # cautious snack controls
            elif chatPlays.currentSnack == "cautious":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 20% chance of no action
                dice = random.randint(1, 5)
                if dice != 1:
                    dice = random.randint(1, 6)
                    match dice:
                        case 1:
                            await down()
                        case 2:
                            await l()
                        case 3:
                            await r()
                        case 4:
                            await select()
                        case 5:
                            await b()
                        case 6:
                            await start()

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
                            await up()
                        case 2:
                            await down()
                        case 3:
                            await left()
                        case 4:
                            await right()
                        case 5:
                            await a()
                        case 6:
                            await b()
        else:
            await asyncio.sleep(5)

# chat controls
async def controller(message):

    # makes sure chat is playing
    if chatPlays.chatPlaying is True:
        global timeSinceLastMessage
        timeSinceLastMessage = time.time()
        message = message.content.lower()

        # making inputs
        if message == "a":
            await a()
        elif message == "b":
            await b()
        elif message == "r":
            await r()
        elif message == "l":
            await l()
        elif "select" in message:
            await select()
        elif "start" in message:
            await start()
        elif "up" in message:
            await up()
        elif "down" in message:
            await down()
        elif "left" in message:
            await left()
        elif "right" in message:
            await right()

async def a():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("L"), .2)

async def b():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("K"), .2)

async def l():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("I"), .2)

async def r():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("O"), .2)

async def select():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("P"), .2)

async def start():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("U"), .2)

async def up():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), .2)

async def down():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), .2)

async def left():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), .2)

async def right():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), .2)