import nextcord
from nextcord.ext import commands 
#Import nextcord and commands from nextcord.ext

bot = commands.Bot(command_prefix="!")
#Define the prefix and bot variable

@bot.event
async def on_ready():
  print("Logged in as: " + bot.user)
  
@bot.command()
@commands.has_permissions(manage_messages=True)
async def test(ctx, arg):
  await ctx.send("Hello.")
  
@test.error
async def test_error(ctx, error):
  if isinstance(error, commands.MissingPermissions): #if the message author is missing the manage_messages permissions
    await ctx.send("You don't have the permissions to use this!")
  elif isinstance(error, commands.MissingRequiredArgument): #if you didn't specify the arg in the in the test command
    await ctx.send("You forgot to give me an arg :(")
    
bot.run("TOKEN")
