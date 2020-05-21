import discord

client = discord.Client()

@client.event
async def on_ready():
	print('logged in as')
	print(client.user.name)
	print(client.user.id)

@client.event	
async def on_group_join(channel, user):
		print(channel)
		print(user)

client.run('NzExNTUyOTc0OTQxNTg1NDY4.XsErjQ.9wWTuQVqSLAYHYzRarzTDhLykkI')
