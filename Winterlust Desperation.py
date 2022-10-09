#Winterlust Desperation
import random
import discord
from discord.ext import commands
#from discord.commands import slash_command

bot = commands.Bot(command_prefix='$')
#slash = SlashCommand(bot, sync_commands=True)

@bot.command()
async def gamble(ctx, points, inputed_spins): #ctx, points:int, inputed_spins:int
      points = int(points)
      inputed_spins = int(inputed_spins)
      if inputed_spins / 10 >= 1:
         actual_spins = inputed_spins + int(inputed_spins/10)
      else:
         actual_spins = inputed_spins
      if points / (50*inputed_spins) < 1:
         await ctx.send("Dude ik gambling is fun, but you can't afford that many spins, try again")
      else:
         for i in range(0, int(actual_spins)):
            result = random.randint(1,100)
            if i+1 <= inputed_spins:
               points = points-50
            #print(result)
            if result >= 1 and result <= 40:
               await ctx.send("10 points it is...")
               points = points + 10
            elif result > 40 and result <= 60:
               await ctx.send("Black Tassle is delivered, earning 20 points")
               points = points + 20
            elif result > 60 and result <= 80:
               await ctx.send("You've summoned Barbara, earning 40 points")
               points = 40 + points
            elif result > 80 and result <= 95:
               await ctx.send("Woah, you got 100 points!")
               points = 100 + points
            elif result > 95 and result <= 99:
               await ctx.send("5 STAR JACKPOT 0_0")
               points = 500 + points
            elif result == 100:
               await ctx.send("**EXOIDA BONUS**")
               points = 2*points
               #dm the player who rolled it the pictures of exec
         await ctx.send(f'You now have {points} points')
        
@bot.command()
async def hello(ctx):
   await ctx.send("Hello! Ready to have some fun?\n\nRates:\n1 pull for 50 points\nFor every 10 spins you pay for we'll throw in another on the house :)\n\nTo gamble, simply type $gamble [points you have now] [spins you'll pay for] without the brackets. (Ex. $gamble 1000 10)\nP.S. This example will give you 11 spins because of our little bonus.")

bot.run()