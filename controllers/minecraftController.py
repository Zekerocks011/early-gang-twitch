import time, random, asyncio, pydirectinput; from libraries import chatPlays
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
                dice = random.randint(1, 24)
                match dice:
                    case 1:
                        await lookDown()
                    case 2:
                        await lookUp()
                    case 3:
                        await lookLeft()
                    case 4:
                        await lookRight()
                    case 5:
                        await attack()
                    case 6:
                        await holdAttack()
                    case 7:
                        await interact()
                    case 8:
                        await holdInteract()
                    case 9:
                        await inventory()
                    case 10:
                        await one()
                    case 11:
                        await two()
                    case 12:
                        await three()
                    case 13:
                        await four()
                    case 14:
                        await five()
                    case 15:
                        await six()
                    case 16:
                        await seven()
                    case 17:
                        await eight()
                    case 18:
                        await nine()
                    case 19:
                        await throw()
                    case 20:
                        await jump()
                    case 21:
                        await sneak()
                    case 22:
                        await sprint()
                    case 23:
                        await unsprint()
                    case 24:
                        await unsneak()

            # 75% chance of directionals
            else:
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
                        await holdRight()
                    case 9:
                        await stop()

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
                    dice = random.randint(1, 6)
                    match dice:
                        case 1:
                            await sneak()
                        case 2:
                            await stop()
                        case 3:
                            await lookDown()
                        case 4:
                            await lookUp()
                        case 5:
                            await lookLeft()
                        case 6:
                            await lookRight()

            # chris snack controls
            elif chatPlays.currentSnack == "chris":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 34)
                    match dice:
                        case 1:
                            await lookUp()
                        case 2:
                            await lookDown()
                        case 3:
                            await lookLeft()
                        case 4:
                            await lookRight()
                        case 5:
                            await interact()
                        case 6:
                            await sneak()
                        case 7:
                            await unsneak()
                        case 8:
                            await holdInteract()
                        case 9:
                            await holdAttack()
                        case 10:
                            await attack()
                        case 11:
                            await stop()
                        case 12:
                            await up()
                        case 13:
                            await down()
                        case 14:
                            await left()
                        case 15:
                            await right()
                        case 16:
                            await holdUp()
                        case 17:
                            await holdDown()
                        case 18:
                            await holdLeft()
                        case 19:
                            await holdRight()
                        case 20:
                            await inventory()
                        case 21:
                            await one()
                        case 22:
                            await two()
                        case 23:
                            await three()
                        case 24:
                            await four()
                        case 25:
                            await five()
                        case 26:
                            await six()
                        case 27:
                            await seven()
                        case 28:
                            await eight()
                        case 29:
                            await nine()
                        case 30:
                            await throw()
                        case 31:
                            await jump()
                        case 32:
                            await sprint()
                        case 33:
                            await unsprint()

            # burst snack controls
            elif chatPlays.currentSnack == "burst":

                # time between inputs
                await asyncio.sleep(random.randint(300, 900))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    for i in range(5):
                        dice = random.randint(1, 8)
                        match dice:
                            case 1:
                                await lookUp()
                            case 2:
                                await lookDown()
                            case 3:
                                await lookLeft()
                            case 4:
                                await lookRight()
                            case 5:
                                await up()
                            case 6:
                                await down()
                            case 7:
                                await left()
                            case 8:
                                await right()

            # silly snack controls
            elif chatPlays.currentSnack == "silly":

                # time between inputs
                await asyncio.sleep(random.randint(10, 80))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 10)
                    match dice:
                        case 1:
                            await lookUp()
                        case 2:
                            await lookDown()
                        case 3:
                            await lookLeft()
                        case 4:
                            await lookRight()
                        case 5:
                            await up()
                        case 6:
                            await down()
                        case 7:
                            await left()
                        case 8:
                            await right()
                        case 9:
                            await sneak()
                        case 10:
                            await unsneak()

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
                            await sneak()
                        case 2:
                            await stop()
                        case 3:
                            await lookUp()
                        case 4:
                            await lookDown()
                        case 5:
                            await lookLeft()
                        case 6:
                            await lookRight()

            # sonic snack controls
            elif chatPlays.currentSnack == "sonic":

                # time between inputs
                await asyncio.sleep(random.randint(20, 60))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    dice = random.randint(1, 5)
                    match dice:
                        case 1:
                            await holdUp()
                        case 2:
                            await sprint()
                        case 3:
                            await holdDown()
                        case 4:
                            await holdLeft()
                        case 5:
                            await holdRight()

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
        if "attack" in message:
            await attack()
        elif "one" in message or message == "1":
            await one()
        elif "two" in message or message == "2":
            await two()
        elif "three" in message or message == "3":
            await three()
        elif "four" in message or message == "4":
            await four()
        elif "five" in message or message == "5":
            await five()
        elif "six" in message or message == "6":
            await six()
        elif "seven" in message or message == "7":
            await seven()
        elif "eight" in message or message == "8":
            await eight()
        elif "nine" in message or message == "9":
            await nine()
        elif "hold attack" in message:
            await holdAttack()
        elif "inventory" in message:
            await inventory()
        elif "throw" in message:
            await throw()
        elif "unsprint" in message:
            await unsprint()
        elif "unsneak" in message:
            await unsneak()
        elif "sneak" in message:
            await sneak()
        elif "sprint" in message:
            await sprint()
        elif "look up" in message:
            await lookUp()
        elif "look down" in message:
            await lookDown()
        elif "look left" in message:
            await lookLeft()
        elif "look right" in message:
            await lookRight()
        elif "hold up" in message:
            await holdUp()
        elif "hold down" in message:
            await holdDown()
        elif "hold left" in message:
            await holdLeft()
        elif "hold right" in message:
            await holdRight()
        elif "up" in message or "forwards" in message:
            await up()
        elif "down" in message or "backwards" in message:
            await down()
        elif "left" in message:
            await left()
        elif "right" in message:
            await right()
        elif "interact" in message:
            await interact()
        elif "hold interact" in message:
            await holdInteract()
        elif "jump" in message:
            await jump()
        elif "stop" in message:
            await stop()


