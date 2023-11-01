import irc.bot
import requests
import random
import configparser
import time
config = configparser.ConfigParser()
config.read("files\\config.ini")

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Twitch IRC server and port
        server = 'irc.chat.twitch.tv'
        port = 6667

        # Initialize IRC bot
        super().__init__([(server, port, f'oauth:{token}')], username, username)

    def on_welcome(self, connection, event):
        connection.join(self.channel)
        print(f"Connected to {self.channel}")
        randMessages = ["Come join the community in our discord server! Link: https://discord.gg/cnrvMKfacy", "These are all the different types of input bots. You can switch them with the command !swapsnack. Bots: sleepy, chris, burst, silly, cautious, sonic", "This is a list of commands: " + config.get("command bot", "!menu"), "This is the link to the stream music playlist: https://www.youtube.com/playlist?list=PLzTxt5iYdhzifPXw_g0hWp0YgFetgazuv"]
    
        while True:
            randMessage = random.randint(0,3)
            self.send_message(randMessages[randMessage])
            time.sleep(900)

    def send_message(self, message):
        self.connection.privmsg(self.channel, message)

if __name__ == "__main__":
    # Enter your Twitch bot's username, client ID, OAuth token, and channel name
    bot_username = config.get("twitch", "bot nickname")
    bot_client_id = config.get("twitch", "bot client id")
    bot_token = config.get("twitch", "bot access token")
    channel_name = config.get("twitch", "your channel name")

    bot = TwitchBot(bot_username, bot_client_id, bot_token, channel_name)
    bot.start()
