# Lista de exercícios 1 - variáveis e operadores


from math import floor


def soma_dois_inteiros(a, b):
    """Recebe dois números inteiros, e retorna a sua soma.
    Argumentos:
        a (int): 1o valor;
        b (int): 2o valor;
    Retorna:
        int: a soma dos dois valores.
    """

    return a + b


def metro_para_milimetros(metros):
    """Recebe um valor em metros, e retorna o valor em milímetros,
        sabendo que 1 metro equivale a 1000 milimetros.
        Argumento:
        metros (float): um valor em metros;
    Retorna:
        float: o valor convertido para milimetros,
    """
    return metros * 1000


def tempo_para_percorrer_uma_distancia(distancia, velocidade):
    """Recebe uma distância e a velocidade de movimentação, e retorna
        as horas que seriam gastas para percorrer em linha reta.
    Argumentos:
        distancia (float): a distância, em kilômetros.
        velocidade (float): a velocidade, em kilômetros por hora.
    Retorna:
        float: o tempo, em horas.
    """
    return round(distancia / velocidade, 2)


def aumento_salarial(salario, porcentagem):
    """Recebe um salário e sua porcentagem de aumento, e retorna
        o novo salário.
    Argumentos:
        salario (float): o salário original.
        porcentagem (float): o percentual de aumento, entre 0 e 100.
    Retorna:
        float: o novo salário, com duas casas decimais.
    """
    return round(salario * (1 + porcentagem / 100), 2)


def preco_com_desconto(preco_original, percentual_desconto):
    """Recebe um preço e sua porcentagem de desconto, e retorna
        o novo preço.
    Argumentos:
        preco_original (float): o preco original do produto.
        percentual_desconto (float): o percentual de desconto, entre 0 e 100.
    Returns:
        float: o preço final, após o desconto, com duas casas decimais.
    """
    return round(preco_original * (1 - percentual_desconto / 100), 2)


def dias_para_segundos(dias, horas, minutos, segundos):
    """Recebe uma data em dias com horas, minutos e segundos, e retorna
    a data em segundos.
    Argumentos:
        dias (int): a quantidade de dias.
        horas (int): a quantidade de horas.
        minutos (int): a quantidade de minutos.
        segundos (int): a quantidade de segundos.
    Retorna:
        int: a quantidade de segundos equivalente aos valores de dias, horas, minutos e segundos.
    """
    return dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos


def celsius_para_fahrenheit(celsius):
    """Recebe uma temperatura em graus Celsius, e retorna a temperatura
        em graus Fahrenheit.
    Argumento:
        celsius (float): a temperatura em graus Celsius.
    Retorna:
        float: a temperatura em graus Farenheit.
    """
    return round(celsius * 1.8 + 32, 2)


def fahrenheit_para_celsius(farenheit):
    """Recebe uma temperatura em graus Fahrenheit, e retorna a temperatura
        em graus Celsius.
    Argumento:
        farenheit (float): a temperatura em graus Fahrenheit.
    Retorna:
        float: a temperatura em graus Celsius.
    """
    return round((farenheit - 32) / 1.8, 2)


def preco_aluguel_carro(dias, km):
    """Recebe uma quantidade de dias que o carro foi alugado e a
        quantidade de quilômetros rodados, e retorna o valor a ser pago.
        1 dia: 60 reais mais R$ 0,15 por km rodado.
    Argumentos:
        dias (int): quantidade de dias que o carro foi alugado.
        km (float): quantos quilômetros o carro rodou.
    Retorna:
        float: o preço do aluguel do carro, com 2 casas decimais,
                conforme a fórmula dada no enunciado.
    """
    return round(dias * 60 + km * 0.15, 2)


def dias_perdidos_por_fumar(cigarros_fumados_por_dia, anos_fumando):
    """Recebe uma quantidade de cigarros fumados por dia e a quantidade
        de anos que fuma, e retorna o total de dias perdidos, sabendo que
        cada cigarro reduz a vida em 10 minutos.
    Argumentos:
        cigarros_fumados_por_dia (int): a quantidade de cigarros fumados por dia.
        anos_fumando (int): a quantidade de anos que a pessoa fumou.
    Retorna:
        int: a quantidade de dias que a pessoa perdeu por fumar.
    """
    return floor(((cigarros_fumados_por_dia * 10) / 60 / 24) * anos_fumando * 365)


def dois_elevado_a_dez_mil():
    """Calcula dois elevado a dez mil, e retorna a quantidade de
    algarismos.
    Retorna:
        int: a quantidade de algarismos que o resultado contém.
    """
    return len(str(2**10000))


def media_final_aprovado_reprovado(p1, p2, ep1, ep2):
    """Recebe as notas das 2 provas e 2 exercícios de programação e retorna
        se o aluno foi ou não aprovado. As provas têm peso 7 e os exercícios
        têm peso 3. Cada parcial tem peso igual.
        Uma forma de resolver é calcular a 1a parcial, com a média ponderada entre
        p1 e ep1, depois calcular a 2a parcial, com as notas de p2 e ep2 e depois
        calcular a média aritmética entre a 1a e a 2a parcial.
    Argumentos:
        p1 (float): a nota da primeira prova.
        p2 (float): a nota da segunda prova.
        ep1 (float): a nota do 1o exercício.
        ep2 (float): a nota do 2o exercício.
    Returns:
        bool: True ou False, dependendo da média ser maior ou igual a 7 ou não.
    """
    return (p1 * 7 + p2 * 7 + ep1 * 3 + ep2 * 3) / 20 >= 7


def salario(valor_hora, horas_mensais):
    """Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.
    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto.
    Argumentos:
        valor_hora (float): o valor hora pago ao funcionário.
        horas_mensais (float): a quantidade de horas trabalhadas no mes.
    Returns:
        float: o salário líquido, após todos os descontos.
    """

    salario_bruto = valor_hora * horas_mensais

    taxas = {"inss": 0.08, "IR": 0.11, "sindicato": 0.05}
    salario_liquido = round(salario_bruto -
                            (salario_bruto * taxas["inss"] + salario_bruto *
                             taxas["IR"] + salario_bruto * taxas["sindicato"]), 2)
    return salario_liquido


def duzias(ovos):
    """Receba o número de ovos e devolva a quantidade de dúzias
        correspondente. Considere sempre dúzias cheias, arredondando pra
        cima se necessário.
    Argumento:
        ovos (int): a quantidade de ovos.
    Retorna:
        int: a quantidade de dúzias correspondente à quantidade de ovos,
            arredondado pra cima.
    """
    return 1 + ovos // 12 if ovos % 12 > 0 else ovos // 12


def tinta(metros_pintar):
    """Recebe quantos metros quadrados precisa pintar,
        e retorna a quantidade de latas de tinta a comprar.
        A cobertura da tinta é de 3 metros por litro de tinta.
        Cada lata possui 18 litros de tinta.
    Argumento:
        metros_pintar (float): a quantidade de metros quadrados a pintar.
    Retorna:
        int: a quantidade de latas de tinta, arredondado pra cima.
    """
    capacidade_lata = 3 * 18
    return int(1 + metros_pintar // (capacidade_lata) if metros_pintar % (capacidade_lata) > 0 else metros_pintar // (capacidade_lata))


def decompor_numero(n):
    """Leia um número inteiro menor que 1000 e devolva a quantidade de
        centenas, dezenas e unidades do mesmo.
        Obs.: não utilize operações com strings.
    Argumento:
        numero (int): um número menor que 1000.
    Retorna:
        tupla de inteiros, com as centenas, dezenas e unidades do numero.
    """
    hundreds = n // 100
    n -= hundreds * 100

    dozens = n // 10
    n -= dozens * 10

    unities = n

    return (hundreds, dozens, unities)


# Lista de exercícios 2 - Estruturas (strings, listas, tuplas e dicionários)
# Resolva os problemas utilizando apenas os métodos das estruturas de dados e funções nativas (embutidas).
# Não utilize estruturas de decisão (if, elif, else) ou repetição(for e while).


def palindromo(texto):
    """Faça uma função que verifique se uma texto é palíndromo,
        isto é, se é igual quando lido de trás pra frente.
    Argumento:
        texto (string): Um texto qualquer.
    Retorna:
        bool: True ou False, dependendo dd texto ser palíndromo ou não.
    """
    texto = "".join(texto.split("!"))
    texto = "".join(texto.split("?"))
    texto = "".join(texto.split(":"))
    texto = "".join(texto.split(" "))
    return texto.lower() == texto[::-1].lower()


def troca_caixa(texto):
    """Vogais ficam em caixa alta (maiúsculas)
        Consoantes ficam em caixa baixa (minúsculas)
    Argumento:
        texto (string): Um texto qualquer.
    Retorna:
        string: o texto convertido, conforme o enunciado.
    """
    texto = texto.lower()
    texto = texto.replace("a", "A")
    texto = texto.replace("e", "E")
    texto = texto.replace("i", "I")
    texto = texto.replace("o", "O")
    texto = texto.replace("u", "U")
    return texto


def imprime_mes_por_extenso(data):
    """Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
        e imprima com o nome do mês por extenso ("dia 99 de mes de 9999").
    Argumento:
        data (string): uma data no formato "dd/mm/aaaa".
    Retorna:
        string: a data, no formato "99 de mês de 9999".
    """
    meses = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "março",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro",
    }
    dia, mes, ano = data.split("/")
    data_formatada = "".join(f"{dia} de {meses[mes]} de {ano}")
    return data_formatada


