# ficha version: 1.0.0
# o programa recebera e enviara via email dados de clientes que desejam usar sua moto usada como parte do pagamento na compra de uma moto zero km

# importaçoes de biblioteca para envio de email automatico
import smtplib
import email.message
import sys
import os

# apresentaçao da janela para usuario
print('               ***** FICHA DE AVALIAÇAO *****\n')
print('. Atençao! Preencha todos campos obrigatorios com seus devidos valores e pressione a tecla "ENTER"\n')

# armazenamento usando estrutura de dicionario
cliente = {'NOME_VENDEDOR': {},
           'NOME': {},
           'CONTATO': {},
           'MOTO': {},
           'ANO': {},
           'KM': {},
           'VALOR': {},
           'CONSERTO': {},
           'APARENCIA': {},
           'CUSTO_APARENCA': {},
           'MOTO_INTRESSE_CLIENTE': {},
           'VALOR_ENTRADA_CONCESSIONARIA': {},
           }

# funçao para reiniciar o programa


def reiniciar():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# captura de dados do usuario
try:
    cliente['NOME_VENDEDOR'] = str(input('Informe nome do VENDEDOR(a): '))
    cliente['NOME'] = input('Digite nome do cliente: ')
    while len(cliente['CONTATO']) != 9:
        cliente['CONTATO'] = list(input('Telefone pra contato: (38) '))
    cliente['MOTO'] = input('Moto do cliente: ')
    cliente['ANO'] = int(input('Ano de fabricaçao: '))
    cliente['KM'] = int(input('Qual KM da motocicleta: '))
    cliente['VALOR'] = float(input('Informe o valor da tabela fipe: R$ '))
    cliente['CONSERTO'] = input(
        'Informe os possiveis reparos a serem realizados na motocicleta: ')
    cliente['APARENCIA'] = input(
        '''Descreva em poucas palavras o estado de conservaçao da motocicleta: ''')
    cliente['CUSTO_APARENCA'] = float(
        input('Custo para reparos na motocicleta: R$ '))
    cliente['MOTO_INTRESSE_CLIENTE'] = input(
        'Qual motocicleta de interesse do cliente: ')
    cliente['VALOR_ENTRADA_CONCESSIONARIA'] = cliente['VALOR'] - (15 * 100)

except (ValueError):
    print('---> Ooops! DADOS INFORMADOS ESTAM INCORRETOS, verifique se houve erro de digitaçao <---')

# destinatario via email
enviar_proposta = input('Enviar para:\n1= Gerencia\n2= Administrativo\n3= Gestao\n---> Escolha o numero e prescione tecla "ENTER\n')
destinario = ''
if enviar_proposta == '1':
    destinario = 'gerencicarmomotos@gmai.com'
elif enviar_proposta == '2':
    destinario = 'administrativo@gmail.com'
elif enviar_proposta == '3':
    destinario = 'gestao@gmail.com'

# formataçao dos dados para o html
proposta = (f'''
           <h2>\n
           <p>. VENDEDOR(a): {cliente["NOME_VENDEDOR"]} 
           <p>> DADOS DO CLIENTE <\n
           <p>. NOME:  {cliente["NOME"]}
           <p>. CONTATO:  (38) 9{cliente["CONTATO"]}
           <p>. MOTO:  {cliente["MOTO"]}
           <p>. ANO:  {cliente["ANO"]}
           <p>. KM:  {cliente["KM"]}
           <p>. FIPE: R$  {cliente["VALOR"]}
           <p>. REPAROS:  {cliente["CONSERTO"]}
           <p>. ESTADO DA MOTOCICLETA:  {cliente["APARENCIA"]}
           <p>. VALOR DO REPARO\MANUTENÇAO:  R${cliente["CUSTO_APARENCA"]}
           <p>. VALOR PROPOSTA:  R$ {cliente["VALOR_ENTRADA_CONCESSIONARIA"]}\n
           <p>. CLIENTE INTERESSADO EM:  {cliente["MOTO_INTRESSE_CLIENTE"]}''')

# funçao para envio de email


def enviar_email():
    conteudo_email = proposta

    msg = email.message.Message()
    msg['Subject'] = "FICHA DE AVALIAÇAO"
    msg['From'] = '' # email do remetente
    msg['To'] = destinario
    password = '' # inserir senha gerada pelo gmail
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(conteudo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587') # porta utilizada para envio
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso')


enviar_email()

reiniciar()
