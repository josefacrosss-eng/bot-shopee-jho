import requests
import urllib.parse
import random
from datetime import datetime

phone = "554195667304"
apikey = "2658217"

# 👇 DEPOIS COLA SEU LINK DE AFILIADA AQUI
# Exemplo: LINK_BASE = "https://s.shopee.com.br/SEU_CODIGO"
LINK_AFILIADO = ""  # Deixa vazio por enquanto

ofertas = [
    {"nome": "Fone Bluetooth Original", "preco": "19,90", "busca": "fone bluetooth"},
    {"nome": "Kit Maquiagem 12 peças", "preco": "29,90", "busca": "kit maquiagem"},
    {"nome": "Tênis Feminino Promoção", "preco": "59,90", "busca": "tenis feminino promocao"},
    {"nome": "Smartwatch X8", "preco": "69,90", "busca": "smartwatch"},
    {"nome": "Vestido Verão", "preco": "39,90", "busca": "vestido verao"},
]

hoje = random.sample(ofertas, 3)
data = datetime.now().strftime("%d/%m")

mensagem = f"🚨 *OFERTAS SHOPEE DO DIA {data}* 🚨\n\n"
for item in hoje:
    busca = urllib.parse.quote(item['busca'])
    # Se tiver link afiliado, usa ele. Se não, usa busca normal
    link = f"https://shopee.com.br/search?keyword={busca}"
    if LINK_AFILIADO:
        link = LINK_AFILIADO
    
    mensagem += f"👉 {item['nome']} - R$ {item['preco']}\n{link}\n\n"

mensagem += "⚡ Corre que acaba rápido! Frete GRÁTIS acima de R$19!\n\n_Digite SAIR para parar_"

url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={urllib.parse.quote(mensagem)}&apikey={apikey}"
r = requests.get(url)
print(r.text)
