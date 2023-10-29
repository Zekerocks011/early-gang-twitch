import os
import random
import time
import asyncio
import threading
import requests
from mutagen.mp3 import MP3
from moviepy.editor import *
from googleapiclient.discovery import build
from pytube import YouTube
import pygame.mixer
from twitchio.ext import commands
import configparser
config = configparser.ConfigParser()
config.read("files\\config.ini")
API_KEY = config.get("youtube", "api key")
PLAYLIST_ID = config.get("youtube", "playlist id")
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Get the list of video IDs in the playlist
playlist_items = []
nextPageToken = None
while True:
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=PLAYLIST_ID,
        maxResults=50,
        pageToken=nextPageToken
    )
    response = request.execute()
    playlist_items.extend(response['items'])
    nextPageToken = response.get('nextPageToken')
    if nextPageToken is None:
        break

queue = []

pygame.mixer.init()

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=config.get("twitch", "bot access token"), prefix='!', initial_channels=[config.get("twitch", "your channel name")])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def forceskip(self, ctx: commands.Context):
        if ctx.author.is_mod:
            try:
                pygame.mixer.music.pause()
                await ctx.reply(f'I successfully skipped the song.')
            except:
                await ctx.reply(f'The command was unsuccessful.')
    
    @commands.command()
    async def nowplaying(self, ctx: commands.Context):
        try:
            await ctx.reply(f"The song currently playing is \"{queue[0][1]}\" uploaded to YouTube by \"{queue[0][2]}\".")
        except:
            await ctx.reply(f'I could not fetch the song that is currently playing.')

    @commands.command()
    async def request(self, ctx: commands.Context):
        try:
            print(ctx.message.content[9:])
            search_response = youtube.search().list(
            q=ctx.message.content[9:],
            part='snippet',
            maxResults=1
            ).execute()
            print("got here")

            # Iterate over the search results and print the title and video ID of each video.
            video_id = search_response['items'][0]['id']['videoId']
            url = f"https://www.youtube.com/watch?v={video_id}"
            yt = YouTube(url)
            stream = yt.streams.get_audio_only()
            download_path = os.getcwd()
            name = random.randint(0,69420)
            stream.download(output_path=download_path, filename=f"{name}.mp4")
            stream.download(output_path=download_path, filename=f"{name}.mp4")
            time.sleep(2)
            video_path = os.path.join(download_path, f"{name}.mp4")
            audio_path = os.path.join(download_path, f"{name}.mp3")
            for pathattempt in range(10):
                if not os.path.exists(video_path):
                    print("no existie")
                    time.sleep(1)
                    continue
            video = AudioFileClip(video_path)
            video.write_audiofile(audio_path)
            os.remove(video_path)
            queue.append([audio_path, yt.title, yt.author, ctx.message.author.display_name, yt.thumbnail_url])
            await ctx.reply(f"I successfully added the song \"{yt.title}\" to the queue!")
        except:
            await ctx.send(f'The song was not added to the queue. You broke it.')

async def start_bot():
    bot = Bot()
    await bot.start()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    bot_thread = threading.Thread(target=loop.run_until_complete, args=(start_bot(),))
    bot_thread.start()

def queuePrint():
    while True:
        print(queue)
        time.sleep(10)
threading.Thread(target=queuePrint).start()

def addToQueue():
    for attempt in range(10):
        try:
            print("trying")
            random_video = random.choice(playlist_items)
            video_id = random_video['snippet']['resourceId']['videoId']
            # Download the selected video
            url = f"https://www.youtube.com/watch?v={video_id}"
            yt = YouTube(url)
            stream = yt.streams.get_audio_only()
            download_path = os.getcwd()
            name = random.randint(0,69420)
            stream.download(output_path=download_path, filename=f"{name}.mp4")
            time.sleep(2)
            video_path = os.path.join(download_path, f"{name}.mp4")
            audio_path = os.path.join(download_path, f"{name}.mp3")
            for pathattempt in range(10):
                if not os.path.exists(video_path):
                    print("no existie")
                    time.sleep(1)
                    continue
            video = AudioFileClip(video_path)
            video.write_audiofile(audio_path)
            os.remove(video_path)
            queue.append([audio_path, yt.title, yt.author, "FooBot", yt.thumbnail_url])
            #insert audio path, title, author, who requested, thumbnail link
        except:
            print("errored")
        else:
            break
    else:
        print("max amount hit")


