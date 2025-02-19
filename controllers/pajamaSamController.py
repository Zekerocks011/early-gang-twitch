import pyautogui, random, time, asyncio;
from libraries import chatPlays
timeSinceLastMessage = time.time()

# top x, top y, bottom x, bottom y
screenBoundaries = [10, 10, 400, 500]
quitButtonBoundaries = [50, 50, 100, 100]

# makes inputs when no one has typed in chat for a while
async def idleBot():
    # checks if idle bot is supposed to be on and if no one has chatted
    while chatPlays.idleBotPlaying:
        global timeSinceLastMessage

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
                await click()

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
                            await click()

            # chris snack controls
            elif chatPlays.currentSnack == "chris":

                # time between inputs
                await asyncio.sleep(random.randint(10, 120))

                # 33% chance of no action
                dice = random.randint(1, 3)
                if dice != 1:
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
                            await click()

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
                                await up()
                            case 2:
                                await down()
                            case 3:
                                await left()
                            case 4:
                                await right()
                            case 5:
                                await click()

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
                    dice = random.randint(1, 4)
                    match dice:
                        case 1:
                            await up()
                        case 2:
                            await down()
                        case 3:
                            await right()
                        case 4:
                            await left()

            # sonic snack controls
            elif chatPlays.currentSnack == "sonic":

                # time between inputs
                await asyncio.sleep(random.randint(20, 60))

                # 10% chance of no action
                dice = random.randint(1, 10)
                if dice != 1:
                    dice = random.randint(1, 4)
                    match dice:
                        case 1:
                            await right()
                        case 2:
                            await left()
                        case 3:
                            await up()
                        case 4:
                            await down()

        else:
            await asyncio.sleep(5)


# chat controls
async def controller(message):
    print(message)
    # makes sure chat is playing
    if chatPlays.chatPlaying is True and not chatPlays.killSwitch:
        global timeSinceLastMessage
        timeSinceLastMessage = time.time()
        message = message.content.lower()

        # making inputs
        if "click" in message:
            await click()
        elif "up" in message:
            await up()
        elif "down" in message:
            await down()
        elif "left" in message:
            await left()
        elif "right" in message:
            await right()

async def up():
    if pyautogui.position().y - 50 > screenBoundaries[1]:
        pyautogui.moveTo(pyautogui.position().x, pyautogui.position().y - 50, duration=.5)
    else:
        pyautogui.moveTo(pyautogui.position().x, screenBoundaries[1], duration=.5)


async def down():
    if pyautogui.position().y + 50 < screenBoundaries[3]:
        pyautogui.moveTo(pyautogui.position().x, (pyautogui.position().y + 50), duration=.5)
    else:
        pyautogui.moveTo(pyautogui.position().x, screenBoundaries[3], duration=.5)


async def left():
    if pyautogui.position().x - 50 > screenBoundaries[0]:
        pyautogui.moveTo((pyautogui.position().x - 50), pyautogui.position().y, duration=.5)
    else:
        pyautogui.moveTo(screenBoundaries[0], pyautogui.position().y, duration=.5)


async def right():
    if pyautogui.position().x + 50 < screenBoundaries[2]:
        pyautogui.moveTo((pyautogui.position().x + 50), pyautogui.position().y, duration=.5)
    else:
        pyautogui.moveTo(screenBoundaries[2], pyautogui.position().y, duration=.5)


async def click():
    if (quitButtonBoundaries[0] > pyautogui.position().x or pyautogui.position().x > quitButtonBoundaries[2]) or (quitButtonBoundaries[1] > pyautogui.position().y or pyautogui.position().y > quitButtonBoundaries[3]):
        pyautogui.mouseDown()
        await asyncio.sleep(.5)
        pyautogui.mouseUp()