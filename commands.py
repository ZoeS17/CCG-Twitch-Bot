#!/usr/bin/env python3
# -*- codinfg: utf-8 -*-

"""Command handler for CCG Twitch chat logger."""
from config.importer import bot, debug


def isAdmin(un):
    un = un.lower()
    with open(f"./Admins", "rt", encoding='utf-8') as a:
        lines = a.read().splitlines()
        if un in lines:
            return True
        else:
            return False


def ismod(ctx):
    if ctx.author.is_mod:
        return True
    else:
        return False


@bot.command()
async def test(ctx):
    Admin = isAdmin(ctx.author.name)
    if Admin:
        debug(f"{ctx.author.id}")
    else:
        debug('test failed!')
