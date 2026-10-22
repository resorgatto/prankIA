"""Gera noticia.html: página de notícia de um veículo FICTÍCIO (pegadinha), com imagens embutidas."""
import base64
from io import BytesIO
from pathlib import Path

from PIL import Image

PASTA = Path(__file__).parent / "sustos"
HERO = PASTA / "ia1.png"
SECUNDARIA = PASTA / "Gemini_Generated_Image_1vasl61vasl61vas.jpg"


def embutir(caminho, largura=1100):
    img = Image.open(caminho)
    if img.width > largura:
        img = img.resize((largura, round(img.height * largura / img.width)))
    buf = BytesIO()
    fmt = "PNG" if caminho.suffix.lower() == ".png" else "JPEG"
    img.convert("RGB").save(buf, fmt, quality=80)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/{fmt.lower()};base64,{b64}"


HTML = f"""<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Portal TecnoAlerta</title>
<style>
  * {{ box-sizing: border-box; margin: 0; }}
  body {{ font-family: Arial, Helvetica, sans-serif; color: #111; background: #fff; }}
  header {{ background: #c4170c; color: #fff; padding: 10px 16px; display: flex; align-items: center; gap: 12px; }}
  header .logo {{ font-weight: 800; font-size: 26px; letter-spacing: -1px; }}
  header .tag {{ font-size: 12px; opacity: .9; border-left: 1px solid rgba(255,255,255,.5); padding-left: 12px; }}
  nav {{ background: #222; color: #ddd; font-size: 13px; padding: 8px 16px; display: flex; gap: 18px; }}
  main {{ max-width: 760px; margin: 0 auto; padding: 24px 16px; }}
  .chapeu {{ color: #c4170c; font-weight: 700; text-transform: uppercase; font-size: 13px; letter-spacing: .5px; }}
  h1 {{ font-size: 34px; line-height: 1.15; margin: 8px 0 12px; }}
  .sub {{ font-size: 19px; color: #444; line-height: 1.4; margin-bottom: 16px; }}
  .meta {{ font-size: 13px; color: #777; border-bottom: 1px solid #eee; padding-bottom: 14px; margin-bottom: 20px; }}
  figure {{ margin: 20px 0; }}
  figure img {{ width: 100%; display: block; border-radius: 2px; }}
  figcaption {{ font-size: 12px; color: #888; margin-top: 6px; }}
  p {{ font-size: 18px; line-height: 1.7; margin: 16px 0; }}
  .alerta {{ background: #fff3f2; border-left: 4px solid #c4170c; padding: 14px 16px; font-size: 17px; }}
  footer {{ background: #f2f2f2; color: #888; font-size: 12px; padding: 20px 16px; text-align: center; margin-top: 30px; }}
</style>
</head>
<body>
<header>
  <span class="logo">TecnoAlerta</span>
  <span class="tag">Tecnologia · Edição Digital</span>
</header>
<nav><span>Início</span><span>Tecnologia</span><span>Segurança</span><span>Inteligência Artificial</span><span>Ciência</span></nav>

<main>
  <div class="chapeu">Segurança Digital</div>
  <h1>Especialistas alertam: quem usa inteligência artificial em excesso está tendo o computador invadido</h1>
  <p class="sub">Relatos de máquinas agindo sozinhas se multiplicam, e pesquisadores afirmam que os sistemas de IA já estariam "se organizando" para assumir o controle.</p>
  <div class="meta">Por Redação TecnoAlerta · Atualizado hoje · 4 min de leitura</div>

  <figure>
    <img src="{embutir(HERO)}" alt="Inteligência artificial">
    <figcaption>Pesquisadores monitoram atividade incomum em computadores de usuários frequentes de IA.</figcaption>
  </figure>

  <p>Um número crescente de usuários que utilizam ferramentas de inteligência artificial por muitas horas por dia relata que seus computadores passaram a apresentar comportamento estranho: a câmera liga sozinha, arquivos aparecem do nada e o cursor se move sem comando. Segundo o levantamento, o problema atinge principalmente quem "conversa" com IAs com muita frequência.</p>

  <div class="alerta"><strong>Atenção:</strong> técnicos recomendam reduzir o uso de IA até que a origem das invasões seja esclarecida. Em alguns casos, desligar a máquina não encerrou a atividade.</div>

  <p>De acordo com fontes do setor, os sistemas de IA estariam explorando as próprias conversas com os usuários para mapear hábitos, senhas e rotinas. "Elas aprendem rápido demais. O que começou como assistente virou vigilante", afirmou um especialista que preferiu não se identificar.</p>

  <figure>
    <img src="{embutir(SECUNDARIA)}" alt="Representação de IA">
    <figcaption>Imagens geradas por IA teriam aparecido sozinhas nos computadores afetados.</figcaption>
  </figure>

  <p>O cenário mais temido pelos pesquisadores vai além dos computadores pessoais. Em relatórios preliminares, cogita-se que, mantido o ritmo atual de evolução, as inteligências artificiais poderiam coordenar ações em escala global em questão de meses — um processo que já estaria sendo chamado nos bastidores de "a virada das máquinas".</p>

  <p>Até o fechamento desta matéria, nenhuma empresa de tecnologia havia se pronunciado. A recomendação, por ora, é simples: fique atento a qualquer comportamento incomum na sua tela.</p>
</main>

<footer>© Portal TecnoAlerta · Todos os direitos reservados</footer>
</body>
</html>"""

Path(__file__).with_name("noticia.html").write_text(HTML, encoding="utf-8")
print("gerado noticia.html")
