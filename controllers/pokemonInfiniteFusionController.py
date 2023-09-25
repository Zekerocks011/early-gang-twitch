import time, random, asyncio; from libraries import chatPlays
timeSinceLastMessage = time.time()

# makes inputs when no one has typed in chat for a while
async def idleBot():

    # checks if idle bot is supposed to be on and if no one has chatted
    while chatPlays.idleBotPlaying:
        if timeSinceLastMessage <= (time.time() - 5 * 60) and not chatPlays.killSwitch:

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
                        await holdA()
                    case 4:
                        await holdB()
                    case 5:
                        await mashB()
                    case 6:
                        await mashA()

            # 75% chance of directionals
            else:
                dice = random.randint(1, 8)
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
                        await holdDown()
                    case 6:
                        await holdLeft()
                    case 7:
                        await holdRight()
                    case 8:
                        await holdUp()

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
        if (not chatPlays.snackShot or chatPlays.snackHealed) and not chatPlays.killSwitch:

            # sleepy snack controls
            if chatPlays.currentSnack == "sleepy":

                # time between inputs
                await asyncio.sleep(random.randint(60, 720))

                # 5% chance of no action
                dice = random.randint(1, 100)
                if dice < 96:
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

            # chris snack controls
            elif chatPlays.currentSnack == "chris":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 14)
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
                            await holdUp()
                        case 6:
                            await holdDown()
                        case 7:
                            await holdLeft()
                        case 8:
                            await holdDown()
                        case 9:
                            await a()
                        case 10:
                            await b()
                        case 11:
                            await holdA()
                        case 12:
                            await holdB()
                        case 13:
                            await mashB()
                        case 14:
                            await mashA()

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
                                await holdUp()
                            case 6:
                                await holdDown()
                            case 7:
                                await holdLeft()
                            case 8:
                                await holdDown()
                            case 9:
                                await a()
                            case 10:
                                await b()

            # silly snack controls
            elif chatPlays.currentSnack == "silly":

                # time between inputs
                await asyncio.sleep(random.randint(10, 80))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 8)
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
                            await holdUp()
                        case 6:
                            await holdDown()
                        case 7:
                            await holdLeft()
                        case 8:
                            await holdDown()

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
                            await up()
                        case 3:
                            await left()
                        case 4:
                            await right()
                        case 5:
                            await b()
                        case 6:
                            await mashB()

            # sonic snack controls
            elif chatPlays.currentSnack == "sonic":

                # time between inputs
                await asyncio.sleep(random.randint(20, 60))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    dice = random.randint(1, 8)
                    match dice:
                        case 1:
                            await holdDown()
                        case 2:
                            await holdLeft()
                        case 3:
                            await holdRight()
                        case 4:
                            await holdUp()
                        case 5:
                           await mashB()
                        case 6:
                            await mashA()
                        case 7:
                            await holdB()
                        case 8:
                            await holdA()

        else:
            await asyncio.sleep(5)

# chat controls
async def controller(message):

    # makes sure chat is playing
    if chatPlays.chatPlaying is True and not chatPlays.killSwitch:
        global timeSinceLastMessage
        timeSinceLastMessage = time.time()
        message = message.content.lower()

        # making inputs
        if message == "a":
            await a()
        elif message == "b":
            await b()
        elif "mash a" in message:
            await mashA()
        elif "mash b" in message:
            await mashB()
        elif "hold a" in message:
            await holdA()
        elif "hold b" in message:
            await holdB()
        elif "hold up" in message:
            await holdUp()
        elif "hold down" in message:
            await holdDown()
        elif "hold left" in message:
            await holdLeft()
        elif "hold right" in message:
            await holdRight()
        elif "up" in message:
            await up()
        elif "down" in message:
            await down()
        elif "left" in message:
            await left()
        elif "right" in message:
            await right()
        elif "stop" in message:
            await stop()

# define controls down here
async def a():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("C"), .2)

async def holdA():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("C"), 5)

async def mashA():
    mashTime = 0
    while mashTime <= 5:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("C"), .2)
        mashTime += .2 + .3
        await asyncio.sleep(.3)

async def b():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("X"), .2)

async def holdB():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("X"), 5)

async def mashB():
    mashTime = 0
    while mashTime <= 5:
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("X"), .2)
        mashTime += .2 + .3
        await asyncio.sleep(.3)

async def holdUp():
    await chatPlays.releaseKey(chatPlays.keyCodes.get("S"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("A"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("D"))
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), 5)

async def holdDown():
    await chatPlays.releaseKey(chatPlays.keyCodes.get("W"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("A"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("D"))
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), 5)

async def holdLeft():
    await chatPlays.releaseKey(chatPlays.keyCodes.get("D"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("S"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("W"))
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), 5)

async def holdRight():
    await chatPlays.releaseKey(chatPlays.keyCodes.get("A"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("W"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("S"))
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), 5)

async def up():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), .2)

async def down():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), .2)

async def left():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), .2)

async def right():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), .2)

async def stop():
    await chatPlays.releaseKey(chatPlays.keyCodes.get("C"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("X"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("W"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("A"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("S"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("D"))