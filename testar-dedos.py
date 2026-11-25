import os
from pyfirmata2 import Arduino
import time

PORTA_ARDUINO = os.environ.get('ARDUINO_PORT', '/dev/ttyUSB0')
board = Arduino(PORTA_ARDUINO)

SERVO = 4

# =========================
# AJUSTE DOS PINOS
# =========================
# Troquei:
# polegar <-> mindinho
# indicador <-> anelar

polegar   = 10
indicador = 9
medio     = 8
anelar    = 7
mindinho  = 6

dedos = [polegar, indicador, medio, anelar, mindinho]

# =========================
# CONFIGURAÇÃO
# =========================
for pino in dedos:
    board.digital[pino].mode = SERVO

def mover(pino, angulo, tempo=0.6):

    angulo = max(20, min(160, angulo))

    board.digital[pino].write(angulo)
    time.sleep(tempo)

ABERTO = 150
FECHADO = 60

# =========================
# ABRIR MÃO
# =========================
print("Abrindo mão")

for pino in dedos:
    mover(pino, ABERTO)

time.sleep(2)

# =========================
# TESTE INDIVIDUAL
# =========================

print("Polegar")
mover(polegar, FECHADO)
mover(polegar, ABERTO)

print("Indicador")
mover(indicador, FECHADO)
mover(indicador, ABERTO)

print("Médio")
mover(medio, FECHADO)
mover(medio, ABERTO)

print("Anelar")
mover(anelar, FECHADO)
mover(anelar, ABERTO)

print("Mindinho")
mover(mindinho, FECHADO)
mover(mindinho, ABERTO)

print("Fim do teste")
