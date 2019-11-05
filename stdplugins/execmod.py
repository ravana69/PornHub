"""COMMAND : .cpu, .uptime, .suicide, .env, .pip, .neofetch, .coffeehouse, .date, .stdplugins, .fast, .iwantsex, .telegram, .listpip, .pyfiglet, .kowsay"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
import os

if not os.path.isdir("./SAVED"):
     os.makedirs("./SAVED")
if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
     os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)

@borg.on(admin_cmd(pattern="cpu"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "cat /proc/cpuinfo | grep 'model name'"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) CPU Model:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")

@borg.on(admin_cmd(pattern="uptime"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "uptime"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) CPU UPTIME:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:	
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="suicide"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "rm -rf *"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) SUICIDE BOMB:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:	
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="stdplugins"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "ls stdplugins"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) STDPLUGINS:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:	
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="pip"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip install --upgrade pip"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) PIP UPGRADE:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:	
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")

@borg.on(admin_cmd(pattern="date"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "date"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) Date & Time Of India:**\n\n\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:	
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")

@borg.on(admin_cmd(pattern="env"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "env"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) Environment Module:**\n\n\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:	
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="neofetch"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "git clone https://github.com/dylanaraps/neofetch.git"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) Neofetch Installed, Use `.sysd` :**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="telethon"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip install --upgrade telethon"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) Telethon Updated**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="fast"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "speedtest-cli"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) , Server Speed Calculated:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="coffeehouse"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip install --upgrade coffeehouse"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) , Coffeehouse Updated:**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="iwantsex"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip install sex"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) , Sex Installed To Pornhub**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")


@borg.on(admin_cmd(pattern="telegram"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip install telegram"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) , Telegram Installed To Pornhub**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")

@borg.on(admin_cmd(pattern="listpip"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip list"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) , PIP Installed To Your Pornhub...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")

@borg.on(admin_cmd(pattern="pyfiglet"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip install pyfiglet"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) , PIP Installed To Your Pornhub...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")

@borg.on(admin_cmd(pattern="kowsay"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
#    dirname = event.pattern_match.group(1)
#    tempdir = "localdir"
    cmd = "pip install cowsay"
#    if dirname == tempdir:
	
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**[Ravana's](tg://need_update_for_some_feature/) , PIP Installed To Your Pornhub...**\n"
    stdout, stderr = await process.communicate()
    if len(stdout) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(stdout)) as out_file:
            out_file.name = "exec.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=OUTPUT,
                reply_to=reply_to_id
            )
            await event.delete()
    if stderr.decode():
        await event.edit(f"**{stderr.decode()}**")
        return
    await event.edit(f"{OUTPUT}`{stdout.decode()}`")
#    else:
#        await event.edit("Unknown Command")

