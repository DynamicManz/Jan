import discord
from discord.ext import commands

# Bot setup with command prefix "-"
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="-", intents=intents)

# Replace this with your specific role ID
ROLE_ID = 1331524868834852904  # Put your role ID here
ROLE_ID2 = 1322671881232584835

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Bot is ready to use!')

@bot.command(name='n')
@commands.has_permissions(manage_roles=True)
async def assign_role(ctx, user: discord.Member):
    """
    Silently assigns the specified role to a user
    Usage: -assignrole @user
    """
    try:
        role = ctx.guild.get_role(ROLE_ID2)
        if role is not None:
            await user.add_roles(role)
    except:
        pass

@bot.command(name='fm')
@commands.has_permissions(manage_roles=True)
async def assign_role(ctx, user: discord.Member):
    """
    Silently assigns the specified role to a user
    Usage: -assignrole @user
    """
    try:
        role = ctx.guild.get_role(ROLE_ID)
        if role is not None:
            await user.add_roles(role)
    except:
        pass

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban_user(ctx, user_id: int):
    """
    Silently bans a user using their user ID
    Usage: -ban user_id
    """
    try:
        user = await bot.fetch_user(user_id)
        await ctx.guild.ban(user)
    except:
        pass

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run()