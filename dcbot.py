import discord
from discord.ext import commands

# Enable privileged intents if required
intents = discord.Intents.default()
intents.message_content = True  # Enable if you're using message content
intents.members = True  # This enables the 'Server Members Intent'

# Create bot instance with specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Example event to respond to messages
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and "hii" in message.content.lower():
        await message.channel.send("hiii")
    await bot.process_commands(message)

bot.run('MTI5Mzg4NDk2ODI0MTU5ODU0NQ.GCKymD.ibKtBETLeCLRe_SFz93jaq-B6XnijjlAaZhIVQ')