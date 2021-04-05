"""COMMAND : ./cull"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "/cull":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @Sahasaurav ,`Please Connect me to Pavel Durov Shukla`",
            "`User Authorised.`",
            "`Calling Pavel Durov Shukla (HellBringer) At 6262176262`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Durov: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` HellBringer",
            "`Durov: OMG!!! I Am FAN Of You Sir...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Durov: Please Don't Thank Sur, Telegram Is Your's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Durov: Yes Sur, There Is A Bug In Telegram v5.8.0.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Durov: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
