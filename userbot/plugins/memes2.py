#Added by @Sur_vivor
import asyncio
import random
import re
import time
from random import choice, randint
from collections import deque
from telethon import events
import requests
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot.utils import admin_cmd


# ================= CONSTANT =================


GAMBAR_TITIT = """
šš
ššš
  ššš
    ššš
     ššš
       ššš
        ššš
         ššš
          ššš
          ššš
      šššš
 šššššš
 ššš  ššš
    šš       šš
"""

# ===========================================

@borg.on(admin_cmd(pattern=r"hf$"))
async def facepalm(e):
    """ Facepalm  š¤¦āā """
    await e.edit("š¤¦āā")

@borg.on(admin_cmd(pattern=r"corona$"))
async def iqless(e):
    await e.edit("Antivirus scan was completed \nā ļø Warning! This  donkey has Corona Virus")


@borg.on(admin_cmd(pattern=r"ggl (.*)"))
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Tap this blue, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


@borg.on(admin_cmd(outgoing=True, pattern="fail$"))
async def fail(e):
        await e.edit("`\nāāāāāāāāāāāāāāāā `" 
                     "`\nāāāāāāāāāāāāāāāā `"    
                     "`\nāāāāāāāāāāāāāāāā `"       
                     "`\nāāāāāāāāāāāāāāāā `")    


@borg.on(admin_cmd(outgoing=True, pattern="lol$"))
async def lol(e):
        await e.edit("`\nā±āāā±ā±ā±ā­āāāā®āāā±ā±ā±ā± `" 
                     "`\nā±āāā±ā±ā±āā­āā®āāāā±ā±ā±ā± `"       
                     "`\nā±āāāāāāā°āāÆāāāāāāā± `" 
                     "`\nā±āāāāāā°āāāāÆāāāāāā± `")
    
@borg.on(admin_cmd(outgoing=True, pattern="rock$"))
async def lol(e):
        await e.edit("`\nāā­ā®āāāāāāāāāāāā `"
                     "`\nāāāāā­ā®āāā®ā­ā®ā­ā®āā­ `"
                     "`\nāāāāāāāā£ā«āāāāā£ā« `"
                     "`\nāāā£ā³ā«āāāā°ā°āÆā°āÆāā° `"
                     "`\nā­ā»ā»ā»ā«āāāā­ā®āāāā³ā `"
                     "`\nāā±ā­āāÆāāāāāāāāāā `"
                     "`\nā°ā®ā±ā±ā±āāāā°āÆā°āÆāāā `")

    
@borg.on(admin_cmd(outgoing=True, pattern="lool$"))
async def lool(e):
        await e.edit("`\nā­ā­āāāā®ā®āāāāāāāāāā\nāāā­āāāÆāāāāāā²āāā±āā\nāāāā±āāāāāāāāā±āāā®ā`"
                     "`\nāāā°āāā±ā­ā®āā±ā±āā±ā±āāā\nāā°āāāāā°āÆāāā±ā±ā±ā°ā»ā«ā\nāāāāāā³āāāāāāā³āāāÆā`"
                     "`\nāāāāāāāāāāāāāāāāā `")
                     


@borg.on(admin_cmd(outgoing=True, pattern="nih$"))
async def nih(e):
        await e.edit("`\n(\_/)`"
                     "`\n(ā¢_ā¢)`"
                     "`\n >š¹ *`"
                     "`\n                    `"
                     "`\n(\_/)`"
                     "`\n(ā¢_ā¢)`"
                     "`\nš¹<\ *`")


@borg.on(admin_cmd(outgoing=True, pattern="hoi$"))  
async def gtfo(e):
        await e.edit("`\nāāāāāāāāā`" 
                     "`\nāāāāāāāāā`"    
                     "`\nāā¼ā¼ā¼ā¼ā¼`"       
                     "`\nā  Hello Man`"
                     "`\nāā²ā²ā²ā²ā²`"
                     "`\nāāāāāāāāā`"
                    "`\n āā   āā`")               


@borg.on(admin_cmd(outgoing=True, pattern="ml(?: |$)(.*)"))
async def gtfo(e):
        message = e.pattern_match.group(1)
        await e.edit("`\nāāāāāāāāā`" 
                     "`\nāāāāāāāāā`"    
                     "`\nāā¼ā¼ā¼ā¼ā¼`"       
                     f"`\nā  {message}`"
                     "`\nāā²ā²ā²ā²ā²`"
                     "`\nāāāāāāāāā`"
                    "`\n āā   āā`")               


@borg.on(admin_cmd(outgoing=True, pattern="taco$")) 
async def taco(e):
        await e.edit("\n{\__/}"
                     "\n(ā_ā)"
                     "\n( >š® Want a taco?")


@borg.on(admin_cmd(outgoing=True, pattern="paw$"))  
async def paw(e):
        await e.edit("`(=āĻā=)")


@borg.on(admin_cmd(outgoing=True, pattern="tf$")) 
async def tf(e):
        await e.edit("(ĢæāĢæāĢæÄ¹ĢÆĢæĢæāĢæ Ģæ)Ģ  ")  
      

@borg.on(admin_cmd(outgoing=True, pattern="gay$"))           
async def gey(e):
        await e.edit("`\nāāāā­āāāāāā®āāāāā\nāāāāāāāāāāāāāāā`"
                     "`\nāāāāāāā­āā®ā»ā®āāāā\nāāāā±ā²āāāāāāāāāā\nāāā­ā»āāā°āā»āā®āāāā`"
                     "`\nāāā°ā³āā­āāāā³āÆāāāā\nāāāāāāā°āāā«āU GAY`"
                    "\nāāāāāāāāāāāāāāā")    


