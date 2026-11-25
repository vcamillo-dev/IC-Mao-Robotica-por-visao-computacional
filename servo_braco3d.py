import os
from pyfirmata2 import Arduino
import time

# ==========================================
# ARDUINO
# ==========================================
PORTA_ARDUINO = os.environ.get('ARDUINO_PORT', '/dev/ttyUSB0')
board = Arduino(PORTA_ARDUINO)

SERVO = 4

# ==========================================
# PINOS
# ==========================================
polegar = 10
indicador = 9
medio = 8
anelar = 7
mindinho = 6

dedos = [polegar, indicador, medio, anelar, mindinho]

# ==========================================
# CONFIGURA SERVOS
# ==========================================
for pino in dedos:
    board.digital[pino].mode = SERVO

# ==========================================
# ESTADO ATUAL
# ==========================================
estado_atual = {}

# ==========================================
# VELOCIDADES CALIBRADAS
# ==========================================

# polegar e indicador
ABRIR_PI = 30
FECHAR_PI = 180

# médio, anelar e mindinho
ABRIR_MAM = 170
FECHAR_MAM = 40

# ==========================================
# FUNÇÃO PRINCIPAL
# ==========================================
def abrir_fechar(pino, fechar):

    # evita repetir comando
    if pino in estado_atual:

        if estado_atual[pino] == fechar:
            return

    estado_atual[pino] = fechar

    # ==========================================
    # POLEGAR E INDICADOR
    # ==========================================
    if pino in [polegar, indicador]:

        if fechar:

            board.digital[pino].write(FECHAR_PI)

        else:

            board.digital[pino].write(ABRIR_PI)

    # ==========================================
    # MÉDIO, ANELAR E MINDINHO
    # ==========================================
    else:

        if fechar:

            board.digital[pino].write(FECHAR_MAM)

        else:

            board.digital[pino].write(ABRIR_MAM)

    time.sleep(0.12)
