import requests
import urllib.parse

phone = "554195667304"
apikey = "2658217"

mensagem = "🤖 *BOT SHOPEE ATIVADO COM SUCESSO!* 🎉\n\nJho, seu robô está funcionando 100%! Todo dia às 8h você vai receber as melhores promoções da Shopee aqui no seu 41 99566-7304 💚"

url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={urllib.parse.quote(mensagem)}&apikey={apikey}"

r = requests.get(url)
print(r.text)