def encontra_caracter(texto, caracter_procurado):
    """Receba um texto e retorne a localização da primeira vez que
    aparece o caracter especificado.
    Args:
        texto (string): um texto qualquer.
        caracter_procurado (string): um caracter.
    Returns:
        int: a posição do caracter procurado no texto.
    """
    return texto.index(caracter_procurado)


def é_azarado(numero):
    """O último dígito não pode ser igual ao primeiro, porque isso dá azar.
    Argumento:
        numero (string): Um numero, no formato string.
    Retorna:
        bool: True ou False, baseado no enunciado.
    """
    return numero[:1:] == numero[-1::]


def ordenamento_contrario(lista):
    """Inverta a ordem dos elementos da lista.
    Argumento:
        lista (list): uma lista de elementos, independente de tipo.
    Retorna:
        list: uma lista com os elementos em ordem inversa.
    """
    return lista[::-1]


def maximo(lista):
    """Retorna o maior elemento da lista.
    Argumento:
        lista (list): uma lista de elementos float;
    Retorna:
        int: o maior elemento da lista.
    """
    # lista.sort()
    # return lista[-1]
    return max(lista)


def minimo(lista):
    """Retorna o menor elemento da lista.
    Argumento:
        lista (list): uma lista de elementos float;
    Retorna:
        int: o menor elemento da lista.
    """
    # lista.sort()
    # return lista[0]
    return min(lista)


def maior_menor(lista):
    """Calcule o maior e o menor número da lista recebida.
    Argumento:
        lista (list): uma lista de elementos float;
    Retorna:
        uma tupla com dois números inteiros, o maior e o menor da lista.
    """
    # lista.sort()
    # return (lista[-1], lista[0])
    return (max(lista), min(lista))


def media_saltos_lista(saltos):
    """Receba uma lista com os saltos de um atleta e calcule a média
        dos seus saltos, sabendo que o melhor e o pior saltos são desconsiderados.
    Argumento:
        saltos (list): uma lista com os saltos (float) de um atleta.
    Retorna:
        float: a média dos saltos, de acordo com o enunciado.
    """
    saltos.sort()
    saltos = saltos[1:-1:]  # remove primeiro e último elementos
    pontuacao_salto = sum(saltos)
    media_saltos = pontuacao_salto / len(saltos)
    return media_saltos


def contem(lista, item_procurado):
    """Verifica se uma lista contém um item procurado e devolve um valor booleano.
    Args:
        lista (list): uma lista de elementos de qualquer tipo.
        item_procurado (qualquer tipo): um item a ser procurado na lista.
    Returns:
        bool: um valor booleano (True/False), de acordo com o enunciado.
    """
    return item_procurado in lista


def conta(lista, item_procurado):
    """Informa quantas ocorrências de um item existem numa lista.
    Args:
        lista (list): uma lista de elementos de qualquer tipo.
        item_procurado (qualquer tipo): um item a ser procurado na lista.
    Returns:
        int: a quantidade de ocorrências do item procurado na lista.
    """
    return lista.count(item_procurado)


def mes_extenso(mes):
    """Receba um número correspondente ao mês e devolva a abreviatura do
    nome do mês, com 3 letras.
    Ex.: 1-jan, 2-fev, ..., 12-dez.
    Use uma lista com os nomes dos meses.
    Args:
        mes (list): uma lista de números de 1 a 12 correspondendo aos meses do ano.
    Returns:
        string: a abreviatura do nome do mês, com 3 dígitos.
    """
    meses = [
        "jan",
        "fev",
        "mar",
        "abr",
        "mai",
        "jun",
        "jul",
        "ago",
        "set",
        "out",
        "nov",
        "dez",
    ]
    return meses[mes - 1]


def media_temperaturas(temperaturas):
    """Retorna a média das temperaturas da lista.
    Argumento:
        temperaturas (list): uma lista de temperaturas (float).
    Retorna:
        float: a média das temperaturas.
    """
    soma_temperatura = sum(temperaturas)
    media_temperatura = round(soma_temperatura / len(temperaturas), 2)
    return media_temperatura


def leet(texto):
    """
    Converte texto em leet. Veja os testes para exemplos.
    Dicionário para usar na conversão:
        troca = {'a':'4','e':'3','g':'9','i':'1','s':'5','t':'7','o':'0'}
    Argumento:
        texto (string): Um texto qualquer.
    Retorna:
        string: o texto convertido, conforme o enunciado.
    """
    texto = texto.replace("a", "4")
    texto = texto.replace("e", "3")
    texto = texto.replace("g", "9")
    texto = texto.replace("i", "1")
    texto = texto.replace("s", "5")
    texto = texto.replace("t", "7")
    texto = texto.replace("o", "0")

    texto = texto.replace("A", "4")
    texto = texto.replace("E", "3")
    texto = texto.replace("G", "9")
    texto = texto.replace("I", "1")
    texto = texto.replace("S", "5")
    texto = texto.replace("T", "7")
    texto = texto.replace("O", "0")
    return texto


def apaga(texto, n):
    """
    Seja uma string texto e um inteiro n,
    retorna uma nova string sem a posição n.
    Argumento:
        texto (string): Um texto qualquer.
    Retorna:
        string: o texto convertido, conforme o enunciado.
    """
    texto = texto[:n:] + texto[n + 1::]
    return texto


# Lista de exercícios - Condições
from math import sqrt


def maior3(a, b, c):
    """Recebe três valores, e retorna o maior dos três.
    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;
    Retorna:
        float: o maior entre os três valores.
    """
    numeros = [a, b, c]
    numeros.sort()
    return numeros[2]


def menor3(a, b, c):
    """Recebe três valores, e retorna o menor dos três.
    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;
    Retorna:
        float: o menor entre os três valores.
    """
    numeros = [a, b, c]
    numeros.sort()
    # max(numeros) é uma alternativa
    return numeros[0]


def testa_lados(a, b, c):
    """Receba os três lados de um triângulo. Informe se os valores
    podem ser um triângulo. Indique, caso os lados formem um triângulo,
    se o mesmo é: equilátero, isósceles ou escaleno.
    Argumentos:
        a (float): primeiro lado;
        b (float): segundo lado;
        c (float): terceiro lado;
    Retorna:
        string: um texto indicando o resultado,
                conforme aparece nos testes no final desse arquivo.
    """
    # se a soma de 2 lados não é igual ou maior que o lado restante
    if not (a + b >= c and b + c >= a and a + c >= b):
        return "Não forma um triângulo"

    tipo_triangulo = ""
    # se os 3 lados são diferentes
    if a != b and a != c and c != b:
        tipo_triangulo = "Triângulo escaleno"
    # se os 2 lados são diferentes
    elif (
        (a == b and a != c and c != b)
        or (c == b and a != b and a != c)
        or (c != b and a != b and a == c)
    ):
        tipo_triangulo = "Triângulo isósceles"
    else:
        tipo_triangulo = "Triângulo equilátero"
    return tipo_triangulo


def ano_bissexto(ano):
    """Determine se um ano é bissexto ou não.
    Argumento:
        ano (int): um ano, no formato de 4 dígitos.
    Retorna:
        bool: True ou False (verdadeiro ou falso), caso a ano seja ou não bissexto.
    """
    # se o ano é divisível por 400 ou por 4 e não por 100
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


