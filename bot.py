import os
import discord
import asyncio

client = discord.Client()

paweu_emoji = ''

paweu_quotes = [
    'Jestem specjalistą od zabezpieczeń IT.',
    'Mam portfel pełen bitcoinów.',
    'Pracowałem w brytyjskiej agencji, ona nie ma nawet polskiej nazwy.'
]

paweu_triggers = ['pawel', 'paweł']

paweu_who = ['kto to pawel?', 'kim jest pawel?', 'kto to paweł?', 'kim jest paweł?']

paweu_info = '''
Paweł to milioner. Zagubiony w świecie IT człowiek z kompleksami. Włada najnowszą technologią - przenośne routery wifi z Playa nie są mu straszne. Zna tajemne techniki walki CQC - aby przedostać się za linię wroga robi fikołka, który sprawia wrażenie, że Paweł jest przez sekundę w dwóch miejscach jednocześnie.
Niech nie zwiedzie was jego wygląd. Bohater Paweł jest człowiekiem na którego skinienie palca wojsko ogłasza alarm najwyższego stopnia. Wystarczy jedno słowo, zbitek cyfr i znają jego koordynaty na które już po 5 sekundach wyrusza jednostka specjalna.
Za dnia przechadza się po lasach w pobliżu jeziora Głębokiego szukając nowych, rządnych wrażeń ludzi do swojej Specjalnej Ekipy Specjalistów IT. {0}
'''


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    emojis = client.get_all_emojis()

    for emoji in emojis:
        if 'pawel' in emoji.name:
            global paweu_emoji
            paweu_emoji = str(emoji)

            break


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author

    # do not respond for own messages
    if author == client.user:
        return

    # commands
    if content in paweu_who:
        await client.send_message(channel, paweu_info.format(paweu_emoji))

    elif any(trigger in content for trigger in paweu_triggers):
        print('triggered by', author, 'in message:', content)
        await client.send_message(channel, paweu_emoji)

discord_apikey = os.environ['APIKEY']
client.run(discord_apikey)
