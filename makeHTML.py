items = [["Kitap Ayracı", "kitap ayraci"], ["İp Bileklik", "ip bileklik"], ["Boncuk Bileklik", "boncuk bileklik"], ["Küpe", "kupe"], ["Kolye", "kolye"]]
foods = [["Mavi Meth", "mavi meth"], ["Zencefilli ve Tarçınlı Kurabiye", "zencefil kurabiye"], ["Makarna Salatası", "marakna salatasi"], ["Alman Salatası", "alman salatasi"], ["Waffle", "waffle"], ["Browni", "browni"], ["Kek", "kek"], ["Normal Kurabiye", "normal kurabiye"], ["Ispanakalı Börek", "ispanakli borek"]]
games = [["Üçlü Kuponn", "uclu"], ["Beşli Kupon", "besli"], ["Yedili Kupon", "yedili"]]

# Mini golf
# Mini basketbol
# Rampalı oyun 
# Ağaca hulahoop bağlama
# Eşek kuyruğu
# Memory games
# White board oyunu
# Salınım (labutlar)
# Halka geçirmece
# Yokuş oyunu (yeni)

# <div>
#   <input type=button class="item-button" value="-" name="sold-item" id="kek" onclick="buttonDec('kek')"/>
#   <input type=button class="item-button" value="+" name="sold-item" id="kek" onclick="buttonInc('kek')"/>
#   <span id="kek num"></span>
#   <span>x Kek</span>
# </div>
html = ""
html += """<p>Items</p>\n"""
for item in items:
  html += "<div>\n"
  html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="buttonDec('{}')"/>\n""".format(item[1], item[1])
  html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="buttonInc('{}')"/>\n""".format(item[1], item[1])
  html += """  <span id="{} num"></span>\n""".format(item[1])
  html += """  <span>x {}</span>\n""".format(item[0])
  html += "</div>\n"

html += """<p>Foods</p>\n"""
for item in foods:
  html += "<div>\n"
  html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="buttonDec('{}')"/>\n""".format(item[1], item[1])
  html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="buttonInc('{}')"/>\n""".format(item[1], item[1])
  html += """  <span id="{} num"></span>\n""".format(item[1])
  html += """  <span>x {}</span>\n""".format(item[0])
  html += "</div>\n"

html += """<p>Games</p>\n"""
for item in games:
  html += "<div>\n"
  html += """  <input type=button class="item-button" value="-" name="sold-item" id="{}" onclick="buttonDec('{}')"/>\n""".format(item[1], item[1])
  html += """  <input type=button class="item-button" value="+" name="sold-item" id="{}" onclick="buttonInc('{}')"/>\n""".format(item[1], item[1])
  html += """  <span id="{} num"></span>\n""".format(item[1])
  html += """  <span>x {}</span>\n""".format(item[0])
  html += "</div>\n"

with open('output.html', 'w') as f:
  f.write(html)