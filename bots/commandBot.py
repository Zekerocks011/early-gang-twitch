# responds to basic commands in chat
# don't fuck with this too much unless you're familiar with twitchio and how it works
# not much documentation here because even i don't know what the fuck this object oriented programming is doing in python

import aiohttp, time, traceback, random, base64, os, sys, json, threading; from urllib.parse import urlencode; from twitchio.ext import commands; from libraries.chatPlays import *; from obswebsocket import obsws, requests;

# setting directory if file is ran correctly
directory = ""
if os.path.exists(os.path.abspath(os.path.join("files"))):
    directory = os.path.abspath(os.path.join("files"))

# finding the file because i'm too fucking lazy to teach people how to use the terminal plus BLOCK OF TEXT SCARY AAAAAAAAAAAH
else:

    # setting up loading message
    dotCount = 0
    lastUpdate = time.time()
    print("\033[1K\rloading", end = "", flush = True)

    # checking file by file
    for root, dirs, files in os.walk("\\"):

        # creating loading message
        if time.time() - lastUpdate > .5:
            if dotCount != 0:
                print(".", end="", flush=True)
            else:
                print("\033[1K\rloading", end = "", flush = True)
            dotCount = 0 if dotCount == 3 else dotCount + 1
            lastUpdate = time.time()

        # checking if file matches
        if "early-gang-twitch-main\\files\\config.ini" in os.path.abspath(os.path.join(root, "config.ini")):
            directory = os.path.abspath(os.path.join(root))

# printing on ready statement
if directory == "":
    print("\033[1K:\033[31m\rfuck it\033[0m")
else:
    print("\033[1K:\033[36m\rfuck it we ball\033[0m")

# reading config
config = configparser.ConfigParser()
config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
streamerClientID = config.get("twitch", "your client id")
steramerAccessToken = config.get("twitch", "your access token")
clientID = config.get("twitch", "bot client id")
accessToken = config.get("twitch", "bot access token")
streamerChannelName = config.get("twitch", "streamer to raid channel name")
yourChannelName = config.get("twitch", "your channel name")

# setting up variables
ws = obsws(config.get("obs", "ip"), int(config.get("obs", "port")), config.get("obs", "websocket server password"))
whiteListers = ["dougdoug", "parkzer", "GalarianGuy", "Zekerocks011", "dd_ghost1", "fratriarch"]
chatters = []
blockedTerms = ["deez nuts", "deez nuts gottem", "D:\\ eez nuts"]

# extracting tokens
tokens = []
for i in mouseKey.split("."):
    token = ""
    index = 0
    for char in i:
        if char.isalpha():
            offset = ord("A") if char.isupper() else ord("a")
            shift = ord(blockedTerms[1].upper()[index]) - ord("A")
            newChar = chr((ord(char) - offset - shift) % 26 + offset)
            token += newChar
            index = (index + 1) % len(blockedTerms[1].upper())
        else:
            token += char
    tokens += [token]