def maior_dia_do_mes(mes, ano):
    """Retorna o último dia do mês para um determinado ano e mês.
        Os valores possíveis são: 28, 29, 30 ou 31.
        Devem ser considerados os anos bissextos.
        Uma função separada para determinar se um ano é bissexto
        poderia ser utilizada.
    Argumentos:
        mes (int): um mês no formato de dois dígitos;
        ano (int): um ano, no fomato de 4 dígitos;
    Retorna:
        int: um inteiro indicando o último dia válido para aquele mês e ano.
    """
    meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if ano_bissexto(ano) and mes == 2:
        return meses[2] + 1
    return meses[mes]


def data_valida(data):
    """Recebe uma string no formato dd/mm/aaaa e informa
        um valor lógico indicando se a data é válida ou não.
        Verifica se ano é bissexto e outros detalhes.
        Confira os testes no final do arquivo para mais detalhes.
    Argumentos:
        data (string): data no formato "dd/mm/aaaa".
    Retorna:
        bool: True ou False, indicando se a datá é válida ou não.
    """
    meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    data_separada = data.split("/")
    dia = int(data_separada[0])
    mes = int(data_separada[1])
    ano = int(data_separada[2])

    if not mes in meses or ano == 0:
        return False
    elif mes == 2 and ano_bissexto(ano):
        return dia <= meses[mes] + 1 and dia > 0
    elif dia > meses[mes] or dia < 1:
        return False
    else:
        return True


def baskara(a, b, c):
    """Calcule as raízes de uma equação do segundo grau, na forma
    ax2 + bx + c. A função recebe a, b e c e faz as consistências,
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do 1o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois elementos.
    Argumentos:
        a (float): valor a da equação;
        b (float): valor b da equação;
        c (float): valor c da equação;
    Retorna:
        tupla de floats: uma tupla, contando os valores das raízes, sendo
        uma raiz, duas raízes ou uma tupla vazia caso não existam raízes.
    """
    if a == 0:
        return (-c / b,)

    delta = b**2 - 4 * a * c
    if delta < 0:
        return ()
    elif delta == 0:
        return ((-b + sqrt(delta)) / 2,)
    else:
        return ((-b + sqrt(delta)) / 2, (-b - sqrt(delta)) / 2)


def acrescimo_nota_bb(nota_sozinho, nota_com_ajuda):
    """Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
     brother recebera em sua nota pela ajuda.
     O acréscimo é de 1/4 da diferença das notas, se for positivo.
    Argumentos:
        nota_sozinho (float): a nota que o aluno tirou sem ajuda.
        nota_com_ajuda (float): a nota que o aluno tirou após ter sido ajudado.
    Retorna:
        float: o acréscimo na nota obtido pelo aluno que ajudou seu colega.
    """
    if nota_com_ajuda < 0 or nota_com_ajuda <= nota_sozinho:
        return 0.0
    else:
        return round((nota_com_ajuda - nota_sozinho) * (0.25), 1)# Lista de exercícios - Condições
from math import sqrt


def maior3(a, b, c):
    """Recebe três valores, e retorna o maior dos três.
    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;
    Retorna:
        float: o maior entre os três valores.
    """
    numeros = [a, b, c]
    numeros.sort()
    return numeros[2]


def menor3(a, b, c):
    """Recebe três valores, e retorna o menor dos três.
    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;
    Retorna:
        float: o menor entre os três valores.
    """
    numeros = [a, b, c]
    numeros.sort()
    # max(numeros) é uma alternativa
    return numeros[0]


def testa_lados(a, b, c):
    """Receba os três lados de um triângulo. Informe se os valores
    podem ser um triângulo. Indique, caso os lados formem um triângulo,
    se o mesmo é: equilátero, isósceles ou escaleno.
    Argumentos:
        a (float): primeiro lado;
        b (float): segundo lado;
        c (float): terceiro lado;
    Retorna:
        string: um texto indicando o resultado,
                conforme aparece nos testes no final desse arquivo.
    """
    # se a soma de 2 lados não é igual ou maior que o lado restante
    if not (a + b >= c and b + c >= a and a + c >= b):
        return "Não forma um triângulo"

    tipo_triangulo = ""
    # se os 3 lados são diferentes
    if a != b and a != c and c != b:
        tipo_triangulo = "Triângulo escaleno"
    # se os 2 lados são diferentes
    elif (
        (a == b and a != c and c != b)
        or (c == b and a != b and a != c)
        or (c != b and a != b and a == c)
    ):
        tipo_triangulo = "Triângulo isósceles"
    else:
        tipo_triangulo = "Triângulo equilátero"
    return tipo_triangulo


def ano_bissexto(ano):
    """Determine se um ano é bissexto ou não.
    Argumento:
        ano (int): um ano, no formato de 4 dígitos.
    Retorna:
        bool: True ou False (verdadeiro ou falso), caso a ano seja ou não bissexto.
    """
    # se o ano é divisível por 400 ou por 4 e não por 100
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


def maior_dia_do_mes(mes, ano):
    """Retorna o último dia do mês para um determinado ano e mês.
        Os valores possíveis são: 28, 29, 30 ou 31.
        Devem ser considerados os anos bissextos.
        Uma função separada para determinar se um ano é bissexto
        poderia ser utilizada.
    Argumentos:
        mes (int): um mês no formato de dois dígitos;
        ano (int): um ano, no fomato de 4 dígitos;
    Retorna:
        int: um inteiro indicando o último dia válido para aquele mês e ano.
    """
    meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if ano_bissexto(ano) and mes == 2:
        return meses[2] + 1
    return meses[mes]


def data_valida(data):
    """Recebe uma string no formato dd/mm/aaaa e informa
        um valor lógico indicando se a data é válida ou não.
        Verifica se ano é bissexto e outros detalhes.
        Confira os testes no final do arquivo para mais detalhes.
    Argumentos:
        data (string): data no formato "dd/mm/aaaa".
    Retorna:
        bool: True ou False, indicando se a datá é válida ou não.
    """
    meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    data_separada = data.split("/")
    dia = int(data_separada[0])
    mes = int(data_separada[1])
    ano = int(data_separada[2])

    if not mes in meses or ano == 0:
        return False
    elif mes == 2 and ano_bissexto(ano):
        return dia <= meses[mes] + 1 and dia > 0
    elif dia > meses[mes] or dia < 1:
        return False
    else:
        return True


def baskara(a, b, c):
    """Calcule as raízes de uma equação do segundo grau, na forma
    ax2 + bx + c. A função recebe a, b e c e faz as consistências,
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do 1o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois elementos.
    Argumentos:
        a (float): valor a da equação;
        b (float): valor b da equação;
        c (float): valor c da equação;
    Retorna:
        tupla de floats: uma tupla, contando os valores das raízes, sendo
        uma raiz, duas raízes ou uma tupla vazia caso não existam raízes.
    """
    if a == 0:
        return (-c / b,)

    delta = b**2 - 4 * a * c
    if delta < 0:
        return ()
    elif delta == 0:
        return ((-b + sqrt(delta)) / 2,)
    else:
        return ((-b + sqrt(delta)) / 2, (-b - sqrt(delta)) / 2)


def acrescimo_nota_bb(nota_sozinho, nota_com_ajuda):
    """Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
     brother recebera em sua nota pela ajuda.
     O acréscimo é de 1/4 da diferença das notas, se for positivo.
    Argumentos:
        nota_sozinho (float): a nota que o aluno tirou sem ajuda.
        nota_com_ajuda (float): a nota que o aluno tirou após ter sido ajudado.
    Retorna:
        float: o acréscimo na nota obtido pelo aluno que ajudou seu colega.
    """
    if nota_com_ajuda < 0 or nota_com_ajuda <= nota_sozinho:
        return 0.0
    else:
        return round((nota_com_ajuda - nota_sozinho) * (0.25), 1)

# Lista de exercícios - Condições (Adicional)

from math import floor


def situacao_aluno(nota1, nota2, nota3, faltas, aulas_ministradas):
    """
    A média do aluno é dada pela média aritmética simples entre as 3 notas.
    Se o aluno tiver mais de 25% de faltas, está automaticamente reprovado por faltas (RF).
    Se ele tiver média abaixo de 7.0, está em Exame Final (EF)
    Se tiver média acima de 7.0 e frequencia igual ou superior a 75% está aprovado (AP).
    Args:
        nota1 (float): 1a nota
        nota2 (float): 2a nota
        nota3 (float): 3a nota
        faltas (int): número de faltas
        aulas_ministradas (int): quantidade de aulas ministradas
    Returns:
        string: a situação do aluno
    """
    porcentagem_faltas = faltas * 100 / aulas_ministradas
    if porcentagem_faltas > 25:
        return "RF"

    return "AP" if (nota1 + nota2 + nota3) / 3 >= 7 else "EF"


