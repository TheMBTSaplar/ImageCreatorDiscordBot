import discord
from discord.ext import commands
import openai
import aiohttp
import io

# Set your Discord bot token here.
BOTTOKEN = 'Your_Discord_Bot_Token'

# Add your OpenAI API Key here.
OPENAI_API_KEY = 'Your_Openai_Api_Key'

# Make sure all intents are checked in Discord Developer Portal.
intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.presences = True

# Choose your prefix to call a command.
bot = commands.Bot(command_prefix='!', intents=intents)

# Set your OpenAI API Key
openai.api_key = OPENAI_API_KEY


# A little message for be sure bot is become online.
@bot.event
async def on_ready():
    print(f'Your bot {bot.user.name} is now online.')


# Here's your command for generating images.
@bot.command()
async def generateimg(ctx, *, prompt):
    await ctx.defer()

    try:
        # Settings for image.
        response = openai.Image.create(
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            response_format="url"
        )
        
        # Generated image become a message for the person who wants a image from bot.
        if response.get('data'):
            image_url = response['data'][0]['url']
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as resp:
                    if resp.status != 200:
                        return await ctx.send('Cannot download the image...')
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, 'image.png'))
        else:
            await ctx.send("No image generated. Try again.")
            
    except Exception as e:
        await ctx.send(f"Houston we got a problem: {e}")

# Starting your bot.
bot.run(BOTTOKEN)