import discord
import asyncio
from discord.ext import commands
import random
import requests
import praw

TOKEN = "MTMzMzY1NTUyMTY2Nzg0NjE3Ng.GCixCk.0kMtxxERCvl2zWe1pqePccVoHaEBd92XFaX21Q"
CHANNEL_ID = 123456789012345678


# Reddit API credentials
reddit = praw.Reddit(
    client_id='	YxJmbRMDIGN-FyNCK6FscQ',  # Your Reddit app client ID
    client_secret='77Mlr6GwIvnaO7z7srHA44lwf_ly5A',  # Your Reddit app client secret
    user_agent='TalkBot/1.0 by u/Fabulous_Delivery_55'

)

# Fetch the top 5 posts from r/memes
subreddit = reddit.subreddit('memes')
for submission in subreddit.top(limit=5):
    print(submission.title)
    print(submission.url)  # This will print out the URL of each meme

    def get_meme():
        subreddit = reddit.subreddit('memes')
        posts = subreddit.hot(limit=10)  # Get the top 10 hot posts
        post = random.choice([post for post in posts if not post.stickied])  # Randomly choose a non-stickied post
        meme_url = post.url  # Meme image URL
        return meme_url
    
    bot = commands.Bot(command_prefix='!')
    
    @bot.command()
    async def t(ctx):
        await ctx.send(get_meme())

bot = commands.Bot(command_prefix='!')

import discord
from discord.ext import commands
import requests
import random

# Create the bot instance
bot = commands.Bot(command_prefix="!")

@bot.command()
async def trivia(ctx):
    # Send a request to the Open Trivia Database API to get a random question
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = response.json()

    if data['response_code'] == 0:  # Check if API request was successful
        # Extract trivia question and answers
        question = data['results'][0]['question']
        correct_answer = data['results'][0]['correct_answer']
        incorrect_answers = data['results'][0]['incorrect_answers']

        
        options = [correct_answer] + incorrect_answers
        random.shuffle(options)

        prize = "$100"  # You can dynamically change this as needed
        await ctx.send(f"**Trivia Question (Prize: {prize}):** {question}")
        await ctx.send("\n".join([f"{i+1}. {option}" for i, option in enumerate(options)]))

      
    else:
        await ctx.send("Sorry, I couldn't fetch a trivia question at the moment.")
        bot.run('MTMzMzY1NTUyMTY2Nzg0NjE3Ng.GCixCk.0kMtxxERCvl2zWe1pqePccVoHaEBd92XFaX21Q')
