from requests.models import Response
from requests.sessions import codes, default_headers
import telebot, requests, re, json

from telebot.apihelper import delete_sticker_from_set

PRIVADO = [1710574146]
#
#
GRUPO = []
#
#
EXCEPT = []
#
#
ANONY = [] # OFF
bot = telebot.TeleBot("5292132986:AAF-fjMe-2gxfNLoqA48Txl93L2juwLsA4Q")

description = "\n@sturdofc"



#########################CNPJ###########################


@bot.message_handler(commands=['cnpj','CNPJ'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    
                    bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>Informações By</b>: @GreenBuscas_Bot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝙑𝙊𝘾𝙀 𝙉𝘼𝙊 𝙏𝙀𝙈 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝘽𝙊𝙏, 𝙋𝘼𝙍𝘼 𝙐𝙏𝙄𝙇𝙄𝙕𝘼𝙍 𝘾𝙊𝙈𝙋𝙍𝙀 𝘼𝘾𝙀𝙎𝙎𝙊



𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼𝙎 𝘿𝙀:

 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼


💲𝙑𝘼𝙇𝙊𝙍𝙀𝙎💲

𝙋𝙍𝙄𝙑𝘼𝘿𝙊
  𝟭 𝘿𝙄𝘼 = 𝙂𝙍𝘼́𝙏𝙄𝙎
  𝟳 𝘿𝙄𝘼𝙎 = 𝟱
  𝟭𝟱 𝘿𝙄𝘼𝙎 = 𝟭𝟮
  𝟭 𝙈𝙀𝙎 = 𝟭𝟱


𝙂𝙍𝙐𝙋𝙊
 𝟭 𝘿𝙄𝘼 = 𝙂𝙍𝘼́𝙏𝙄𝙎
 𝟭𝟱 𝘿𝙄𝘼𝙎 = 𝟭𝟬
  𝟭 𝙈𝙀𝙎 = 𝟮𝟬

      ❕ 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 ❕
❕𝘼𝘾𝙀𝙄𝙏𝘼𝙈𝙊𝙎 𝘼𝙋𝙀𝙉𝘼𝙎 𝙋𝙄𝙓 ❕

<a href='http://t.me/SturdOfc'>COMPRE ACESSO AQUI</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')




#########################CPF###########################



@bot.message_handler(commands=['cpf','CPF','CEPEFE'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cpf')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://server2.trackear.com.br/juvi/cpf/' + ip)
                    req = url.json()
                    response = f'✔ <b>CPF LOCALIZADO</b> ✔\n\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>INFORMAÇÕES:</b>\n\n<b>• CPF</b>: <code>{req["cpf"]}</code>\n<b>• NOME</b>: <code>{req["nome"]}</code>\n<b>• DATA DE NASCIMENTO</b>: <code>{req["dtNascimento"]}</code>\n<b>• SEXO</b>: <code>{req["sexo"]}</code>\n<b>• SITUAÇÃO RECEITA FEDERAL</b>: <code>{req["situacao"]}</code>\n\n\n<b>• FAMILIARES</b>\n\n<b>• NOME DA MÃE</b>: <code>{req["mae"]}</code>\n\n\n<b>• ENDEREÇOS</b>\n\n<b>• RUA</b>: <code>{req["endereco"]}</code>\n<b>• NUMERO DA CASA</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• CIDADE</b>: <code>{req["cidade"]}</code>\n<b>• ESTADO</b>: <code>{req["estado"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n\n<b>━━━━━━━━━━━━━━━</b>\n\n<b>INFORMAÇÕES BY</b>: @GreenBuscas_Bot\n\n<b>Entre no meu grupo</b>: https://t.me/greenbusca'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝙑𝙊𝘾𝙀 𝙉𝘼𝙊 𝙏𝙀𝙈 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝘽𝙊𝙏, 𝙋𝘼𝙍𝘼 𝙐𝙏𝙄𝙇𝙄𝙕𝘼𝙍 𝘾𝙊𝙈𝙋𝙍𝙀 𝘼𝘾𝙀𝙎𝙎𝙊



𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼𝙎 𝘿𝙀:

 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼


💲𝙑𝘼𝙇𝙊𝙍𝙀𝙎💲

𝙋𝙍𝙄𝙑𝘼𝘿𝙊
  𝟭 𝘿𝙄𝘼 = 𝙂𝙍𝘼́𝙏𝙄𝙎
  𝟳 𝘿𝙄𝘼𝙎 = 𝟱
  𝟭𝟱 𝘿𝙄𝘼𝙎 = 𝟭𝟮
  𝟭 𝙈𝙀𝙎 = 𝟭𝟱


𝙂𝙍𝙐𝙋𝙊
 𝟭 𝘿𝙄𝘼 = 𝙂𝙍𝘼́𝙏𝙄𝙎
 𝟭𝟱 𝘿𝙄𝘼𝙎 = 𝟭𝟬
  𝟭 𝙈𝙀𝙎 = 𝟮𝟬

      ❕ 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 ❕
❕𝘼𝘾𝙀𝙄𝙏𝘼𝙈𝙊𝙎 𝘼𝙋𝙀𝙉𝘼𝙎 𝙋𝙄𝙓 ❕

<a href='http://t.me/SturdOfc'>COMPRE ACESSO AQUI</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')





#########################MENU###########################  

@bot.message_handler(commands=['menu', 'help', 'start'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠ VOCÊ ESTÁ DIGITANDO ERRADO⚠' + '</b>')
    else:
        try:
        	menu = f'<b>𝙈𝙚𝙣𝙪</b>\n<b>━━━━━━━━━━━━━━━</b>\n<b>Para consultar cnpj você precisa digitar o comando e em seguida, digitar o cnpj da empresa.\nExemplo</b>: <code>/cnpj 27865757000102</code>\n\n'

        	bot.reply_to(men, menu, parse_mode='HTML')
        except:
                    bot.reply_to(men, 'VOCÊ ESTÁ DIGITANDO ERRADO',)



bot.polling()