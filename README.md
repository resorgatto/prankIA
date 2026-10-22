# prankIA 🎭🤖

Kit de pegadinhas com tema de inteligência artificial. Dois componentes:

- **`susto.py`** — app que abre **invisível** e, de tempos em tempos, joga uma imagem em **tela cheia** pra dar um susto.
- **`index.html`** — uma página de notícia de um **veículo fictício** ("TecnoAlerta"), hospedada via GitHub Pages: <https://resorgatto.github.io/prankIA/>

> ⚠️ É só brincadeira. A "notícia" é ficção de um veículo inventado e o app é inofensivo (só mostra uma imagem). Use com amigos que vão rir depois. 😄

---

## 😱 O app de susto (`susto.py`)

Fica rodando em segundo plano sem mostrar nada. Depois de um tempo aleatório, aparece uma imagem da pasta `sustos/` em tela cheia, por cima de tudo, e some em seguida. Se existir um `sustos/grito.wav`, ele toca junto.

- **Esc** fecha o app (durante um susto).
- Fora de um susto, encerre pelo **Gerenciador de Tarefas** (processo `python`/`pythonw`).

### Requisitos

- Python 3.x
- Bibliotecas:
  ```bash
  pip install pillow pyinstaller
  ```

### Rodar direto (sem gerar .exe)

```bash
pythonw susto.py
```

Com `pythonw` nem a janela preta do terminal aparece.

### Gerar o executável (.exe)

Um único arquivo `.exe` que roda em qualquer Windows, **sem precisar de Python instalado**:

```bash
python -m PyInstaller --onefile --noconsole --name PegadinhaSusto --add-data "sustos;sustos" susto.py
```

O resultado fica em `dist/PegadinhaSusto.exe`. As imagens da pasta `sustos/` ficam **embutidas** no .exe.

O que cada flag faz:

| Flag | Para quê |
|------|----------|
| `--onefile` | junta tudo num único `.exe` |
| `--noconsole` | não abre janela de terminal |
| `--name PegadinhaSusto` | nome do arquivo final |
| `--add-data "sustos;sustos"` | embute a pasta de imagens |

> Trocou as imagens em `sustos/`? Gere o `.exe` de novo pra elas entrarem.

### Configuração

No topo do `susto.py`:

```python
ESPERA_SEG = (60, 180)  # intervalo aleatório (segundos) até cada susto
DURACAO_MS = 2500       # tempo que a imagem fica na tela (ms)
```

---

## 📰 A página de notícia

A página fictícia está em [`index.html`](index.html) e no ar em <https://resorgatto.github.io/prankIA/>.

É autossuficiente (imagens embutidas em base64), então funciona abrindo o arquivo direto no navegador também. Pra regenerá-la a partir das imagens em `sustos/`, use o [`gerar_noticia.py`](gerar_noticia.py):

```bash
python gerar_noticia.py
```

---

## 🖼️ Contribuindo com imagens

Quer somar sustos novos?

1. Jogue imagens (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`) na pasta `sustos/`.
2. Gere o `.exe` de novo (comando acima).
3. Pull requests com imagens são bem-vindos! 🎉
