
import requests
import urllib.parse
import random
from datetime import datetime

phone = "554195667304"
apikey = "2658217"

# SEU LINK DE AFILIADA OFICIAL
LINK_AFILIADO = "https://s.shopee.com.br/3B7Ba9YE3D"

ofertas = [
    {"nome": "🔥 Fone Bluetooth Original", "preco": "19,90", "link": LINK_AFILIADO},
    {"nome": "💄 Kit Maquiagem 12 peças", "preco": "29,90", "link": LINK_AFILIADO},
    {"nome": "👟 Tênis Feminino Promoção", "preco": "59,90", "link": LINK_AFILIADO},
    {"nome": "⌚ Smartwatch X8 Ultra", "preco": "69,90", "link": LINK_AFILIADO},
    {"nome": "👗 Vestido Verão Tendência", "preco": "39,90", "link": LINK_AFILIADO},
]

hoje = random.sample(ofertas, 3)
data = datetime.now().strftime("%d/%m")

mensagem = f"🚨 *SUPER OFERTAS SHOPEE - {data}* 🚨\n\n"
for item in hoje:
    mensagem += f"{item['nome']}\n💰 Por apenas R$ {item['preco']}\n👉 {item['link']}\n\n"

mensagem += "⚡ *Frete GRÁTIS acima de R$19*\n⏰ Oferta por tempo limitado!\n\n_Comissão: Jho Luzz_"

url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={urllib.parse.quote(mensagem)}&apikey={apikey}"
r = requests.get(url)
print(r.text)