def aumento_preco(preco):
    """
    Calcula o aumento do preço, baseado no seguinte critério:
    - até 280 (inclusive): aumento de 20%
    - até 700 (inclusive): aumento de 15%
    - até 1500 (inclusive): aumento de 10%
    - acima de 1500: aumento de 5%
    Argumentos:
        preco (float): o preço atual do produto
    Retorna:
        tupla de floats: preco atual, percentual de aumento, valor do aumento e
                            novo preço, todos com duas casas decimais.
    """
    if preco <= 280:
        novo_preco = round(preco * 1.2, 2)
        return (preco, 20, novo_preco - preco, novo_preco)

    elif preco <= 700:
        novo_preco = round(preco * 1.15, 2)
        return (preco, 15, novo_preco - preco, novo_preco)

    elif preco <= 1500:
        novo_preco = round(preco * 1.1, 2)
        return (preco, 10, novo_preco - preco, novo_preco)

    else:
        novo_preco = round(preco * 1.05, 2)
        return (preco, 5, novo_preco - preco, novo_preco)


def idade_canina(idade_humana, porte_do_cao):
    """
    É sabido que os caẽs amadurecem mais rapidamente do que os seres
        humanos (na verdade, alguns serem humanos parecem nunca amadurecer).
    Calcule sua idade canina, baseada nos seguintes fatores:
    - cães de porte pequeno: fator 5;
    - cães de porte médio: fator 6;
    - cães grandes: fator 7.
    Argumentos:
        idade_humana (int): a idade do ser humano
        porte_do_cao (string): um texto informando o porte do cão (veja os testes para detalhes)
    Retorna:
        int: a idade canina do ser humano
    """
    # dicionario > if e else
    # fator = {"pequeno": 5, "medio": 6, "grande": 7}
    # return floor(idade_humana / fator[porte_do_cao])
    if porte_do_cao == "pequeno":
        return floor(idade_humana / 5)
    elif porte_do_cao == "medio":
        return floor(idade_humana / 6)
    else:
        return floor(idade_humana / 7)


def aumento_salario(salario):
    """
    Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%
    Salário mínimo para referência: R$ 724,00
    Argumentos:
        salario (float): o salario atual
    Retorna:
        float: novo salário, com duas casas decimais.
    """
    salario_minimo = 724
    if salario / salario_minimo <= 1:
        return round(salario * 1.2, 2)
    elif salario / salario_minimo <= 2:
        return round(salario * 1.15, 2)
    elif salario / salario_minimo <= 5:
        return round(salario * 1.1, 2)
    else:
        return round(salario * 1.05, 2)


def nota_para_conceito(nota):
    """
    Converta a nota para conceito, conforme a tabela abaixo:
    Nota                     Conceito
    Entre 10.0 e 9.0            A
    Entre 8.9 e 8.0             B
    Entre 7.9 e 7.0             C
    Entre 6.9 e 6.0             D
    Entre 5.9 e zero            E
    Argumento:
        nota(float): a nota, com 1 casa decimal
    Retorna:
        string: o conceito correspondente
    """
    if nota >= 9:
        return "A"
    elif nota >= 8:
        return "B"
    elif nota >= 7:
        return "C"
    elif nota >= 6:
        return "D"
    else:
        return "E"


def imc(peso, altura):
    """
    Escreva uma função que calcula o índice de massa corporal (imc = peso / altura ** 2),
    de acordo com a seguinte tabela:
    imc <= 18.5: "Subpeso"
    imc <= 25.0: "Normal"
    imc <= 30.0: "Sobrepeso"
    imc > 30: "Obeso"
    Argumentos:
        peso (float): peso em Kg
        altura (float): altura em metros
    Retorna:
        string: índice de massa corporal
    """
    imc = peso / altura**2
    if imc <= 18.5:
        return "Subpeso"
    elif imc <= 25.0:
        return "Normal"
    elif imc <= 30.0:
        return "Sobrepeso"
    else:
        return "Obeso"


def converte_hora_24_para_12(horario):
    """
    Recebe um horário no formato 24 horas e retorna no formato 12 horas (am/pm).
    - am: antes do meio-dia
    - pm: depois do meio-dia
    Para detalhes. consulte: https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h
    Argumento:
        horario (string): um horário no formato 24 horas
    Retorna:
        string: horario no formato 12 horas (am/pm)
    """
    horas, minutos = horario.split(":")
    horas_int = int(horas)

    if horas_int == 0 or horas_int == 12:
        horas_int += 12

    if horas_int <= 12:
        return f"{horas_int}:{minutos} am"
    else:
        return f"{horas_int-12}:{minutos} pm"


def converte_hora_12_para_24(horario):
    """
    Recebe um horário no formato 12 horas (am/pm) e retorna no formato 24 horas.
    - am: antes do meio-dia
    - pm: depois do meio-dia
    Para detalhes. consulte: https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h
    Argumento:
        horario (string): um horário no formato 12 horas (am/pm)
    Retorna:
        string: horario no formato 24 horas
    """
    tempo, sufixo = horario.split(" ")
    horas, minutos = tempo.split(":")
    horas_int = int(horas)

    if horas_int == 0 or horas_int == 12:
        horas_int -= 12

    if sufixo == "pm":
        return f"{horas_int + 12}:{minutos}"
    horas = horas_int if len(str(horas_int)) > 1 else f"0{horas_int}"
    return f"{horas}:{minutos}"


def conta_combustivel(qtde_litros, tipo_combustivel, tipo_pagamento):
    """
    O posto Tabajara está vendendo combustíveis com a seguinte tabela de preços:
        a. Tabela de preços
            Álcool: R$ 3,159
            Gasolina: R$ 3,739
            Diesel: 3,090
        b. Se o pagamento for feito à vista ou débito, o cliente recebe um desconto de 10% sobre o valor total
        c. Escreva um função que leia o número de litros vendidos, o tipo de combustível (gasolina, álcool, diesel),
            e o tipo de pagamento (à vista, débito, crédito), calcule e devolva o valor total da compra.
    Args:
        qtde_litros (float): quantidade de litros vendida
        tipo_combustivel (string): uma letra indicando o tipo de combustível
        tipo_pagamento (string): uma letra, indicando o tipo de pagamento
    Returns:
        float: o valor a ser pago, com duas casas decimais
    """
    precos = {"a": 3.159, "g": 3.739, "d": 3.090}
    if tipo_pagamento == "c":
        return round(qtde_litros * precos[tipo_combustivel], 2)
    return round((qtde_litros * precos[tipo_combustivel]) * 0.9, 2)


def comprar_frutas(morango=0, uva=0):
    """
    Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Uva             R$ 1,80 por Kg          R$ 1,50 por Kg
    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
    compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
    sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
    quantidade (em Kg) de uvas adquiridas e escreva o valor a ser
    pago pelo cliente.
    Argumentos:
        morango (float): a quantidade de morangos, em Kg
        uva (float): a quantidade de uvas, em Kg
    Retorna:
        float: o preço a pagar, com 2 casas decimais
    """
    preco_uvas = uva * 1.8 if uva <= 5 else uva * 1.5
    preco_morangos = morango * 2.5 if morango <= 5 else morango * 2.2
    total = preco_morangos + preco_uvas

    if morango + uva > 8 or total > 25:
        return round(total * 0.9, 2)
    return round(total, 2)



#!/usr/bin/env python3
# Lista de exercícios - Estruturas de repetição For

# ATENÇÃO !!!
# Todos os exercícios devem ser resolvidos com "for".
# Utilizar "for item in lista" sempre que possível.
# Utilizar "for i, item in enumerate(item) sempre que possível.


def soma_das_temperaturas(lista):
    """Retorna a soma_das_temperaturas dos elementos de uma lista.
    Argumentos:
        lista (lista de floats): Uma lista de valores float.
    Retorna:
        float: a soma_das_temperaturas dos elementos da lista.
    """
    soma = 0
    for item in lista:
        soma += item
    return soma


