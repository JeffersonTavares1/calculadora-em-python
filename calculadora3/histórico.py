

from random import choice
from limpar import limpa_tela
from banner import apresentação, carregamento, cores

lista_total = list()

def histórico(lista_total):
    if len(lista_total) > 0:
        
        apresentação(simbolos="•", ativo_linha1=False, texto1="Qual Retornar?", local_texto1="\t   ", cor_texto1=f"{choice(cores)}", quantidade_linha2=11, local_linha2="      ")
        print("\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        
        for pos, intem in enumerate(lista_total):
            print(f"\x1b[1m\x1b[7m{choice(cores)} {pos}:  ", end="")
            for simb, elemento in enumerate(intem):
                print(f"{elemento}", end="  ")
                if simb == 2:
                    print(" = ", end="  ")
            print()
        
        print("\x1b[m\x1b[1m\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        
        while True: 
            retornar = str(input("\x1b[38;5;57m>>>\x1b[1m   ")).strip()
            if retornar.isdigit() and int(retornar) < len(lista_total):
                retornar = int(retornar)
                break
            else:
                continue
        print("\x1b[38;5;247m" + ("一" * 18) + "\x1b[m")
        carregamento(texto="CARREGANDO!.")
        limpa_tela()
        return lista_total[retornar]
