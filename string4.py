text = """Tipos de registro de DNS com suporte
PDF
RSS
Amazon Route 53O oferece suporte aos tipos de registros de DNS listados nesta seção. Cada tipo de registro também inclui um exemplo de como formatar o elemento Value ao acessar o Route 53 usando a API.

nota
Para os tipos de registros que incluem um nome de domínio, digite um nome de domínio totalmente qualificado, como www.exemplo.com. Incluir o ponto final é opcional; o Route 53 pressupõe que o nome de domínio seja totalmente qualificado. Isso significa que Route 53 trata www.example.com (sem um ponto final) e www.example.com. (com um ponto final) como valores idênticos.

Route 53O fornece uma extensão para a funcionalidade DNS conhecida como registros de alias. Semelhantes aos registros CNAME, os registros de alias permitem que você roteie o tráfego para recursos da AWS selecionados, como as distribuições do CloudFront e os buckets do Amazon S3 Para obter mais informações, incluindo uma comparação entre registros de alias e CNAME, consulte Escolher entre registros de alias e não alias.

Tópicos

Tipo de registro A
Tipo de registro AAAA
Tipo de registro CAA
Tipo de registro CNAME
Tipo de registro DS
Tipo de registro MX
Tipo de registro NAPTR
Tipo de registro NS
Tipo de registro PTR
Tipo de registro SOA
Tipo de registro SPF
Tipo de registro SRV
Tipo de registro TXT
Tipo de registro A
Use um registro A para rotear o tráfego para um recurso, como um servidor web, usando um endereço IPv4 em notação decimal com ponto.

Exemplo para o console doAmazon Route 53

192.0.2.1
Exemplo para a API doRoute 53

<Value>192.0.2.1</Value>
Tipo de registro AAAA
Use um registro AAAA para rotear o tráfego para um recurso, como um servidor web, usando um endereço do IPv6 em formato hexadecimal separado por dois pontos.

Exemplo para o console doAmazon Route 53

2001:0db8:85a3:0:0:8a2e:0370:7334
Exemplo para a API doRoute 53

<Value>2001:0db8:85a3:0:0:8a2e:0370:7334</Value>
Tipo de registro CAA
Um registro CAA especifica quais autoridades de certificação (CAs) têm permissão para emitir certificados para um domínio ou subdomínio. A criação de um registro CAA ajuda a evitar que o CAs errado emita certificados para seus domínios. Um registro CAA não é um substituto para os requisitos de segurança que são especificados por sua autoridade de certificação, como o requisito para validar que você é o proprietário de um domínio.

Você pode usar registros CAA para especificar:

Quais autoridades de certificação (CAs) podem emitir certificados SSL/TLS, se houver

O endereço de e-mail ou o URL a ser contatado quando a CA emitir um certificado para o domínio ou o subdomínio

Quando você adiciona um registro CAA a sua zona hospedada, você especifica três configurações separadas por espaços:

flags tag "value"

Observe o seguinte sobre o formato dos registros CAA:

O valor de tag pode conter somente os caracteres A-Z, a-z e 0-9.

Sempre coloque o value entre aspas ("").

Alguns CAs permitem ou exigem valores adicionais para value. Especifique valores adicionais como pares de nome-valor e separe-os com ponto-e-vírgula (;), por exemplo:

0 issue "ca.example.net; account=123456"

Se um CA recebe uma solicitação de certificado para um subdomínio (como www.example.com) e se não existe nenhum registro CAA no subdomínio, o CA envia uma consulta de DNS para um registro CAA para o domínio pai (como example.com). Se existir um registro para o domínio pai e se a solicitação de certificado for válida, o CA emitirá o certificado para o subdomínio.

Recomendamos que você consulte sua CA para determinar quais valores especificar para um registro da CAA.

Não é possível criar um registro de CAA e um registro do CNAME com o mesmo nome, pois o DNS não permite usar o mesmo nome para um registro do CNAME e para qualquer outro tipo de registro ao mesmo tempo.

Tópicos

Autorizar um CA a emitir um certificado para um domínio ou subdomínio
Autorizar um CA a emitir um certificado curinga para um domínio ou subdomínio
Impedir qualquer CA de emitir um certificado para um domínio ou subdomínio
Solicitar que um CA entre em contato com você caso receba uma solicitação de certificado inválida
Usar outra configuração que é compatível com o CA
Examples
Autorizar um CA a emitir um certificado para um domínio ou subdomínio
Para autorizar um CA a emitir um certificado para um domínio ou subdomínio, crie um registro com o mesmo nome do domínio ou do subdomínio, e especifique as seguintes configurações:

flags – 0

tag – issue

value – o código da CA que você autoriza para emitir um certificado para o domínio ou subdomínio

Por exemplo, suponha que você deseja autorizar ca.example.net a emitir um certificado para example.com. Você cria um registro CAA para example.com com as seguintes configurações:

0 issue "ca.example.net"
Para obter informações sobre como autorizar o AWS Certificate Manager a emitir um certificado, consulte Configurar um registro CAA no Guia do usuário do AWS Certificate Manager.

Autorizar um CA a emitir um certificado curinga para um domínio ou subdomínio
Para autorizar um CA a emitir um certificado curinga para um domínio ou subdomínio, crie um registro com o mesmo nome de domínio ou subdomínio, e especifique as seguintes configurações. Um certificado curinga se aplica ao domínio ou subdomínio e a todos os seus subdomínios.

flags – 0

tag – issuewild

value – o código da CA que você autoriza para emitir um certificado para um domínio ou subdomínio e seus subdomínios

Por exemplo, suponha que você deseja autorizar ca.example.net a emitir um certificado curinga para example.com, aplicável a example.com e a todos os seus subdomínios. Você cria um registro CAA para example.com com as seguintes configurações:

0 issuewild "ca.example.net"
Quando você quiser autorizar um CA a emitir um certificado curinga para um domínio ou subdomínio, crie um registro com o mesmo nome do domínio ou subdomínio, e especifique as seguintes configurações. Um certificado curinga se aplica ao domínio ou subdomínio e a todos os seus subdomínios.

Impedir qualquer CA de emitir um certificado para um domínio ou subdomínio
Para impedir qualquer CA de emitir um certificado para um domínio ou subdomínio, crie um registro com o mesmo nome do domínio ou subdomínio, e especifique as seguintes configurações:

flags – 0

tag – issue

valor – ";"

Por exemplo, suponha que você deseja impedir que qualquer CA emita um certificado para example.com. Você cria um registro CAA para example.com com as seguintes configurações:

0 issue ";"

Se você deseja impedir que qualquer CA emita um certificado para example.com ou seus subdomínios, crie um registro CAA para example.com com as seguintes configurações:

0 issuewild ";"

nota
Se você criar um registro CAA para example.com e especificar os valores a seguir, um CA que esteja usando o valor ca.example.net poderá emitir o certificado para example.com:

0 issue ";"
0 issue "ca.example.net"
Solicitar que um CA entre em contato com você caso receba uma solicitação de certificado inválida
Se você deseja que qualquer CA que receba uma solicitação inválida para um certificado entre em contato com você, especifique as seguintes configurações:

flags – 0

tag – iodef

value – a URL ou o endereço de e-mail que você deseja que a CA notifique quando receber uma solicitação inválida de um certificado. Use o formato aplicável:

"mailto:email-address"

"http://URL"

"https://URL"

Por exemplo, se você deseja que qualquer CA que receba uma solicitação inválida para um certificado envie um e-mail para admin@example.com, crie um registro de CAA com as seguintes configurações:

0 iodef "mailto:admin@example.com"
Usar outra configuração que é compatível com o CA
Se o seu CA oferece suporte a um recurso que não está definido na RFC para registros de CAA, especifique as seguintes configurações:

flags – 128 (esse valor impede que a CA emita um certificado se ela não ela no oferecer suporte ao recurso especificado.)

tag – a tag que você autoriza a CA a usar

value – o valor que corresponde ao valor da tag

Por exemplo, suponha que o CA oferece suporte ao envio de uma mensagem de texto caso receba uma solicitação inválida para certificado. (Não estamos ciente de nenhuma CAs que ofereça suporte a essa opção.) As configurações do registro podem ser as seguintes:

128 exampletag "15555551212"
Examples
Exemplo para o console doRoute 53

0 issue "ca.example.net"
0 iodef "mailto:admin@example.com"
Exemplo para a API doRoute 53

<ResourceRecord>
   <Value>0 issue "ca.example.net"</Value>
   <Value>0 iodef "mailto:admin@example.com"</Value>
</ResourceRecord>
Tipo de registro CNAME
Um registro CNAME mapeia consultas DNS para o nome do registro atual, como acme.example.com, para outro domínio (example.com ou example.net) ou subdomínio (acme.example.com ou zenith.example.org).

Importante
O protocolo DNS não permite que você crie um registro CNAME no nó superior de um namespace DNS, também conhecido como o apex de zona. Por exemplo, se você registrar o nome do DNS exemplo.com, o apex de zona será exemplo.com. Você não pode criar um registro CNAME para exemplo.com, mas pode criar registros CNAME para www.exemplo.com, produtonovo.exemplo.com e assim por diante.

Além disso, se você criar um registro CNAME para um subdomínio, não poderá criar outros registros para esse subdomínio. Por exemplo, se você criar um CNAME para www.example.com, não poderá criar outros registros para os quais o valor do campo Name (Nome) é www.example.com.

O Amazon Route 53 também oferece suporte para registros com alias, que permitem rotear consultas para recursos selecionados da AWS, como distribuições do CloudFront e buckets do Amazon S3 Os aliases têm algumas semelhanças com o tipo de registro CNAME. No entanto, você pode criar um alias para o apex de zona. Para obter mais informações, consulte Escolher entre registros de alias e não alias.

Exemplo para o console doRoute 53

hostname.example.com
Exemplo para a API doRoute 53

<Value>hostname.example.com</Value>
Tipo de registro DS
Um registro de assinante de delegação (DS) refere-se a uma chave de zona para uma zona de subdomínio delegada. Você pode criar um registro DS ao estabelecer uma cadeia de confiança ao configurar a assinatura DNSSEC. Para obter mais informações sobre como configurar o DNSSEC no Route 53, consulte Configurar a assinatura DNSSEC no Amazon Route 53.

Os três primeiros valores são números decimais que representam a tag da chave, o algoritmo e o tipo de resumo. O quarto valor é o resumo da chave de zona. Para obter mais informações sobre o formato de registro DS, consulte RFC 4034.

Exemplo para o console doRoute 53

123 4 5 1234567890abcdef1234567890absdef
Exemplo para a API doRoute 53

<Value>123 4 5 1234567890abcdef1234567890absdef</Value>
Tipo de registro MX
Um registro MX especifica os nomes dos servidores de e-mail e, se você tiver dois ou mais servidores de e-mail, a ordem de prioridade. Cada valor de um registro MX contém dois valores, prioridade e nome de domínio.

Priority
Um número inteiro que representa a prioridade para um servidor de e-mail. Se você especificar somente um servidor, a prioridade pode ser qualquer inteiro entre 0 e 65535. Se você especificar vários servidores, o valor especificado para a prioridade indica para qual servidor de e-mail você deseja que o e-mail seja roteado para em primeiro lugar, em segundo e assim por diante. O servidor com o menor valor para a prioridade tem precedência. Por exemplo, se você tiver dois servidores de e-mail e especificar valores de 10 e 20 para a prioridade, o e-mail sempre vai para o servidor com uma prioridade 10, a não ser que ele esteja indisponível. Se você especificar valores de 10 e 10, o e-mail será roteado para os dois servidores de forma praticamente igual.

Nome de domínio
O nome do domínio do servidor de e-mail. Especifique o nome (como email.exemplo.com) de um registro A ou AAAA. Em RFC 2181, Esclarecimentos para a especificação de DNS, a seção 10.3 proíbe especificar o nome de um registro CNAME para o valor do nome de domínio. (Quando a RFC menciona "alias", indica um registro do CNAME, não um registro de alias do Route 53

Exemplo para o console doAmazon Route 53

10 mail.example.com
Exemplo para a API doRoute 53

<Value>10 mail.example.com</Value>
Tipo de registro NAPTR
O Name Authority Pointer (NAPTR – Ponteiro de autoridade de nome) é um tipo de registro usado pelas aplicações Dynamic Delegation Discovery System (DDDS – Sistema de descoberta de delegação dinâmica) para converter um valor em outro ou substituir um valor por outro. Por exemplo, um uso comum é converter números de telefone em SIP URIs.

O elemento Value de um registro NAPTR consiste em seis valores separados por espaço:

Ordem
Quando você especifica mais de um registro, a sequência na qual deseja que a aplicação DDDS avalie os registros. Valores válidos: 0 - 65535.

Preferência
Quando você especifica dois ou mais registros que têm a mesma ordem, sua preferência para a sequência na qual esses registros são avaliados. Por exemplo, se dois registros têm uma ordem de 1, a aplicação DDDS primeiro avalia o registro que tem a menor preferência. Valores válidos: 0 - 65535.

Sinalizadores
Uma configuração específica para as aplicações DDDS. Os valores atualmente definidos na RFC 3404 são letras maiúsculas e minúsculas "A", "P", "S"e "U"e a string vazia "". Coloque sinalizadores entre aspas.

Serviço
Uma configuração específica para as aplicações DDDS. Coloque o serviço entre aspas.

Para obter mais informações, consulte o RFCs aplicável:

URI DDDS application – https://tools.ietf.org/html/rfc3404#section-4.4

S-NAPTR DDDS application – https://tools.ietf.org/html/rfc3958#section-6.5

U-NAPTR DDDS application – https://tools.ietf.org/html/rfc4848#section-4.5

Regexp
Uma expressão regular que a aplicação DDDS usa para converter um valor de entrada em um valor de saída. Por exemplo, um sistema de telefone IP pode usar uma expressão regular para converter um número de telefone inserido por um usuário em um SIP URI. Coloque Regexp entre aspas. Especifique um valor para Regexp ou um valor para Substituição, mas não ambos.

A expressão regular pode incluir qualquer um dos seguintes caracteres ASCII imprimíveis:

a-z

0-9

- (hífen)

(espaço)

! # $ % & ' ( ) * + , - / : ; < = > ? @ [ ] ^ _ ` { | } ~ .

" (aspas). Para incluir uma citação literal em uma string, preceda-a de um caractere \: \".

\ (barra invertida). Para incluir uma barra invertida em uma string, preceda-a de um caractere \: \\.

Especifique todos os outros valores, como nomes de domínio internacionalizados, no formato octal.

Para a sintaxe de Regexp, consulte RFC 3402, seção 3.2, Sintaxe de expressão de substituição

Substituição
O nome de domínio totalmente qualificado (FQDN) do próximo nome de domínio para o qual você deseja que a aplicação DDDS envie uma consulta de DNS. A aplicação DDDS substitui o valor de entrada pelo o valor que você especificar para Substituição, se houver. Especifique um valor para Regexp ou um valor para Substituição, mas não ambos. Se você especificar um valor para Regexp, especifique um ponto (.) em Replacement (Substituição).

O nome do domínio pode incluir a-z, 0-9 e – (hífen).

Para obter mais informações sobre as aplicações DDDS e os registros NAPTR, consulte o seguinte RFCs:

RFC 3401

RFC 3402

RFC 3403

RFC 3404

Exemplo para o console doAmazon Route 53

100 50 "u" "E2U+sip" "!^(\\+441632960083)$!sip:\\1@example.com!" .
100 51 "u" "E2U+h323" "!^\\+441632960083$!h323:operator@example.com!" .
100 52 "u" "E2U+email:mailto" "!^.*$!mailto:info@example.com!" .
Exemplo para a API doRoute 53

<ResourceRecord>
   <Value>100 50 "u" "E2U+sip" "!^(\\+441632960083)$!sip:\\1@example.com!" .</Value>
   <Value>100 51 "u" "E2U+h323" "!^\\+441632960083$!h323:operator@example.com!" .</Value>
   <Value>100 52 "u" "E2U+email:mailto" "!^.*$!mailto:info@example.com!" .</Value>
</ResourceRecord>
Tipo de registro NS
Um registro de NS identifica os servidores de nome da zona hospedada. Observe o seguinte:

O uso mais comum de um registro NS é controlar como o tráfego da Internet é roteado para um domínio. Para usar os registros em uma zona hospedada para rotear o tráfego para um domínio, atualize as configurações de registro de domínio para usar os quatro servidores de nomes no registro NS padrão. (Este é o registro NS que tem o mesmo nome que a zona hospedada.)

É possível criar uma zona hospedada separada para um subdomínio (acme.example.com) e usar essa zona hospedada para rotear o tráfego de Internet para o subdomínio e seus subdomínios (subdomain.acme.example.com). Defina esta configuração, conhecida como “delegar a responsabilidade por um subdomínio a uma zona hospedada” ao criar outro registro NS na zona hospedada para o domínio raiz (example.com). Para obter mais informações, consulte Rotear tráfego para subdomínios.

Os registros NS também são usados para configurar servidores de nomes de rótulo branco. Para obter mais informações, consulte Configurar servidores de nome de rótulo branco.

Para obter mais informações sobre registros de NS, consulte Registros de NS e SOA que o Amazon Route 53 cria para uma zona hospedada pública.

Exemplo para o console doAmazon Route 53

ns-1.example.com
Exemplo para a API doRoute 53

<Value>ns-1.example.com</Value>
Tipo de registro PTR
Um registro PTR mapeia um endereço IP para o nome de domínio correspondente.

Exemplo para o console doAmazon Route 53

hostname.example.com
Exemplo para a API doRoute 53

<Value>hostname.example.com</Value>
Tipo de registro SOA
Um registro de início de autoridade (SOA) fornece informações sobre um domínio e a zona hospedada correspondente do Amazon Route 53 Para obter informações sobre os campos em um registro de SOA, consulte Registros de NS e SOA que o Amazon Route 53 cria para uma zona hospedada pública.

Exemplo para o console doRoute 53

ns-2048.awsdns-64.net hostmaster.awsdns.com 1 1 1 1 60
Exemplo para a API doRoute 53

<Value>ns-2048.awsdns-64.net hostmaster.awsdns.com 1 1 1 1 60</Value>
Tipo de registro SPF
Anteriormente, os registros de SPF eram usados para verificar a identidade do remetente de mensagens de e-mail. No entanto, não recomendamos mais que você crie registros cujo tipo de registro seja SPF. A RFC 7208, Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, versão 1, foi atualizada para dizer "...[ I]ts existente e o mecanismo definido em [RFC4408] levaram a alguns problemas de interoperabilidade. Da mesma forma, seu uso não é mais apropriado para a SPF versão 1; as implementações não são para usá-la." Na RFC 7208, consulte a seção 14.1, The SPF DNS Record Type.

Em vez de um registro SPF, recomendamos que você crie um registro TXT que contém o valor aplicável. Para obter mais informações sobre os valores válidos, consulte o artigo da Wikipédia Sender Policy Framework.

Exemplo para o console doAmazon Route 53

"v=spf1 ip4:192.168.0.1/16 -all"
Exemplo para a API doRoute 53

<Value>"v=spf1 ip4:192.168.0.1/16 -all"</Value>
Tipo de registro SRV
Um elemento Value de um registro SRV consiste em quatro valores separados por espaços. Os três primeiros valores são números decimais que representam prioridade, peso e porta. O quarto valor é um nome de domínio. Para obter informações sobre o formato de registros de SRV, consulte a documentação aplicável.

Exemplo para o console doAmazon Route 53

10 5 80 hostname.example.com
Exemplo para a API doRoute 53

<Value>10 5 80 hostname.example.com</Value>
Tipo de registro TXT
Um registro TXT contém uma ou mais strings que estão entre aspas duplas ("). Quando você usar a política de roteamento simples, inclua todos os valores para um domínio (example.com) ou subdomínio (www.example.com) no mesmo registro TXT.

Tópicos

Inserir valores de registro TXT
Caracteres especiais em um valor de registro TXT
Maiúsculas e minúsculas em um valor de registro TXT
Examples
Inserir valores de registro TXT
Uma única string pode incluir até 255 caracteres, incluindo:

a-z

A-Z

0-9

Espaço

- (hífen)

! " # $ % & ' ( ) * + , - / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ .

Se for necessário inserir um valor maior que 255 caracteres, quebre o valor em strings de 255 caracteres ou menos e coloque cada string entre aspas duplas ("). No console, liste todas as strings na mesma linha:

"String 1" "String 2" "String 3"
Para a API, inclua todas as strings no mesmo elemento Value

<Value>"String 1" "String 2" "String 3"</Value>
O tamanho máximo de um valor em um registro TXT é de 4.000 caracteres.

Caracteres especiais em um valor de registro TXT
Se o seu registro TXT contiver qualquer um dos caracteres a seguir, você deverá especificar os caracteres usando códigos de escape no formato \.three-digit octal code:

Os caracteres 000 a 040 octal (0 a 32 decimal, 0x00 a 0x20 hexadecimal)

Os caracteres 177 a 377 octal (127 a 255 decimal, 0x7F a 0xFF hexadecimal)

Por exemplo, se o valor do seu registro TXT é "exämple.com", você especifica "ex\344mple.com".

Para um mapeamento entre caracteres ASCII e códigos octais, faça uma pesquisa na Internet com "ascii octal codes." Uma referência útil é Código ASCII – A tabela ASCII estendida.

Para incluir as aspas (") em uma string, coloque um caractere de barra invertida (\) antes das aspas: \".

Maiúsculas e minúsculas em um valor de registro TXT
O uso de maiúsculas e minúsculas é preservado, portanto, "Ab" e "aB" são valores diferentes.

Examples
Exemplo para o console doAmazon Route 53

Coloque cada valor em uma linha separada:

"This string includes \"quotation marks\"."
"The last character in this string is an accented e specified in octal format: \351"
"v=spf1 ip4:192.168.0.1/16 -all"
Exemplo para a API doRoute 53

Coloque cada valor em um elemento de Value separado:

<Value>"This string includes \"quotation marks\"."</Value>
<Value>"The last character in this string is an accented e specified in octal format: \351"</Value>
<Value>"v=spf1 ip4:192.168.0.1/16 -all"</Value>
"""

print (text)