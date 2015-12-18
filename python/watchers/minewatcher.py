#!/usr/bin/python2.7

import requests,re,sys,time
from gi.repository import Notify

def print_usage():
    print("You didn't specify any arguments, therefore manticore has been set to default.\nUsage : ./minewatcher.py [optional : name]")

def get_data(url):
    req = requests.get(url, allow_redirects=False)
    data = req.text
    
    try:
        data = data.split('<td class="bold">Joueurs</td>')[1].split("</tr>")[0]
    except IndexError:
        print("Error while fetching data")
        return None
    return data

def parse_data(data):
    searchObj = re.search(r'(\d)/(\d)',data)
    return searchObj.group(1)

def check_diff(nb_players):
    filename = "minewatcher.txt"
    try:
        fichier = open(filename, "r")
        stored_stats = fichier.read()
        fichier.close()
        if stored_stats != nb_players:
            if nb_players == '1':
                text = "x has joined"
            elif nb_players == '2':
                text = "Enjoy :)"
            elif nb_players == '0':
                text = "x has left"
            else:
                text = "error, unkown value received"
            fichier = open(filename, "w")
            fichier.write(nb_players)
            fichier.close()
        else:
            text = "no change"

    except:
        fichier = open(filename, "w")
        fichier.write(nb_players)
        fichier.close()
        text = "No database found, updating..."
        
    return text

if __name__ == "__main__":

    url = "https://www.mtxserv.fr/viewer/game/minecraft/37.187.25.76/27330?players=true"
    name = "Minecraft"
    while True:
        data = get_data(url)
        nb_players = parse_data(data)
        notification_content = check_diff(nb_players)

        if notification_content != "no change":
            Notify.init ("{0} Watcher".format(name))
            notification = Notify.Notification.new("{0} Watcher".format(name), notification_content, "dialog-information")
            notification.show()
        time.sleep(30)