async def lookUp():
    pydirectinput.move(xOffset = 0, yOffset = -50, duration = 1, relative = True)

async def lookDown():
    pydirectinput.move(xOffset = 0, yOffset = 50, duration = 1, relative = True)

async def lookLeft():
    pydirectinput.move(xOffset = -50, yOffset = 0, duration = 1, relative = True)

async def lookRight():
    pydirectinput.move(xOffset = 50, yOffset = 0, duration = 1, relative = True)

async def up():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), .2)

async def down():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), .2)

async def left():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), .2)

async def right():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), .2)

async def holdUp():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), 5)

async def holdDown():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), 5)

async def holdLeft():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), 5)

async def holdRight():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), 5)

async def attack():
    pydirectinput.mouseDown(button = "left")
    await asyncio.sleep(.1)
    pydirectinput.mouseUp(button = "left")

async def holdAttack():
    pydirectinput.mouseDown(button = "left")
    await asyncio.sleep(5)
    pydirectinput.mouseUp(button = "left")

async def interact():
    pydirectinput.mouseDown(button="right")
    await asyncio.sleep(.1)
    pydirectinput.mouseUp(button="right")

async def holdInteract():
    pydirectinput.mouseDown(button = "right")
    await asyncio.sleep(5)
    pydirectinput.mouseUp(button = "right")

async def inventory():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("E"), .2)

async def one():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("ONE"), .2)

async def two():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("TWO"), .2)

async def three():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("THREE"), .2)

async def four():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("FOUR"), .2)

async def five():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("FIVE"), .2)

async def six():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("SIX"), .2)

async def seven():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("SEVEN"), .2)

async def eight():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("EIGHT"), .2)

async def nine():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("NINE"), .2)

async def throw():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("Q"), .2)

async def jump():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("SPACE"), .2)

async def sneak():
    await chatPlays.holdKey(chatPlays.keyCodes.get("SHIFT"))

async def sprint():
    await chatPlays.holdKey(chatPlays.keyCodes.get("CONTROL"))

async def unsneak():
    print("unsneak")
    await chatPlays.releaseKey(chatPlays.keyCodes.get("SHIFT"))

async def unsprint():
    await chatPlays.releaseKey(chatPlays.keyCodes.get("CONTROL"))

async def stop():
    pydirectinput.mouseUp(button = "right")
    pydirectinput.mouseUp(button = "left")
    await chatPlays.releaseKey(chatPlays.keyCodes.get("CONTROL"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("SHIFT"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("Q"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("E"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("ONE"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("TWO"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("THREE"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("FOUR"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("FIVE"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("SIX"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("SEVEN"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("EIGHT"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("NINE"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("SPACE"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("W"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("A"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("S"))
    await chatPlays.releaseKey(chatPlays.keyCodes.get("D"))