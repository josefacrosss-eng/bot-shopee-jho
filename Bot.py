
import requests
import urllib.parse
import random
from datetime import datetime

phone = "554195667304"
apikey = "2658217"

# Lista de ofertas reais da Shopee (com link direto)
ofertas = [
    "🔥 Fone Bluetooth Original - R$19,90 👉 https://shopee.com.br/search?keyword=fone%20bluetooth",
    "💄 Kit Maquiagem 12 peças - R$29,90 👉 https://shopee.com.br/search?keyword=kit%20maquiagem",
    "👟 Tênis Feminino Promoção - R$59,90 👉 https://shopee.com.br/search?keyword=tenis%20feminino%20promocao",
    "⌚ Smartwatch X8 - R$69,90 👉 https://shopee.com.br/search?keyword=smartwatch",
    "👗 Vestido Verão - R$39,90 👉 https://shopee.com.br/search?keyword=vestido%20verao",
    "🏠 Organizador Multiuso - R$15,90 👉 https://shopee.com.br/search?keyword=organizador%20casa",
    "📱 Capinha Celular - R$9,90 👉 https://shopee.com.br/search?keyword=capinha%20celular"
]

# Pega 3 ofertas aleatórias do dia
hoje = random.sample(ofertas, 3)

data = datetime.now().strftime("%d/%m")
mensagem = f"🚨 *OFERTAS SHOPEE DO DIA {data}* 🚨\n\n"
for o in hoje:
    mensagem += f"{o}\n\n"
mensagem += "⚡ Corre que acaba rápido! Frete grátis acima de R$19!\n\n_Digite SAIR para parar_"

url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={urllib.parse.quote(mensagem)}&apikey={apikey}"
r = requests.get(url)
print(r.text)
