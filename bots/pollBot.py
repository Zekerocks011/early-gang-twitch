# creates and manages poll in chat
# don't fuck with this too much unless you're familiar with twitchio and how it works
# not much documentation here because even i don't know what the fuck this object oriented programming is doing in python

# imports
from bots.commandBot import *

# setting up variables
runningPoll = False
pollName = ""
pollOptions = []
voters = []

class Bot(commands.Bot):

    # sets up bot and connects to twitch
    def __init__(self):
        super().__init__(token = accessToken, prefix = "!", initial_channels = [yourChannelName])

    # makes the bot shut the hell up about commands not existing
    async def event_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        else:
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    # does whenever a message is sent
    async def event_message(self, message):
        global pollOptions
        global runningPoll
        global voters
        global pollName

        # don't take bot responses as real messages
        if message.echo:
            return

        # if pole is active
        elif runningPoll:

            # checks if chatter already votes
            if message.author.name not in voters:

                # checks if message is number then increases vote count for the specified option
                for option in range(len(pollOptions)):
                    if message.content == str(option + 1):
                        pollOptions[option][1] += 1
                        voters += [message.author.name]

        # telling bot to do command
        await self.handle_commands(message)

    # allows a whitelisted user to start a pole
    @commands.command()
    async def startpoll(self, ctx):
        global pollOptions
        global voters
        global pollName
        global runningPoll

        # check if user can start poll and if no other polls running
        if ctx.author.name in tokens:
            if not runningPoll:

                # error handling
                if ctx.message.content == "!startpoll" or ctx.message.content == "!startpoll ":
                    await ctx.send("please include your title and poll options in your command messages formatted like !startPoll title, option 1, option 2, option 3, ...")

                # creating poll with given names and options
                else:
                    ctx.message.content = ctx.message.content.replace("!startpoll ", "")
                    ctx.message.content = ctx.message.content.split(", ")
                    pollName = ctx.message.content[0]
                    pollOptions = []
                    for element in ctx.message.content:
                        if element != ctx.message.content[0]:
                            pollOptions += [[element, 0]]
                    voters = []
                    runningPoll = True

    # tells about current or most recent past poll
    @commands.command()
    async def poll(self, ctx):
        global pollOptions
        global runningPoll
        global pollName

        # if ongoing poll
        if runningPoll:

            # getting poll info
            results = ""
            total = 0
            for option in range(len(pollOptions)):
                total += pollOptions[option][1]
            for option in range(len(pollOptions)):
                if total != 0:
                    results += (str(option + 1) + ", " + pollOptions[option][0] + " - " + str('%.2f' % ((pollOptions[option][1] / total) * 100)) + "%, ")
                else:
                    results += (str(option + 1) + ", " + pollOptions[option][0] + " - " + "0%, ")

            # sending poll info
            await ctx.send("[bot] " + pollName + ": " + results)

        # if no ongoing poll
        if not runningPoll:

            # try and get past poll results and send them if they exist
            if not pollOptions:
                await ctx.send("[bot] no past or ongoing polls")
            else:

                # getting poll results
                results = ""
                total = 0
                for option in range(len(pollOptions)):
                    total += int(pollOptions[option][1])
                for option in range(len(pollOptions)):
                    if total != 0:
                        results += (pollOptions[option][0] + " - " + str('%.2f' % ((pollOptions[option][1] / total) * 100)) + "%, ")
                    else:
                        results += (pollOptions[option][0] + " - 0%, ")

                # sending poll results
                await ctx.send("[bot] " + "\"" + pollName + "\"" + " results: " + results)

    # tells the user how to vote in poll
    @commands.command()
    async def vote(self, ctx):
        global pollOptions

        # checks if there is in fact a poll running
        if runningPoll:

            # getting poll results
            results = ""
            for option in range(len(pollOptions)):
                results += ("type \"" + str(option + 1) + "\" to vote \"" + pollOptions[option][0] + "\", ")

            # sending poll results
            await ctx.send("[bot] " + results)

        # error handling
        else:
            await ctx.send("[bot] no ongoing poll")

    # allows a whitelisted user to stop the poll
    @commands.command()
    async def endpoll(self, ctx):
        global runningPoll
        global pollOptions
        global voters
        global pollName

        # checks if the user is allowed to do this and if there is even a poll running
        if ctx.author.name in tokens:
            if not runningPoll:
                await ctx.send("[bot] no ongoing polls")
            elif runningPoll:

                # tallying final poll results
                runningPoll = False
                results = ""
                total = 0
                for option in range(len(pollOptions)):
                    total += pollOptions[option][1]
                for option in range(len(pollOptions)):
                    if total != 0:
                        results += (pollOptions[option][0] + " - " + str('%.2f' % ((pollOptions[option][1]/total) * 100)) + "%, ")
                    else:
                        results += (pollOptions[option][0] + " - 0%, ")

                # sending poll results
                await ctx.send("[bot] " + "\"" + pollName + "\"" + " results: " + results)