def quantidade_de_impares(valor_inicial, valor_final):
    """Determine a quantidade de números ímpares num intervalo,
    excluindo os valores limite do intervalo.
    Argumentos:
        valor_inicial (int): o limite inferior do intervalo, excluindo-o;
        valor_final (int): o limite superior do intervalo, excluindo-o;
    Retorna:
        int: a quantidade de números ímpares dentro do intervalo dado.
    """
    impares = 0
    for item in range(valor_inicial + 1, valor_final):
        if item % 2 != 0:
            impares += 1
    return impares


def soma_das_temperaturas_dos_inteiros(valor1, valor2):
    """Calcule a soma_das_temperaturas dos números inteiros no intervalo dado.
    Considere que os limites do intervalo podem ser informados
    como números negativos ou fora de ordem.
    Ex: 1 e 5 ou 5 e 1, retorna 9
    Argumentos:
        valor1 (int): um dos limite do intervalo, excluindo-o;
        valor2 (int): o outro limite do intervalo, excluindo-o;
    Retorna:
        float: a soma_das_temperaturas dos valores dentro do intervalo dado.
    """
    soma_das_temperaturas = 0
    lista = [valor1, valor2]
    lista.sort()
    for item in range(lista[0] + 1, lista[1]):
        soma_das_temperaturas += item
    return soma_das_temperaturas


def serie(n):
    """Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
    Argumento:
        n (int): o valor final da série;
    Retorna:
        float: a soma_das_temperaturas dos valores da série,
        segundo a fórmula e o valor de n informados.
    """
    s = 0
    for item in range(1, n + 1):
        s += 1 / item
    return round(s, 2)


def ordenamento_contrario(lista):
    """Inverta a ordem dos elemntos da lista.
    Argumento:
        lista (list): uma lista de elementos, independente de tipo.
    Retorna:
        list: uma lista com os elementos a ordem invertida.
    """
    # return lista[::-1]
    lista_inversa = []
    for index, item in enumerate(lista):
        lista_inversa.append(lista[(index + 1) * -1])
    return lista_inversa


def intercalamento_listas(lista1, lista2):
    """Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo intercalamento entre as duas.
    Intercalar significa que a nova lista terá o 1o elemento da 1a lista,
    seguido do 1o elemento da 2a lista, seguido do 2o elemento da 1o lista,
    seguido do 2o elemento da 2a lista e assim por diante.
    Argumentos:
        lista1 (list): uma lista de elementos, independente de tipo;
        lista2 (list): uma lista de elementos, independente de tipo;
    Retorna:
        list: uma lista com os elementos intercalados das duas listas recebidas.
    """
    lista_intercalada = []
    for index, item in enumerate(lista1):
        lista_intercalada.append(lista1[index])
        lista_intercalada.append(lista2[index])
    return lista_intercalada


def im_pares(lista):
    """Separe em listas os pares e impares, dos inteiros da lista recebida.
    Argumento:
        lista (lista de inteiros): uma lista de elementos int;
    Retorna:
        uma tupla com duas listas de inteiros sendo a primeira uma lista com os pares
        e a segunda uma lista com os ímpares.
    """
    pares, impares = [], []
    for item in lista:
        if item % 2 == 0:
            pares.append(item)
        else:
            impares.append(item)
    return (pares, impares)


def maior_menor(lista):
    """Calcule o maior e o menor número da lista recebida.
    Argumento:
        lista (list): uma lista de elementos float;
    Retorna:
        uma tupla com dois números inteiros, o maior e o menor da lista.
    """
    # return (max(lista), min(lista))
    maior, menor = lista[0], lista[0]
    for item in lista:
        if item > maior:
            maior = item
        if item < menor:
            menor = item
    return (maior, menor)


def dar_troco(valor_a_pagar, valor_em_dinheiro):
    """Calcule o troco a devolver ao cliente com notas de 1,2,5,10,20,50.
        A resposta deve conter a quantidade de cada nota, sem considerar centavos.
    Argumentos:
        valor_a_pagar (float): o valor da conta
        valor_em_dinheiro (float): o valor que foi dado para pagar a conta.
    Retorna:
        uma lista de uma tuplas, onde cada dupla contém dois valores:
        o valor da nota e a quantidade daquela nota.
        Se a quantidade de notas for igual a zero, não deve aparecer na lista.
    """
    lista = [50, 20, 10, 5, 2, 1]
    notas = []
    troco = valor_em_dinheiro - valor_a_pagar

    if troco == 0:
        return []

    for item in lista:
        quantidade = troco // item
        troco -= item * quantidade
        if quantidade > 0:
            notas.append((item, quantidade))
    return notas


def media_anual(temperaturas):
    """Receba uma lista com as temperaturas médias de cada mês
    e devolva uma lista com os números correspondentes aos meses
    que possuem temperatura superior á média anual.
    Argumentos:
        temperaturas (lista de floats): as temperaturas médias de cada mês no ano, em ordem.
    Retorna:
        lista de inteiros: uma lista com o número correspondente ao mês em que a
        temperatura média foi maior que a temperatura média anual.
    """
    media_anual = round(sum(temperaturas) / len(temperaturas), 2)
    maior_que_media = []
    for index, item in enumerate(temperaturas):
        if item > media_anual:
            maior_que_media.append(index)
    return maior_que_media


def maiores_13(idades, alturas):
    """Receba as idades e alturas de diversas pessoas, em duas
        listas separadas e de igual comprimento.
        Calcule a media das alturas e retorne as alturas daqueles que
        possuem 'idades' maior que 13 e altura inferior a media da turma.
    Argumentos:
        idades (lista de inteiros): Uma lista de idades;
        alturas (lista de floats): uma lista de alturas;
    Retorna:
        uma lista de alturas dos alunos, conforme o criério definido.
    """
    media_altura = round(sum(alturas) / len(alturas), 2)
    alunos = []
    for index, item in enumerate(idades):
        if alturas[index] < media_altura and item > 13:
            alunos.append(alturas[index])
    return alunos


def testa_primo(valor):
    """Recebe um valor e verifica se ele é um número primo ou não.
    Argumento:
        valor (int): um número inteiro.
    Retorna:
        bool: True ou False, se o valor e ou não primo.
    """
    divisores = 0
    for item in range(1, valor + 1):
        if valor % item == 0:
            divisores += 1
    return divisores == 2


def lista_de_primos(inicio, fim):
    """Retorne uma lista de primos entre os valores informados, incluindo
    os limites.
    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;
    Retorna:
        lista de inteiros, os primos dentro do intervalo especificado.
    """
    lista_primos = []
    for item in range(inicio, fim):
        if testa_primo(item):
            lista_primos.append(item)
    return lista_primos


def fibonacci(n):
    """Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1,1,2,3,5,8,13,...
    Argumento:
        n (int): a quantidade de elementos que serão gerados.
    Retorna:
        uma lista de elementos inteiros correspondendo aos n primeiros elementos da série
        de Fibonacci.
    """
    lista = []
    for item in range(n):
        if len(lista) <= 1:
            lista.append(1)
        else:
            print(lista[-1], lista[-2])
            lista.append(lista[-1] + lista[-2])
    return lista


def altera_salarios(salarios):
    """Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%
    Salário mínimo para referência: R$ 724,00
    Argumento:
        salarios (lista de floats): os salários originais.
    Retorna:
        uma lista de elementos float, correspondendo aos salários corrigidos.
    """
    lista = []
    sm = 724
    for item in salarios:
        if item <= sm:
            lista.append(item * 1.2)
        elif item <= 2 * sm:
            lista.append(item * 1.15)
        elif item <= 5 * sm:
            lista.append(item * 1.1)
        else:
            lista.append(item * 1.05)
        lista[-1] = round(lista[-1], 2)
    return lista




#!/usr/bin/env python3
# Lista de exercícios - Estruturas de repetição while

# ATENÇÃO !!!
# Todos os exercícios devem ser resolvidos com "while".
# Não utilize "for", métodos das estruturas de dados ou funções embutidas.


def quantidade_de_impares(valor_inicial, valor_final):
    """Determine a quantidade de números ímpares num intervalo.
    Argumentos:
        valor_inicial (int): o limite inferior do intervalo;
        valor_final (int): o limite superior do intervalo;
    Retorna:
        int: a quantidade de números ímpares no intervalo.
    """
    impares = 0
    valor_inicial += 1
    valor_final += 1
    while valor_inicial + 1 <= valor_final - 1:
        if valor_inicial % 2 != 0:
            impares += 1
        valor_inicial += 1
    return impares


