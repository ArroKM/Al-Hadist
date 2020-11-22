# Coded By Asecx
# https://github.com/ArroKM

import os
try:
	import requests
except ImportError:
	os.system("python3 -m pip install -q requests")
try:
	from bs4 import BeautifulSoup as _
except ImportError:
	os.system("python3 -m pip install -q bs4")
	from bs4 import BeautifulSoup as _

class Hadis:
	url2 = "https://www.hadits.id"
	def __init__(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.get_data()

	def logo(self):
		print(f"""\x1b[35;1m    __  __\x1b[101m\x1b[37;1m:XiuzCode:\x1b[0m\x1b[35;1m___      __
   / / / /___ _____/ (_)____/ /_
  / /_/ / __ `/ __  / / ___/ __/
 / __  / /_/ / /_/ / (__  ) /_
/_/ /_/\__,_/\__,_/_/____/\__/\n\x1b[105m\x1b[37;1m::     Coded By AsecX     ::\x1b[0m\n""")

	def get_data(self):
		self.logo()
		name = input("\n\x1b[32;1m[\x1b[36;1m?\x1b[32;1m] \x1b[36;1mCari Hadist : \x1b[32;1m")
		print("")
		niat = requests.get(self.url2+"/tentang/"+name)
		parser = _(niat.text, "html.parser")
		soup = parser.find("div", class_="search-result")
		judul = soup.find_all("a")
		no = 0
		li = []
		pil = []
		for z in judul:
			no += 1
			lin = z["href"]
			li.append(lin)
			pil.append(z.text)
			print(f"\x1b[37;1m(\x1b[36;1m{no}\x1b[37;1m) \x1b[36;1m{z.text}")

		self.mantan(li, pil)

	def mantan(self, li, pil):
		tot = 0
		cou = int(input("\n\x1b[32;1m[\x1b[36;1m?\x1b[32;1m] \x1b[36;1m>>>> \x1b[32;1m"))
		for res in li:
			tot += 1
			if tot >= cou:
				di = requests.get(self.url2+res)
				bbs = _(di.text, "html.parser")
				art = bbs.find("article", class_="hadits-content").text
				print("\x1b[37;1m"+art)
				break
			continue
		tobat = input("\x1b[32;1m[\x1b[36;1m?\x1b[32;1m] \x1b[36;1mCari Lagi / Lanjut (C/L)? : \x1b[32;1m")
		os.system('cls' if os.name == 'nt' else 'clear')
		self.logo()
		if tobat == "L" or tobat == "l":
			no = 0
			for ulang in pil:
				no += 1
				print(f"\x1b[37;1m(\x1b[36;1m{no}\x1b[37;1m) \x1b[36;1m{ulang}")
			self.mantan(li, pil)
		else:
			self.__init__()


if __name__ == '__main__':
	try:
		Hadis()

	except KeyboardInterrupt:
		exit("\x1b[32;1m[\x1b[36;1m*\x1b[32;1m] \x1b[36;1mWaalaikumsalam")
