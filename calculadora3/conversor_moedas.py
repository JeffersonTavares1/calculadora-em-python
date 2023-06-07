
import requests
import json
from random import  choice
from limpar import limpa_tela
from lista_de_paises import paises, pesquisar_letra
from banner import apresentação, carregamento, cores



def conversor(valor=0):
    tel = "Novo valor"

    pais_de = "Real Brasileiro"
    pais_para = "Dólar Americano"
    #valor = 0

    while True:
        if tel.startswith("S"):
            limpa_tela()
            break
            
        elif tel.startswith("N"):
            apresentação(ativo_linha1=False, texto1="Conversor de Moeda", local_texto1="\t ", cor_texto1=choice(cores))
            valor = str(input(f"{choice(cores)}          < {pais_de} > \r" if valor == 0 else f"{valor}          {choice(cores)}< {pais_de} >\r")).strip() or str(valor)
            
            apresentação(cor_texto1=f"\x1b[7m{choice(cores)}" , texto1=f"< Convertido Para ↙>", local_texto1="\t\t", ativo_linha2=False)
            
            #一一Trata-se一erros一一一一一一一一一一一一
            deu_erro = False
            for verificando in valor:
                if verificando.isalpha() or verificando.isspace() or verificando in "/:;()°&@一,?!'[]{}#%\"^*+=_\|~<>$×÷•二™®©♨":
                    deu_erro = True
                    
            if deu_erro or not bool(valor):
                 limpa_tela()
                 valor = ""
                 continue
            #一一一e一int一ou一float一一一一一一一一一一.
            if "." in valor:
                valor = float(valor)
            else:
                valor = int(valor)
            #一一一一一一一一一一一一一一一一一一一
            tel = "Resultado"
            
        elif tel.startswith("R"):
            buscar_cotacao = (paises[pais_para] + "-" + paises[pais_de])
            pesquisador = requests.get("https://economia.awesomeapi.com.br/last/" + buscar_cotacao).json()
            cotaçao = (valor / float(pesquisador[buscar_cotacao.replace("-", "")]["bid"]))
            
            apresentação(texto1=f"{choice(cores)}{cotaçao:.2f}          < {pais_para} >\r" ,local_linha1="\n")
            tel = "Opções Menu"
        
        elif tel.startswith("O"):
            print(f"""{choice(cores)}
< I >    Inverter Conversão Atual →←
< T |    Trocar Paises/Conversão
< N |    Novo Valor •
< S |    Voltar Para a Calculadora +×
< B >   Sair do Programa :(
            \x1b[m""")
            print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
            
            op = "  "
            while op not in "ITNSB" or not bool(op) or op.isspace():
                op = str(input(f"\x1b[1m\x1b[7m{choice(cores)} Sua Opção?\x1b[m\x1b[1m\x1b[38;5;99m >>>  ")).strip().upper()
            print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
            carregamento(texto="CARREGANDO!.")
            
            #一一一一一一一一一一一一一一一一一一一一一
            if op in "I":
                guarda = pais_para
                pais_para = pais_de
                pais_de = guarda
                limpa_tela()
                tel = "Novo valor"
            
            elif op in "T":
                tel = "Trocar Paise"
                limpa_tela()
                
            elif op in "N":
                tel = "Novo Valor"
                limpa_tela()
                
            elif op in "S":
                tel = "Sair"
                limpa_tela()
                return "Novo Valor"
                
            elif op in "B":
                exit()
            #一一一一一一一一一一一一一一一一一一一一一
            
        elif tel.startswith("T"):
            cont = 0
            while True:
                
                if cont == 2:
                    tel = "Novo Valor"
                    break
                
                apresentação(texto1=(" Converter De?" if cont == 0 else " Converter Para?"),  cor_texto1=f"\x1b[7m{choice(cores)}")
                procurando = str(input(f"{choice(cores)}       Exp: Nome do País. / Moeda.\r")).strip().upper()
                print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                
                if procurando.isdigit() or not bool(procurando) or procurando.isspace():
                    limpa_tela()
                    continue
                
                for letra in pesquisar_letra(procurando).values():
                    for pos, pais in enumerate(letra):
                        print(f"\x1b[1m\x1b[7m{choice(cores)} {pos}:   {pais}\x1b[m")
                
                print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                apresentação(cor_texto1=f"{choice(cores)}" , texto1="< P >    Pesquisa de Novo", local_texto1="\t ", ativo_linha1=False)
                
                op = "  "
                while not op.isdigit() or not bool(op) or op.isspace():
                    op = str(input(f"\x1b[1m\x1b[7m{choice(cores)} Sua Escolha?\x1b[m\x1b[1m\x1b[38;5;99m >>>  ")).strip().upper()
                    if op in "P":
                        break
                print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
                limpa_tela()
                
                if op in "P":
                    continue
                if cont == 0:
                    pais_de = pesquisar_letra(procurando)[procurando[0].upper()][int(op)]
                elif cont == 1:
                    pais_para = pesquisar_letra(procurando)[procurando[0].upper()][int(op)]
          
                cont += 1