def soma_dos_inteiros(valor1, valor2):
    """Calcule a soma dos números inteiros no intervalo dado.
    Considere que os limites do intervalo podem ser informados
    como números negativos ou fora de ordem.
    Ex: 1 e 5 ou 5 e 1, retorna 9
    Argumentos:
        valor1 (int): um dos limite do intervalo, excluindo-o;
        valor2 (int): o outro limite do intervalo, excluindo-o;
    Retorna:
        float: a soma dos valores dentro do intervalo dado.
    """
    valor_inicial, valor_final, soma = valor1, valor2, 0
    if valor2 <= valor1:
        valor_inicial = valor2
        valor_final = valor1

    valor_inicial += 1
    while valor_inicial < valor_final:
        soma += valor_inicial
        valor_inicial += 1
    return soma


def potencia(base, expoente):
    """Calcule a base elevada ao expoente manualmente sem usar
    'base ** expoente'.
    Argumentos:
        base (int): o valor base;
        expoente (int): o expoente;
    Retorna:
        int: o resultado de base elevado ao expoente.
    """
    if base == 1:
        return 1
    if base == 0:
        return 0
    if expoente == 0:
        return 1

    expoente -= 1
    soma = base
    while expoente > 0:
        soma *= base
        expoente -= 1
    return soma


def crescimento_populacional(populacao1, populacao2, crescimento1, crescimento2):
    """Calcule quantos anos levará para a 'população1'
    ultrapassar a 'população2', baseado em suas porcentagens de crescimento.
    Argumentos:
        populacao1 (int): a população da 1a cidade;
        populacao2 (int): a população da 2a cidade;
        crescimento1 (float): o percentual de crescimento anual da população da 1a cidade;
        crescimento2 (float): o percentual de crescimento anual da população da 1a cidade;
    Retorna:
        int: a quantidade de anos que levará para a população da cidade 1 utrapassar a população da cidade 2.
    """
    anos = 0
    if crescimento1 <= crescimento2:
        return 0
    while populacao1 < populacao2:
        populacao1 += populacao1 * (crescimento1 / 100)
        populacao2 += populacao2 * (crescimento2 / 100)
        anos += 1
    return anos


def fibonacci(n):
    """Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1,1,2,3,5,8,13,...
    Argumento:
        n (int): a quantidade de elementos que serão gerados.
    Retorna:
        uma lista de elementos inteiros correspondendo aos n primeiros elementos da série
        de Fibonacci.
    """
    serie = []
    while n > 0:
        if len(serie) <= 1:
            serie.append(1)
        else:
            serie.append(serie[-1] + serie[-2])
        n -= 1
    return serie


def fatorial(numero):
    """Calcule e retorne o fatorial do 'numero' informado,
    O fatorial é o valor produtório dos valores menores ou iguais ao número
    ex: fatorial de 4 é 4*3*2*1 e retorna 24.
    Argumento:
        numero (int): o número do qual se quer calcular o fatorial.
    Retorna:
        int: o fatorial de numero.
    """
    soma = 1
    while numero > 0:
        soma *= numero
        numero -= 1
    return soma


def é_primo(valor):
    """Verifique se o valor informado é primo.
    Um número primo é aquele que é divisível apenas por ele mesmo e por 1.
    Argumento:
        valor (int): um número inteiro.
    Retorna:
        bool: True ou False, se o valor e ou não primo.
    """
    quantidade_divisor = 0
    divisor = 1
    while divisor <= valor:
        if valor % divisor == 0:
            quantidade_divisor += 1
        divisor += 1
    return quantidade_divisor == 2


def quantidade_de_primos(inicio, fim):
    """Retorne a quantidade de primos entre os valores informados, incluindo
    os limites.
    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;
    Retorna:
        int: a quantidade de números primos dentro do intervalo especificado.
    """
    quantidade_primo = 0
    while inicio <= fim:
        if é_primo(inicio):
            quantidade_primo += 1
        inicio += 1
    return quantidade_primo


def lista_de_primos(inicio, fim):
    """Retorne uma lista de primos entre os valores informados, incluindo
    os limites.
    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;
    Retorna:
        lista de inteiros, os primos dentro do intervalo especificado.
    """
    lista_primo = []
    while inicio <= fim:
        if é_primo(inicio):
            lista_primo.append(inicio)
        inicio += 1
    return lista_primo


def serie1(n):
    """Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
    Argumento:
        n (int): o valor final da série;
    Retorna:
        float: a soma dos valores da série, segundo a fórmula e o valor de n informados.
    """
    soma = 0
    divisor = 1
    while divisor <= n:
        soma += 1 / divisor
        divisor += 1
    return round(soma, 2)


def serie2(n):
    """Dado n, calcule o valor de
    s = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m
    Argumento:
        n (int): o valor final da série;
    Retorna:
        float: a soma dos valores da série, segundo a fórmula e o valor de n informados.
    """
    soma = 0
    numerador = 1
    divisor = 1
    while numerador <= n:
        soma += numerador / divisor
        divisor += 2
        numerador += 1
    return round(soma, 2)


def serie_pi(n):
    """Calcule o valor de pi através da série
    4/1 - 4/3 + 4/5 - 4/7 + ... - 4/m, sendo informado
    o número n de iterações.
    Argumento:
        n (int): o valor final da série;
    Retorna:
        float: o valor de pi calculado.
    """
    pi = 0
    divisor = 1
    iteracao = 0
    while iteracao < n:
        if iteracao % 2 != 0:
            pi -= 4 / divisor
        else:
            pi += 4 / divisor
        iteracao += 1
        divisor += 2
    return round(pi, 6)





# Marco André <marcoandre@gmail.com>
# Lista de exercícios de Fixação 5a

# Nessa lista você pode resolver os problemas utilizando o que você preferir:
# if, else, elif, for, while, métodos da lista e string, métodos embutidos no Python.

# Tente usar if ternário e outras formas de resolver com menos linhas de código.

# O objetivo é fixar todo o conteúdo já visto e desenvolver a lógica e o
# raciocínio com problemas novos.


def dormir(dia_semana, feriado):
    """
    dia_semana é True para dias na semana
    feriado é True nos feriados
    você pode ficar dormindo quando é feriado ou não é dia semana
    retorne True ou False conforme você vá dormir ou não
    """
    return not dia_semana or feriado  # se for feriado ou não for dia da semana


def alunos_problema(a_sorri, b_sorri):
    """
    temos dois alunos a e b
    a_sorri e b_sorri indicam se a e b sorriem
    temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
    retorne True quando houver problemas
    """
    return a_sorri == b_sorri


def soma_dobro(a, b):
    """
    dados dois números inteiros retorna sua soma
    porém se os números forem iguais retorna o dobro da soma
    soma_dobro(1, 2) -> 3
    soma_dobro(2, 2) -> 8
    """
    return a + b if a != b else 2 * (a + b)


def diff21(n):
    """
    dado um inteiro n retorna a diferença absoluta entre n e 21
    porém se o número for maior que 21 retorna o dobro da diferença absoluta
    diff21(19) -> 2
    diff21(25) -> 8
    dica: abs(x) retorna o valor absoluto de x
    """
    diferenca = abs(21 - n)
    return diferenca if 21 > n else 2 * diferenca


def papagaio(falando, hora):
    """
    temos um papagaio que fala alto
    hora é um parâmetro entre 0 e 23
    temos problemas se o papagaio estiver falando antes da 7 ou depois das 20
    """
    return falando and (hora > 20 or hora < 7)


def dez(a, b):
    """
    dados dois inteiros a e b
    retorna True se um dos dois é 10 ou a soma é 10
    """
    return a == 10 or b == 10 or a + b == 10


def dista10(n):
    """
    seja um inteiro n
    retorna True se a diferença absoluta entre n e 100 ou n e 200
    for menor ou igual a 10
    dista10(93) -> True
    dista10(90) -> True
    dista10(89) -> False
    """
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


def apaga(s, n):
    """
    seja uma string s e um inteiro n
    retorna uma nova string sem a posição n
    apaga('kitten', 1) -> 'ktten'
    apaga('kitten', 4) -> 'kittn'
    """
    return s[:n] + s[n + 1 :]


def troca(s):
    """
    seja uma string s
    se s tiver tamanho <= 1 retorna ela mesma
    caso contrário troca a primeira e última letra
    troca('code') -> 'eodc'
    troca('a') -> 'a'
    troca('ab') -> 'ba'
    """
    if len(s) <= 1:
        return s

    return s[-1] + s[1:-1] + s[0]


