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
                dice = random.randint(1, 4)
                match dice:
                    case 1:
                        await a()
                    case 2:
                        await b()
                    case 3:
                        await select()
                    case 4:
                        await start()

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
        if (not chatPlays.snackShot or chatPlays.snackHealed) and not chatPlays.killSwitch:

            # sleepy snack controls
            if chatPlays.currentSnack == "sleepy":

                # time between inputs
                await asyncio.sleep(random.randint(60, 720))

                # 5% chance of no action
                dice = random.randint(1, 100)
                if dice < 96:
                    dice = random.randint(1, 16)
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
                            await holdA()
                        case 11:
                            await b()
                        case 12:
                            await holdB()
                        case 15:
                            await select()
                        case 16:
                            await start()

            # chris snack controls
            elif chatPlays.currentSnack == "chris":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 16)
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
                            await holdA()
                        case 11:
                            await b()
                        case 12:
                            await holdB()
                        case 15:
                            await select()
                        case 16:
                            await start()

            # burst snack controls
            elif chatPlays.currentSnack == "burst":

                # time between inputs
                await asyncio.sleep(random.randint(300, 900))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    for i in range(5):
                        dice = random.randint(1, 16)
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
                                await holdA()
                            case 11:
                                await b()
                            case 12:
                                await holdB()
                            case 15:
                                await select()
                            case 16:
                                await start()

            # silly snack controls
            elif chatPlays.currentSnack == "silly":

                # time between inputs
                await asyncio.sleep(random.randint(10, 80))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 9)
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
                            await slightUp()
                        case 2:
                            await slightDown()
                        case 3:
                            await slightRight()
                        case 4:
                            await slightLeft()
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
                    dice = random.randint(1, 6)
                    match dice:
                        case 1:
                            await slightUp()
                        case 2:
                            await slightDown()
                        case 3:
                            await slightLeft()
                        case 4:
                            await slightRight()
                        case 5:
                            await mashA()
                        case 6:
                            await mashB()
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
        elif "hold a" in message:
            await holdA()
        elif "mash a" in message:
            await mashA()
        elif message == "b":
            await b()
        elif "hold b" in message:
            await holdB()
        elif "mash b" in message:
            await mashB()
        elif "select" in message:
            await select()
        elif "start" in message:
            await start()
        elif "hold up" in message:
            await holdUp()
        elif "hold down" in message:
            await holdDown()
        elif "hold left" in message:
            await holdLeft()
        elif "hold right" in message:
            await holdRight()
        elif "slup" in message:
            await slightUp()
        elif "slown" in message:
            await slightDown()
        elif "sleft" in message:
            await slightLeft()
        elif "slight" in message:
            await slightRight()
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

if chatPlays.mode == "keyboard":
    async def a():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("L"), .2)

    async def holdA():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("L"), 5)

    async def mashA():
        mashTime = 0
        while mashTime <= 5:
            await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("L"), .2)
            mashTime += .2 + .3
            await asyncio.sleep(.3)

    async def b():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("K"), .2)

    async def holdB():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("K"), 5)

    async def mashB():
        mashTime = 0
        while mashTime <= 5:
            await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("K"), .2)
            mashTime += .2 + .3
            await asyncio.sleep(.3)

    async def select():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("P"), .2)

    async def start():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("U"), .2)

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

    async def slightUp():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), .002)

    async def slightDown():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), .002)

    async def slightLeft():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), .002)

    async def slightRight():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), .002)

    async def up():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), .2)

    async def down():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), .2)

    async def left():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), .2)

    async def right():
        await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), .2)

    async def stop():
        await chatPlays.releaseKey(chatPlays.keyCodes.get("K"))
        await chatPlays.releaseKey(chatPlays.keyCodes.get("L"))
        await chatPlays.releaseKey(chatPlays.keyCodes.get("U"))
        await chatPlays.releaseKey(chatPlays.keyCodes.get("P"))
        await chatPlays.releaseKey(chatPlays.keyCodes.get("W"))
        await chatPlays.releaseKey(chatPlays.keyCodes.get("A"))
        await chatPlays.releaseKey(chatPlays.keyCodes.get("S"))
        await chatPlays.releaseKey(chatPlays.keyCodes.get("D"))

if chatPlays.mode == "controller":
    async def a():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("a"), .2)
    async def holdA():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("a"), 5)
    async def mashA():
        mashTime = 0
        while mashTime <= 5:
            await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("a"), .2)
            mashTime += .2 + .3
            await asyncio.sleep(.3)
    async def b():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("b"), .2)
    async def holdB():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("b"), 5)
    async def mashB():
        mashTime = 0
        while mashTime <= 5:
            await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("b"), .2)
            mashTime += .2 + .3
            await asyncio.sleep(.3)
    async def select():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("select"), .2)

    async def start():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("start"), .2)

    async def holdUp():
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("down"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("left"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("right"))
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("up"), 5)

    async def holdDown():
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("up"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("left"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("right"))
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("down"), 5)

    async def holdLeft():
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("up"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("down"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("right"))
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("left"), 5)

    async def holdRight():
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("up"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("down"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("left"))
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("right"), 5)

    async def slightUp():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("up"), .002)

    async def slightDown():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("down"), .002)

    async def slightLeft():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("left"), .002)

    async def slightRight():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("right"), .002)

    async def up():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("up"), .2)

    async def down():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("down"), .2)

    async def left():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("left"), .2)

    async def right():
        await chatPlays.holdAndReleaseKey(chatPlays.controllerCodes.get("right"), .2)
        
    async def stop():
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("up"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("down"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("left"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("right"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("a"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("b"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("start"))
        await chatPlays.releaseKey(chatPlays.controllerCodes.get("select"))
