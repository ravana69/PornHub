"""

Let me Google / YouTube / DuckDuckGo / altnews / Stripe / Imdb / var / log / dyno that for you! 

Syntax:

 .lmg <search query>

 .lmy <search query>
 
 .ddg <search query>

 .lmalt <search news>

 .lmx <search porn>

 .lmx2 <search porn>

 .lmp <search porn>

 .lmvar <heroku app name>

 .lmlog <heroku app name>

 .dyno <type billing>




"""







from telethon import events



import os



import requests



import json



from uniborg.util import admin_cmd











@borg.on(admin_cmd(pattern="lmg (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=http://google.com/search?q={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **Google** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")





@borg.on(admin_cmd(pattern="lmy (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.youtube.com/results?search_query={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **UThoob** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")




@borg.on(admin_cmd(pattern="ddg (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://duckduckgo.com/?q={}&t=h_&ia=about".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **duckduckgo** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")




@borg.on(admin_cmd(pattern="lmx (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.xvideos.com/?k={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **Stripe** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")




@borg.on(admin_cmd(pattern="lmp (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.pornhub.com/video/search?search={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **Hack** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")


@borg.on(admin_cmd(pattern="lmalt (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.altnews.in/?s={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **altnews** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")



@borg.on(admin_cmd(pattern="lmvar (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/settings".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **var** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")



@borg.on(admin_cmd(pattern="lmlog (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/logs".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **log** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")



@borg.on(admin_cmd(pattern="lmx2 (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.xvideos2.com/?k={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **imdb** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")



@borg.on(admin_cmd(pattern="dyno(.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/account/{}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **dyno** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")

