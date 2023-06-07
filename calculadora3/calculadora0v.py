
from platform import system
from banner import apresentação, carregamento, data, hora, cores, frases, simbolos_matematicos
from histórico import histórico
from tabuada import tabuada, choice
from conversor_moedas import conversor
from limpar import limpa_tela

operações = list()

texto_menu = "vou pro menu de operações"
tela = "Novo valores"

apresentação_interuptor = True
operador = "?"
resultado = 0

while True:
    apresentação(ativo_linha1=False, cor_texto1=f"\x1b[7m{choice(cores)}", texto1=f" <{system()}", texto2=f"\x1b[48;5;247m{choice(cores)}{operador}\x1b[m", ativo_linha2=False, ativo_tempo=True, ativador=apresentação_interuptor)   
    apresentação(fonte_estilo1="\x1b[7m", texto1=f" Data: {data}  |  Hora: {hora}", quantidade_linha2=16, ativo_tempo=True, ativador=apresentação_interuptor)
    apresentação(ativo_linha1=False, cor_texto1=choice(cores), texto1=f"{choice(frases)} CALCULADORA", simbolo_texto1="•", ativo_tempo=True, ativador=apresentação_interuptor)
    
    if tela.startswith("S"):
        carregamento(texto="SAINDO!...")
        limpa_tela()
        apresentação(ativo_linha1=False, cor_texto1="\x1b[7m\x1b[38;5;57m", texto1=" <Ichiro", texto2="\x1b[48;5;247m\x1b[38;5;57mv.001\x1b[m", ativo_linha2=False, ativo_tempo=True)
        break
    
    elif tela.startswith("N"):
        apresentação(ativo_linha1=False, texto1="Informe Os Valores", local_texto1="\t ", cor_texto1=choice(cores))
        valor1 = str(input(f"\x1b[1m{choice(cores)}" if resultado == 0 else f"\x1b[1m{choice(cores)}{resultado}    \x1b[38;5;237m enter pra usar esse valor\r" + f"{choice(cores)}")) or str(resultado)
        operador_de_antes = operador
        operador = str(input(f"{operador}\r")) or operador
        valor2 = str(input("")).strip()
        print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        
        #一一一verificando erros no v1 e v2一一一一一一一
        deu_erro = False
        for verificando in (valor1 + valor2):
            if verificando.isalpha() or verificando.isspace() or verificando in "/:;()°&@一,?!'[]{}#%\"^*+=_\|~<>$×÷•二™®©♨":
                deu_erro = True
                break
        
        if deu_erro or not (bool(valor1) and bool(valor2)) or operador not in "?+-×÷/%":
            operador = operador_de_antes
            limpa_tela()
            continue
        # --convertendo-de-str-pra-int-ou-float--
        if "." in (valor1 + valor2):
            valor1, valor2 = float(valor1), float(valor2)
        else:
            valor1, valor2 = int(valor1), int(valor2)
        #一一一一一一一一一一一一一一一一一一一一一一一一
        if operador == "?":
            tela = "Operação Menu"
            apresentação_interuptor = False
        else:
            tela = "Resultado"
            limpa_tela()
            apresentação_interuptor = True
            
    elif tela.startswith("O"):
        apresentação(simbolos="•", ativo_linha1=False, texto1="Escolha o Operador", local_texto1="\t  ", cor_texto1="\x1b[38;5;166m", quantidade_linha2=11, local_linha2="      ")
        if texto_menu == "vou pro menu de operações":
            print(f"""        \x1b[1m{choice(cores)}< 0 >  <ADIÇÃO>
                  < 1> SUBTRAÇÃO
                  < 2 > MULTIPLICAÇÃO
                  < 3 > DIVISÃO
                  
                  < m> MAIS OPÇÕES
                  < n > NOVOS VALORES
                  < s > SAIR FORA\x1b[m""")
                  
        elif texto_menu == "menu mais opções":
            print(f"""       \x1b[1m{choice(cores)}< 4> POTÊNCIA
               < 5 > DIVISÃO INTEIRA
               < 6 > RESTO DA DIVISÃO
               < v > VOLTAR
               
               < a > CALCULAR A MÉDIA
               < c > CONVERSOR/MOEDA
               < t > TABUADA
               < h > HISTÓRICOS
               < s > SAIR FORA\x1b[m""")          
        print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        op = ""
        while op not  in "0123456MNSVACTH" or not bool(op):
            op = str(input("\x1b[38;5;57m>>> \x1b[1m\x1b[38;5;99m ")).strip().upper()
        print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        carregamento(texto="CARREGANDO!.", cor_fundo="\x1b[48;5;57m", cor_texto=choice(cores))
        limpa_tela()
        #一一一一一一一一一一一一一一一一
        if op == "S":
            tela = op
            #apresentação_interuptor = True
        elif op in "MV":
            texto_menu = "menu mais opções" if op == "M" else "vou pro menu de operações"
           # apresentação_interuptor = True
        elif op in "N":
            tela = "Novos Valores"
            continue
        elif op in "0123456":
             tela = "Resultados"
             operador = simbolos_matematicos[int(op)]
             #apresentação_interuptor = True
        elif op in "H":
             tela = "Histórico"
             #apresentação_interuptor = True
        elif op in "T":
            tela = "Tabuada"
            #apresentação_interuptor = True
        elif op in "C":
             tela = "Conversor de Moedas"
             
        apresentação_interuptor = True
         #一一一一一一一一一一一一一一一一
         
    elif tela.startswith("R"):
        #tela onde mostra os resultados das somas
        if operador == "+":
            resultado = valor1 + valor2
        elif operador == "-":
             resultado = valor1 - valor2
        elif operador == "×":
              resultado = valor1 * valor2
        elif operador == "÷":
              resultado = valor1 / valor2
        elif operador == "××":
              resultado = valor1 ** valor2
        elif operador == "/":
              resultado = valor1 // valor2
        elif operador == "%":
              resultado = valor1 % valor2
              
        operações.append([valor1, operador, valor2, resultado])  #historico
        
        apresentação(simbolos="•", ativo_linha1=False, texto1="Resultado da Operação", local_texto1="\t ", cor_texto1=choice(cores), quantidade_linha2=11, local_linha2="      ")
        apresentação(cor_texto1=choice(cores), texto1=f" {valor1}    {operador}    {valor2}    =    {resultado}")
        
        tela = "Opções Menu"
        apresentação_interuptor = False
        continue
        
    elif tela.startswith("H"):
        lista_escolhida = histórico(operações)
        valor1 = lista_escolhida[0]
        operador = lista_escolhida[1]
        valor2 = lista_escolhida[2]
        resultado = lista_escolhida[3]
        tela = "Novo Valores"
    
    elif tela.startswith("Tabuada"):
        tela = tabuada(resultado=str(resultado), operador=operador)
        
    elif tela.startswith("C"):
        tela = conversor(resultado)
        
    elif tela.startswith("A"):
        ...
