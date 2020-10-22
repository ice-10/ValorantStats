import discord
import datetime
from discord.ext import commands
from discord.utils import get
import json
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


@client.command()
async def trends(ctx):

    match_description = """
    ***Trends over the past act***

    **Kill Death Ratio**:
    **Accuracy**:
    **Headshot Accuracy**:



    """


    trends_embed = Embed(
        title = 'Trend History',
        timestamp = 'now',
        color = 5000,
        description = match_description,


    )
    trends_embed.set_image('https://quickchart.io/chart?bkg=transparent&c=%7B%0A%20%20type%3A%20%27line%27%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2F%2F%20Show%20a%20bar%20chart%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%27Act%201%27%2C%20%27Act%202%27%2C%20%27Act%203%27%5D%2C%20%20%20%2F%2F%20Set%20X-axis%20labels%0A%20%20%20%20yAxisID%3A%20100%2C%0A%20%20%20%20backgroundColor%3A%20%27rgba(255%2C255%2C0%2C1)%27%2C%0A%20%20%20%20%0A%20%20%20%20datasets%3A%20%5B%7B%0A%20%20%20%20%20%20label%3A%20%27Accuracy%27%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%2F%2F%20Create%20the%20%27Users%27%20dataset%0A%20%20%20%20%20%20data%3A%20%5B32%2C%2040%2C%2043%5D%2C%20%20%0A%20%20%20%20%20%20%2F%2F%20Add%20data%20to%20the%20chart%0A%20%20%20%20%20%20borderColor%3A%20%27rgba(255%2C0%2C0%2C1)%27%2C%0A%20%20%20%20%20%20pointBorderColor%3A%20%27rgba(255%2C255%2C0%2C)%27%2C%0A%20%20%20%20%20%20pointBackgroundColor%3A%20%27rgba(0%2C0%2C0%2C1)%27%2C%0A%20%20%20%20%20%20fontColor%20%3A%27black%27%2C%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20fill%3A%20false%2C%0A%20%20%20%20%20%20%0A%20%20%20%20%7D%5D%0A%20%20%20%20%0A%20%20%7D%0A%7D')


    hook.send(embed=trends_embed, username='ValorantStats',avatar_url='https://cdn.discordapp.com/avatars/764330534556925973/b796c759a2322eb3a5837d07ee102d56.png?size=128')





client.run('Insert Token Here')
