# objective: bot replying to a specific messge

import discord
import requests
import os

title_ = ''
start_ = ""
curTe_ = ''
duH_ = ''
duD_ = ''
ctfUrl = ''

client = discord.Client()

@client.event
# on_ready() is called when the bot has fininshed logging in and setting things up
async def on_ready():
    print('Logged in as user {0}'.format(client))

@client.event
async def on_message(message):
    # checking if the message author is same as the client user
    if message.author == client.user:
        return

    if message.content.startswith('CTFS'):
        # requests function
        url_ = "https://ctftime.org/api/v1/events/?limit=100"
        headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

        req_ = requests.get(url=url_, headers=headers_)
        if req_.status_code == 200:
            ctfs_ = req_.json()
            print('Found: {} ctfs.'.format(str(len(ctfs_))))

        for i in range(1, len(ctfs_)):
            title_ = ctfs_[i]['title']
            start_ = ctfs_[i]['start'].split('T')[0]
            curTe_ = ctfs_[i]['participants']
            duH_ = ctfs_[i]['duration']['hours']
            duD_ = ctfs_[i]['duration']['days']
            ctfUrl = ctfs_[i]['ctftime_url']
        #print(
        
            ctfDN_ = f' {title_}, ctf is starting on {start_} and lasts for {duD_} days and {duH_} hours, currently {curTe_} teams have registered. Check out the CTF at {ctfUrl}'
            embed = discord.Embed(title=title_)
            embed.add_field(name="Starts on", value=(str(start_)) + " UTC")
            embed.add_field(name="Duration", value=((str(duD_) + " days, ") + str(duH_)) + " hours \n")
            embed.add_field(name='Registration URL',value=ctfUrl)
            embed.add_field(name='Participants', value=curTe_)

            await message.channel.send(embed=embed)

client.run(os.getenv("TOKEN"))#token in .env 
