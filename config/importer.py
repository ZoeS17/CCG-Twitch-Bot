import os   # for importing env vars for the bot to use
import sys  # for argument processing
# from commands import *
from datetime import *
from pwnlib.term import text
from setproctitle import setproctitle
from twitchio.ext import commands
from dotenv import load_dotenv


load_dotenv()

class debug:
    def __init__(self, msg):
        sys.__stdout__.write(str(msg) + "\n")
        sys.__stdout__.flush()

class _print:
    def __init__(self, msg, color=None):
        self.color = color
        msg = str(msg)
        red = text.red
        yellow = text.yellow
        green = text.green
        log.write(msg+"\n")
        if self.color == "red":
            sys.__stdout__.write(red(msg) + "\a\n")
            sys.__stdout__.flush()
        elif self.color == "yellow":
            sys.__stdout__.write(yellow(msg) + "\n")
            sys.__stdout__.flush()
        elif self.color == "green":
            sys.__stdout__.write(green(msg) + "\n")
            sys.__stdout__.flush()
        else:
            sys.__stdout__.write(msg + "\n")
            sys.__stdout__.flush()

channel = ""

if len(sys.argv) > 1:
    channel = str(sys.argv[1])
else:
    channel = str(os.environ['CHANNEL']).lower()

class Logger:

    def __init__(self, stdout):
        global CHATDEBUG
        today = date.today()
        debug(today)
        self.filename = f"./logs/{channel}/{today}.mlog"
        self.stdout = stdout
        self.logfile = open(self.filename, "a", buffering=1)

    def __getattr__(self, attr):
        return getattr(self.stdout, attr)

    def close(self):
        self.logfile.close()

    def flush(self):
        self.logfile.flush()

    def write(self, text):
        self.logfile.write(text)
        self.logfile.flush()

log = Logger(sys.stdout)
sys.stdout = log
sys.__stdout__.flush()

setproctitle(f"Twitch[{channel}]")

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    api_token=os.environ['API_TOKEN'],
    initial_channels=[channel]
)


@bot.event
async def event_ready():
    """Called once when the bot goes online."""
    debug(f"{os.environ['BOT_NICK']} is online!")
    # ws = bot._ws  # this is only needed to send messages within event_ready
    # await ws.send_privmsg(channel, f"/me has landed!")


@bot.event
async def event_message(ctx):
    """Will run every time a message is sent in chat."""

    # make sure the bot ignores itself and the streamer
    _print(f"{ctx.author.name}: {ctx.content}")
    debug(f"{ctx.raw_data}")
    await bot.handle_commands(ctx)

    # if 'hello' in ctx.content.lower():
    #    await ctx.channel.send(f"Hi, @{ctx.author.name}!")
