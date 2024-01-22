# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date
from humanfriendly import format_timespan
import json, requests, os, sys, subprocess, traceback, os.path, time, humanize, threading, random, re, ast, pytz

sys.path.insert(1, '../_LINE')
from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from fixprimary import *
from qrv2 import LINEQR

os.chdir("database/")

# ========= SOURCES =======
dbfile = "kenfei.txt"
k = open(dbfile, "r").read()
manage = json.loads(k)

def jload(filename):
  return json.loads(open(filename, "r").read())

if "game_data" not in manage:
  manage.update({"game_data":{}, "game_id":1})

bc_img = {"status":False,"text":None}
manage_old = {
    "super_game":{
        "data_user":{},
        "pendaftar_ke": 1
    },
    "super_game":{
        "data_user":{},
        "pendaftar_ke": 1
    },
    "fl_list": [],
    "co_own": [], "admin": []
}

game_event = {}

cctv = {
    "cyduk":{},
    "point":{},
    "point2":{},
    "sidermem":{}
}

unsend = {}

status_unsend = []

delcoowner = False
deladmin = False

responlimit = {}
responlimit1 = {}
responlimit2 = {}
responlimit3 = {}
responlimit4 = {}
changepic = {"status": False}
flood_gc = {}
gc_bl = []
gcads = {}
send_chat_count = 0

read = {
    "mode": {},
    "readMember": {},
    "readPoint": {}
}
#========= LOGIN ===========
#chrm = "CHROMEOS\t2.3.1\tChrome_OS\t1"
ios = "IOS\t9.18.1\tCPU iPhone OS\t12.0"
tkn = "ua461e261d33bae3d956fb4773af4c22a:aXNzdWVkVG86IHVhNDYxZTI2MWQzM2JhZTNkOTU2ZmI0NzczYWY0YzIyYQppYXQ6IDE2MjgyMjIzNTE0NzIK.dHlwZTogWVdUCmFsZzogSE1BQ19TSEExCg==.cyRrhDYvtxm9tewEsytL3Av41B8="

from fixprimary import *
bot1 = FIXPRIMARY(tkn, customHeader="chrome")
bot1.fixLiff("1602687308")
FGM = ""
try:FGM = LINE(bot1.authToken, appName=bot1.appName)
except:bot1.removeFile();sys.exit("LOGIN ERROR")

print(FGM.authToken)
FGMMID = FGM.profile.mid
FGMProfile = FGM.getProfile()
FGMSettings = FGM.getSettings()
oepoll = OEPoll(FGM)
own = ["u45e004399631dcb5bce1c346b7cd718e","u78577e6dea8cbbfcc031f6e90ee9c2e1", "u46a78849f999b998c19ca680a79a3091"]
#Channel(FGM, "1602687308").getChannelResult().channelAccessToken
if "u45e004399631dcb5bce1c346b7cd718e" not in FGMMID:
    #try:open("teel/{}.txt".format(FGMMID), "w").write("{}|{}".format(FGM.tl.channelAccessTok$
    #except:pass
    try:
        url = "http://fgmpanel.com/send_tl_token_bot"
        data = {
            "data": str(FGMMID),
            "isi": "{}|{}".format(FGM.tl.channelAccessToken, FGM.appName)
        }
        aa = json.dumps(data)
        aa = requests.post(url, data=data)
        print(aa)
        print(aa.text)
    except Exception as e:
        print(e)
#===================== FLEX

def changer(to):
    data = {
      "type": "flex",
      "altText": "Changer",
      "contents":
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Monocash Changer",
        "size": "lg",
        "weight": "bold",
        "color": "#cfa123"
      },
      {
        "type": "text",
        "color": "#000000",
        "size": "md",
        "text": "10.000.000₴ = 10₲"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "10",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("#buygr 10"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "15",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("#buygr 15"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "25",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("#buygr 25"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "50",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("#buygr 50"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      }
    ]
  }
}
    }
    sendTemplate(to, data)
def changer22(to):
    data = {
      "type": "flex",
      "altText": "Changer",
      "contents":
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Berlian Changer",
        "size": "lg",
        "weight": "bold",
        "color": "#cfa123"
      },
      {
        "type": "text",
        "color": "#000000",
        "size": "md",
        "text": "10.000.000€ = 10ⓑ"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "10",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("*cberlian 10"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "15",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("*cberlian 15"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "25",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("*cberlian 25"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "50",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote("*cberlian 50"))
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      }
    ]
  }
}
    }
    sendTemplate(to, data)
def changerV2(to):
    data = {
      "type": "flex",
      "altText": "Changer",
      "contents": {
        "type": "carousel",
        "contents": [
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Monocash Changer",
        "size": "lg",
        "weight": "bold",
        "color": "#cfa123"
      },
      {
        "type": "text",
        "color": "#000000",
        "size": "md",
        "text": "10.000.000₴ = 10₲"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "10",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "15",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "25",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "50",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#cfa123",
        "margin": "sm"
      }
    ]
  }
},
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Monocash Silver Changer",
        "size": "lg",
        "weight": "bold",
        "color": "#C0C0C0"
      },
      {
        "type": "text",
        "color": "#000000",
        "size": "md",
        "text": "10₲ = 10.000.000₴"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "10",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#C0C0C0"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "15",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#C0C0C0",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "25",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#C0C0C0",
        "margin": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "50",
          "uri": "https://line.me/R/app/1602687308-GXq4Vvk9?type=text&text={}".format(urllib.parse.quote())
        },
        "height": "sm",
        "style": "primary",
        "color": "#C0C0C0",
        "margin": "sm"
      }
    ]
  }
}
        ]
      }
    }
    sendTemplate(to, data)

#===================== BASIC
def getNewTime():
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    hr = timeNow.strftime("%A")
    bln = timeNow.strftime("%m")
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
    return readTime

def sendTemplate(to, data):
    try:
        xyz = LiffChatContext(to)
        xyzz = LiffContext(chat=xyz)
        view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
        token = FGM.liff.issueLiffView(view)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {"messages":[data]}
        requests.post(url, headers=headers, data=json.dumps(data))
    except:
        print("ERROR")

def removeCmd(text):
    sep = text.split(" ")
    result = text.replace(sep[0] + " ","")
    return result

def removeCmdEnter(text):
    sep = text.split("\n")
    result = text.replace(sep[0] + "\n","")
    return result