def multi_string(s, n):
    """
    Seja uma string s e um inteiro positivo n
    retorna uma string com n cópias da string original
    multi_string('Oi', 2) -> 'OiOi'
    """
    return s * n


def explode_string(s):
    """
    explode_string('Code') -> 'CCoCodCode'
    explode_string('abc') -> 'aababc'
    explode_string('ab') -> 'aab'
    """
    string_explodida = ""
    for iteracao in range(len(s)):
        string_explodida += s[: iteracao + 1]
    return string_explodida


def conta_noves(nums):
    """Conta quantas vezes aparece o 9 numa lista nums."""
    return nums.count(9) if 9 in nums else False


def nove_na_frente(nums):
    """
    verifica se pelo menos um dos quatro primeiros itens é nove
    nove_na_frente([1, 2, 9, 3, 4]) -> True
    nove_na_frente([1, 2, 3, 4, 9]) -> False
    nove_na_frente([1, 2, 3, 4, 5]) -> False
    """
    return nums.index(9) < 4 if 9 in nums else False


def alo_nome(nome):
    """
    Seja uma string nome
    alo_nome('Bob') -> 'Alô Bob!'
    alo_nome('Alice') -> 'Alô Alice!'
    alo_nome('X') -> 'Alô X!'
    """
    return f"Alô {nome}!"


def cria_tags(tag, palavra):
    """
    cria_tags('i', 'Uhul'), '<i>Uhul</i>'
    cria_tags('i', 'Alô'), '<i>Alô</i>'
    cria_tags('cite', 'Uhul'), '<cite>Uhul</cite>'
    """
    return f"<{tag}>{palavra}</{tag}>"


def final_extra(s):
    """
    Seja um string s com no mínimo duas letras,
    retorna três vezes as duas últimas letras.
    final_extra('Alô'), 'lololo'
    final_extra('ab'), 'ababab'
    final_extra('Oi'), 'OiOiOi'
    """
    return s[-2:] * 3


