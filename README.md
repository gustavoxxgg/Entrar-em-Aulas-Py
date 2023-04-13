
# Script para abrir página no navegador
Este é um script em Python que permite você ~~entrar nas aulas enquanto você dorme~~ abrir uma página no navegador em um horário e dia específicos, de acordo com as informações fornecidas pelo usuário.

## Como utilizar
Para utilizar este script, siga as instruções abaixo:

Certifique-se de ter o Python instalado em sua máquina.

Faça o download do código-fonte deste repositório para sua máquina.

Abra um terminal e navegue até a pasta em que o código-fonte foi baixado.

Execute o comando 

> python abrir_pagina.py.

O script irá solicitar as informações necessárias para abrir a página no navegador:
Digite o link da página.

Digite o dia da semana em que a página deve ser aberta (ex: segunda, terca, quarta, quinta, sexta, sabado, domingo).

Digite o horário no formato HH:MM (ex: 10:30).

O script irá calcular a data e hora agendadas para abrir a página, aguardar o tempo restante até o agendamento e, por fim, abrir a página no navegador.

### Exemplo

Vamos dizer que você queira entrar em um link de uma aula online do zoom (Apenas um exemplo)

você copia o link da aula e cola no prompt 
> Digite o link da página.
> > https://zoom.us/j/00000000000?pwd=00000000000000000000000000000000#success

~~Por experiência própria~~ Remova o "#success#" se não o nosso "Exemplo" não vai funcionar

Após isso você digita no prompt o dia da semana que você quer que ele entre
> Digite o dia da semana em que a página deve ser aberta (ex: segunda, terca, quarta, quinta, sexta, sabado, domingo).
>> quarta

Agora é só digitar a hora no prompt
>Digite o horário no formato HH:MM (ex: 10:30).
>>07:10

agora vem a parte mais importante do nosso exemplo e você só precisa fazer uma vez entre no link da aula e permita que o seu navegador abra o zoom de maneira automática como na imagem :

![Exemplo](https://storage.googleapis.com/support-forums-api/attachment/thread-18281110-7834331976130183402.jpg) 
## Requisitos
- Python 3.x
 - Bibliotecas:
- webbrowser
- datetime
- time

## Contribuição
Este script é um exemplo simples e pode ser melhorado de diversas maneiras. Caso queira contribuir, sinta-se à vontade para fazer um fork deste repositório, implementar melhorias e submeter um pull request.

## Licença
Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.