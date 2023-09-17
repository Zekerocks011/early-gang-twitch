# imports
import time
import random
import asyncio
from libraries import chatPlays
import pydirectinput
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
                dice = random.randint(1, 7)
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
                        await interact()
                    case 6:
                        await crouch()
                    case 7:
                        await uncrouch()

            # 75% chance of directionals
            else:
                dice = random.randint(1, 4)
                match dice:
                    case 1:
                        await forwards()
                    case 2:
                        await backwards()
                    case 3:
                        await walk()
                    case 4:
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
                            await crouch()
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
                    dice = random.randint(1, 11)
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
                            await crouch()
                        case 7:
                            await uncrouch()
                        case 8:
                            await forwards()
                        case 9:
                            await backwards()
                        case 10:
                            await walk()
                        case 11:
                            await stop()

            # burst snack controls
            elif chatPlays.currentSnack == "burst":

                # time between inputs
                await asyncio.sleep(random.randint(300, 900))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    for i in range(5):
                        dice = random.randint(1, 9)
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
                                await forwards()
                            case 7:
                                await crouch()
                            case 8:
                                await backwards()
                            case 9:
                                await uncrouch()

            # silly snack controls
            elif chatPlays.currentSnack == "silly":

                # time between inputs
                await asyncio.sleep(random.randint(10, 80))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
                    dice = random.randint(1, 5)
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
                            await crouch()
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
                            await forwards()
                        case 2:
                            await backwards()
                        case 3:
                            await stop()
                        case 4:
                            await walk()

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
        if "look up" in message:
            await lookUp()
        elif "look down" in message:
            await lookDown()
        elif "look left" in message:
            await lookLeft()
        elif "look right" in message:
            await lookRight()
        elif "interact" in message:
            await interact()
        elif "crouch" in message:
            await crouch()
        elif "uncrouch" in message:
            await uncrouch()
        elif "forwards" in message:
            await forwards()
        elif "backwards" in message:
            await backwards()
        elif "left" in message:
            await left()
        elif "right" in message:
            await right()
        elif "jump" in message:
            await jump()
        elif "walk" in message:
            await walk()
        elif "stop" in message:
            await stop()

async def lookUp():
    pydirectinput.move(xOffset = 0, yOffset = -50, duration = .5, relative = True)

async def lookDown():
    pydirectinput.move(xOffset = 0, yOffset = 50, duration = .5, relative = True)

async def lookLeft():
    pydirectinput.move(xOffset = -50, yOffset = 0, duration = .5, relative = True)

async def lookRight():
    pydirectinput.move(xOffset = 50, yOffset = 0, duration = .5, relative = True)

async def interact():
    pydirectinput.click()

async def forwards():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("W"), .2)

async def backwards():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("S"), .2)

async def left():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("A"), .2)

async def right():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("D"), .2)

async def jump():
    await chatPlays.holdAndReleaseKey(chatPlays.keyCodes.get("SPACE"), .2)

async def crouch():
    await chatPlays.holdKey(chatPlays.keyCodes.get("CONTROL"))

async def uncrouch():
    await chatPlays.releaseKey(chatPlays.keyCodes.get("CONTROL"))

async def walk():
    pydirectinput.mouseDown(button = "right")

async def stop():
    pydirectinput.mouseUp(button = "right")