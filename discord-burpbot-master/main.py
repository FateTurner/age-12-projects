import discord
import requests
import keepalive

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status='dnd', activity = discord.Activity(type = discord.ActivityType.watching, name = 'people burp'))
    print('Beep Boop! Success fully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    burpserver = client.get_guild(573142747590950923)

    if '😒' in message.content:
        await message.delete()

    if message.content.startswith('burp.help'):
        help = discord.Embed(title=('Burp Station - 911'), color=0x1e85ca)
        help.set_thumbnail(url="https://i.imgur.com/ilDSp64.jpg")
        help.add_field(name = "Prefix", value = "``burp.{command}``")
        help.add_field(name= "Commands", value = "``help``, ``serverinfo``, ``google``, ``avatar``, ``dog``, ``cat``,  ``meme``, ``dict``")
        help.set_footer(text="Burp Station - 911, DO NOT PRANK CALL!")
        await message.channel.send(embed=help)

    if message.content.startswith('burp.serverinfo'):
        serverinfo = discord.Embed(title=(''), color=0x1e85ca)
        serverinfo.set_author(name="T3CH", icon_url="https://cdn.discordapp.com/attachments/518672062232133636/577752657280892939/T3CH_OPTION_1.jpg")
        serverinfo.add_field(name= "Owner", value=(f"{burpserver.owner}"))
        serverinfo.add_field(name= "Created At", value=f"{burpserver.created_at.date()}")
        serverinfo.add_field(name="Custom Emojis", value=f"{len(burpserver.emojis)}")
        serverinfo.add_field(name="Channels", value=(f"{len(burpserver.channels)}"))
        serverinfo.add_field(name= "Member Count", value=f"{burpserver.member_count}")
        serverinfo.add_field(name= "Roles", value=f"{len(burpserver.roles)}")
        serverinfo.set_footer(text= "Made by TrustedMercury#1953")
        await message.channel.send(embed=serverinfo)

    if message.content.startswith('burp.avatar'):
        user = message.author
        await message.channel.send(f"{user.avatar_url}")

    if message.content.startswith('burp.google'):
        search_q = message.content.split('burp.google')[1].strip().replace(' ','%20')
        await message.channel.send('https://www.google.com/search?q=' + search_q)

    if message.content.startswith('burp.dog'):
        page = requests.get('https://dog.ceo/api/breeds/image/random').json()
        dogpic = page['message']
        embeddog = discord.Embed(title=(':dog: Woof!'), color=0x1e85ca)
        embeddog.set_image(url = (dogpic))
        embeddog.set_footer(text="Cute woofies, thanks to https://dog.ceo/")
        await message.channel.send(embed = embeddog)

    if message.content.startswith('burp.cat'):
        page1 = requests.get('https://api.thecatapi.com/v1/images/search').json()
        cat = page1[0]
        catpic =  cat['url']
        embedcat = discord.Embed(title=(':cat: Meow!'), color=0x1e85ca)
        embedcat.set_image(url = (catpic))
        embedcat.set_footer(text="Cute meows, thanks to https://thecatapi.com/")
        await message.channel.send(embed = embedcat)

    if message.content.startswith('burp.meme'):
        page2 = requests.get('https://meme-api.herokuapp.com/gimme').json()
        memepic = page2['url']
        embedmeme = discord.Embed(title=(':rofl: Reddit memes are da best!'), color=0x1e85ca)
        embedmeme.set_image(url = (memepic))
        embedmeme.set_footer(text="LOL memes, thanks to https://meme-api.herokuapp.com/")
        await message.channel.send(embed = embedmeme)

    if message.content.startswith('burp.dict'):
        search_q = message.content.split('burp.dict')[1].strip().replace(' ',' ')
        app_id = "YOUR OXFOR API APP ID HERE"
        app_key = "YOUR OXFORD API APP KEY HERE"
        language = "en-gb"
        word_id = search_q
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id
        dictdata = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key}).json()
        wordname = dictdata['id']
        worddefinition = dictdata['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        dict = discord.Embed(title=('Burp Dictionary'), color=0x1e85ca)
        dict.add_field(name = "Word", value = "%s" % (wordname))
        dict.add_field(name= "Definition", value = "%s" % (worddefinition))
        dict.set_footer(text=" Your pocket burping dictionary, thanks to https://developer.oxforddictionaries.com/")
        await message.channel.send(embed = dict)


keepalive.keepalive()

client.run('YOUR BOT TOKEN HERE')
