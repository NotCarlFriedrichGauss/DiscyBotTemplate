import discord
import json
from discord.ext import commands
import keepalive
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

prompts_and_replies = {}

try:
    with open('prompts_and_replies.json', 'r') as file:
        prompts_and_replies = json.load(file)
except FileNotFoundError:
    pass


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if content == 'ping':
        await message.channel.send('Pong!')

    for prompt, reply in prompts_and_replies.items():
        if prompt.lower() in content:
            await message.channel.send(reply)
            break

    await bot.process_commands(message)


@bot.command()
async def addprompt(ctx):
    await ctx.send("Please enter the prompt:")
    try:
        prompt = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
        await ctx.send("Please enter the reply for the prompt:")
        reply = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
        prompts_and_replies[prompt.content] = reply.content
        with open('prompts_and_replies.json', 'w') as file:
            json.dump(prompts_and_replies, file)
        await ctx.send(f'Prompt added: "{prompt.content}" -> "{reply.content}"')
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond. The prompt addition has been canceled.")


@bot.command()
async def editprompt(ctx):
    prompt_list = "\n".join(prompts_and_replies.keys())
    if not prompt_list:
        await ctx.send("There are no prompts to edit.")
        return

    await ctx.send("Here are the prompts available for editing:\n" + prompt_list)
    await ctx.send("Please enter the prompt you want to edit:")
    try:
        prompt = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
        if prompt.content in prompts_and_replies:
            await ctx.send(f"Please enter the new prompt:")
            new_prompt = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
            prompts_and_replies[new_prompt.content] = prompts_and_replies.pop(prompt.content)
            with open('prompts_and_replies.json', 'w') as file:
                json.dump(prompts_and_replies, file)
            await ctx.send(f'Prompt updated: "{prompt.content}" -> "{new_prompt.content}"')
        else:
            await ctx.send(f'Prompt "{prompt.content}" not found.')
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond. The prompt edit has been canceled.")


@bot.command()
async def editreply(ctx):
    prompt_list = "\n".join(prompts_and_replies.keys())
    if not prompt_list:
        await ctx.send("There are no prompts to edit.")
        return

    await ctx.send("Here are the prompts available for editing:\n" + prompt_list)
    await ctx.send("Please enter the prompt for which you want to edit the reply:")
    try:
        prompt = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
        if prompt.content in prompts_and_replies:
            await ctx.send(f"Please enter the new reply:")
            new_reply = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
            prompts_and_replies[prompt.content] = new_reply.content
            with open('prompts_and_replies.json', 'w') as file:
                json.dump(prompts_and_replies, file)
            await ctx.send(f'Reply updated for "{prompt.content}"')
        else:
            await ctx.send(f'Prompt "{prompt.content}" not found.')
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond. The reply edit has been canceled.")


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

keepalive.keep_alive()
bot.run(#Enter Your Bot Token Here)