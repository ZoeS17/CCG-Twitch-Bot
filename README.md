# Twitch Chat Logger
Here's Courtesy Call Gaming's repo for their Twitch Chat Logger

## Getting Started

### Prerequisites
- [Python 3.7](https://www.python.org/downloads/release/python-379/)
- [git](https://git-scm.com/downloads)
- setproctitle -> `python -m pip install setproctitle`
- twitchio -> `python -m pip install twitchio`
- twitchio -> `python -m pip install python-dotenv`
- pwntools -> `python -m pip install --upgrade git+https://github.com/Gallopsled/pwntools.git@dev`
- oauth token & client-id for a Twitch account for your bot

### Installing
1. Clone the repo or unzip it somewhere
2. Open up a console window and navigate to the directory you cloned(unzipped) it in
3. Install requirements
4. Pop in all your secrets into the respective areas in `.env`
5. Back to the console, `python logger.py` to start the bot
6. Type `!test` in the chatroom to test the bot's working


## Usage
To run the chatbot, you will need to provide an OAuth access token with the chat_login scope.  You can reference an authentication sample to accomplish this, or simply use the [Twitch Chat OAuth Password Generator](http://twitchapps.com/tmi/).

```sh
$ python logger.py [channel]
```

* Channel - [OPTIONAL if set in .env] The channel your bot will connect to

## Bot Interaction
Right now, you can only interact with the bot via the single command, `!test`. You can create similar commands pretty easily, just copy the function and change out the function name decorator arguement...

```python
@bot.command(name='likethis', aliases=['this'])
async def likethis(ctx):
    await ctx.send(f'ZoeS17, @{ctx.author.name}!')
```

## Events

There are 2 events that are used in the code right now.. `event_ready` and `event_message`.

### event_ready
This executes when the bot comes online, and will print out to the console. 
```python
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')
```

### event_message
This function executes once per event (or message) sent. You can make it handle input from chat that *aren't* necesarily commands, and fun stuff like that.

```python
@bot.event
async def event_message(message):
    print(message.content)
    await bot.handle_commands(message)
```
You can find more info in [TwitchIO's official documentation](https://twitchio.readthedocs.io/en/rewrite/twitchio.html).