import os
import datetime
import pytz

def limpar_tela():
    os.system("cls" if os.name == 'nt' else "clear")

def data_hora():
    fuso = pytz.timezone("America/Sao_Paulo")
    datahora = datetime.datetime.now(fuso)
    return datahora.strftime("%d/%m/%Y %H:%M:%S")
