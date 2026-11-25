import os
from pyfirmata2 import Arduino
import time

# =========================
# PORTA
# =========================
PORTA_ARDUINO = os.environ.get('ARDUINO_PORT', '/dev/ttyUSB0')
board = Arduino(PORTA_ARDUINO)

SERVO = 4

# =========================
# PINOS
# =========================
polegar   = 10
indicador = 9
medio     = 8
anelar    = 7
mindinho  = 6

todos = [polegar, indicador, medio, anelar, mindinho]

# =========================
# CONFIGURAÇÃO
# =========================
for pino in todos:
    board.digital[pino].mode = SERVO

# ==================================================
# FUNÇÕES
# ==================================================

def parar(pino):
    board.digital[pino].write(90)

# ==================================================
# FECHAMENTO FORTE
# ==================================================

def fechar_forte(pino, invertido=False):

    for _ in range(15):

        if invertido:
            board.digital[pino].write(180)
        else:
            board.digital[pino].write(0)

        time.sleep(0.15)

# ==================================================
# ABERTURA FORTE
# ==================================================

def abrir_forte(pino, invertido=False):

    for _ in range(15):

        if invertido:
            board.digital[pino].write(0)
        else:
            board.digital[pino].write(180)

        time.sleep(0.15)

# ==================================================
# FECHAR MÃO
# ==================================================

print("Fechando mão")

# polegar e indicador invertidos
fechar_forte(polegar, invertido=True)
fechar_forte(indicador, invertido=True)

# demais dedos
fechar_forte(medio)
fechar_forte(anelar)
fechar_forte(mindinho)

# parar todos
for dedo in todos:
    parar(dedo)

time.sleep(2)

# ==================================================
# ABRIR MÃO
# ==================================================

print("Abrindo mão")

abrir_forte(polegar, invertido=True)
abrir_forte(indicador, invertido=True)

abrir_forte(medio)
abrir_forte(anelar)
abrir_forte(mindinho)

# parar todos
for dedo in todos:
    parar(dedo)

print("Fim")
