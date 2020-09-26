"""
Torrent Search Plugin for Userbot. //torrentdownloads.me
cmd: .tsearch search_string
Note: Number of results are currently limited to 20

"""
from bs4 import BeautifulSoup as bs 
import requests
from telethon import events
from uniborg.util import admin_cmd
import asyncio
from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name='{}'.format(borg.me.username))


@borg.on(admin_cmd(pattern="search ?(.*)", allow_sudo=True))
async def tor_search(event):
	if event.fwd_from:
		return 
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

	search_str = event.pattern_match.group(1)

	print(search_str)
	await event.edit("Searching for "+search_str+".....")
	if " " in search_str:
		search_str = search_str.replace(" ","+")
		print(search_str)
		res = requests.get("https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="+search_str,headers)

	else:
		res = requests.get("https://www.torrentdownloads.me/search/?search="+search_str,headers)

	source = bs(res.text,'lxml')
	with open("source.html",'w') as f:
		f.write(str(source))

	urls = []
	magnets = []

	counter = 0
	for a in source.find_all('a',{'class':'cloud'}):
		# print("https://www.torrentdownloads.me"+a['href'])
		try:
			urls.append("https://www.torrentdownloads.me"+a['href'])
		except:
			pass
		if counter == 19:
			break		
		counter = counter + 1
	if not urls:
		await event.edit("Either the Keyword was restricted or not found..")		
		return

	print("Found URLS....")
		
	for url in urls:
		res = requests.get(url,headers)
		# print("URl: "+url)
		source = bs(res.text,'lxml')
		with open("source2.html",'w') as f:
			f.write(str(source))
		for div in source.find_all('div',{'class':'grey_bar1 back_none'}):
			try:
				mg = div.p.a['href']
				# print(str(mg))
				magnets.append("<b>URL: </b>"+str(url)+"<br/><b>\nMagnet: </b>{}\n<br/>".format(str(mg)))
			except:
				pass	
	print("Found Magnets...")			
	msg = ""
	try:
		search_str = search_str.replace("+"," ")
	except:
		pass	
	for i in magnets:
		msg = msg + i
	response = telegraph.create_page(
	search_str,
	html_content = msg
	)	
	await event.edit('Magnet Links for {}:\nhttps://telegra.ph/{}'.format(search_str,response['path']))
