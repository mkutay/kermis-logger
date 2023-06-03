items = [["Kitap Ayraci", "kitap ayraci"], ["Kek", "kek"], ["Kurabiye", "kurabiye"]]

# <div>
#   <input type=button class="item-button" value="-" name="sold-item" id="kek" onclick="buttonDec('kek')"/>
#   <input type=button class="item-button" value="+" name="sold-item" id="kek" onclick="buttonInc('kek')"/>
#   <span id="kek num"></span>
#   <span>x Kek</span>
# </div>
html = ""
for item in items:
  html += "<div>\n"
  html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="buttonDec('{}')"/>\n""".format(item[1], item[1])
  html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="buttonInc('{}')"/>\n""".format(item[1], item[1])
  html += """  <span id="{} num"></span>\n""".format(item[1])
  html += """  <span>x {}</span>\n""".format(item[0])
  html += "</div>\n"

with open('output.html', 'w') as f:
  f.write(html)