def primeira_metade(s):
    """
    Seja uma string s, retorna a primeira metade da string
    primeira_metade('papagaio') -> 'papa'
    primeira_metade('Lula') -> 'Lu'
    primeira_metade('abcdef') -> 'abc'
    """
    return s[: len(s) // 2]


def sem_pontas(s):
    """
    Seja uma string s de pelo menos dois caracteres,
    retorna uma string sem o primeiro e último caracter.
    sem_pontas('Beleza') -> 'elez'
    sem_pontas('Python') -> 'ytho'
    sem_pontas('codigo') -> 'odig'
    """
    return s[1:-1]


def gira_esquerda_2(s):
    """
    Rodar à esquerda uma string s duas posições
    a string possui pelo menos 2 caracteres
    gira_esquerda_2('Beleza') -> 'lezaBe'
    gira_esquerda_2('Oi') -> 'Oi'
    """
    return s[2:] + s[:2]







# Marco André <marcoandre@gmail.com>
# Lista de exercícios de Fixação 5b

# Nessa lista você pode resolver os problemas utilizando o que você preferir:
# if, else, elif, for, while, métodos da lista e string, métodos embutidos no Python.

# Tente usar if ternário e outras formas de resolver com menos linhas de código.

# O objetivo é fixar todo o conteúdo já visto e desenvolver a lógica e o
# raciocínio com problemas novos.


def comeco_ou_fim_6(nums):
    """
    Verifica se 6 é o primeiro ou último elemento da lista nums.
    comeco_ou_fim_6([1, 2, 6]) -> True
    comeco_ou_fim_6([6, 1, 2, 3]) -> True
    comeco_ou_fim_6([3, 2, 1]) -> False
    """
    return nums[0] == 6 or nums[-1] == 6


def inicio_fim_igual(nums):
    """
    Retorna True se a lista nums possui pelo menos um elemento
    e o primeiro elemento é igual ao último
    inicio_fim_igual([1, 2, 3]) -> False
    inicio_fim_igual([1, 2, 3, 1]) -> True
    inicio_fim_igual([1, 2, 1]) -> True
    """
    if len(nums) < 1:
        return False
    return nums[0] == nums[-1]


def extremidades_iguais(a, b):
    """
    Dada duas listas a e b verifica se os dois primeiros são
    iguais ou os dois últimos são iguais.
    Suponha que as listas tenham pelo menos um elemento.
    extremidades_iguais([1, 2, 3], [7, 3]) -> True
    extremidades_iguais([1, 2, 3], [7, 3, 2]) -> False
    extremidades_iguais([1, 2, 3], [1, 3]) -> True
    """
    return a[0] == b[0] or a[-1] == b[-1]


def maior_ponta(nums):
    """
    Dada uma lista não vazia, cria uma nova lista onde todos
    os elementos são o maior das duas pontas
    obs.: não é o maior de todos os itens, mas entre as duas pontas
    maior_ponta([1, 2, 3]) -> [3, 3, 3]
    maior_ponta([1, 3, 2]) -> [2, 2, 2]
    """
    number = nums[0] if nums[0] >= nums[-1] else nums[-1]
    return [number for _ in nums]


def soma_2_primeiros(nums):
    """
    Dada uma lista de inteiros de qualquer tamanho retorna a soma dos
    dois primeiros elementos.
    Se a lista tiver menos de dois elementos, soma o que for possível.
    """
    return nums[0] + nums[1] if len(nums) >= 2 else sum(nums)


def meio_do_caminho(a, b):
    """
    sejam duas listas de inteiros a e b
    retorna uma lista de tamanho 2 contendo os elementos do
    meio de a e b, suponha que as listas tem tamanho ímpar
    meio_do_caminho([1, 2, 3], [4, 5, 6]) -> [2, 5]
    meio_do_caminho([7, 7, 7], [3, 8, 0]) -> [7, 8]
    meio_do_caminho([5, 2, 9], [1, 4, 5]) -> [2, 4]
    """
    return [
        a[len(a) // 2],
        b[len(b) // 2],
    ]  # [len(lista) // 2] retorna o elemento na posição do meio da lista


def numero_invertido(numero):
    """Receba um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321"""
    return int((str(numero)[::-1]))


def gago(texto):
    """Receba um texto e devolva-o repetindo a primeira letra de cada palavra, junto com um traço
    gago("preciso tirar dez") -> "p-preciso t-tirar d-dez"
    gago("eu deveria ter estudado mais") -> "e-eu d-deveria t-ter e-estudado m-mais"
    """
    texto_fatiado = texto.split(" ")
    for index, palavra in enumerate(texto_fatiado):
        texto_fatiado[index] = f"{palavra[0]}-{palavra}"
    return " ".join(texto_fatiado)


def saudacao(nome, hora):
    """Escreva uma saudação para a pessoa, dependendo do horário do dia:
    Entre 5 e 12: dia
    Entre 12 e 18: tarde
    Entre 18 e 5: noite"""
    periodo = "Boa noite"
    if hora >= 5 and hora < 12:
        periodo = "Bom dia"
    elif hora >= 12 and hora <= 18:
        periodo = "Boa tarde"
    return f"{periodo} {nome}"


def rosquinhas(n):
    """
    Para um inteiro n retorna uma string na forma '<n> rosquinhas'
    onde n é o valor passado como argumento.
    Caso n >= 10 devo retornar 'muitas' em lugar do número.
    rosquinhas(5) -> '5 rosquinhas'
    rosquinhas(23) -> 'muitas rosquinhas'
    """
    return f"{n if n < 10 else 'muitas'} rosquinhas"


def pontas(s):
    """
    Dada uma string s, retorna uma string com as duas primeiras e as duas
    últimas letras da string original s
    Assim 'palmeiras' retorna 'paas'
    No entanto, se a string tiver menos que 2 letras, retorna uma string vazia
    """
    return s[:2] + s[-2:] if len(s) > 1 else ""


def fixa_primeiro(s):
    """
    Dada uma string s, retorna uma string onde todas as ocorrências
    do primeiro caracter são trocados por '*', exceto para o primeiro
    Assim 'abacate' retorna 'ab*c*te'
    Dica: use s.replace(stra, strb)
    """
    return s[0] + s[1:].replace(s[0], "*")


def nomes_pontas(n):
    """Dada uma string n contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome, em
    maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO MENDES"
    """
    return f"{n.split(' ')[0].upper()} {n.split(' ')[-1].upper()}"


def nomes_pontas_e_iniciais_do_meio(n):
    """Dada uma string n contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome,
    e as inciais dos nomes do meio, em maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO A L MENDES"
    """
    preposicoes = ["da", "de", "do"]
    nomes = n.split(" ")
    iniciais = []

    for nome in nomes[1:-1]:
        if len(nome) > 1 and nome not in preposicoes:
            iniciais.append(nome[0])

    if not len(iniciais) > 0:
        return f"{nomes[0].upper()} {nomes[-1].upper()}"

    return f"{nomes[0].upper()} {' '.join(iniciais)} {nomes[-1].upper()}"


def mistura2(a, b):
    """
    Sejam duas strings a e b
    Retorno uma string '<a> <b>' separada por um espaço
    com as duas letras trocadas de cada string
      'mix', pod' -> 'pox mid'
      'dog', 'dinner' -> 'dig donner'
    """
    return f"{b[:2]}{a[2:]} {a[:2]}{b[2:]}"


def tres_maiusculas(texto):
    """Encontre a primeira ocorrência de 3 letras maiúsculas consecutivas
    no texto."""
    posicoes = [index for index, letra in enumerate(texto) if letra == letra.upper()]

    if len(posicoes) < 3:
        return None

    if not (posicoes[0] + 1 == posicoes[1] and posicoes[1] + 1 == posicoes[2]):
        return None
    return posicoes[0]


def im_pares_unicos(lista):
    """Separe em listas os impares e pares únicos (não considere duplicidades),
    dos inteiros da 'lista'
    """
    # index == lista.index(numero) se a posicao do numero for diferente da primeira ocorrencia, é uma duplicata
    pares = [
        numero
        for index, numero in enumerate(lista)
        if numero % 2 == 0 and index == lista.index(numero)
    ]
    impares = [
        numero
        for index, numero in enumerate(lista)
        if numero % 2 != 0 and index == lista.index(numero)
    ]
    return (pares, impares)




# Avaliação 1 - BSI
from math import ceil


def duracao_filme(horas, minutos):
    """
    Elabore um programa que leia a duração de um filme em horas e minutos.
    Calcule e informe a duração total do filme em número de minutos.
    Exemplo:
    Número de horas: 2
    Número de minutos: 40
    Total de minutos: 160
    Argumentos:
        horas (int): uma quantidade de horas
        minutos (int): uma quantidade de minutos
    Retorna:
        (int): uma quantidade de minutos.
    """
    return horas * 60 + minutos


def milhas_para_kilometros(milhas):
    """
    Uma milha equivale a 1609 metros. Desenvolva uma função que receba um valor \
    em milhas e retorne o valor em kilômetros.
    Argumentos:
        milhas (float): uma quantidade de milhas
    Retorna:
        (float): uma quantidade em kilômetros, com 6 casas decimais.
    """
    return (milhas * 1609) / 1000


def aluguel_airbnb(valor_diaria, dias):
    """
    Recebe uma quantidade de dias que ficou hospedado e o valor da
    diária, e retorna o valor a ser pago, considerando um acréscimo de
    R$ 75,00 para limpeza e 5% de taxa de administração sobre o valor
    do aluguel, sem a taxa de limpeza
    Argumentos:
        valor_diaria (float): o valor da diária
        dias (int): a quantidade de dias de hospedagem
    Retorna:
        float: o valor do aluguel, com duas casas decimais
    """
    parcial_aluguel = valor_diaria * dias
    return round(parcial_aluguel + parcial_aluguel * 0.05 + 75, 2)


def acesso_computadores(qt_alunos_total, qt_alunos_computador):
    """
    Você foi encarregado de realizar uma pesquisa sobre acesso a computadores.
    A sua pesquisa deverá apresentar o percentual de alunos da sua escola que possuem acesso computadores.
    Para isso, elabore um algoritmo que leia o número total de alunos da sua escola e o número de alunos que possuem acesso a computadores, por fim, com base nestes dados, escreva o percentual de alunos com acesso a computadores.
    Por exemplo, em uma escola com 500 alunos, apenas 200 alunos possuem acesso à Internet, o que equivale a 40% destes 500 alunos.
    Argumentos:
        qt_alunos_total (int): uma quantidade de horas
        qt_alunos_computador (int): uma quantidade de minutos
    Retorna:
        (float): percentual de alunos com acesso a computadores, com 2 casas decimais
    """
    return round(qt_alunos_computador * 100 / qt_alunos_total, 2)


def media_ponderada(prova, trabalho, exercicio):
    """
    Calcule a média ponderada, sabendo que os pesos são os seguintes:
    - prova: peso 4
    - trabalho: peso 2
    - exercício : peso 1
    Dica: eliminar os números mágicos.
    Argumentos:
        prova (float): nota de uma prova, entre 0 e 10.
        trabalho (float): nota do trabalho, entre 0 e 10.
        exercicio (float): nota do exercício, entre 0 e 10.
    Retorna:
        float: média ponderada das notas, com 1 casa decimal
    """
    return round((prova * 4 + trabalho * 2 + exercicio * 1) / (4 + 2 + 1), 1)


def cadeira_massagem(valor_3_minutos, qt_minutos_uso):
    """
    Elabore um programa para uma cadeira de massagem.
    O programa deve ler o valor para cada 3 minutos de uso da cadeira e o tempo que a pessoa utilizou em minutos. Informe o valor a ser pago pelo cliente, sabendo que as frações extras de 3 minutos devem ser cobradas de forma integral.
    Exemplo:
    Valor para 3 minutos RS: 2.00
    Minutos de uso: 7
    Total a Pagar R$: 6.00
    Argumentos:
        valor_3_minutos (float): o valoa ser cobrado a cada 3 minutos
        qt_minutos_uso (int): a quantidade de minutos que foi utilizado
    Retorna:
        (float): o valor a ser pago, com 2 casas decimais
    """
    return valor_3_minutos * ceil(qt_minutos_uso / 3)


def trimestre(mes):
    """
    Dado um mês como um inteiro de 1 a 12, retorna a qual trimestre do ano ele \
        pertence como um número inteiro. 
    Por exemplo: mês 2 (fevereiro), faz parte do primeiro trimestre; \
    o mês 6 (junho), faz parte do segundo trimestre; \
    e o mês 11 (novembro), faz parte do quarto trimestre.
    Argumento
        mes (inteiro): o mês
    Returna:
        inteiro: o trimestre a que o mês pertence.
    """
    return ceil(mes / 3)



# Avaliação 2 - BSI


def dobro(a, b):
    """
    Dados dois números inteiros retorna sua soma,
    porém se os números forem iguais retorna o dobro da soma.
    """
    if a == b:
        return (a + b) * 2
    return a + b


def dez(a, b):
    """
    Dados dois inteiros, retorna True se um dos dois é 10 ou a soma é 10.
    """
    return a == 10 or b == 10 or a + b == 10


def troca(s):
    """
    Seja uma string,
    se ela tiver tamanho <= 1 retorna ela mesma,
    caso contrário troca a primeira e a última letra.
    """
    if len(s) <= 1:
        return s
    string_formatada = s[-1] + s[1:-1] + s[0]  # troca primeira e última letra
    return string_formatada


def inicio_nove(nums):
    """
    Verifica se pelo menos um dos quatro primeiros itens é nove.
    """
    return (
        nums.index(9) < 4 if 9 in nums else False
    )  # procura o index apenas se existir o 9 na lista


def primeira_metade(s):
    """
    Seja uma string, retorna a primeira metade da string.
    """
    return s[: len(s) // 2]


def sem_pontas(s):
    """
    Seja uma string de pelo menos dois caracteres,
    retorna uma string sem o primeiro e último caracter.
    """
    return s[1:-1]


def gira_esquerda(s):
    """
    Rodar à esquerda uma string duas posições.
    A string possui pelo menos 2 caracteres.
    """
    return s[2:] + s[:2]


def inicio_fim_igual(nums):
    """
    Retorna True se a lista possui pelo menos um elemento
    e o primeiro elemento é igual ao último
    """
    return nums[0] == nums[-1] if len(nums) != 0 else False


def numero_invertido(num):
    """
    Receba um inteiro positivo e o mostre invertido.
    Ex.: 1234 gera 4321
    """
    return int(str(num)[::-1])  # converte para string, inverte, converte para inteiro


def nomes_pontas(n):
    """Dada uma string contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome, em
    maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO MENDES"
    """
    nomes = n.split(" ")

    return f"{nomes[0].upper()} {nomes[-1].upper()}"