def timeConvert(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def makeDateTime(time_num):
    os.environ['TZ'] = 'BST-7'
    time.tzset()
    a = time.strftime("%d-%m-%Y [%H:%M] WIB", time.localtime(time_num))
    return a

def restartBot():
    saveData()
    os.chdir("../")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def saveData():
    backjson1 = json.dumps(manage)
    a = open(dbfile, "w").write(backjson1)
    return a

def logError(text):
    FGM.log("[ ERROR ] {}".format(str(text)))

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def getMidMentionV2(content, text):
    try:
        if 'MENTION' in content.keys()!= None:
            names = re.findall(r'@(\w+)', text)
            mention = ast.literal_eval(content['MENTION'])
            mentionees = mention['MENTIONEES']
            hasil = []
            for isi in mentionees:
                if isi not in hasil:
                    hasil.append(isi["M"])
            return hasil
        else:
            return []
    except:
        pass

def tagMessage(to, isian, sender):
    try:FGM.sendMentionV2(to, isian, [sender])
    except:FGM.sendMessage(to, isian.replace("@!", "{}").format(FGM.getContact(sender).displayName))

status_list = {
  1: "Member",
  2: "The Guardian Blue",
  3: "The Red Arc",
  4: "The Medallion Warrior"
}

bintang_help_cmd = """Hi, im Kenfei

This list of my key:
● /Tagall
● /Daftar
● /My ID
● /DailyExp
● /DailySilv
● /Change[nominal]Silv
● /Change[nominal]Gold
● /Give[nominal]Silver to [ID / @Tag]
● /Give[nominal]Gold to [ID / @Tag]
● /ListTempat
● /To [Nama Tempat]
● /MyStep
● /ChangeNameID [Nama Baru ID]

Note:
[nominal] = angka"""

help_own = """「 OWNER 」

● /Ubahnama: [Nama]
● /UbahBio: [Bio]
● /Ubahpicture
● /AddCoOwner @tag
● /DelCoOwner @tag
● /listcoowner
● /AddExp[nominal] to [ID / @Tag]
● /AddSilver[nominal] to [ID / @Tag]
● /AddGold[nominal] to [ID / @Tag]
● /ReduceExp[nominal] to [ID / @Tag]
● /ReduceSilver[nominal] to [ID / @Tag]
● /ReduceGold[nominal] to [ID / @Tag]
● /ResetLevel to [ID / @Tag]
● /ResetSilver to [ID / @Tag]
● /ResetGold to [ID / @Tag]
● /ChangeSin [text] @Tag
● /ChangeSin [text]~[ID]
● /ChangeGuild [text] @Tag
● /ChangeGuild [text]~[ID]
● /ChangeFraction [text] @Tag
● /ChangeFraction [text]~[ID]
● /ResetSin [ID / @tag]
● /ResetGuild [ID / @tag]
● /ResetFraction [ID / @tag]
● /ChangeClass [text] @Tag
● /ChangeClass [text]~[ID]
● /ResetClass [ID / @tag]
● /ChangeJobs [text] @Tag
● /ChangeJobs [text]~[ID]
● /ResetJobs [ID / @tag]
● /addplayerstats [ID / @tag]<enter>[Long Text]
● /addplayeritems [ID / @tag]<enter>[Long Text]
● /Resetplayerstats [ID / @tag]
● /Resetplayeritems [ID / @tag]
● /ID [ID]"""


me_template2 = """—Chara Information—
•ID: /{}
•Name: {}
•Level : {}
•Exp : {}
•Silver : {:,}
•Gold : {:,}
•Sin: {}
•Guild: {}
•Fraction: {}
•Class: {}
•Jobs: {}"""

super_status_list = {
  1: "Member",
  2: "Headmaster",
  3: "Vice Principal",
  4: "Petinggi",
  5: "Coach",
  6: "Teacher",
  7: "Staff"
}

super_clan_list = {
  1: "DM",
  2: "MD"
}

super_sign_type = {
  1: "Murid Penuh Waktu",
  2: "Murid Paruh Waktu"
}

location = {
  0: "town square",
  1: "barrack",
  2: "rainforest",
  3: "garden",
  4: "steppe",
  5: "waterway village",
  6: "death town rugaven",
  7: "nightforest",
  8: "mineshaft",
  9: "crystal terrain",
  10: "temple",
  11: "meakata city",
  12: "carmille land",
  13: "secret mountain",
  14: "catambo region"
}

def super_moneylimit(mid):
    if manage["super_game"]["data_user"][mid]["silver"] > 999999999999999999:
        manage["super_game"]["data_user"][mid]["silver"] = 999999999999999999
    if manage["super_game"]["data_user"][mid]["gold"] > 999999999999999999:
        manage["super_game"]["data_user"][mid]["gold"] = 999999999999999999

def beliEuro(mid, angka):
        harga = 2000000
        total = harga * angka
        if angka <= manage["super_game"]["data_user"][mid]["gold"]:
            manage["super_game"]["data_user"][mid]["silver"] += total
            manage["super_game"]["data_user"][mid]["gold"] -= angka
            return "{} Mengubah berlian sebanyak {:,} ⓑ".format(manage["super_game"]["data_user"][mid]["user_name"], angka)
        else:return "Berlian tidak cukup"

def goldToSilver(mid, angka):
        harga = 1000
        total = angka * harga
        if angka <= manage["super_game"]["data_user"][mid]["gold"]:
            manage["super_game"]["data_user"][mid]["silver"] += total
            manage["super_game"]["data_user"][mid]["gold"] -= angka
            return "Sukses mengganti {} gold menjadi {} silver".format(angka, int(total))
        else:return "Maaf, Gold tidak cukup"

def silverToGold(mid, angka):
        harga = 1000
        total = angka / harga
        p = len(str(total))
        komanya = str(total)[p-2:p]
        print(komanya)
        if ".0" in komanya:
          if angka <= manage["super_game"]["data_user"][mid]["silver"]:
            manage["super_game"]["data_user"][mid]["silver"] -= angka
            manage["super_game"]["data_user"][mid]["gold"] += int(total)
            return "Sukses mengganti {} silver menjadi {} gold".format(angka, int(total))
          else:return "Maaf, silver tidak cukup"
        else:return "Harus kelipatan 1000"

def sortUp(targetnya):
    def sortSecond(val):
        return val[1]
    list_rank = {}
    for a in targetnya:list_rank[a] = targetnya[a]
    new = list_rank
    total1 = sorted(new.items(), key = lambda kv:(kv[1], kv[0]))
    total1.sort(key = sortSecond, reverse = True)
    return total1

def sortUp2(targetnya):
    def sortSecond(val):
        return val[1]
    list_rank = {}
    for a in targetnya:list_rank[a] = targetnya[a]["mono_silver"]
    new = list_rank
    total1 = sorted(new.items(), key = lambda kv:(kv[1], kv[0]))
    total1.sort(key = sortSecond, reverse = True)
    return total1

def sortUp3(targetnya):
    def sortSecond(val):
        return val[1]
    list_rank = {}
    for a in targetnya:list_rank[a] = targetnya[a]["silver"]
    new = list_rank
    total1 = sorted(new.items(), key = lambda kv:(kv[1], kv[0]))
    total1.sort(key = sortSecond, reverse = True)
    return total1

def sortUp4(targetnya, angka):
    def sortSecond(val):
        return val[1]
    list_rank = {}
    for a in targetnya:
      if angka == targetnya[a]["sign_type"]:
        list_rank[a] = targetnya[a]["silver"]
    new = list_rank
    total1 = sorted(new.items(), key = lambda kv:(kv[1], kv[0]))
    total1.sort(key = sortSecond, reverse = True)
    return total1

def getTargetGroup(nomer):
    grup = FGM.getGroupIdsJoined()
    num = int(nomer)-1
    return grup[num]

def reverseDict(dictnya):
  final = {}
  for x in dictnya:
    final.update({dictnya[x].lower():x})

  return final

def getStatusMember(posisi):
    final = []
    statusnya = reverseDict(super_status_list)
    if posisi in statusnya:
      angka = statusnya[posisi]
      for waw in manage["super_game"]["data_user"]:
        if super_status_list[angka] == manage["super_game"]["data_user"][waw]["status"]:
          final.append(waw)

    return final

def getClanMember(posisi):
    final = []
    clannya = reverseDict(super_clan_list)
    if posisi in clannya:
      angka = clannya[posisi]
      for waw in manage["super_game"]["data_user"]:
        if super_clan_list[angka] == manage["super_game"]["data_user"][waw]["clan"]:
          final.append(waw)

    return final

def listSlicer(midMember, count):
    #bagi2 = len(midMember)//count
    midSelect = len(midMember)//count
    total = []
    for mentionMembers in range(midSelect+1):
        dataMid = []
        for dataMention in midMember[mentionMembers*count : (mentionMembers+1)*count]:
            dataMid.append(dataMention)
        total.append(dataMid)
    return total

def mentionUserStatus(to, bagian):
    usernya = getStatusMember(bagian)
    listnya = listSlicer(usernya, 20)
    if usernya == []:
      FGM.sendMessage(to, "Member Kosong")
    else:
      for x in listnya:
          if x != []:
              tagmsg = f"[TAG {bagian.upper()}]"+"".join([f"\n{n}. @! " for n in range(1, len(x)+1)])
              FGM.sendMentionV2(to, tagmsg, x)

def mentionUserClan(to, bagian):
    usernya = getClanMember(bagian)
    listnya = listSlicer(usernya, 20)
    if usernya == []:
      FGM.sendMessage(to, "Member Kosong")
    else:
      for x in listnya:
          if x != []:
              tagmsg = f"[TAG {bagian.upper()}]"+"".join([f"\n{n}. @! " for n in range(1, len(x)+1)])
              FGM.sendMentionV2(to, tagmsg, x)


def checkLevel(to, mid):
    hasil = None
    while True:
      game = manage["super_game"]["data_user"][mid]
      level = game["level"]
      exp = game["exp"]
      rumus = level
      if exp >= rumus and level != 30:
        manage["super_game"]["data_user"][mid]["level"] += 1
        manage["super_game"]["data_user"][mid]["exp"] -= rumus
        hasil = "Selamat, {} naik ke level {}\nExp Anda saat ini: {:,}".format(game["user_name"], manage["super_game"]["data_user"][mid]["level"], manage["super_game"]["data_user"][mid]["exp"])
      else:
        break

    if hasil != None:
      FGM.sendMessage(to, hasil)

def infoLevel(mid):
    game = manage["super_game"]["data_user"][mid]
    level = game["level"]
    exp = game["exp"]
    rumus = level
    if level == 30:
      return "MAX"
    else:return "{:,}/{:,}".format(exp, rumus)

def dailyLogin(to, sender, item):
  hadiah_login = {"exp": 2, "silver": 10}
  game = manage["super_game"]["data_user"][sender]
  if time.time() > game["daily_"+item]:
    if item == "exp":
      if game["level"] != 30:
        manage["super_game"]["data_user"][sender][item] += hadiah_login[item]
        FGM.sendMessage(to, "Sukses mendapat 2 exp")
        checkLevel(to, sender)
      else:
        manage["super_game"]["data_user"][sender][item] += hadiah_login["silver"]
        FGM.sendMessage(to, "Sukses mendapat 10 silver")

    else:
      manage["super_game"]["data_user"][sender][item] += hadiah_login[item]
      FGM.sendMessage(to, "Sukses mendapat 10 silver")

    manage["super_game"]["data_user"][sender]["daily_"+item] = time.time() + 86400

  else:
    FGM.sendMessage(to, "Anda telah melakukan Daily {}. Silahkan tunggu {}".format(item.title(), timeConvert(game["daily_"+item] - time.time())))

def findCommand(regex, text):
  isi = "none"
  hasil = re.findall(regex, text)
  if hasil != []:
    isi = hasil[0]
  return isi

def findUserByID(angka):
    hasil = ""
    for a in manage["super_game"]["data_user"]:
        if angka == manage["super_game"]["data_user"][a]["ID"]:
            hasil += a
            break
    return hasil
#=======================

bc_img = {}
contact_act = {}

def FGMBots(op):
    global contact_act, flood_gc, gc_bl, send_chat_count, game_event, ww_pc, ww_games, status_unsend, delcoowner, deladmin, bcimg
    try:
        if op.type == 0:
            return

        if op.type == 5:
            if op.param1 not in manage["fl_list"]:manage["fl_list"].append(op.param1)

        if op.type in [13,124]:
            #if FGMMID in op.param3 and op.param1 not in gc_bl and op.param2 not in own:
            #    accInv(op.param1)
            if op.param2 in own+manage["co_own"] and FGMMID in op.param3:
                FGM.acceptGroupInvitation(op.param1)

        if op.type == 25:send_chat_count += 1

        if op.type == 26:
           msg = op.message
           text = str(msg.text)
           cmd = text.lower()
           receiver = msg.to
           sender = msg._from
           msg_id = msg.id
           if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
            if msg.toType == 0:
                    if msg._from != FGM.profile.mid:
                        to = msg._from
                    else:
                        to = msg.to
            elif msg.toType == 1:
                    to = msg.to
            elif msg.toType == 2:
                    to = msg.to
            if to not in responlimit:responlimit[to] = time.time()
            if to not in game_event:game_event[to] = {"title": "None"}

            if time.time() > responlimit[to] and msg.toType == 2:

                if msg.contentType == 0 and cmd[0:1] == "/":

                    cmd = cmd.replace("/", "", 1)
                    if text is None:
                      return

                    ### BASIC COMMAND ###
                    print("SEKTOR 1")

                    if cmd == "help":
                        FGM.sendMessage(to, bintang_help_cmd)
# ================================
                    elif cmd == "daftar":
                        if sender not in manage["super_game"]["data_user"]:
                            urutan_id = manage["super_game"]["pendaftar_ke"]
                            manage["super_game"]["data_user"][sender] = {
                                "daily_exp": 0,
                                "daily_silver": 0,
                                "ID": urutan_id - 1,
                                "user_name": FGM.getContact(sender).displayName,
                                "silver": 0,
                                "gold": 0,
                                "exp": 0,
                                "level": 0,
                                "sin": "-",
                                "guild": "-",
                                "fraction": "-",
                                "class":"-", "player_stats":"-", "items":"-", "jobs": "-",
                                "location": 0,
                                "is_walk": False,
                                "go_to": None,
                                "time_arrive": None
                            }
                            FGM.sendMessage(to, "ID: /{}\nUntuk mengecek ID, ketik /my id".format(urutan_id - 1))
                            manage["super_game"]["pendaftar_ke"] += 1
                        else:FGM.sendMessage(to, "Anda sudah daftar")

                    if cmd.startswith("to "):
                      if sender in manage["super_game"]["data_user"]:
                        tujuan = removeCmd(cmd)
                        game = manage["super_game"]["data_user"][sender]
                        #if game["is_walk"]:
                        if 1==2:
                          FGM.sendMessage(to, "Anda masih jalan menuju tempat tujuan")
                        else:
                          statusnya = reverseDict(location)
                          if tujuan in statusnya:
                            angka = statusnya[tujuan]
                            if game["location"] != angka:
                              jaraknya = int(str(game["location"] - angka).replace("-","")) * 600
                              waktunya = time.time() + jaraknya
                              game["is_walk"] = True
                              game["go_to"] = angka
                              game["time_arrive"] = waktunya
                              FGM.sendMessage(to, f"Kamu akan sampai di {tujuan.title()} dalam waktu {timeConvert(jaraknya)}")
                            else:FGM.sendMessage(to, "Lokasi sama")
                          else:FGM.sendMessage(to, "Lokasi tidak ditemukan")

                    if cmd == "listtempat":
                      if sender in manage["super_game"]["data_user"]:
                        statusnya = reverseDict(location)
                        listnya = "[NAMA TEMPAT]"
                        for kiw in statusnya:
                          listnya += "\n - "+kiw
                        FGM.sendMessage(to,listnya)

                    if cmd == "mystep":
                      if sender in manage["super_game"]["data_user"]:
                        game = manage["super_game"]["data_user"][sender]
                        tempatnya = location[game["location"]]
                        if game["is_walk"]:
                          if time.time() > game["time_arrive"]:
                              tempatnya = location[game["go_to"]]
                              game["location"] = game["go_to"]
                              game["is_walk"] = False
                              game["go_to"] = None
                              game["time_arrive"] = None

                              FGM.sendMessage(to, "Kamu sedang berada di "+tempatnya.title())
                          else:
                            sisa_waktu = game["time_arrive"] - time.time()
                            tujuan = location[game["go_to"]]
                            FGM.sendMessage(to, f"Kamu akan sampai di {tujuan.title()} dalam waktu {timeConvert(sisa_waktu)}")

                        else:
                          FGM.sendMessage(to, "Kamu sedang berada di "+tempatnya.title())

                    if cmd == "updategamedb" and sender in own:
                      for x in manage["super_game"]["data_user"]:
                        if "jobs" not in manage["super_game"]["data_user"][x]:
                          #manage["super_game"]["data_user"][x].update({"sin": "-","guild": "-","fraction": "-"})
                          #manage["super_game"]["data_user"][x].update({"class":"-", "player_stats":"-", "items":"-"})
                          manage["super_game"]["data_user"][x].update({"jobs":"-"})
                        #if "clan" not in manage["super_game"]["data_user"][x]:
                        #  manage["super_game"]["data_user"][x].update({"clan": None})

                      FGM.sendMessage(to, "DONE")

                    elif cmd == "my id":
                        if sender in manage["super_game"]["data_user"]:
                            game = manage["super_game"]["data_user"][sender]
                            isian = me_template2.format(
                              game["ID"], game["user_name"], game["level"], infoLevel(sender),
                              game["silver"], game["gold"], game["sin"], game["guild"], game["fraction"], game["class"], game["jobs"]
                            )

                            FGM.sendMessage(to, isian)
                            time.sleep(0.1)
                            FGM.sendMessage(to, "[ Player Stats ]\n"+game["player_stats"])
                            time.sleep(0.1)
                            FGM.sendMessage(to, "[ Items ]\n"+game["items"])
                            time.sleep(0.1)
                            FGM.sendMessage(to, "/"+str(game["ID"]))
                        else:FGM.sendMessage(to, "Ketik /daftar untuk melanjutkan...")

                    elif cmd.startswith("changenameid "):
                        if sender in manage["super_game"]["data_user"]:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 20:
                                    manage["super_game"]["data_user"][sender]["user_name"] = name
                                    FGM.sendMessage(to, "Berhasil mengubah nama menjadi "+name)
                                else:FGM.sendMessage(to, "Kepanjangan kak.. Max 20 Huruf")
                        else:FGM.sendMessage(to, "Ketik /daftar untuk melanjutkan...")

                    if cmd == "dailyexp" and sender in manage["super_game"]["data_user"]:
                      dailyLogin(to, sender, "exp")

                    if cmd == "dailysilv" and sender in manage["super_game"]["data_user"]:
                      dailyLogin(to, sender, "silver")

                    if cmd == findCommand("change[0-9]+silver",cmd):
                        if sender in manage["super_game"]["data_user"]:
                            belah = re.findall("(?:change)([0-9]+)",cmd)[0]
                            if int(belah) > 0:
                                FGM.sendMessage(to, silverToGold(sender, int(belah)))
                            else:
                              FGM.sendMessage(to, "Angka minus")
                        else:FGM.sendMessage(to, "Daftar dulu kak...\nKetik #daftar")

                    if cmd == findCommand("change[0-9]+gold",cmd):
                        if sender in manage["super_game"]["data_user"]:
                            belah = re.findall("(?:change)([0-9]+)",cmd)[0]
                            if int(belah) > 0:
                                FGM.sendMessage(to, goldToSilver(sender, int(belah)))
                            else:
                              FGM.sendMessage(to, "Angka minus")
                        else:FGM.sendMessage(to, "Daftar dulu kak...\nKetik #daftar")

                    if findCommand("give[0-9]+silv",cmd) in cmd:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:give)([0-9]+)",cmd)[0])
                        if sender in manage["super_game"]["data_user"] and penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                            if angka <= manage["super_game"]["data_user"][sender]["silver"] and angka > 0:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][sender]["silver"] -= angka
                                manage["super_game"]["data_user"][penerima]["silver"] += angka
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mengirim {angka} Silver ke id lain")
                            else:FGM.sendMessage(to, "Maaf, Silver tidak cukup")
                          #else:FGM.sendMessage(to, "Akun dibanned karena belum membayar hutang")
                        else:FGM.sendMessage(to, "Penerima / Pengirim Blm daftar\nKetik /daftar")

                    if findCommand("give[0-9]+gold",cmd) in cmd:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:give)([0-9]+)",cmd)[0])
                        if sender in manage["super_game"]["data_user"] and penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                            if angka <= manage["super_game"]["data_user"][sender]["gold"] and angka > 0:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][sender]["gold"] -= angka
                                manage["super_game"]["data_user"][penerima]["gold"] += angka
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mengirim {angka} Gold ke id lain")
                            else:FGM.sendMessage(to, "Maaf, Gold tidak cukup")
                          #else:FGM.sendMessage(to, "Akun dibanned karena belum membayar hutang")
                        else:FGM.sendMessage(to, "Penerima / Pengirim Blm daftar\nKetik /daftar")

                    if cmd.startswith("cnama "):
                        if sender in manage["super_game"]["data_user"]:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 20:
                                    manage["super_game"]["data_user"][sender]["user_name"] = name
                                    FGM.sendMessage(to, "Berhasil mengubah nama menjadi "+name)
                                else:FGM.sendMessage(to, "Kepanjangan kak.. Max 20 Huruf")
                        else:FGM.sendMessage(to, "Daftar dulu kak...\nKetik #daftar")

                    elif cmd.startswith("ubahgold "):
                        if sender in manage["super_game"]["data_user"]:
                            belah = removeCmd(text).split(" ")
                            if int(belah[0]) > 0:
                                FGM.sendMessage(to, beliEuro(sender, int(belah[0])))
                        else:FGM.sendMessage(to, "Daftar dulu kak...\nKetik #daftar")

            # =========== OWNER
                    if cmd.startswith("changesin ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" @")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                rem = removeCmd(text).split("~")
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        manage["super_game"]["data_user"][mid]["sin"] = rem[0].title()
                        FGM.sendMessage(to, "DONE")
                       
                    if cmd.startswith("changeguild ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" @")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                rem = removeCmd(text).split("~")
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        manage["super_game"]["data_user"][mid]["guild"] = rem[0].title()
                        FGM.sendMessage(to, "DONE") 

                    if cmd.startswith("changefraction ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" @")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                rem = removeCmd(text).split("~")
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        manage["super_game"]["data_user"][mid]["fraction"] = rem[0].title()
                        FGM.sendMessage(to, "DONE")

                    if cmd.startswith("changeclass ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" @")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                rem = removeCmd(text).split("~")
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        manage["super_game"]["data_user"][mid]["class"] = rem[0].title()
                        FGM.sendMessage(to, "DONE") 

                    if cmd.startswith("changejobs ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" @")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                rem = removeCmd(text).split("~")
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        manage["super_game"]["data_user"][mid]["jobs"] = rem[0].title()
                        FGM.sendMessage(to, "DONE") 

                    if findCommand("addsilver[0-9]+",cmd) in cmd and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:addsilver)([0-9]+)",cmd)[0])
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["silver"] += angka
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mengirim {angka} Silver ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar\nKetik /daftar")

                    if findCommand("addgold[0-9]+",cmd) in cmd and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:addgold)([0-9]+)",cmd)[0])
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["gold"] += angka
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mengirim {angka} Gold ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar\nKetik /daftar")

                    if findCommand("addexp[0-9]+",cmd) in cmd and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:addexp)([0-9]+)",cmd)[0])
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["exp"] += angka
                                FGM.sendMessage(to, f"Sukses mengirim {angka} exp ke id lain")
                                checkLevel(to, penerima)
                        else:FGM.sendMessage(to, "Pengirim Blm daftar\nKetik /daftar")

                    if cmd.startswith("addplayerstats ") and sender in own+manage["co_own"]:
                        long_text = removeCmdEnter(text)
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(removeCmd(text).split("\n")[0])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        if penerima in manage["super_game"]["data_user"]:
                            manage["super_game"]["data_user"][penerima]["player_stats"] = long_text
                            FGM.sendMessage(to, f"Sukses add player stats ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("addplayeritems ") and sender in own+manage["co_own"]:
                        long_text = removeCmdEnter(text)
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(removeCmd(text).split("\n")[0])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        if penerima in manage["super_game"]["data_user"]:
                            manage["super_game"]["data_user"][penerima]["items"] = long_text
                            FGM.sendMessage(to, f"Sukses add player items ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if findCommand("reducesilver[0-9]+",cmd) in cmd and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:reducesilver)([0-9]+)",cmd)[0])
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["silver"] -= angka
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mengurangi {angka} Silver ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar\nKetik /daftar")

                    if findCommand("reducegold[0-9]+",cmd) in cmd and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:reducegold)([0-9]+)",cmd)[0])
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["gold"] -= angka
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mengurangi {angka} Gold ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar\nKetik /daftar")

                    if findCommand("reduceexp[0-9]+",cmd) in cmd and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        angka = int(re.findall("(?:reduceexp)([0-9]+)",cmd)[0])
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["exp"] -= angka
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mengurangi {angka} exp ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar\nKetik /daftar")

                    if cmd.startswith("resetgold to ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["gold"] = 0
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mereset Gold ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetsilver to ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["silver"] = 0
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mereset Silver ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")


                    if cmd.startswith("resetlevel to ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                          #if sender not in manage["pm_list"]:
                                info = manage["super_game"]["data_user"]
                                manage["super_game"]["data_user"][penerima]["exp"] = 0
                                manage["super_game"]["data_user"][penerima]["level"] = 0
                                super_moneylimit(penerima)
                                FGM.sendMessage(to, f"Sukses mereset Level ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetsin ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                                manage["super_game"]["data_user"][penerima]["sin"] = "-"
                                FGM.sendMessage(to, f"Sukses mereset sin ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetguild ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                                manage["super_game"]["data_user"][penerima]["guild"] = "-"
                                FGM.sendMessage(to, f"Sukses mereset guild ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetfraction ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                                manage["super_game"]["data_user"][penerima]["fraction"] = "-"
                                FGM.sendMessage(to, f"Sukses mereset fraction ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetclass ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                                manage["super_game"]["data_user"][penerima]["class"] = "-"
                                FGM.sendMessage(to, f"Sukses mereset class ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetjobs ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text).split(" ")
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem[1])
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                                manage["super_game"]["data_user"][penerima]["jobs"] = "-"
                                FGM.sendMessage(to, f"Sukses mereset jobs ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetplayerstats ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text)
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem)
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                                manage["super_game"]["data_user"][penerima]["player_stats"] = "-"
                                FGM.sendMessage(to, f"Sukses mereset player stats ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("resetplayeritems ") and sender in own+manage["co_own"]:
                        rem = removeCmd(text)
                        mid = ""
                        cektag = getMidMentionV2(msg.contentMetadata, text)
                        if cektag != []:mid = cektag[0]
                        if cektag == []:
                            try:
                                angka = int(rem)
                                mid = findUserByID(angka)
                            except:pass
                        penerima = mid
                        print(mid)
                        if penerima in manage["super_game"]["data_user"]:
                                manage["super_game"]["data_user"][penerima]["items"] = "-"
                                FGM.sendMessage(to, f"Sukses mereset player items ke id lain")
                        else:FGM.sendMessage(to, "Pengirim Blm daftar")

                    if cmd.startswith("id ") and sender in own+manage["co_own"]+manage["admin"]:
                        try:
                            rem = removeCmd(text)
                            mid = ""
                            cektag = getMidMentionV2(msg.contentMetadata, text)
                            if cektag != []:mid = cektag[0]
                            if cektag == []:
                                try:
                                    angka = int(rem)
                                    mid = findUserByID(angka)
                                except:pass
                            sender = mid
                            print(sender)
                            game = manage["super_game"]["data_user"][sender]
                            isian = me_template2.format(
                              game["ID"], game["user_name"], game["level"], infoLevel(sender),
                              game["silver"], game["gold"], game["sin"], game["guild"], game["fraction"], game["class"], game["jobs"]
                            )

                            FGM.sendMessage(to, isian)
                            time.sleep(0.1)
                            FGM.sendMessage(to, "[ Player Stats ]\n"+game["player_stats"])
                            time.sleep(0.1)
                            FGM.sendMessage(to, "[ Items ]\n"+game["items"])
                            time.sleep(0.1)
                            FGM.sendMessage(to, "/"+str(game["ID"]))
                        except Exception as e:
                          traceback.print_tb(e.__traceback__)
                          print(e)
                          FGM.sendMessage(to, "ID tidak ditemukan")


                    elif cmd.startswith(",,,resetgold ") and sender in own+manage["co_own"]+manage["admin"]:
                        org = getMidMentionV2(msg.contentMetadata, text)[0]
                        if org in manage["super_game"]["data_user"]:
                            manage["super_game"]["data_user"][org]["gold"] = 0
                            FGM.sendMessage(to, "Done reset gold")

                    elif cmd.startswith(",,,,resetsilver ") and sender in own+manage["co_own"]+manage["admin"]:
                        org = getMidMentionV2(msg.contentMetadata, text)[0]
                        if org in manage["super_game"]["data_user"]:
                            manage["super_game"]["data_user"][org]["silver"] = 0
                            FGM.sendMessage(to, "Done reset silver")

                    elif cmd == "resetallgold" and sender in own+manage["co_own"]+manage["admin"]:
                        for org in manage["super_game"]["data_user"]:
                            manage["super_game"]["data_user"][org]["gold"] = 0
                        FGM.sendMessage(to, "Done reset gold")

                    elif cmd == "resetallsilver" and sender in own+manage["co_own"]+manage["admin"]:
                        for org in manage["super_game"]["data_user"]:
                            manage["super_game"]["data_user"][org]["silver"] = 0
                        FGM.sendMessage(to, "Done reset silver")

                    elif cmd.startswith("cheatgold ") and sender in own+manage["co_own"]:
                        if sender in manage["super_game"]["data_user"]:
                            angka = int(removeCmd(text))
                            manage["super_game"]["data_user"][sender]["gold"] += angka
                            super_moneylimit(sender)
                            FGM.sendMessage(to, "Done tambah gold")
                        else:FGM.sendMessage(to, "Daftar dulu kak...\nKetik #daftar")

                    elif cmd.startswith("cheatsilver ") and sender in own+manage["co_own"]:
                        if sender in manage["super_game"]["data_user"]:
                            angka = int(removeCmd(text))
                            manage["super_game"]["data_user"][sender]["silver"] += angka
                            super_moneylimit(sender)
                            FGM.sendMessage(to, "Done tambah silver")
                        else:FGM.sendMessage(to, "Daftar dulu kak...\nKetik #daftar")

                    elif cmd == "statuslist" and sender in own+manage["co_own"]:
                        hsl = "[STATUS LIST]"
                        for x in range(1, len(super_status_list)+1):
                            hsl += "\n{}. {}".format(x, super_status_list[x])
                        FGM.sendMessage(to, hsl)


                    if cmd.startswith("addstatus ") and sender in own+manage["co_own"]:
                        posisi = removeCmd(text).split(" @")[0].lower()
                        statusnya = reverseDict(super_status_list)
                        if posisi in statusnya:
                          angka = statusnya[posisi]
                          jabatan = super_status_list[angka]
                          for midnya in getMidMentionV2(msg.contentMetadata, text):
                            if midnya in manage["super_game"]["data_user"]:
                              manage["super_game"]["data_user"][midnya]["status"] = jabatan
                              FGM.sendMessage(to, "Berhasil add status "+posisi)
                            else:
                              FGM.sendMessage(to, "Tidak terdaftar dalam bot")
                        else:FGM.sendMessage(to, "Status tidak ditemukan")

                    if cmd.startswith("delstatus ") and sender in own+manage["co_own"]:
                          for midnya in getMidMentionV2(msg.contentMetadata, text):
                            if midnya in manage["super_game"]["data_user"]:
                              manage["super_game"]["data_user"][midnya]["status"] = super_status_list[1]
                              FGM.sendMessage(to, "Berhasil menghapus status")
                            else:
                              FGM.sendMessage(to, "Tidak terdaftar dalam bot")

                    if cmd.startswith("resetstatus ") and sender in own+manage["co_own"]:
                        posisi = removeCmd(text).split(" ")[0].lower()
                        statusnya = reverseDict(super_status_list)
                        if posisi in statusnya:
                          angka = statusnya[posisi]
                          for waw in manage["super_game"]["data_user"]:
                            if super_status_list[angka] == manage["super_game"]["data_user"][waw]["status"]:
                              manage["super_game"]["data_user"][waw]["status"] = super_status_list[1]

                        FGM.sendMessage(to, "Sukses reset status")

                    if cmd.startswith("addclan ") and sender in own+manage["co_own"]:
                        posisi = removeCmd(text).split(" ")[0].lower()
                        clannya = reverseDict(super_clan_list)
                        if posisi in clannya:
                          angka = clannya[posisi]
                          for midnya in getMidMentionV2(msg.contentMetadata, text):
                            if midnya in manage["super_game"]["data_user"]:
                              manage["super_game"]["data_user"][midnya]["clan"] = super_clan_list[angka]
                              FGM.sendMessage(to, "Berhasil add clan "+posisi)
                            else:
                              FGM.sendMessage(to, "Tidak terdaftar dalam bot")
                        else:FGM.sendMessage(to, "clan tidak ditemukan")

                    if cmd.startswith("delclan ") and sender in own+manage["co_own"]:
                          for midnya in getMidMentionV2(msg.contentMetadata, text):
                            if midnya in manage["super_game"]["data_user"]:
                              manage["super_game"]["data_user"][midnya]["clan"] = None
                              FGM.sendMessage(to, "Berhasil menghapus clan")
                            else:
                              FGM.sendMessage(to, "Tidak terdaftar dalam bot")

                    if cmd.startswith("farel") and sender in own:
                                try:
                                    sep = text.split("\n")
                                    cond = text.replace(sep[0] + "\n","")
                                    exec(cond)
                                except Exception as error:
                                    FGM.sendMessage(to,'ERROR EXECUTE\n'+str(error))


                    if cmd.startswith("resetclan ") and sender in own+manage["co_own"]:
                        posisi = removeCmd(text).split(" ")[0].lower()
                        clannya = reverseDict(super_clan_list)
                        if posisi in clannya:
                          angka = clannya[posisi]
                          for waw in manage["super_game"]["data_user"]:
                            if super_clan_list[angka] == manage["super_game"]["data_user"][waw]["clan"]:
                              manage["super_game"]["data_user"][waw]["clan"] = None

                        FGM.sendMessage(to, "Sukses reset clan")

                    elif cmd.startswith("cstatus ") and sender in own+manage["co_own"]:
                        penerima = getMidMentionV2(msg.contentMetadata, text)[0]
                        angka = int(removeCmd(text).split(" ")[0])
                        if penerima in manage["super_game"]["data_user"] and angka in super_status_list:
                            manage["super_game"]["data_user"][penerima]["status"] = super_status_list[angka]
                            FGM.sendMessage(to, "Berhasil mengubah status")

                    elif cmd.startswith("findmem ") and sender in own+manage["co_own"]:
                        waw = int(removeCmd(text))
                        total = sortUp3(manage["super_game"]["data_user"])
                        midnya = total[waw-1][0]
                        FGM.sendContact(to, midnya)
                        #game = manage["super_game"]["data_user"][midnya]
                        #isian = me_template2.format(game["user_name"], game["status"],"-" if game["clan"] == None else game["clan"], game["silver"], game["gold"], super_sign_type[game["sign_type"]] if game["sign_type"] != None else "-")
                        #tagMessage(to, isian, midnya)

                    if cmd.startswith("deltype ") and sender in own+manage["co_own"]:
                        tagmid = getMidMentionV2(msg.contentMetadata, text)
                        if tagmid == []:
                          belah = removeCmd(text).split(" ")
                          angka, waw = int(belah[0]), int(belah[1])
                          total = sortUp4(manage["super_game"]["data_user"], angka)
                          midnya = total[waw-1][0]
                          manage["super_game"]["data_user"][midnya]["sign_type"] = None
                          FGM.sendMessage(to, "DONE")

                        else:
                          for midnya in tagmid:
                            if midnya in manage["super_game"]["data_user"]:
                              manage["super_game"]["data_user"][midnya]["sign_type"] = None
                              FGM.sendMessage(to, "DONE")

                    elif cmd.startswith("delmem ") and sender in own+manage["co_own"]:
                        waw = int(removeCmd(text))
                        total = sortUp3(manage["super_game"]["data_user"])
                        del manage["super_game"]["data_user"][total[waw-1][0]]
                        """
                        data_sementara = {}
                        for x in manage["super_game"]["data_user"]:
                            infoan = manage["super_game"]["data_user"][x]
                            data_sementara.update({infoan["ID"]: x})
                        del manage["super_game"]["data_user"][data_sementara[waw]]
                        """
                        FGM.sendMessage(to, "Done apus User urutan no "+str(waw))

                    elif cmd == "listmem" and sender in own+manage["co_own"]:
                        isian = "[LIST DATA]"
                        num = 1
                        total = sortUp3(manage["super_game"]["data_user"])
                        for waw in total:
                            infoan = manage["super_game"]["data_user"][waw[0]]
                            isian += "\n{}. {}\n{:,} € | {:,} ⓑ".format(num, infoan["user_name"], infoan["silver"], infoan["gold"])
                            num += 1
                        FGM.sendMessage(to, isian)

                    if cmd.startswith("signtype ") and sender in manage["super_game"]["data_user"]:
                        angka = int(removeCmd(text))
                        if angka in super_sign_type:
                          manage["super_game"]["data_user"][sender]["sign_type"] = angka
                          FGM.sendMessage(to, "Berhasil daftar menjadi "+super_sign_type[angka])
                        else:
                          FGM.sendMessage(to, "Type tidak ditemukan")

                    elif cmd.startswith("listtype ") and sender in own+manage["co_own"]:
                      angka = int(removeCmd(text))
                      if angka in super_sign_type:
                        isian = f"[LIST TYPE {angka}]"
                        num = 1
                        total = sortUp4(manage["super_game"]["data_user"], angka)
                        for waw in total:
                            infoan = manage["super_game"]["data_user"][waw[0]]
                            isian += "\n{}. {}".format(num, infoan["user_name"])
                            num += 1
                        FGM.sendMessage(to, isian)

                    if cmd.startswith("cnama "):
                        if sender in own+manage["co_own"]:
                            tagmid = getMidMentionV2(msg.contentMetadata, text)
                            for midnya in tagmid:
                                name = removeCmd(text).split(" @")[0]
                                if len(name) <= 20:
                                    manage["super_game"]["data_user"][midnya]["user_name"] = name
                                    FGM.sendMessage(to, "Berhasil mengubah nama menjadi "+name)
                                else:FGM.sendMessage(to, "Kepanjangan kak.. Max 20 Huruf")

#================== SIDER TAG ALL ===============   
                    if cmd.startswith("tagall ") and sender in manage["super_game"]["data_user"]:
                      posisi = removeCmd(text).split(" ")[0].lower()
                      if posisi in ["petinggi", "coach", "teacher", "staff"]:
                        mentionUserStatus(to, posisi)
                      if posisi in ["md","dm"]:
                        mentionUserClan(to, posisi)

                    elif cmd == "jodohku":
                            if msg.toType == 2:
                                group = FGM.getGroup(to)
                                org = [contact['mid'] for contact in group['members']]
                                jodoh = random.choice(org)
                                FGM.sendMentionV2(to, "@! adalah jodohnya @!", [jodoh, sender])
                            else:
                                FGM.sendMessage(to, "Fitur ini hanya bisa digunakan di grup chat")
                                

                    if cmd == 'tagall':
                          if msg.toType == 2:
                            group = FGM.getGroup(to)
                            midMembers = [contact['mid'] for contact in group['members']]
                            midSelect = len(midMembers)//20
                            no = 0
                            for mentionMembers in range(midSelect+1):
                                ret_ = "╔══[ Mention Members ]"
                                dataMid = []
                                for dataMention in group['members'][mentionMembers*20 : (mentionMembers+1)*20]:
                                    dataMid.append(dataMention["mid"])
                                    no += 1
                                    ret_ += "\n╠ {}. @!".format(str(no))
                                ret_ += "\n╚══[ Total {} Members]".format(str(len(dataMid)))
                                no = (no)
                                FGM.sendMentionV2(to, ret_, dataMid)

                    elif cmd == "ciduk on":
                            readTime = getNewTime()
                            if to in read['readPoint']:
                                try:
                                    del read['readPoint'][to]
                                    del read['readMember'][to]
                                    del read['mode'][to]
                                except:
                                    pass
                                read['readPoint'][to] = msg_id
                                read['readMember'][to] = []
                                read['mode'][to] = True
                                FGM.sendMessage(to, "Lurking telah diaktifkan")
                            else:
                                try:
                                    del read['readPoint'][to]
                                    del read['readMember'][to]
                                except:
                                    pass
                                read['readPoint'][to] = msg_id
                                read['readMember'][to] = []
                                FGM.sendMessage(to, "Set reading point : \n{}".format(readTime))
                    elif cmd == "ciduk off":
                            readTime = getNewTime()
                            if to not in read['readPoint']:
                                FGM.sendMessage(to,"Lurking telah dinonaktifkan")
                            else:
                                try:
                                    del read['readPoint'][to]
                                    del read['readMember'][to]
                                    del read['mode'][to]
                                except:
                                    pass
                                FGM.sendMessage(to, "Delete reading point : \n{}".format(readTime))
                    elif cmd == "ciduk":
                            if to in read['readPoint']:
                                if read["readMember"][to] == []:
                                    return FGM.sendMessage(to, "Tidak Ada Sider")
                                else:
                                    no = 0
                                    result = "╔══[ Reader ]"
                                    for dataRead in read["readMember"][to]:
                                        no += 1
                                        result += "\n╠ {}. @!".format(str(no))
                                    result += "\n╚══[ Total {} Sider ]".format(str(len(read["readMember"][to])))
                                    FGM.sendMentionV2(to, result, read["readMember"][to])
                                    read['readMember'][to] = []

                    if cmd == 'sider on':
                                if to not in cctv['point2']:
                                    cctv['point2'][to] = msg_id
                                    cctv['sidermem'][to] = []
                                    cctv['cyduk'][to] = True 
                                    FGM.sendMessage(to, "••➤ Ciduk otomatis on")
                                else:
                                    FGM.sendMessage(to, "••➤ Ciduk otomatis on")
                            
                    if cmd == 'sider off':
                                if to in cctv['point2']:
                                    del cctv['point2'][to]
                                    del cctv['sidermem'][to]
                                    del cctv['cyduk'][to]
                                    FGM.sendMessage(to, "••➤ Ciduk otomatis off")
                                else:
                                    FGM.sendMessage(to, "••➤ Ciduk otomatis off")

                    if cmd == 'detectunsend on':
                        if to not in status_unsend:
                            status_unsend.append(to)
                        FGM.sendMessage(to, "mengaktifkan fitur unsend. Jika diaktifkan bila anggota grup unsend pesan, pesan tersebut akan ditampilkan oleh bot.")

                    if cmd == 'detectunsend off':
                        if to in status_unsend:
                            status_unsend.remove(to)
                        FGM.sendMessage(to, "menonaktifkan fitur unsend. Jika diaktifkan bila anggota grup unsend pesan, pesan tersebut akan ditampilkan oleh bot.")

                    if cmd == "mybio":
                                h = FGM.getContact(sender)
                                FGM.sendMessage(to, "「 Status 」\n"+str(h.statusMessage))

                    if cmd == "mydp":
                                h = FGM.getContact(sender)
                                image = "https://obs.line-scdn.net/" + h.pictureStatus
                                FGM.sendImageWithURL(to, image)

                    if cmd.startswith("bio "):
                                    lists = getMidMentionV2(msg.contentMetadata, text)
                                    for ls in lists:
                                        contact = FGM.getContact(ls)
                                        FGM.sendMessage(to, "{}".format(str(contact.statusMessage)))

                    if cmd.startswith("displaypicture "):
                                    lists = getMidMentionV2(msg.contentMetadata, text)
                                    for ls in lists:
                                        h = FGM.getContact(ls)
                                        image = "https://obs.line-scdn.net/" + h.pictureStatus
                                        FGM.sendImageWithURL(to, image)

                    elif cmd == "randomdice":
                        acak = random.randint(1,6)
                        FGM.sendMessage(to, "Dadu Angka {}".format(acak))

                    elif cmd == "flipcoin":
                        acak = random.choice(["Head", "Tail"])
                        FGM.sendMessage(to, "{}".format(acak))

                    if cmd == "updb" and sender in own:
                        manage.update({"super_game":{
                            "data_user":{},
                            "pendaftar_ke": 1
                        }})

                    if cmd == "listgrup" and sender in own+manage["co_own"]:
                                gid = FGM.getGroupIdsJoined()
                                #sd = FGM.getGroups(gid)
                                ret = "「 Group List 」\n"
                                no = 0
                                total = len(gid)
                                cd = "\n\nTotal {} Groups".format(total)
                                for xx in gid:
                                    G = FGM.getGroup(xx)
                                    member = len(G['members'])
                                    no += 1
                                    ret += "\n{}. {} {}".format(no, G['name'][0:20], member)
                                ret += cd
                                k = len(ret)//10000
                                for aa in range(k+1):
                                    #FGM.sendMessage(msg.to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                                    FGM.sendMessage(to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))


                    if cmd.startswith("outgrup ") and sender in own+manage["co_own"]:
                            anaa = int(removeCmd(text))
                            gcnya = FGM.getGroupIdsJoined()
                            gcid = gcnya[int(anaa)-1]
                            FGM.leaveGroup(gcid)
                            FGM.sendMessage(to, "DONE")

                    if cmd == "owner" and sender in own+manage["co_own"]:
                        FGM.sendMessage(to, help_own)

                    if cmd == "byeallgc" and sender in own+manage["co_own"]:
                        gcid = FGM.getGroupIdsJoined()
                        for a in gcid:
                            if a != to:
                                FGM.leaveGroup(a)
                        FGM.sendMessage(to, "Done")

                    if cmd.startswith("bc ") and sender in own+manage["co_own"]:
                                txt = removeCmd(text)
                                groups = FGM.getGroupIdsJoined()
                                for group in groups:
                                    FGM.sendMessage(group, "「 Siaran Radio MonoBee 」\n\n{}".format(str(txt)))
                                    #time.sleep(1)
                                FGM.sendMessage(to, "Succes broadcast to {} group".format(str(len(groups))))

                    if cmd.startswith("pesangrup ") and sender in own+manage["co_own"]:
                        anu = removeCmd(text)
                        angka = int(anu.split(" ")[0])
                        pesan = removeCmd(anu)
                        tujuan = getTargetGroup(angka)
                        FGM.sendMessage(tujuan, pesan)
                        time.sleep(0.3)
                        FGM.sendMessage(to, "DONE")

                    if cmd.startswith("bcimg ") and sender in own+manage["co_own"]:
                            bc_img["status"] = True
                            bc_img["text"] = removeCmd(text)
                            FGM.sendMessage(to,"SEND FOTO...")

                    if cmd == "cban" and sender in own+manage["co_own"]:
                        gc_bl.clear()
                        FGM.sendMessage(to, "DONE")

                    if cmd == "chats" and sender in own+manage["co_own"]:
                        FGM.sendMessage(to, str(send_chat_count))

                    if cmd == "tiket" and sender in own+manage["co_own"]:
                        tiket = "https://line.me/ti/p/" + FGM.getSettings().contactMyTicket
                        FGM.sendMessage(to, tiket)

                    if cmd == "ubahpicture" and sender in own+manage["co_own"]:
                                changepic["status"] = True
                                FGM.sendMessage(to, "Silahkan kirim gambarnya")

                    if cmd.startswith("ubahnama: ") and sender in own+manage["co_own"]:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 20:
                                    profile = FGM.getProfile()
                                    profile.displayName = name
                                    FGM.updateProfile(profile)
                                    FGM.sendMessage(to, "Berhasil mengubah nama menjadi : {}".format(name))

                    if cmd.startswith("ubahbio: ") and sender in own+manage["co_own"]:
                                sep = text.split(" ")
                                bio = text.replace(sep[0] + " ","")
                                if len(bio) <= 500:
                                    profile = FGM.getProfile()
                                    profile.statusMessage = bio
                                    FGM.updateProfile(profile)
                                    FGM.sendMessage(to, "Berhasil mengubah bio menjadi : {}".format(bio))

                    elif cmd == "grouplist" and sender in own+manage["co_own"]:
                                gid = FGM.getGroupIdsJoined()
                                sd = FGM.getGroups(gid)
                                ret = "「 Group List 」\n"
                                no = 0
                                total = len(gid)
                                cd = "\n\nTotal {} Groups".format(total)
                                for G in sd:
                                    member = len(G['members'])
                                    no += 1
                                    ret += "\n{}. {} {}".format(no, G['name'][0:20], member)
                                ret += cd
                                k = len(ret)//10000
                                for aa in range(k+1):
                                    FGM.sendMessage(msg.to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))

                    elif cmd == "resetcoowner" and sender in own+manage["co_own"]:
                            manage["co_own"] = []
                            FGM.sendMessage(to, "DONE")

                    elif cmd == "resetadmin" and sender in own+manage["co_own"]:
                            manage["admin"] = []
                            FGM.sendMessage(to, "DONE")

                    if cmd == "addadmin" and sender in own+manage["co_own"]:
                            contact_act.update({
                                sender:{
                                  "act": "add",
                                  "posiiton": "admin",
                                }
                              })
                            FGM.sendMessage(to, "Send contact")

                    if cmd == "addcoowner" and sender in own+manage["co_own"]:
                            contact_act.update({
                                sender:{
                                  "act": "add",
                                  "posiiton": "co_own",
                                }
                              })
                            FGM.sendMessage(to, "Send contact")

                    elif cmd.startswith('addcoowner ') and sender in own+manage["co_own"]:
                            sep = text.lower().split(" ")
                            isi = text.lower().replace(sep[0] + " ","")
                            tag = getMidMentionV2(msg.contentMetadata, text)
                            pesan = "Berhasil menambahkan co own"
                            for isi in tag:
                                if isi not in manage["co_own"]:
                                       manage["co_own"].append(isi)
                            FGM.sendMessage(to, pesan)

                    if cmd == "delcoowner" and sender in own+manage["co_own"]:
                            delcoowner = sender
                            FGM.sendMessage(to, "Kirim kontak")

                    if cmd.startswith('delcoowner ') and sender in own+manage["co_own"]:
                            sep = text.lower().split(" ")
                            isi = text.lower().replace(sep[0] + " ","")
                            tag = getMidMentionV2(msg.contentMetadata, text)
                            pesan = "Berhasil menghapus co own"
                            for isi in tag:
                                if isi in manage["co_own"]:
                                   manage["co_own"].remove(isi)
                            FGM.sendMessage(to, pesan)


                    elif cmd.startswith('addadmin ') and sender in own+manage["co_own"]:
                            sep = text.lower().split(" ")
                            isi = text.lower().replace(sep[0] + " ","")
                            tag = getMidMentionV2(msg.contentMetadata, text)
                            pesan = "Berhasil menambahkan admin"
                            for isi in tag:
                                if isi not in manage["admin"]:
                                       manage["admin"].append(isi)
                            FGM.sendMessage(to, pesan)

                    if cmd == "deladmin" and sender in own+co_own:
                            deladmin = sender
                            FGM.sendMessage(to, "Kirim kontak")

                    if cmd.startswith('deladmin ') and sender in own+manage["co_own"]:
                            sep = text.lower().split(" ")
                            isi = text.lower().replace(sep[0] + " ","")
                            tag = getMidMentionV2(msg.contentMetadata, text)
                            pesan = "Berhasil menghapus admin"
                            for isi in tag:
                                if isi in manage["admin"]:
                                   manage["admin"].remove(isi)
                            FGM.sendMessage(to, pesan)

                    elif cmd == "listcoowner" and sender in own+manage["co_own"]:
                            ma = ""
                            mb = ""
                            mc = ""
                            a = 0
                            b = 0
                            c = 0
                            for m_id in manage["co_own"]:
                                a = a + 1
                                end = '\n'
                                try:ma += str(a) + ". " +FGM.getContact(m_id).displayName + "\n"
                                except:ma += str(a) + ". " +"Deleted Account" + "\n"
                            #for m_id in manage["admin2"]:
                            #    b = b + 1
                            #    end = '\n'
                            #    try:mb += str(b) + ". " +FGM.getContact(m_id).displayName + "\n"
                            #    except:mb += str(b) + ". " +"Deleted Account" + "\n"
                            #for m_id in manage["co_own"]:
                            #    c = c + 1
                            #    end = '\n'
                            #    try:mc += str(c) + ". " +FGM.getContact(m_id).displayName + "\n"
                            #    except:mc += str(c) + ". " +"Deleted Account" + "\n"
                            FGM.sendMessage(to, "✒ [ᴀᴅᴍɪɴɪsᴛʀᴀᴛɪᴏɴ]\nCo own:\n"+ma)

                    elif cmd == "listadmin" and sender in own+manage["co_own"]:
                            ma = ""
                            mb = ""
                            mc = ""
                            a = 0
                            b = 0
                            c = 0
                            for m_id in manage["admin"]:
                                a = a + 1
                                end = '\n'
                                try:ma += str(a) + ". " +FGM.getContact(m_id).displayName + "\n"
                                except:ma += str(a) + ". " +"Deleted Account" + "\n"
                            #for m_id in manage["admin2"]:
                            #    b = b + 1
                            #    end = '\n'
                            #    try:mb += str(b) + ". " +FGM.getContact(m_id).displayName + "\n"
                            #    except:mb += str(b) + ". " +"Deleted Account" + "\n"
                            #for m_id in manage["co_own"]:
                            #    c = c + 1
                            #    end = '\n'
                            #    try:mc += str(c) + ". " +FGM.getContact(m_id).displayName + "\n"
                            #    except:mc += str(c) + ". " +"Deleted Account" + "\n"
                            FGM.sendMessage(to, "✒ [ᴀᴅᴍɪɴɪsᴛʀᴀᴛɪᴏɴ]\nAdmin:\n"+ma)

                    elif cmd == "reboot" and sender in own+manage["co_own"]:
                        FGM.sendMessage(to, "Bot direboot")
                        restartBot()

                if msg.contentType == 1:
                        if changepic["status"] == True:
                                try:
                                    path = FGM.downloadObjectMsg(msg.id)
                                    changepic["status"] = False
                                    FGM.updateProfilePicture(path)
                                    FGM.sendMessage(to, "Berhasil mengubah foto profile")
                                    FGM.deleteFile(path)
                                except:FGM.sendMessage(to, "Tahap ini gagal. Silahkan kirim foto yang sama")

                        if bc_img["status"] == True and sender in own+manage["co_own"]:
                            path = FGM.downloadObjectMsg(msg_id)
                            pesan = bc_img["text"]
                            bc_img = {"status":False,"text":None}
                            FGM.sendMessage(to, "BROADCAST IMAGE DIPROSES...")
                            gid = FGM.getGroupIdsJoined()
                            done = []
                            start = time.time()
                            for i in gid:
                                try:
                                    FGM.sendImage(i,path)
                                    time.sleep(2)
                                    FGM.sendMessage(i, pesan)
                                    time.sleep(1)
                                    done.append(i)
                                except:
                                    print ("not found")
                            jmlh = str(len(done))
                            elapsed_time = time.time() - start
                            time.sleep(2)
                            FGM.sendMessage(to, "Berhasil Broadcast teks ke "+ jmlh +" Grup\nWaktu mengirim: %s detik" % (elapsed_time))
                            #restartBot()

                if msg.contentType == 13:
                    mid = msg.contentMetadata["mid"]
                    if sender in contact_act:
                        konten = contact_act[sender]
                        posisinya = konten["posiiton"]
                        if konten["act"] == "add":
                          if mid not in manage["posisinya"]:
                            manage[posisinya].append(mid)
                            FGM.sendMessage(to,"Sukses add "+posisinya)
                          else:
                            FGM.sendMessage(to, "Udah keadd")

                        del contact_act[sender]

                    if sender in [delcoowner]:
                        mid = msg.contentMetadata["mid"]
                        if mid in manage["co_own"]:
                            manage["co_own"].remove(mid)
                        FGM.sendMessage(to, "DONE")
                        delcoowner = False

                    if sender in [deladmin]:
                        mid = msg.contentMetadata["mid"]
                        if mid in manage["admin"]:
                            manage["admin"].remove(mid)
                        FGM.sendMessage(to, "DONE")
                        deladmin = False

        udins = True
        if op.type == 26 and udins == True:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = text.lower()
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != FGM.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                #==================
                # CHECK MENTION AREA
                #==================
                if 1==1:
                #if to not in responlimit2:
                #    responlimit2[to] = time.time()
                #if time.time() > responlimit2[to]:
                        #==================
                        # RESEND / UNSEND DATABASE AREA
                        #==================
                        if to in status_unsend:
                            if msg.contentType == 0:
                                try:
                                    unsendTime = time.time()
                                    unsend[msg_id] = {"text": text, "from": sender, "time": unsendTime}
                                    print("DONE SAVE")
                                except Exception as error:
                                    logError(error)

                            if msg.contentType == 1:
                                try:
                                    unsendTime = time.time()
                                    image = FGM.downloadObjectMsg(msg_id)
                                    unsend[msg_id] = {"from": sender, "image": image, "time": unsendTime}
                                except Exception as error:
                                    logError(error)

                            if msg.contentType == 7:
                                try:
                                    unsendmsg7 = time.time()
                                    sticker = msg.contentMetadata["STKID"]
                                    link = "https://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                                    unsend[msg_id] = {"from":sender,"sticker":link,"time":unsendmsg7}
                                except Exception as e:
                                    print(e)

                            if msg.contentType == 13:
                                try:
                                    unsendmsg13 = time.time()
                                    mid = msg.contentMetadata["mid"]
                                    unsend[msg_id] = {"from":sender,"mid":mid,"time":unsendmsg13}
                                except Exception as e:
                                    print(e)
                        #=========================
                        responlimit2[to] = time.time() + 0.2
                        #=========================

#======================
# RESEND AREA
#======================
        if op.type == 65:
            print("ANSEND")
            try:
                    to = op.param1
                    sender = op.param2
                    if to not in responlimit3:
                        responlimit3[to] = time.time()
                    if time.time() > responlimit3[to]:
                            unsendTime = time.time()
                            contact = FGM.getContact(unsend[sender]["from"])
                            if "text" in unsend[sender]:
                                print("IN")
                                try:
                                    sendTime = unsendTime - unsend[sender]["time"]
                                    sendTime = format_timespan(sendTime)
                                    ret_ = "「 Resend Message 」"
                                    ret_ += "\n• Sender: @!"
                                    ret_ += "\n• Send At: {} ago".format(sendTime)
                                    ret_ += "\n• Type : Text"
                                    ret_ += "\n\n「 Text 」\n{}".format(unsend[sender]["text"])
                                    FGM.sendMentionV2(to, ret_, [contact.mid])
                                    del unsend[sender]
                                except:
                                    del unsend[sender]

                            elif "image" in unsend[sender]:
                                try:
                                    sendTime = unsendTime - unsend[sender]["time"]
                                    sendTime = format_timespan(sendTime)
                                    ret_ = "「 Resend Message 」"
                                    ret_ += "\n• Sender: @!"
                                    ret_ += "\n• Send At: {} ago".format(sendTime)
                                    ret_ += "\n• Type : Image"
                                    FGM.sendMentionV2(to, ret_, [contact.mid])
                                    FGM.sendImage(to, unsend[sender]["image"])
                                    FGM.deleteFile(unsend[sender]["image"])
                                    del unsend[sender]
                                except:
                                    FGM.deleteFile(unsend[sender]["image"])
                                    del unsend[sender]

                            elif "sticker" in unsend[sender]:
                                try:
                                    sendTime = unsendTime - unsend[sender]["time"]
                                    sendTime = format_timespan(sendTime)
                                    ret_ = "「 Resend Message 」"
                                    ret_ += "\n• Sender: @!"
                                    ret_ += "\n• Send At: {} ago".format(sendTime)
                                    ret_ += "\n• Type : Sticker"
                                    FGM.sendMentionV2(to, ret_, [contact.mid])
                                    FGM.sendImageWithURL(to, unsend[sender]["sticker"])
                                except:
                                    pass

                            elif "mid" in unsend[sender]:
                                try:
                                    sendTime = unsendTime - unsend[sender]["time"]
                                    sendTime = format_timespan(sendTime)
                                    ret_ = "「 Resend Message 」"
                                    ret_ += "\n• Sender: @!"
                                    ret_ += "\n• Send At: {} ago".format(sendTime)
                                    ret_ += "\n• Type : Contact"
                                    FGM.sendMentionV2(to, ret_, [contact.mid])
                                    FGM.sendContact(to, unsend[sender]["mid"])
                                except:
                                    pass
                            #=========================
                            responlimit3[to] = time.time() + 0.5
                            #=========================
            except Exception as e:
                print(e)

        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)

            if op.param1 in cctv['point2']:
                    if op.param2 in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1].append(op.param2)
                        FGM.sendMentionV2(op.param1, "@! hey jangan sider", [op.param2])

    except Exception as e:
        traceback.print_tb(e.__traceback__)
        logError(e)

clear_e2ee = False
def run():
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
            if clear_e2ee == False:
                line = FGM
                for pk in line.talk.getE2EEPublicKeys():
                    line.talk.removeE2EEPublicKey(pk)
                clear_e2ee = True

            if ops != None:
                for op in ops:
                    FGMBots(op)
                    oepoll.setRevision(op.revision)
            saveData()
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            logError(e)

if __name__ == "__main__":
    run()