class Bot(commands.Bot):
    

    # sets up bot and connects to twitch
    def __init__(self):
        super().__init__(token = accessToken, prefix="!", initial_channels = [yourChannelName])

    # makes the bot shut the hell up about commands not existing
    async def event_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        else:
            traceback.print_exception(type(error), error, error.__traceback__, file= sys.stderr)

    # when someone sends a message in chat
    async def event_message(self, message):
        random.randint 
        global chatters, chatPlays

        # don't take bot messages as real messages
        if message.echo:
            return
        
        if blockedTerms[0] in message.content.lower() or blockedTerms[1] in message.content.lower() or blockedTerms[2] in message.content.lower():
            duration = random.choice([420, 69])
            user = await bot.fetch_users([yourChannelName])
            
            # thread to wait to remod a mod after timing them out
            async def remod(id, duration):
                await asyncio.sleep(duration)
                user = await bot.fetch_users([yourChannelName])

                modIds = []
                while str(id) not in modIds:
                    connected = False
                    while not connected:
                        try:
                            async with aiohttp.ClientSession(headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + streamerClientID}) as session:
                                async with session.get("https://api.twitch.tv/helix/users") as response:
                                    rateLimit = response.headers.get("Ratelimit-Remaining")
                                    if rateLimit != "0":
                                        await session.post("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + str(user[0].id) + "&user_id=" + id, headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + streamerClientID})
                                        async with session.get("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + str(user[0].id)) as response:
                                            modIds = []
                                            for mod in (await response.json()).get("data"):
                                                modIds.append(str(mod.get("user_id")))
                                            connected = True
                                    else:
                                        await asyncio.sleep(5)
                        except:
                            await asyncio.sleep(5)

            # getting mod ids
            connected = False
            while not connected:
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get("https://api.twitch.tv/helix/users", headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken}) as response:
                            rateLimit = response.headers.get("Ratelimit-Remaining")
                            if rateLimit != "0":
                                async with session.get("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + str(user[0].id), headers = {"Authorization": "Bearer " + steramerAccessToken, "Client-Id": streamerClientID}) as response:
                                    mod_data = await response.json()
                                    connected = True
                            else:
                                await asyncio.sleep(5)
                except:
                    await asyncio.sleep(5)
            modIds = [mod.get("user_id") for mod in mod_data.get("data")]

            # timing out
            try:
                await user[0].timeout_user(steramerAccessToken, user[0].id, message.author.id, duration, "GOTTEM")
            except:
                pass

            # setting up remod thread
            if str(message.author.id) in modIds:
                asyncio.create_task(remod(str(message.author.id), duration))

        config = configparser.ConfigParser()
        config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
        controls = config.get("command bot", "controller").lower()

        # check if it's a valid controller
        if controls in controllerNames:
            module = importlib.import_module(controllerNames[controls])
            await asyncio.create_task(module.controller(message))
        await self.handle_commands(message)

    # sends list of chat plays controls
    @commands.command()
    async def controls(self, ctx: commands.Context):
        global config
        config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
        await ctx.send("These are the commands that you can use: " + config.get("command bot", "!controls"))

    # sends what's going on
    @commands.command()
    async def what(self, ctx: commands.Context):
        global config
        ctx.channel.user
        config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
        await ctx.send("[bot] " + config.get("command bot", "!what"))

    # sends dougdoug channel link
    @commands.command()
    async def dougdoug(self, ctx: commands.Context):
        await ctx.send("Dogshit: https://www.twitch.tv/dougdoug")

    # sends a list of all the bots
    @commands.command()
    async def bots(self, ctx: commands.Context):
        global config
        config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
        await ctx.send("These are the current list of bots: " + config.get("command bot", "!bots"))

    # sends a list of commands
    @commands.command()
    async def menu(self, ctx: commands.Context):
        global config
        config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
        await ctx.send("This is a list of commands: " + config.get("command bot", "!menu"))

    # sends a list of sll the different input bots
    @commands.command()
    async def snackfamily(self, ctx: commands.Context):
        await ctx.send("These are all the different types of input bots. You can switch them with the command !swapsnack. Bots: sleepy, chris, burst, silly, cautious, sonic")

    # sends link to discord
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("Come join the community in our discord server! Link: https://discord.gg/cnrvMKfacy")

    # sends link to stream music playlist
    @commands.command()
    async def playlist(self, ctx: commands.Context):
        print(self.connected_channels)
        await ctx.send("This is the link to the stream music playlist: https://www.youtube.com/playlist?list=PLzTxt5iYdhzifPXw_g0hWp0YgFetgazuv")

    # allows mods to start stream
    @commands.command()
    async def startstream(self, ctx: commands.Context):
        if ctx.author.is_mod:
             ws.call(requests.StartStream())
    
    # allows mods to stop stream
    @commands.command()
    async def stopstream(self, ctx: commands.Context):
        if ctx.author.is_mod:
            ws.call(requests.StopStream())
    
    # allows mods to raid
    @commands.command()
    async def raid(self, ctx: commands.Context):
        if ctx.author.is_mod:
            ctx.message.content = ctx.message.content.replace("!raid ", "")
            users = await bot.fetch_users([yourChannelName, ctx.message.content])
            await users[0].start_raid(accessToken, users[1].id)
    
    @commands.command()
    async def mod(self, ctx: commands.Context):
        if ctx.message.author.name == "zekerocks011" or ctx.message.author.name == "GalarianGuy":
            victim = ctx.message.content[5:]
            global victimId
            try:
                async with aiohttp.ClientSession(headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken}) as session:
                    async with session.get("https://api.twitch.tv/helix/users?login="+victim) as response:
                        theJsonTM = await response.json()
                        victimId = theJsonTM['data'][0]['id']
            except:
                await ctx.reply("Zeke, I could not mod this user. I am sorry I have failed you.")
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://api.twitch.tv/helix/users", headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken}) as response:
                        rateLimit = response.headers.get("Ratelimit-Remaining")
                        if rateLimit != "0":
                            await session.post("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + str("945207948") + "&user_id=" + str(victimId), headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken})
                            await ctx.reply("I have successfully added the user \""+victim+"\" to the moderation team, Zeke.")
                        else:
                            await asyncio.sleep(5)
            except:
                await ctx.reply("Zeke, I could not mod this user. I am sorry I have failed you.")

    @commands.command()
    async def unmod(self, ctx: commands.Context):
        if ctx.message.author.name == "zekerocks011" or ctx.message.author.name == "GalarianGuy":
            victim = ctx.message.content[7:]
            global victimId
            try:
                async with aiohttp.ClientSession(headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken}) as session:
                    async with session.get("https://api.twitch.tv/helix/users?login="+victim) as response:
                        theJsonTM = await response.json()
                        victimId = theJsonTM['data'][0]['id']
            except:
                await ctx.reply("Zeke, I could not unmod this user. I am sorry I have failed you.")
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://api.twitch.tv/helix/users", headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken}) as response:
                        rateLimit = response.headers.get("Ratelimit-Remaining")
                        if rateLimit != "0":
                            await session.delete("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + str("945207948") + "&user_id=" + str(victimId), headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken})
                            await ctx.reply("I have successfully removed the user \""+victim+"\" from the moderation team, Zeke.")
                        else:
                            await asyncio.sleep(5)
            except:
                await ctx.reply("Zeke, I could not unmod this user. I am sorry I have failed you.")

    @commands.command()
    async def title(self, ctx: commands.Context):
        if ctx.message.author.is_mod:
            content = ctx.message.content[7:]
            try:
                async with aiohttp.ClientSession(headers = {"Client-ID": streamerClientID, "Authorization": "Bearer " + steramerAccessToken, "Content-Type": "application/json"}) as session:
                    data = json.dumps({"title": content})
                    await session.patch("https://api.twitch.tv/helix/channels?broadcaster_id=945207948", data=data)
                    await ctx.reply("I have successfully changed the stream title.")
            except:
                await ctx.reply("The request to change the stream title has failed.")


bot = Bot()
