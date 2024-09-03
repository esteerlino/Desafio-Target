# Desafio-Target

Este repositório contém as soluções para o Desafio Target. Cada questão do desafio é abordada com implementações de código e explicações.

## Desafios

### Desafio 01. **Fibonacci**

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

    Exemplos:

    Entrada: 1
    Saída: O número 1 pertence à sequência de Fibonacci.

    Entrada: 4
    Saída: O número 4 não pertence à sequência de Fibonacci.

    Entrada: 9
    Saída: O número 9 não pertence à sequência de Fibonacci.

    Entrada: 144
    Saída: O número 144 pertence à sequência de Fibonacci.

### Desafio 02. **Contagem de ocorrências da letra "a"**

Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

    Exemplos:

    Entrada: InformadA
    Saída: A letra 'a' aparece 2 vez(es) em informada.

    Entrada: LAmpadA
    Saída: A letra 'a' aparece 3 vez(es) em lampada.

    Entrada: memoria
    Saída: A letra 'a' aparece 1 vez(es) em memoria.

    Entrada: copo
    Saída: A letra 'a' não está presente em copo.

### Desafio 03. **Análise de código**

Observe o trecho de código abaixo:

    int INDICE = 12, SOMA = 0, K = 1; 
    enquanto K < INDICE 
        faça { K = K + 1; SOMA = SOMA + K; } 
    imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA? **Resposta: 77**

### Desafio 04. **Qual o próximo número da seuqência?**

Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___ <br>
b) 2, 4, 8, 16, 32, 64, ____<br>
c) 0, 1, 4, 9, 16, 25, 36, ____<br>
d) 4, 16, 36, 64, ____<br>
e) 1, 1, 2, 3, 5, 8, ____<br>
f) 2,10, 12, 16, 17, 18, 19, ____

**Respostas:**

a) **9**. A sequência apresenta os números ímpares.<br>
b) **128**. A sequência apresenta potências de 2.<br>
c) **49**. A sequência apresenta quadrados perfeitos.<br>
d) **100**. A sequência apresenta quadrados perfeitos de números pares.<br>
e) **13**. A sequência apresenta a Sequência de Fibonacci.<br>
f) **200**. A sequência apresenta todos os números que começam com a letra "d".

### Desafio 05. **Simulação: interruptores e lâmpadas**

Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

**Resposta:** Para resolver essa questão basta seguir os seguintes passos:

1- Ligar o primeiro interruptor e deixar a lâmpada um tempo acessa e depois apagar. Assim, ela vai esquentar;<br>
2- Ligar o segundo interurptor e deixar a lâmpada acessa;<br>
3- Não é necessário ligar o terceiro interruptor.

Agora, vamos entrar nas duas salas. Basta verificar se as lâmpadas estão nos seguintes estados:

a- Lâmpada acessa e quente: foi ligada pelo segundo interruptor;<br>
b- Lâmpada desligada e quente: foi ligada pelo primeiro interruptor;<br>
c- Lâmpada desligada e fria: relacionada ao terceiro interruptor, que não foi ligado.

Assim, já é possível concluir a ligação entre os interruptores e suas respectivas salas.<br>
Se aparecer um caso da lâmpada estar ligada e fria, então existe algum problema.<br>
A lógica é identificar o estado da lâmpada: acessa ou desligada, fria ou quente.
