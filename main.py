import asyncio
import warnings
import traceback; from libraries.chatPlays import *; from bots import commandBot, econBot, pollBot
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import subprocess

# subprocess.run(["python", "music.py"])
#subprocess.run(["python", "zorbeez.py"])

# main code loop
async def main():

    # setting up
    commandBot.ws.connect()
    await updateSnatus()

    # so you don't have to restart stream
    if await commandBot.bot.fetch_streams(user_logins = [commandBot.yourChannelName]):
        await startChatPlays()
        await startInputBot()
        await startIdleBot()
        await asyncio.sleep(5)
        

    # infinite loop to check stream statuses
    while True:
        try:
            # if streamer goes live
            if await commandBot.bot.fetch_streams(user_logins = [commandBot.streamerChannelName]) != [] and await commandBot.bot.fetch_streams(user_logins = [commandBot.yourChannelName]) != []:

                # shut down everything
                if chatPlaying:
                    await stopChatPlays()
                if inputBotPlaying:
                    await stopInputBot()
                if idleBotPlaying:
                    await stopIdleBot()

                # end stream
                if await commandBot.bot.fetch_streams(user_logins = [commandBot.yourChannelName]):

                    # start raid
                    users = await commandBot.bot.fetch_users([commandBot.yourChannelName, commandBot.streamerChannelName])

                    try:
                        await users[0].start_raid(commandBot.accessToken, users[1].id)
                    except:
                        print("FUCK TWITCH")
                    
                    # # display timer
                    response = ws.call(requests.GetSceneItemId(sceneName = "Main", sourceName = "raid status"))
                    raid_Status_Id = int(response.datain['sceneItemId'])
                    commandBot.ws.call(requests.SetSceneItemEnabled(sceneName = "Main", sceneItemId = raid_Status_Id, sceneItemEnabled = True))

                    # update timer
                    clock = [1, 30]
                    while clock != [0, 0]:
                        if clock[1] < 10:
                            ws.call(requests.SetInputSettings(inputName = "raid status", inputSettings = {"text": "RAID INCOMING\n" + str(clock[0]) + ":0" + str(clock[1])}))
                        else:
                            ws.call(requests.SetInputSettings(inputName = "raid status", inputSettings = {"text": "RAID INCOMING\n" + str(clock[0]) + ":" + str(clock[1])}))

                        if clock[1] == 0:
                            clock[1] = 59
                            clock[0] -= 1
                        else:
                            clock[1] -= 1
                        await asyncio.sleep(1)

                    # stop raid and hide timer
                    commandBot.ws.call(requests.StopStream())
                    commandBot.ws.call(requests.SetSceneItemEnabled(sceneName = "Main", sceneItemId = 2, sceneItemEnabled = True))

            # if streamer goes offline
            elif await commandBot.bot.fetch_streams(user_logins = [commandBot.yourChannelName]) == [] and await commandBot.bot.fetch_streams(user_logins = [commandBot.streamerChannelName]) == []:

                # start stream
                if not await commandBot.bot.fetch_streams(user_logins=[commandBot.yourChannelName]):
                    commandBot.ws.call(requests.StartStream())
                    await asyncio.sleep(5)
                if not chatPlaying:
                    await startChatPlays()
                if not inputBotPlaying:
                    await startInputBot()
                if not idleBotPlaying:
                    await startIdleBot()

            await asyncio.sleep(3)
        except:
            print("timed out, trying again")
            continue

# running command bot for inputs
async def setup():
    await asyncio.gather(commandBot.Bot().start(), econBot.Bot().start(), pollBot.Bot().start(), main())

# don't touch this
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup())
    loop.run_forever()
except Exception as e:
    print(traceback.format_exc())