@borg.on(admin_cmd(outgoing=True, pattern="bot$"))
async def bot(e):
        await e.edit("` \n   ā²ā²ā­āāāāā® \nā­ā®āāāāāāā­ā® \nāā°ā«ā½ā½ā½ā£āÆā \nā°āā«ā³ā³ā³ā£āāÆ`"
                     "`\nā²ā²āāāāāā  \nā²ā²āāāāāā `")


@borg.on(admin_cmd(outgoing=True, pattern="hai$"))
async def hey(e):
        await e.edit("\nāāāā±āāāāā²āā­āāāāā\nāāāāāāāāāāāHELLO!āš`"
                     "`\nāāāāāāāā³āāā°ā³ā®HELLO!ā\nāāāā­āā°āÆāā®āāāÆā°āāā\nā±āāāāāāāāāāā²āāāā`"
                     "`\nāāāā²āāāāā±āāāāāāā`")


@borg.on(admin_cmd(outgoing=True, pattern="nou$"))
async def nou(e):
        await e.edit("`\nāā­ā®ā­ā®\nāāāāā\nā­ā»āā»āā®`"
                     "`\nāāāāāā\nāāā­āāā®āā®\nāāāā­ā°āÆā°āÆā®`"
                     "`\nā«āā  NoU\nāāā°ā°āāāāāÆ`"
                     "`\nāāāā»āā`")



@borg.on(admin_cmd(outgoing=True, pattern="mf$"))
async def gtfo(e):
        await e.edit(
"\n......................................../Ā“ĀÆ/) "
"\n......................................,/ĀÆ../ "
"\n...................................../..../ "
"\n..................................../Ā“.ĀÆ/"
"\n..................................../Ā“ĀÆ/"
"\n..................................,/ĀÆ../ "
"\n................................../..../ "
"\n................................./Ā“ĀÆ./"
"\n................................/Ā“ĀÆ./"
"\n..............................,/ĀÆ../ "
"\n............................./..../ "
"\n............................/Ā“ĀÆ/"
"\n........................../Ā“ĀÆ./"
"\n........................,/ĀÆ../ "
"\n......................./..../ "
"\n....................../Ā“ĀÆ/"
"\n....................,/ĀÆ../ "
"\n.................../..../ "
"\n............./Ā“ĀÆ/'...'/Ā“ĀÆĀÆ`Ā·Āø "
"\n........../'/.../..../......./ĀØĀÆ\ "
"\n........('(...Ā“...Ā“.... ĀÆ~/'...') "
"\n.........\.................'...../ "
"\n..........''...\.......... _.Ā·Ā“ "
"\n............\..............( "
"\n..............\.............\...")



@borg.on(admin_cmd(outgoing=True, pattern="sayhi$"))
async def shalom(e):
    await e.edit(
        "\nššššššššš"
        "\nšš·š·š·š·š·š·š·š"
        "\nššššš·šššš"
        "\nššššš·šššš"
        "\nššššš·šššš"
        "\nšš·š·š·š·ļøš·š·š·š"
        "\nššššššššš"
        "\nššššššššš"
        "\nšš·ššļøšššš·š"
        "\nšš·š·š·š·š·š·š·š"
        "\nšš·š·š·š·š·š·ļøš·š"
        "\nšš·ššššļøšš·š"
        "\nššššššššš")

@borg.on(admin_cmd(outgoing=True, pattern=r"(?:penis|dick)\s?(.)?"))
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace('š', emoji)
    await e.edit(titid)


@borg.on(admin_cmd(pattern=f"muth", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)
         
    animation_chars = [

            "8āļø===D",

            "8=āļø==D",

            "8==āļø=D",

            "8===āļøD",

            "8==āļø=D",

            "8=āļø==D",

            "8āļø===D",

            "8===āļøDš¦",

            "8==āļø=Dš¦š¦",

            "8=āļø==Dš¦š¦š¦"

        ]

    for i in animation_ttl:
        
            await asyncio.sleep(animation_interval)
        
            await event.edit(animation_chars[i % 8])

emojis = {
    "yee": "ć",
    "happy": "(ŹāæŹ)",
    "veryhappy": "=ĶĶĶĶŁ©(ą¹āį“ā)ą©­ą„ā¾ā¾",
    "amazed": "ć¾(oāŖāæāŖo)ļ½¼",
    "crying": "ą¼ąŗ¶ļøµą¼ąŗ¶",
    "dicc": "ā°UāÆā(āÉ·ā )",
    "fek": "ā°UāÆ\n(āæĖ āæ)",
    "ded": "āāæā",
    "sad": "āļøæā",
    "lenny": "( Ķ”Ā°( Ķ”Ā° ĶŹ( Ķ”Ā° ĶŹ Ķ”Ā°)Ź Ķ”Ā°) Ķ”Ā°)",
    "idc": "ĀÆ\_(ć)_/ĀÆ",
    "f": "šššššššš\nššššššššš\nšš\nšš\nšššššš\nšššššš\nšš\nšš\nšš\nšš\nšš"
}

unpacked_emojis = ""

for emoji in emojis:
    unpacked_emojis += f"`{emoji}`\n"
    
@borg.on(admin_cmd(pattern="emoji ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_emoji = emojis[str(input_str)]
        await event.edit(req_emoji)
    except KeyError:
        await event.edit("Emoji not found!")
