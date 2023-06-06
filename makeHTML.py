import json
selling = {}
with open("selling.json", "r") as f:
  selling = json.load(f)

# <div>
#   <input type=button class="item-button" value="-" name="sold-item" id="kek" onclick="buttonDec('kek')"/>
#   <input type=button class="item-button" value="+" name="sold-item" id="kek" onclick="buttonInc('kek')"/>
#   <span id="kek num"></span>
#   <span>x Kek</span>
# </div>
html = ""
html += """<p>Items</p>\n"""
for item in selling["items"]:
  for i in range(len(item["cost"])):
    id = item["name"] + str(item["cost"][i])
    html += "<div>\n"
    html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="buttonDec('{}')"/>\n""".format(id, id)
    html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="buttonInc('{}')"/>\n""".format(id, id)
    html += """  <span id="{} num" name="{}"></span>\n""".format(id, item["cost"][i])
    html += """  <span>x {} ({} TL)</span>\n""".format(item["name"], item["cost"][i])
    html += "</div>\n"

html += """<p>Foods</p>\n"""
for item in selling["foods"]:
  for i in range(len(item["cost"])):
    id = item["name"] + str(item["cost"][i])
    html += "<div>\n"
    html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="buttonDec('{}')"/>\n""".format(id, id)
    html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="buttonInc('{}')"/>\n""".format(id, id)
    html += """  <span id="{} num" name="{}"></span>\n""".format(id, item["cost"][i])
    html += """  <span>x {} ({} TL)</span>\n""".format(item["name"], item["cost"][i])
    html += "</div>\n"

html += """<p>Games</p>\n"""
for item in selling["games"]:
  for i in range(len(item["cost"])):
    id = item["name"] + str(item["cost"][i])
    html += "<div>\n"
    html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="buttonDec('{}')"/>\n""".format(id, id)
    html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="buttonInc('{}')"/>\n""".format(id, id)
    html += """  <span id="{} num" name="{}"></span>\n""".format(id, item["cost"][i])
    html += """  <span>x {} ({} TL)</span>\n""".format(item["name"], item["cost"][i])
    html += "</div>\n"

html += """<p>Discounts</p>\n"""
for item in selling["discounts"]:
  id = item["name"] + str(item["discount"])
  html += "<div>\n"
  html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="discountDec('{}')"/>\n""".format(id, id)
  html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="discountInc('{}')"/>\n""".format(id, id)
  html += """  <span id="{} num" name="{}"></span>\n""".format(id, item["discount"])
  html += """  <span>x {}</span>\n""".format(item["name"])
  html += "</div>\n"

with open('output.html', 'w') as f:
  f.write(html)