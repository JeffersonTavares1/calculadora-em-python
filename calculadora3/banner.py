
from time import sleep
from datetime import  date, datetime

simbolos_matematicos = ["+", "-", "×", "÷", "××", "/", "%"]

data = f"{date.today().day}/{date.today().month}/{date.today().year}"
hora = f"{datetime.now().hour}:{datetime.now().minute}"
cores = ("\x1b[38;5;57m", "\x1b[38;5;124m", "\x1b[38;5;99m", "\x1b[38;5;166m", "\x1b[38;5;196m", "\x1b[38;5;36m", "\x1b[38;5;202m", "\x1b[38;5;143m", "\x1b[38;5;58m", "\x1b[38;5;56m", "\x1b[38;5;94m", "\x1b[38;5;100m")
frases = ("bem vindo!.   ", "estude pra valer!.", "O dia hoje tá massa!.", "O número de Pi é 3.14")

def apresentação(
ativo_linha1=True, 
local_linha1="",
cor_linha1="\x1b[38;5;247m",
estilo_linha1="\x1b[1m",
simbolo_linha1="一",
quantidade_linha1=18, 

ativo_texto1=True, 
local_texto1="",
cor_texto1="\x1b[38;5;166m",
fonte_estilo1="\x1b[1m",
simbolo_texto1="",
texto1="Vazil",
texto2="",


ativo_linha2=True, 
local_linha2="",
cor_linha2="\x1b[38;5;247m",
estilo_linha2="\x1b[1m",
simbolos="",
simbolo_linha2="一",
quantidade_linha2=18, 

ativo_tempo=False,
tempo = 0.2,

fimcor = "\x1b[m",
colar_a_baixo="\n",
ativador=True
):
    if ativador:
        if ativo_linha1:
            print(local_linha1 + cor_linha1 + estilo_linha1 + simbolos + (simbolo_linha1 * quantidade_linha1) + simbolos + simbolos)
            
        if ativo_texto1:
            print(simbolo_texto1 + local_texto1 + cor_texto1 + fonte_estilo1 + texto1 + fimcor + texto2, end=colar_a_baixo)
            if ativo_tempo:
                sleep(tempo)
            
        if ativo_linha2:
            print(local_linha2 + cor_linha2 + estilo_linha2 + simbolos + (simbolo_linha2 * quantidade_linha2)+ simbolos + fimcor)


def carregamento(
local_texto="",
cor_texto="\x1b[38;5;232m",
cor_fundo="\x1b[48;5;166m",
fonte_estilo="\x1b[1m",
texto="Vazil!...",
simbolo_texto="",

fimcor = "\x1b[m",
tempo=0.1,
ativador=True
):
    if ativador:
        print(simbolo_texto + local_texto, end="")
        for letra in texto:
            print(f"{cor_fundo}{fonte_estilo}{cor_texto} {letra}{fimcor}", end=" ", flush=True)
            sleep(tempo)
        print()
