# Mão robótica com MediaPipe e Arduino

O programa detecta uma mão pela webcam e comanda cinco servos da mão robótica através de um Arduino. O código Python roda no computador; o Arduino deve estar carregado com **StandardFirmata**.

## Requisitos

- Ubuntu/Linux ou Windows
- Python 3.10 (recomendado para as versões fixadas abaixo)
- Webcam
- Arduino ligado por USB e cinco servos conectados aos pinos digitais 6, 7, 8, 9 e 10
- Fonte adequada para os servos. Não alimente vários servos pelo pino 5 V do Arduino; use uma fonte externa dimensionada para os servos e una o GND da fonte ao GND do Arduino.

## 1. Preparar o Arduino

1. No Arduino IDE, abra **Arquivo → Exemplos → Firmata → StandardFirmata**.
2. Selecione a placa e a porta corretas e carregue o exemplo.
3. Feche o Monitor Serial e qualquer outro programa que esteja usando a porta.
4. Conecte os servos conforme a montagem e confira que a fonte externa e o Arduino compartilham o GND.

Os scripts usam os pinos 10 (polegar), 9 (indicador), 8 (médio), 7 (anelar) e 6 (mindinho). Se a fiação for diferente, altere os pinos em `servo_braco3d.py`.

## 2. Instalar as dependências

Abra o terminal na pasta deste projeto e crie um ambiente virtual:

### Linux

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Se não houver Python 3.10 instalado, instale-o pelo gerenciador de pacotes da sua distribuição ou use o `uv`:

```bash
uv python install 3.10
uv venv --python 3.10 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Descobrir a porta do Arduino

No Linux, rode `ls /dev/ttyACM* /dev/ttyUSB* 2>/dev/null`. Normalmente aparece `/dev/ttyACM0` ou `/dev/ttyUSB0`. Se o acesso for negado, adicione seu usuário ao grupo serial da distribuição (geralmente `dialout`) e entre novamente na sessão. No Windows, confira a porta COM no Gerenciador de Dispositivos.

Os programas usam `/dev/ttyACM0` por padrão no Linux. Para informar outra porta:

```bash
ARDUINO_PORT=/dev/ttyUSB0 python main.py
```

No PowerShell:

```powershell
$env:ARDUINO_PORT = 'COM3'
python main.py
```

Troque o exemplo pela porta que apareceu no seu computador.

## 4. Executar

Com o ambiente virtual ativado, StandardFirmata carregado e a mão ligada:

```bash
python main.py
```

A janela **Mao Robotica** mostra o vídeo e os pontos detectados. Coloque uma mão no campo de visão. Pressione **Esc** para sair. Se houver mais de uma câmera, altere `cv2.VideoCapture(0)` em `main.py` para o índice correto (por exemplo, `1`).

## Teste e calibração

Primeiro teste sem forçar os dedos contra os limites mecânicos. `testar-dedos.py` movimenta cada servo entre ângulos fixos; ajuste os limites para a sua montagem antes de executar. `calibrar-dedos.py` usa os extremos 0° e 180° por vários segundos e pode danificar os servos ou a estrutura se a montagem travar. Use-o apenas depois de verificar mecanicamente os limites e reduza os ângulos/tempo se necessário.

## Solução de problemas

- **Erro ao abrir a porta:** confirme a porta, feche o Monitor Serial e tente novamente; no Linux, confira as permissões do dispositivo serial.
- **Câmera não abre:** permita o acesso à webcam, feche outros aplicativos que a usam e tente outro índice em `VideoCapture`.
- **Servos tremem ou Arduino reinicia:** use fonte externa apropriada para os servos e conecte os terras (GND) em comum.
- **Dedos se movem invertidos ou até o limite:** desligue a alimentação dos servos e ajuste pinos, direção e ângulos em `servo_braco3d.py` antes de tentar novamente.
