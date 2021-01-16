import pprint
message = ''' Yeah
São Paulo, Brasil
Aham, aham
Cosa Nostra, é
Vila Fundão, Capão
Simples assim, o povão da Sabin
Por um gosto pessoal do finado Neguin
Laranja e preto decidiu, se ser assim é assim
Honra branco marfim, vinho tinto, carmim
Quem? Quem permitiu?
Deus dirigiu esse filme
Dizem: "Crime é o Rap"
Dizem: "Rap é o crime"
Você diz, você decide
O resto só coincide
Olho por olho era lei, cegava todos sem ver
Pra ver direito, rever, viver e deixar viver
Bandeira branca sobe pra quem não sabe saber
Falsos não conseguem, quem tem juízo segue
Se você não deve, firmão, fica leve!
Seis preto na esquina, objetivo só: notas verde azul piscina
Careta é bem melhor
Vinte mil papelote, ó! A 20 cada um
Pra quatro molecote a 400 mil bruto
Eu sei como fazer um plano estratégico, sei
Traz… '''
count = {}

for caractere in message.upper():
    count.setdefault(caractere,0)
    count[caractere] = count[caractere] + 1

pprint.pprint(count)
