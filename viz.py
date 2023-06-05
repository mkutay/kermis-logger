import json
import os.path
import sys

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import strftime, localtime

data = []

with open('./data.json', 'r') as f:
  data = json.load(f)["data"]

boughtItems = {}
boughtItemNames = []
boughtItemCnt = []
totalCost = 0

times = []
timeItems = []
amogus = []
mxLength = 0

for item in data:
  times.append([strftime('%Y-%m-%d %H:%M:%S', localtime(item["timeStamp"] / 1000 + 10800))])
  totalCost += int(item["cost"])
  timeItem = []
  for key, value in item["bought"].items():
    timeItem.append(str(value) + " " + key)
    if boughtItems.get(key) != None:
      boughtItems[key] += value
    else:
      boughtItems[key] = value
  mxLength = max(mxLength, len(timeItem))
  timeItems.append(timeItem)

for i in range(len(timeItems)):
  while len(timeItems[i]) < mxLength:
    timeItems[i].append("")

print(timeItems)

for key, value in boughtItems.items():
  boughtItemNames.append([key])
  boughtItemCnt.append([value])

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("tokenn.json", scopes)
file = gspread.authorize(credentials)
sheet = file.open("kermes-mkutay-dev")
sheet = sheet.sheet1

sheet.update_acell("B1", totalCost)
sheet.update("A3:A" + str(2 + len(boughtItemNames)), boughtItemNames)
sheet.update("B3:B" + str(2 + len(boughtItemCnt)), boughtItemCnt)

sheet.update("D3:D" + str(2 + len(times)), times)
sheet.update("E3:" + chr(ord("@") + 4 + mxLength) + str(2 + len(timeItems)), timeItems)

sys.stdout.flush()
