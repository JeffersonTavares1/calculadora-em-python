

from limpar import limpa_tela
from random import choice
from banner import apresentação, carregamento, cores, simbolos_matematicos


def tabuada(resultado="0", operador="?"):
    while True:
        apresentação(ativo_linha1=False, cor_texto1=choice(cores), texto1="Informe o Valor", local_texto1="\t    ")
        valor = str(input(f"\x1b[1m{choice(cores)}" if resultado in "0" else f"\x1b[1m{choice(cores)}{resultado}    \x1b[38;5;237m enter pra usar esse valor\r" + f"{choice(cores)}")) or resultado
        print("\x1b[m\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        
        resultado = valor
        #一一一一一一一一一一一一一一一
        deu_erro = False
        for verificando in valor:
            if verificando.isalpha() or verificando.isspace() or verificando in "-/:;()°&@一,?!'[]{}#%\"^*+=_\|~<>$×÷•二™®©♨":
                deu_erro = True
                break
        if deu_erro or not bool(valor):
            limpa_tela()
            continue
       #一一一一一一一一一一一一一一一
        if "." in valor:
            valor = float(valor)
        else:
            valor = int(valor)
        #一一一一一一一一一一一一一一一一
        
        apresentação(simbolos="•", ativo_linha1=False, texto1="Escolha o Operador", local_texto1="\t  ", cor_texto1="\x1b[38;5;166m", quantidade_linha2=11, local_linha2="      ")
        print(f"""        \x1b[1m{choice(cores)}< 0 >  <ADIÇÃO>
                  < 1> SUBTRAÇÃO
                  < 2 > MULTIPLICAÇÃO
                  < 3 > DIVISÃO
                  < 4 > POTÊNCIA
                  
                  < n > NOVOS VALORES
                  < s > SAIR FORA\x1b[m""")
        print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        op = ""
        while op not  in "01234SN" or not bool(op):
            op = str(input("\x1b[38;5;57m>>> \x1b[1m\x1b[38;5;99m ")).strip().upper()
        print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        carregamento(texto="CARREGANDO!.", cor_fundo="\x1b[48;5;57m", cor_texto=choice(cores))
        limpa_tela()
        #一一一一一一一一一一一一一一一一
        if op == "S":
            return "Novo valor"
            break
        elif op == "n":
            continue
        elif op in "01234":
            operador = simbolos_matematicos[int(op)]
        
        
        if operador in "+-×÷/%":
            
            while True:
                print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                do = str(input(f"\x1b[1m\x1b[7m{choice(cores)} Começo da Tabuada\x1b[m\x1b[1m\x1b[38;5;99m >>>  ")).strip()
                print("\x1b[m\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                ate = str(input(f"\x1b[1m\x1b[7m{choice(cores)} Final da Tabuada \x1b[m\x1b[1m\x1b[38;5;99m >>>  ")).strip()
                print("\x1b[m\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                carregamento(texto="MONTANDO!...", cor_fundo="\x1b[48;5;57m", cor_texto=choice(cores))
                limpa_tela()
                
                if not do.isdigit() or not ate.isdigit() or not (bool(do) and bool(ate)):
                    continue
                
                #aqui soma e mostre os resultados
                do, ate = int(do), int(ate)
                print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                for cont in range(do, ate + 1):
                    if "+" in operador:
                        soma = valor + cont
                        
                    elif "-" in operador:
                        soma = valor - cont
                        
                    elif "×" in operador:
                        soma = valor * cont
                        
                    elif "÷" in operador:
                        soma = valor / cont
                        
                    elif "××" in operador:
                        soma = valor ** cont
                        
                    elif "/" in operador:
                        soma = valor // cont
                        
                    elif "%" in operador:
                        soma = valor % cont
                        
                    print("\x1b[1m{}{:^4} {:^4} {:^4}{:^4}{:^4}\x1b[m".format(choice(cores), valor, operador, cont, "=", soma))
                    
                print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                
                while True:
                    op = str(input(f"\x1b[1m\x1b[7m{choice(cores)} Mostra Mais? [S/N]\x1b[m\x1b[1m\x1b[38;5;99m >>>  ")).upper()
                    if op in "SN" and not op.isspace():
                        break
                        
                if op == "N":
                    limpa_tela()
                    break
                limpa_tela()
