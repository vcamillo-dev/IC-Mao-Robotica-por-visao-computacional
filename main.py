import cv2
import mediapipe as mp
import servo_braco3d as mao

# =========================
# CÂMERA
# =========================
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    mao.board.exit()
    raise RuntimeError("Não foi possível abrir a câmera 0. Verifique a câmera e a permissão de acesso.")

cap.set(3, 640)
cap.set(4, 480)

# =========================
# MEDIAPIPE
# =========================
hands = mp.solutions.hands

Hands = hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.90,
    min_tracking_confidence=0.90
)

mpDraw = mp.solutions.drawing_utils

# ==================================================
# ESTADOS
# ==================================================
estado_polegar = None
estado_indicador = None
estado_medio = None
estado_anelar = None
estado_mindinho = None

# ==================================================
# LOOP PRINCIPAL
# ==================================================
try:
    while True:

        success, img = cap.read()

        if not success:
            continue

        # espelha imagem
        img = cv2.flip(img, 1)

        # RGB
        frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # processa mão
        results = Hands.process(frameRGB)

        handPoints = results.multi_hand_landmarks

        h, w, _ = img.shape

        pontos = []

        # ==================================================
        # MÃO DETECTADA
        # ==================================================
        if handPoints:

            for points in handPoints:

                # desenha conexões
                mpDraw.draw_landmarks(
                    img,
                    points,
                    hands.HAND_CONNECTIONS
                )

                # ==================================================
                # PEGA PONTOS
                # ==================================================
                for id, cord in enumerate(points.landmark):

                    cx = int(cord.x * w)
                    cy = int(cord.y * h)

                    pontos.append((cx, cy))

                    cv2.circle(
                        img,
                        (cx, cy),
                        4,
                        (255, 0, 0),
                        -1
                    )

                # ==================================================
                # GARANTE 21 PONTOS
                # ==================================================
                if len(pontos) >= 21:

                    # ==================================================
                    # DETECÇÃO DOS DEDOS
                    # ==================================================

                    polegar_aberto = pontos[4][0] > pontos[3][0]

                    indicador_aberto = pontos[8][1] < pontos[6][1]

                    medio_aberto = pontos[12][1] < pontos[10][1]

                    anelar_aberto = pontos[16][1] < pontos[14][1]

                    mindinho_aberto = pontos[20][1] < pontos[18][1]

                    # ==================================================
                    # POLEGAR
                    # ==================================================
                    if polegar_aberto:

                        if estado_polegar != 1:

                            # abre
                            mao.abrir_fechar(10, 1)

                            estado_polegar = 1

                    else:

                        if estado_polegar != 0:

                            # fecha
                            mao.abrir_fechar(10, 0)

                            estado_polegar = 0

                    # ==================================================
                    # INDICADOR
                    # ==================================================
                    if indicador_aberto:

                        if estado_indicador != 0:

                            # abre
                            mao.abrir_fechar(9, 0)

                            estado_indicador = 0

                    else:

                        if estado_indicador != 1:

                            # fecha
                            mao.abrir_fechar(9, 1)

                            estado_indicador = 1

                    # ==================================================
                    # MÉDIO
                    # AGORA CORRETO
                    # ==================================================
                    if medio_aberto:

                        if estado_medio != 1:

                            # abre
                            mao.abrir_fechar(8, 1)

                            estado_medio = 1

                    else:

                        if estado_medio != 0:

                            # fecha
                            mao.abrir_fechar(8, 0)

                            estado_medio = 0

                    # ==================================================
                    # ANELAR
                    # AGORA CORRETO
                    # ==================================================
                    if anelar_aberto:

                        if estado_anelar != 1:

                            # abre
                            mao.abrir_fechar(7, 1)

                            estado_anelar = 1

                    else:

                        if estado_anelar != 0:

                            # fecha
                            mao.abrir_fechar(7, 0)

                            estado_anelar = 0

                    # ==================================================
                    # MINDINHO
                    # AGORA CORRETO
                    # ==================================================
                    if mindinho_aberto:

                        if estado_mindinho != 1:

                            # abre
                            mao.abrir_fechar(6, 1)

                            estado_mindinho = 1

                    else:

                        if estado_mindinho != 0:

                            # fecha
                            mao.abrir_fechar(6, 0)

                            estado_mindinho = 0

        # ==================================================
        # MOSTRAR TELA
        # ==================================================
        cv2.imshow("Mao Robotica", img)

        # ESC fecha
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # ==================================================
    # FINALIZA
    # ==================================================
    cap.release()

    cv2.destroyAllWindows()
finally:
    cap.release()
    cv2.destroyAllWindows()
    mao.board.exit()