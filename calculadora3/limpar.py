
import platform
from os import system


def limpa_tela(padrão="cls"):
    if platform.system() == "Linux":
        padrão = "clear"
    system(padrão)
