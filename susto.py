"""Pegadinha: abre sem mostrar nada e, de tempos em tempos, joga uma imagem de susto em tela cheia.

Coloque imagens (png/jpg/gif/bmp) em sustos/ e, opcionalmente, um sustos/grito.wav.
Esc fecha o app (durante um susto). Fora disso, encerre pelo Gerenciador de Tarefas.
"""
import random
import sys
import tkinter as tk
import winsound
from pathlib import Path

from PIL import Image, ImageTk

ESPERA_SEG = (60, 180)  # intervalo aleatório até cada susto
DURACAO_MS = 2500  # tempo que a imagem fica na tela

PASTA = Path(getattr(sys, "_MEIPASS", Path(__file__).parent)) / "sustos"  # _MEIPASS = rodando via PyInstaller
SOM = PASTA / "grito.wav"


EXTENSOES = (".png", ".jpg", ".jpeg", ".gif", ".bmp")


def carregar(caminho, sw, sh):
    img = Image.open(caminho)
    img.thumbnail((sw, sh))  # encaixa na tela mantendo proporção
    return ImageTk.PhotoImage(img)


def main():
    imagens = [p for p in PASTA.iterdir() if p.suffix.lower() in EXTENSOES]
    if not imagens:
        sys.exit(f"Nenhuma imagem .png/.gif em {PASTA}")

    root = tk.Tk()
    root.withdraw()
    root.configure(bg="black", cursor="none")
    root.bind("<Escape>", lambda e: root.destroy())
    tela = tk.Label(root, bg="black")
    tela.pack(expand=True, fill="both")

    def agendar():
        root.after(random.randint(*ESPERA_SEG) * 1000, assustar)

    def assustar():
        tela.image = carregar(random.choice(imagens), root.winfo_screenwidth(), root.winfo_screenheight())
        tela.configure(image=tela.image)
        root.deiconify()
        root.attributes("-fullscreen", True, "-topmost", True)
        root.focus_force()
        if SOM.exists():
            winsound.PlaySound(str(SOM), winsound.SND_FILENAME | winsound.SND_ASYNC)
        root.after(DURACAO_MS, esconder)

    def esconder():
        root.withdraw()
        agendar()

    agendar()
    root.mainloop()


if __name__ == "__main__":
    main()
