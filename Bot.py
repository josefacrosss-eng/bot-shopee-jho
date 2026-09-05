import requests, urllib.parse
PHONE = "5541995667304"
APIKEY = "2658217"
AF_ID = "18304170585"
msg = "Bom dia Jho! TOP 3 hoje: 1) Calcinha R$17,98 https://shopee.com.br/search?keyword=calcinha&af_id=18304170585 2) Sutia https://shopee.com.br/search?keyword=sutia&af_id=18304170585 3) VS https://shopee.com.br/search?keyword=victoria&af_id=18304170585"
url = f"https://api.callmebot.com/whatsapp.php?phone={PHONE}&text={urllib.parse.quote(msg)}&apikey={APIKEY}"
requests.get(url)
