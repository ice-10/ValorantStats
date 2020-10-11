import discord
import datetime
from discord.ext import commands
from discord.utils import get

from dhooks import Webhook, Embed

hook = Webhook(url='https://discord.com/api/webhooks/764941548886294578/GpVKEL4goKnl6x1wytDAOrsInUpj_cWhTv9iSY83SzwArgv_nNqDVf7UG3bMWhQy9kks')



client = commands.Bot(command_prefix='v.')
@client.event
async def on_ready():
        print('ready')

@client.command()
async def matches(ctx):
    #All 'games' displayed are just palceholders

    #roundResultCode would be fetched
    #map would also be fetched (not implemented yet)
    score = []
    score.append('13-1')
    score.append('13-2')

    match_description = """
    ***Displaying your 10 most recent games***

    **{} W - Haven**

    **{} L - Bind**

    **{} W - Haven**

    **{} L - Bind**

    **{} W - Haven**

    **{} L - Bind**

    **{} W - Haven**

    **{} L - Bind**

    **{} W - Haven**

    **{} L - Bind**
""".format(score[0],score[1],score[0],score[1],score[0],score[1],score[0],score[1],score[0],score[1])


    match_history_embed = Embed(
        title = 'Match History',
        timestamp = 'now',
        color = 5000,
        description = match_description
    )

    hook.send(embed=match_history_embed, username='ValorantStats',avatar_url='https://cdn.discordapp.com/avatars/764330534556925973/b796c759a2322eb3a5837d07ee102d56.png?size=128')

@client.command()
async def stats(ctx):
    #pull stats from player
    wins = 50
    losses = 20
    kills = 1200
    deaths = 1000
    assists = 500
    accuracy = 40
    headshot_accuracy = 16
    total_damage = 34980;
    most_used_weapon1 = 'Vandal'
    most_used_weapon2 = 'Operator'
    most_used_weapon3 = 'Bulldog'

    stat_description = """
    **Wins**: {}
    **Losses**: {}

    **Kills**: {}
    **Deaths**: {}
    **Assists**: {}

    **Headshot Accuracy**: {}%
    **Accuracy**: {}%
    **Total Damage**: {}

    **Most Used Weapons**:
        **1.** - {}
        **2.** - {}
        **3.** - {}
""".format(wins, losses, kills, deaths, assists, accuracy, headshot_accuracy, total_damage, most_used_weapon1,most_used_weapon2,most_used_weapon3)





    statistics_embed = Embed(
        title = 'Statistics',

        timestamp = 'now',
        color = 5000,
        description = stat_description

    )
    hook.send(embed=statistics_embed, username='ValorantStats',avatar_url='https://cdn.discordapp.com/avatars/764330534556925973/b796c759a2322eb3a5837d07ee102d56.png?size=128')



client.run('NzY0MzMwNTM0NTU2OTI1OTcz.X4EsSA.hE80o32-KnhM8X1S47SIXO0z_TA')