# Randomly select a video from the playlist
for i in range(3):
    for attempt in range(10):
        try:
            print("trying")
            random_video = random.choice(playlist_items)
            video_id = random_video['snippet']['resourceId']['videoId']
            # Download the selected video
            url = f"https://www.youtube.com/watch?v={video_id}"
            yt = YouTube(url)
            stream = yt.streams.get_audio_only()
            download_path = os.getcwd()
            name = random.randint(0,69420)
            stream.download(output_path=download_path, filename=f"{name}.mp4")
            time.sleep(2)
            video_path = os.path.join(download_path, f"{name}.mp4")
            audio_path = os.path.join(download_path, f"{name}.mp3")
            for pathattempt in range(10):
                if not os.path.exists(video_path):
                    print("no existie")
                    time.sleep(1)
                    continue
            video = AudioFileClip(video_path)
            video.write_audiofile(audio_path)
            os.remove(video_path)
            queue.append([audio_path, yt.title, yt.author, "FooBot", yt.thumbnail_url])
            #insert audio path, title, author, who requested, thumbnail link
        except:
            print("errored")
        else:
            break
    else:
        print("max amount hit")
        break

print(queue)


print(f"Now playing: {queue[0][1]}")
response = requests.get(queue[0][4])
with open('image.png', 'wb') as f:
    f.write(response.content)
pygame.mixer.music.load(queue[0][0])
pygame.mixer.music.play()

def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None
        

def updateCurrentTime():
    while True:
        try:
            with open("C:/Users/2006z/Documents/streamfiles/text/currentTime.txt", "w") as e:
                e.write(f"{str(int((pygame.mixer.music.get_pos()/(1000*60))%60))}:{str(int((pygame.mixer.music.get_pos()/1000)%60)).zfill(2)}")
            with open("C:/Users/2006z/Documents/streamfiles/text/title.txt", "w") as e:
                e.write(f"{queue[0][1]}")
            with open("C:/Users/2006z/Documents/streamfiles/text/author.txt", "w") as e:
                e.write(f"{queue[0][2]}")
            with open("C:/Users/2006z/Documents/streamfiles/text/requester.txt", "w") as e:
                e.write(f"{queue[0][3]}")
            with open("C:/Users/2006z/Documents/streamfiles/text/fullTime.txt", "w") as e:
                length = mutagen_length(queue[0][0])
                e.write(str(int(length/60)) + ':' + str(int(length%60)).zfill(2))
            time.sleep(1)
        except:
            continue

b = threading.Thread(name="updateCurrentTime", target=updateCurrentTime)
b.start()

while True:
    while pygame.mixer.music.get_busy():
        pass
    else:
        pygame.mixer.music.unload()
        print("not busy")
        os.remove(queue[0][0])
        queue.pop(0)
        print(queue)
        while len(queue) < 3:
            if not pygame.mixer.music.get_busy():
                try:
                    if len(queue) == 0:
                        addToQueue()
                    print(f"Now playing: {queue[0][1]}")
                    pygame.mixer.music.load(queue[0][0])
                    pygame.mixer.music.play()
                    response = requests.get(queue[0][4])
                    with open('image.png', 'wb') as f:
                        f.write(response.content)
                except:
                    break
            print("attempting to add song to queue") 
            addToQueue()
        else:
            if not pygame.mixer.music.get_busy():
                try:
                    print(f"Now playing: {queue[0][1]}")
                    pygame.mixer.music.load(queue[0][0])
                    pygame.mixer.music.play()
                    response = requests.get(queue[0][4])
                    with open('image.png', 'wb') as f:
                        f.write(response.content)
                except:
                    break
            continue



# Need to make a function that makes a script so it constantly keeps 3 songs in the auto queue at all times. Make a table to keep track of this data. Delete songs and
# entry in queue afterwards
