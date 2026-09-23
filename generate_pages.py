"""Generate the static editorial pages for the Luiz Arcanjo site.

Run with: python3 generate_pages.py
The source material and product decisions are tracked in PROJECT_PLAN.md.
"""

from html import escape
from pathlib import Path
from music_catalog import platform_bar as music_platform_bar, selection as music_selection

ROOT = Path(__file__).resolve().parent
NOINDEX_UNTIL_CONTENT = {"cursos", "conteudos"}


def hero(kicker, title, description, image, alt, variant="", video=""):
    variant_class = f" inner-hero--{variant}" if variant else ""
    if video:
        media = f'''<div class="inner-hero__media inner-hero__video-wrap"><video class="inner-hero__video" autoplay muted loop playsinline preload="metadata" poster="/assets/images/{image}" aria-hidden="true"><source src="/assets/video/{video}" type="video/mp4"></video></div>'''
    else:
        media = f'''<div class="inner-hero__media photo inner-hero__photo"><img src="/assets/images/{image}" alt="{escape(alt)}" fetchpriority="high"></div>'''
    return f"""
    <section class="inner-hero{variant_class}">
      {media}
      <div class="inner-hero__shade"></div>
      <div class="shell inner-hero__content">
        <h1>{title}</h1><p>{description}</p>
      </div>
    </section>"""


def page(slug, title, description, content):
    robots_meta = '<meta name="robots" content="noindex,follow">' if slug in NOINDEX_UNTIL_CONTENT else ''
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#202D3A">
  <meta name="description" content="{escape(description, quote=True)}">
  {robots_meta}
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="Luiz Arcanjo">
  <meta property="og:title" content="{escape(title, quote=True)} | Luiz Arcanjo">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:image" content="https://luizarcanjo.com/assets/images/open-graph-v3.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Luiz Arcanjo — Canções que atravessam gerações">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://luizarcanjo.com/assets/images/open-graph-v3.png">
  <title>{escape(title)} | Luiz Arcanjo</title>
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/assets/favicon-512.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/site.css?v=60">
  <script defer src="/assets/site.js?v=24"></script>
</head>
<body id="topo" data-page="{slug}">
  <div id="site-header"></div>
  <main id="conteudo">{content}</main>
  <div id="site-footer"></div>
</body>
</html>"""
    target = ROOT / slug / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(target.relative_to(ROOT))


def redirect(slug, destination):
    target = ROOT / slug / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><link rel="canonical" href="{destination}"><meta http-equiv="refresh" content="0;url={destination}"><title>Redirecionando | Luiz Arcanjo</title></head><body><p>Esta página agora está em <a href="{destination}">{destination}</a>.</p></body></html>''', encoding="utf-8")
    print(target.relative_to(ROOT))


page(
    "historia",
    "História",
    "A trajetória de Luiz Arcanjo na música cristã brasileira, da formação musical à carreira solo e ao ministério pastoral.",
    hero("História", "Uma vida<br>em <em>canções.</em>", "Uma trajetória construída entre a música, a fé e as pessoas encontradas pelo caminho.", "history-hero-stage.jpg", "Luiz Arcanjo no palco, com violão e braços abertos sob luzes azuis", variant="history")
    + """
    <section class="section-pad section--ivory"><div class="shell biography-grid">
      <div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>As primeiras notas</p><h2 class="display-title">A música nasceu <em>em comunidade.</em></h2></div>
      <div class="prose" data-reveal><p>Luiz Arcanjo cresceu em Nova Iguaçu, na Baixada Fluminense. Sua formação musical começou na igreja, onde aprendeu a ler partituras. Tocou clarinete e, ainda jovem, encontrou no violão um instrumento para desenvolver sua expressão como músico e compositor.</p><p>O começo dessa história ajuda a entender sua obra: a música nunca esteve distante da fé e da vida com outras pessoas.</p></div>
    </div></section>
    <section class="history-family" aria-label="Momentos da família de Luiz Arcanjo"><div class="history-family__slideshow family-slideshow" data-family-slideshow>
      <figure class="family-slideshow__slide is-active"><img src="/assets/images/history-family-1017.jpeg" alt="Luiz Arcanjo com Ângela Aló e os filhos reunidos em casa" loading="lazy"></figure>
      <figure class="family-slideshow__slide"><img src="/assets/images/history-family-1057.jpeg" alt="Retrato descontraído da família de Luiz Arcanjo" loading="lazy"></figure>
      <figure class="family-slideshow__slide"><img src="/assets/images/history-family-1022.jpeg" alt="Luiz Arcanjo, Ângela Aló e os filhos no sofá" loading="lazy"></figure>
      <div class="history-family__caption shell"><span>Uma história vivida em família</span><div class="family-slideshow__progress" aria-hidden="true"><span></span><span></span><span></span></div></div>
    </div></section>
    <section class="section-pad"><div class="shell biography-grid">
      <div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Uma voz coletiva</p><h2 class="display-title">Canções que se tornaram <em>memória.</em></h2></div>
      <div class="prose" data-reveal><p>A partir de 2002, Luiz integrou a formação do Toque no Altar e construiu, ao lado de outros músicos, uma trajetória marcante para a música cristã brasileira. Mais tarde, tornou-se um dos fundadores e vocalistas do Trazendo a Arca.</p><p>Como compositor, participou de canções interpretadas pelo grupo e por artistas como Aline Barros, Fernanda Brum e Kleber Lucas. Sua caminhada solo abriu espaço para outras sonoridades, incluindo influências da música popular brasileira.</p><div class="biography-actions"><button class="text-link biography-open" type="button" data-biography-open>Leia a biografia completa <span aria-hidden="true">↗</span></button><a class="text-link" href="/musica/">Conheça a música <span aria-hidden="true">↗</span></a></div></div>
    </div></section>
    <section class="biography-portrait section-pad section--blue"><div class="shell biography-portrait__grid">
      <div class="biography-portrait__visual photo"><img src="/assets/images/history-solo-1221.jpeg" alt="Retrato editorial de Luiz Arcanjo sentado" loading="lazy"></div>
      <div class="biography-portrait__copy" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Além do palco</p><h2>Arte, palavra<br>e <em>serviço.</em></h2><p>Além da música, Luiz é autor de <cite>Por Detrás da Canção</cite> e compartilha sua experiência em iniciativas de ensino. Desde 2017, atua no pastoreio da Sobre as Águas Church, em Nova Iguaçu.</p><p>Essas frentes compõem uma vida dedicada a criar, cuidar e servir.</p><a class="button button--outline" href="/igreja/"><span>Sua atuação pastoral</span><span aria-hidden="true">↗</span></a></div>
    </div></section>
    <dialog class="biography-dialog" data-biography-dialog aria-labelledby="biography-dialog-title">
      <div class="biography-dialog__frame">
        <header class="biography-dialog__header"><span>Luiz Arcanjo · Biografia</span><button type="button" data-biography-close aria-label="Fechar biografia"><span aria-hidden="true">Fechar</span><b aria-hidden="true">×</b></button></header>
        <div class="biography-dialog__scroll">
          <div class="biography-dialog__intro">
            <p class="eyebrow"><span class="eyebrow__rule"></span>Uma vida entre canções e pessoas</p>
            <h2 id="biography-dialog-title">Antes da voz conhecida,<br>há uma história <em>vivida.</em></h2>
            <p class="biography-dialog__lead">Luiz Arcanjo construiu uma trajetória pública de mais de três décadas. Por trás dos palcos, das composições e do ministério, existe uma caminhada formada pela família, pela igreja e pelos encontros que deram sentido à sua música.</p>
          </div>
          <article class="biography-dialog__story">
            <p class="biography-dialog__opening">Luiz Carlos da Silva nasceu em 11 de julho de 1974, em Nova Iguaçu, e cresceu em uma família humilde da Baixada Fluminense. Foi dentro da igreja que a música deixou de ser apenas som e começou a se tornar linguagem. Ali, aprendeu a ler partituras, iniciou no clarinete e, aos 12 anos, encontrou no violão uma nova maneira de expressar o que carregava. Mais tarde, também se desenvolveria na guitarra.</p>
            <p>Essa origem ajuda a compreender sua obra. Para Luiz, música, fé e vida em comunidade nunca caminharam separadas. Antes dos grandes públicos, vieram o aprendizado, o serviço e a convivência com pessoas. Foi desse lugar que nasceu uma trajetória capaz de unir excelência musical, sensibilidade e propósito.</p>
            <p>Ao lado de sua esposa, Ângela Aló, Luiz construiu a família que também sustenta sua caminhada longe dos palcos. O casal é pai de Samuel Arcanjo e Ariel Arcanjo. Entre compromissos, viagens, canções e responsabilidades ministeriais, é na vida compartilhada que sua história encontra uma dimensão mais íntima e cotidiana. Essa presença familiar revela o homem por trás da voz: alguém cuja caminhada também é feita de afeto, permanência e vínculos.</p>
            <p>A partir de 2002, Luiz tornou-se líder e um dos vocalistas da formação original do Toque no Altar. Ao lado de Davi Sacer, participou de uma das parcerias mais reconhecidas da música cristã brasileira. Depois, esteve entre os fundadores do Trazendo a Arca e, a partir de 2010, assumiu a voz principal da banda.</p>
            <p>Projetos como <cite>Marca da Promessa</cite>, <cite>Ao Vivo no Japão</cite> e <cite>Ao Vivo no Maracanãzinho</cite> fazem parte dessa história. Como compositor, Luiz teve canções gravadas por nomes como Aline Barros, Fernanda Brum, Kleber Lucas, Soraya Moraes, Ton Carfi e Carlinhos Felix. Em sua carreira solo, ampliou a própria linguagem musical e aproximou sua obra de referências brasileiras, incluindo a MPB.</p>
            <p>Com o livro <cite>Por Detrás da Canção</cite>, Luiz abriu os bastidores espirituais e criativos de composições nascidas em parceria com músicos como Davi Sacer, Ronald Fonseca, Deco Rodrigues, David Cerqueira e Marcell Compan. O livro reúne memória, testemunho e os processos que deram origem a canções ouvidas no Brasil e em outros países.</p>
            <p>Essa experiência também é compartilhada em workshops de música, adoração e composição. Desde 2017, Luiz atua como pastor sênior da Sobre as Águas Church, em Nova Iguaçu. É ainda fundador e presidente do Instituto Luiz Arcanjo. No palco, na escrita, no ensino ou no pastoreio, o fio condutor permanece o mesmo: usar a arte e a experiência para servir pessoas.</p>
          </article>
          <footer class="biography-dialog__footer"><p>Uma vida dedicada a criar, cuidar e servir.</p><a class="button button--dark" href="/musica/"><span>Conhecer a música</span><span aria-hidden="true">↗</span></a></footer>
        </div>
      </div>
    </dialog>
    <section class="section-pad"><div class="shell centered-cta" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Continue a explorar</p><h2 class="display-title">A história segue <em>em movimento.</em></h2><div class="button-row"><a class="button button--dark" href="/musica/"><span>Ouvir música</span><span aria-hidden="true">↗</span></a><a class="button button--outline-dark" href="/livro/"><span>Conhecer o livro</span><span aria-hidden="true">↗</span></a></div></div></section>"""
)

page(
    "musica",
    "Música",
    "Ouça Luiz Arcanjo em sua carreira solo e com o Trazendo a Arca. Descubra lançamentos e canais oficiais.",
    hero("Música", "Do altar <span class=\"nowrap\">aos grandes</span> palcos.<br><em>Uma obra <span class=\"nowrap\">que atravessa</span> gerações.</em>", "Compositor de canções que se tornaram memória coletiva, Luiz Arcanjo construiu uma trajetória entre o Toque no Altar, o Trazendo a Arca e uma carreira solo marcada por fé, poesia e serviço.", "music-hero-cropped.jpg", "Auditório cheio durante apresentação de Luiz Arcanjo", variant="music", video="music-hero-web.m4v")
    + music_platform_bar()
    + """
    <section class="section-pad section--ivory"><div class="shell music-intro">
      <div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Duas frentes, uma trajetória</p><h2 class="display-title">A voz de Luiz.<br>O som de uma <em>geração.</em></h2></div>
      <div class="prose" data-reveal><p>Conheça a carreira solo de Luiz Arcanjo e sua história com o Trazendo a Arca. Os catálogos têm identidades e créditos próprios; aqui, cada um encontra seu espaço.</p><p>As plataformas oficiais reúnem os lançamentos disponíveis e permitem ouvir diretamente no serviço de sua preferência.</p></div>
    </div></section>
    <section class="music-panel music-panel--solo"><div class="music-panel__image photo"><img src="/assets/images/music-solo-cutout.png" alt="Luiz Arcanjo segurando o violão, em retrato sem fundo" loading="lazy"></div><div class="music-panel__body" data-reveal><span class="music-panel__number">01 / Carreira solo</span><h2>Luiz <em>Arcanjo.</em></h2><p>Uma voz própria, aberta a diferentes sonoridades e à força da composição.</p><div class="music-panel__releases"><span>Para começar a ouvir</span><ul><li>Luiz Arcanjo · álbum</li><li>Rei das Nações · single</li><li>Me Apaixona (Ao Vivo) · single</li></ul></div><a class="button button--gold" href="https://open.spotify.com/artist/3jhaArlXRtYY9R7GJrvcZ2" target="_blank" rel="noopener"><span>Ouvir no Spotify</span><span aria-hidden="true">↗</span></a></div></section>
    <section class="music-panel music-panel--reverse"><div class="music-panel__image photo"><img src="/assets/images/live-crowd.jpg" alt="Público em apresentação musical" loading="lazy"></div><div class="music-panel__body" data-reveal><img class="music-panel__band-logo" src="/assets/images/trazendo-a-arca-logo.png?v=3" alt="Trazendo a Arca"><span class="music-panel__number">02 / Banda</span><h2>Trazendo<br><em>a Arca.</em></h2><p>Uma história coletiva que levou canções de adoração a tantos lugares e continua presente na memória da música cristã.</p><div class="music-panel__releases"><span>Projetos para revisitar</span><ul><li>Marca da Promessa</li><li>Ao Vivo no Japão</li><li>Trazendo a Arca (Ao Vivo em São Paulo)</li></ul></div><a class="button button--gold" href="https://open.spotify.com/artist/1KJkhqZNLx1JY9vXkBhGV5" target="_blank" rel="noopener"><span>Ouvir a banda</span><span aria-hidden="true">↗</span></a></div></section>
    """ + music_selection() + """
    <section class="section-pad section--ivory"><div class="shell listen-section"><div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Ouça agora</p><h2 class="display-title">A música no seu <em>tempo.</em></h2><p>Abra o perfil oficial ou reproduza uma seleção diretamente aqui.</p></div><div class="listen-section__links"><a href="https://open.spotify.com/artist/3jhaArlXRtYY9R7GJrvcZ2" target="_blank" rel="noopener">Luiz Arcanjo no Spotify <span>↗</span></a><a href="https://open.spotify.com/artist/1KJkhqZNLx1JY9vXkBhGV5" target="_blank" rel="noopener">Trazendo a Arca no Spotify <span>↗</span></a><a href="https://www.youtube.com/luizarcanjo" target="_blank" rel="noopener">Luiz Arcanjo no YouTube <span>↗</span></a></div></div><div class="shell"><iframe class="spotify-player" title="Player oficial do Spotify — Luiz Arcanjo" src="https://open.spotify.com/embed/artist/3jhaArlXRtYY9R7GJrvcZ2?utm_source=generator&amp;theme=0&amp;si=9d84d27370e74b4a" width="100%" height="352" loading="lazy" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe></div></section>"""
)

page(
    "cursos",
    "Academy",
    "Cursos, workshops e mentorias de Luiz Arcanjo para músicos, compositores e líderes.",
    hero("Academy", "Três décadas de&nbsp;estrada.<br><em>Conhecimento para quem quer avançar.</em>", "Formação prática em música, composição, liderança e propósito, conduzida por quem vive esses caminhos dentro e fora do palco.", "academy-hero.jpg", "Luiz Arcanjo no palco, diante do público", variant="academy")
    + """
    <section class="section-pad section--ivory" id="cursos"><div class="shell learning-intro"><div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Luiz Arcanjo Academy</p><h2 class="display-title">Experiência transformada em <em>direção prática.</em></h2></div><div class="prose" data-reveal><p>Palco, estúdio, composição, liderança e ministério formaram um repertório de mais de 30 anos. A Academy organiza esse conhecimento para músicos, compositores e líderes que desejam desenvolver técnica, identidade e clareza.</p><p>Cada formação nasce de situações reais e conecta fundamento, prática e acompanhamento.</p></div></div></section>
    <section class="learning-paths section-pad"><div class="shell learning-paths__grid">
      <article class="learning-card" data-reveal><span>01 / Cursos e workshops</span><h2>Conteúdo para transformar <em>prática em repertório.</em></h2><p>Formações sobre música, composição, adoração e os aprendizados reunidos ao longo da trajetória de Luiz Arcanjo.</p><ul><li>Conteúdo estruturado</li><li>Experiência aplicada</li><li>Formatos presenciais e digitais</li></ul><a class="text-link" href="/contato/?assunto=cursos#mensagem">Registrar interesse <span aria-hidden="true">↗</span></a></article>
      <article class="learning-card learning-card--blue" id="mentoria" data-reveal><span>02 / Mentoria</span><h2>Experiência que encontra <em>propósito.</em></h2><p>Conversas orientadas para artistas, líderes e pessoas que desejam clareza para avançar em sua caminhada.</p><ul><li>Escuta e direcionamento</li><li>Planos individuais ou em grupo</li><li>Conexão entre vocação e ação</li></ul><a class="text-link" href="/contato/?assunto=mentoria#mensagem">Falar sobre mentoria <span aria-hidden="true">↗</span></a></article>
    </div></section>
    <section class="academy-next section-pad section--blue"><div class="shell academy-next__grid"><div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Seu próximo passo</p><h2 class="display-title">Escolha a experiência que responde ao seu <em>momento.</em></h2><p class="lead-serif">Conte à equipe o que você deseja desenvolver. A resposta indicará o formato, a disponibilidade e o caminho mais adequado.</p></div><div class="academy-next__paths" data-reveal><a href="/contato/?assunto=cursos#mensagem"><span>01 / Cursos e workshops</span><strong>Quero desenvolver técnica e repertório.</strong><b aria-hidden="true">↗</b></a><a href="/contato/?assunto=mentoria#mensagem"><span>02 / Mentoria</span><strong>Quero direção para uma decisão ou projeto.</strong><b aria-hidden="true">↗</b></a></div></div></section>"""
)

redirect("mentoria", "/cursos/#mentoria")

page(
    "livro",
    "Loja",
    "Por Detrás da Canção, de Luiz Arcanjo: histórias inéditas, memórias e bastidores das canções que atravessaram gerações.",
    """<section class="book-sales-hero">
      <div class="book-sales-hero__media"><img src="/assets/images/book-hero-reading.jpg" alt="Luiz Arcanjo lendo o livro Por Detrás da Canção" fetchpriority="high"></div>
      <div class="book-sales-hero__shade"></div>
      <div class="shell book-sales-hero__content" data-reveal>
        <p class="eyebrow"><span class="eyebrow__rule"></span>Por Detrás da Canção · Luiz Arcanjo</p>
        <h1>As canções que você conhece.<br><em>As histórias que nunca ouviu.</em></h1>
        <p>Relatos inéditos sobre a fé, os encontros e os bastidores criativos de músicas que atravessaram igrejas, cidades e gerações.</p>
        <a class="button button--dark" href="https://drafteditora.com.br/produtos/por-detras-da-cancao-luiz-arcanjo-70t8l/" target="_blank" rel="noopener"><span>Adquira o teu</span><span aria-hidden="true">↗</span></a>
      </div>
    </section>
    <section class="book-promise section-pad section--ivory" id="livro"><div class="shell book-promise__grid">
      <div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>O que existe antes do refrão</p><h2 class="display-title">Quando uma canção nasce,<br>uma história começa a <em>ecoar.</em></h2></div>
      <div class="book-promise__copy" data-reveal><p class="lead-serif">Há músicas que não terminam quando o último acorde se cala. Elas permanecem porque encontraram pessoas em momentos decisivos.</p><p><cite>Por Detrás da Canção</cite> abre, pela primeira vez, os bastidores espirituais e criativos de composições que se tornaram parte da identidade musical das igrejas evangélicas no Brasil.</p><p>Luiz Arcanjo revisita experiências, testemunhos e parcerias com Davi Sacer, Ronald Fonseca, Deco Rodrigues, David Cerqueira e Marcell Compan para revelar o caminho entre a inspiração e a canção que chegou ao público.</p></div>
    </div></section>
    <section class="book-inside section-pad"><div class="shell book-inside__grid">
      <div class="book-inside__visual photo" data-reveal><img src="/assets/images/book-editorial-new.png" alt="Composição editorial com o livro Por Detrás da Canção aberto e fechado" loading="lazy"></div>
      <div class="book-inside__copy" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Dentro da obra</p><h2>Memória, música<br>e <em>testemunho.</em></h2><p>Mais que um registro musical, o livro aproxima o leitor do propósito e das experiências que deram origem a canções ouvidas no Brasil e no mundo.</p><ul class="book-inside__list"><li><span>01</span>Histórias e bastidores jamais revelados ao público</li><li><span>02</span>Letras das canções apresentadas ao longo da narrativa</li><li><span>03</span>Relatos de fé em formato de memórias</li><li><span>04</span>Palheta assinada e marcador de página</li></ul><a class="button button--dark" href="https://drafteditora.com.br/produtos/por-detras-da-cancao-luiz-arcanjo-70t8l/" target="_blank" rel="noopener"><span>Entre nos bastidores das canções</span><span aria-hidden="true">↗</span></a></div>
    </div></section>
    <section class="book-signature section-pad section--blue"><div class="shell book-signature__grid">
      <div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Da voz para a página</p><h2 class="display-title">Três décadas de música,<br>agora contadas por quem as <em>viveu.</em></h2></div>
      <div class="book-signature__copy" data-reveal><p>Luiz Arcanjo cresceu na Baixada Fluminense, iniciou sua formação musical dentro da igreja e se tornou cantor, compositor, multi-instrumentista e pastor. Sua trajetória com o Toque no Altar, o Trazendo a Arca e a carreira solo atravessa mais de 30 anos.</p><p>Nestas páginas, a experiência do artista encontra a memória do homem que viu canções como “Marca da Promessa”, “Restitui”, “Olha para Mim” e “Deus de Promessas” ganharem a voz de milhares de pessoas.</p></div>
    </div></section>
    <section class="book-final section-pad"><div class="shell book-final__grid">
      <div class="book-final__cover photo" data-reveal><img src="/assets/images/book-final-editorial.jpg" alt="Livro Por Detrás da Canção em composição editorial" loading="lazy"></div>
      <div class="book-final__copy" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Uma história para guardar</p><h2 class="display-title">Leve para perto as histórias que já fazem parte da sua <em>vida.</em></h2><p class="lead-serif">Uma leitura para quem cantou, foi tocado e deseja conhecer o que Deus fez antes de cada canção chegar ao altar.</p><dl class="book-meta"><div><dt>Categoria</dt><dd>Biografia · Música · Memórias</dd></div><div><dt>Formato</dt><dd>Físico · 128 páginas</dd></div><div><dt>Dimensões</dt><dd>21 × 14 × 1 cm</dd></div><div><dt>ISBN</dt><dd>9786583297167</dd></div></dl><a class="button button--dark" href="https://drafteditora.com.br/produtos/por-detras-da-cancao-luiz-arcanjo-70t8l/" target="_blank" rel="noopener"><span>Leve esta história com você</span><span aria-hidden="true">↗</span></a><small class="external-note">Compra realizada no ambiente seguro da Draft Editora.</small></div>
    </div></section>"""
)

redirect("produtos", "/livro/#produtos")

page(
    "conteudos",
    "Devocionais",
    "Devocionais, mensagens e vídeos de Luiz Arcanjo para acompanhar a fé, a música e a vida cotidiana.",
    hero("Devocionais", "Palavras para continuar a <em>caminhada.</em>", "Mensagens, reflexões e conversas para viver a fé com profundidade no cotidiano.", "portrait-olive.jpg", "Luiz Arcanjo com violão", variant="light")
    + """
    <section class="devotional-intro section-pad section--ivory"><div class="shell devotional-intro__grid">
      <div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Devocionais</p><h2 class="display-title">Conteúdo para ouvir com calma e levar para a <em>vida.</em></h2></div>
      <div class="devotional-intro__copy" data-reveal><p class="lead-serif">Um espaço editorial para mensagens, reflexões e encontros que continuam depois do palco.</p><p>Os vídeos abaixo reúnem ministrações e conversas de Luiz Arcanjo publicadas por igrejas e canais parceiros.</p></div>
    </div></section>
    <section class="devotional-videos section-pad"><div class="shell">
      <div class="section-head devotional-section-head" data-reveal><div><p class="eyebrow"><span class="eyebrow__rule"></span>Assista</p><h2 class="display-title">Mensagens em <em>vídeo.</em></h2></div><p>Cinco encontros para escolher pelo tema e assistir no seu tempo.</p></div>
      <article class="video-post video-post--featured" data-reveal>
        <a class="video-post__media" href="https://www.youtube.com/watch?v=HMkFJUzOcDk" target="_blank" rel="noopener"><img src="/assets/images/devotional-HMkFJUzOcDk.jpg" alt="Maturidade — mensagem de Luiz Arcanjo" loading="lazy"><span class="video-post__play" aria-hidden="true">▶</span><span class="video-post__duration">Mensagem</span></a>
        <div class="video-post__body"><p class="video-post__meta">Mensagem · Quadrangular Búzios</p><h3>Maturidade</h3><p>Uma palavra do Pr. Luiz Arcanjo sobre crescimento, escolhas e a fé que aprende a permanecer.</p><div class="post-actions"><button type="button" data-post-like="video-HMkFJUzOcDk" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="Maturidade — Pr. Luiz Arcanjo" data-share-url="https://www.youtube.com/watch?v=HMkFJUzOcDk"><span aria-hidden="true">↗</span> Compartilhar</button></div></div>
      </article>
      <div class="video-post-grid">
        <article class="video-post" data-reveal><a class="video-post__media" href="https://www.youtube.com/watch?v=dsNY0KoGTM8" target="_blank" rel="noopener"><img src="/assets/images/devotional-dsNY0KoGTM8.jpg" alt="Culto da Resposta com Luiz Arcanjo" loading="lazy"><span class="video-post__play" aria-hidden="true">▶</span></a><div class="video-post__body"><p class="video-post__meta">Mensagem · Atitude TV</p><h3>Culto da Resposta</h3><div class="post-actions"><button type="button" data-post-like="video-dsNY0KoGTM8" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="Culto da Resposta — Luiz Arcanjo" data-share-url="https://www.youtube.com/watch?v=dsNY0KoGTM8"><span aria-hidden="true">↗</span> Compartilhar</button></div></div></article>
        <article class="video-post" data-reveal><a class="video-post__media" href="https://www.youtube.com/watch?v=jFT6qQmJJP4" target="_blank" rel="noopener"><img src="/assets/images/devotional-jFT6qQmJJP4.jpg" alt="Nada lhe será impossível segundo a sua fé — mensagem de Luiz Arcanjo" loading="lazy"><span class="video-post__play" aria-hidden="true">▶</span></a><div class="video-post__body"><p class="video-post__meta">Mensagem · IPAN</p><h3>Nada lhe será impossível segundo a sua fé</h3><div class="post-actions"><button type="button" data-post-like="video-jFT6qQmJJP4" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="Nada lhe será impossível segundo a sua fé — Pr. Luiz Arcanjo" data-share-url="https://www.youtube.com/watch?v=jFT6qQmJJP4"><span aria-hidden="true">↗</span> Compartilhar</button></div></div></article>
        <article class="video-post" data-reveal><a class="video-post__media" href="https://www.youtube.com/watch?v=GJohQvwXXDA" target="_blank" rel="noopener"><img src="/assets/images/devotional-GJohQvwXXDA.jpg" alt="Fazendo as escolhas certas — mensagem de Luiz Arcanjo" loading="lazy"><span class="video-post__play" aria-hidden="true">▶</span></a><div class="video-post__body"><p class="video-post__meta">Mensagem · Mais de Cristo TV</p><h3>Fazendo as escolhas certas</h3><div class="post-actions"><button type="button" data-post-like="video-GJohQvwXXDA" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="Fazendo as escolhas certas — Luiz Arcanjo" data-share-url="https://www.youtube.com/watch?v=GJohQvwXXDA"><span aria-hidden="true">↗</span> Compartilhar</button></div></div></article>
        <article class="video-post" data-reveal><a class="video-post__media" href="https://www.youtube.com/watch?v=rpTqfnBNfsI" target="_blank" rel="noopener"><img src="/assets/images/devotional-rpTqfnBNfsI.jpg" alt="Luiz Arcanjo fala sobre unção, secreto e responsabilidade" loading="lazy"><span class="video-post__play" aria-hidden="true">▶</span></a><div class="video-post__body"><p class="video-post__meta">Conversa · Vânia Franco</p><h3>O peso da unção, do secreto e da responsabilidade</h3><div class="post-actions"><button type="button" data-post-like="video-rpTqfnBNfsI" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="Luiz Arcanjo explica o peso da unção, do secreto e da responsabilidade" data-share-url="https://www.youtube.com/watch?v=rpTqfnBNfsI"><span aria-hidden="true">↗</span> Compartilhar</button></div></div></article>
      </div>
    </div></section>
    <section class="devotional-articles section-pad section--blue"><div class="shell">
      <div class="section-head devotional-section-head" data-reveal><div><p class="eyebrow"><span class="eyebrow__rule"></span>Leia</p><h2 class="display-title">Três novas leituras,<br>em preparação <em>editorial.</em></h2></div><p>O espaço já está estruturado para receber os primeiros artigos autorais.</p></div>
      <div class="article-preview-grid">
        <article class="article-preview" id="artigo-1" data-reveal><div class="article-preview__image photo"><img src="/assets/images/speaker.jpg" alt="Luiz Arcanjo ministrando" loading="lazy"></div><div class="article-preview__body"><span>01 · Fé no cotidiano</span><h3>A fé que continua depois do culto</h3><p>Artigo em edição.</p><div class="post-actions"><button type="button" data-post-like="article-1" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="A fé que continua depois do culto" data-share-url="/conteudos/#artigo-1"><span aria-hidden="true">↗</span> Compartilhar</button></div></div></article>
        <article class="article-preview" id="artigo-2" data-reveal><div class="article-preview__image photo"><img src="/assets/images/portrait-guitar.jpg" alt="Luiz Arcanjo com violão" loading="lazy"></div><div class="article-preview__body"><span>02 · Música e memória</span><h3>O que uma canção guarda além da letra</h3><p>Artigo em edição.</p><div class="post-actions"><button type="button" data-post-like="article-2" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="O que uma canção guarda além da letra" data-share-url="/conteudos/#artigo-2"><span aria-hidden="true">↗</span> Compartilhar</button></div></div></article>
        <article class="article-preview" id="artigo-3" data-reveal><div class="article-preview__image photo"><img src="/assets/images/history-solo-1221.jpeg" alt="Retrato editorial de Luiz Arcanjo" loading="lazy"></div><div class="article-preview__body"><span>03 · Liderança e serviço</span><h3>Servir também é aprender a permanecer</h3><p>Artigo em edição.</p><div class="post-actions"><button type="button" data-post-like="article-3" aria-pressed="false"><span aria-hidden="true">♡</span> Curtir</button><button type="button" data-post-share data-share-title="Servir também é aprender a permanecer" data-share-url="/conteudos/#artigo-3"><span aria-hidden="true">↗</span> Compartilhar</button></div></div></article>
      </div>
    </div></section>"""
)

page(
    "igreja",
    "Sobre as Águas Church",
    "Conheça a Sobre as Águas Church, comunidade pastoreada por Luiz Arcanjo em Nova Iguaçu, com horários e endereço para sua visita.",
    """<section class="inner-hero inner-hero--church">
      <div class="inner-hero__media photo inner-hero__photo"><img src="/assets/images/church-auditorium.jpg" alt="Congregação reunida no auditório da Sobre as Águas Church" fetchpriority="high"></div>
      <div class="inner-hero__shade"></div>
      <div class="shell inner-hero__content">
        <img class="church-hero__mark" src="/assets/images/sobre-as-aguas-mark.png?v=4" alt="Sobre as Águas Church">
        <h1>Sobre as Águas <em>Church</em></h1>
        <p>Em Nova Iguaçu, pessoas se reúnem para adorar, crescer na Palavra e caminhar juntas.</p>
        <a class="button button--outline" href="#conheca"><span>Conheça essa história</span><span aria-hidden="true">↓</span></a>
      </div>
    </section>
    <section class="church-story section-pad" id="conheca"><div class="shell church-story__grid">
      <div class="church-story__copy" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Desde 2017 · Nova Iguaçu</p><h2 class="display-title">De um chamado nasceu uma <em>comunidade.</em></h2><p class="lead-serif">Luiz Arcanjo voltou à cidade onde cresceu para iniciar encontros de adoração. Ao lado de Ângela Aló, hoje pastoreia uma casa construída pela fé e pelo cuidado com pessoas.</p><p>A caminhada começou no auditório de um hotel, passou por encontros sob uma lona e ganhou um templo próprio. Depois de uma ventania derrubar a estrutura maior em 2023, a comunidade permaneceu unida e reconstruiu o espaço em 2024.</p><p>Essa história continua em cada família acolhida, em cada encontro e em cada vida tocada pela Palavra.</p></div>
      <div class="church-story__photo photo" data-reveal><img src="/assets/images/church-luiz.jpg" alt="Pastor Luiz Arcanjo ministrando na Sobre as Águas Church" loading="lazy"></div>
    </div></section>
    <section class="church-panorama"><div class="church-panorama__photo photo"><img src="/assets/images/church-gathering.jpg" alt="Auditório da Sobre as Águas Church com a comunidade reunida" loading="lazy"></div><div class="shell church-panorama__caption" data-reveal><span>Uma comunidade em movimento</span><p>Há histórias que só acontecem quando caminhamos <em>juntos.</em></p></div></section>
    <section class="church-visit section-pad"><div class="shell church-visit__grid">
      <div class="church-visit__photo photo" data-reveal><img src="/assets/images/church-worship.jpg" alt="Pessoas em momento de adoração na Sobre as Águas Church" loading="lazy"></div>
      <div class="church-visit__copy" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Venha nos visitar</p><h2 class="display-title">Há lugar para <em>você.</em></h2><p>Uma comunidade cristocêntrica reunida para adorar, aprender e servir. Você é bem-vindo para compartilhar esse caminho.</p><dl class="church-visit__details"><div><dt>Encontros</dt><dd>Quarta-feira, 20h<br>Domingo, 18h</dd></div><div><dt>Endereço</dt><dd>Rua Professor Joaquim Cardoso de Matos, 499<br>Bairro da Luz · Nova Iguaçu, RJ</dd></div></dl><p class="church-visit__note">Estacionamento e estrutura para crianças no local.</p><div class="button-row"><a class="button button--dark" href="https://www.google.com/maps/search/?api=1&query=Rua+Professor+Joaquim+Cardoso+de+Matos+499+Nova+Iguacu+RJ" target="_blank" rel="noopener"><span>Como chegar</span><span aria-hidden="true">↗</span></a><a class="button button--outline-dark" href="https://www.instagram.com/sobreasaguaschurch/" target="_blank" rel="noopener"><span>Conheça a comunidade</span><span aria-hidden="true">↗</span></a></div></div>
    </div></section>"""
)

page(
    "contato",
    "Agenda & Contato",
    "Agenda pública, convites, imprensa e canais oficiais da equipe de Luiz Arcanjo.",
    hero("Agenda & Contato", "Cada encontro<br><span class=\"nowrap\">começa com uma</span><br><em>ponte.</em>", "Agenda pública, convites e o caminho certo para falar com a equipe de Luiz Arcanjo.", "contact-hero-stage.jpg", "Luiz Arcanjo diante do público em uma apresentação", variant="contact")
    + """
    <nav class="contact-subnav" aria-label="Nesta página"><div class="shell"><a href="#agenda">Agenda</a><a href="#canais">Canais oficiais</a><a href="#mensagem">Enviar mensagem</a></div></nav>
    <section class="contact-agenda section-pad section--ivory" id="agenda"><div class="shell contact-agenda__grid">
      <div data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Agenda pública</p><h2 class="display-title">Onde os próximos encontros <em>acontecem.</em></h2><p class="lead-serif">Apresentações, ministrações e compromissos abertos ao público, organizados mês a mês.</p></div>
      <div class="agenda-month" data-reveal><div class="agenda-month__head"><span>Setembro de 2026</span><small>Agenda oficial</small></div><ol class="agenda-list" aria-label="Agenda de setembro de 2026">
        <li class="agenda-event is-past"><time datetime="2026-09-02"><b>02</b><span>set</span></time><div><strong>Luiz Arcanjo</strong><p>São Lourenço · MG</p></div><small>Realizado</small></li>
        <li class="agenda-event is-past"><time datetime="2026-09-05"><b>05</b><span>set</span></time><div><strong>Trazendo a Arca</strong><p>Santo Antônio do Monte · MG</p></div><small>Realizado</small></li>
        <li class="agenda-event is-past"><time datetime="2026-09-08"><b>08</b><span>set</span></time><div><strong>Luiz Arcanjo</strong><p>Nova Resende · MG</p></div><small>Realizado</small></li>
        <li class="agenda-event is-past"><time datetime="2026-09-09"><b>09</b><span>set</span></time><div><strong>Luiz Arcanjo</strong><p>Vila Isabel · RJ</p></div><small>Realizado</small></li>
        <li class="agenda-event is-past"><time datetime="2026-09-12"><b>12</b><span>set</span></time><div><strong>Luiz Arcanjo</strong><p>Rochedo · MS</p></div><small>Realizado</small></li>
        <li class="agenda-event is-past"><time datetime="2026-09-16"><b>16</b><span>set</span></time><div><strong>Luiz Arcanjo</strong><p>Brasília · DF</p></div><small>Realizado</small></li>
        <li class="agenda-event is-past"><time datetime="2026-09-18"><b>18</b><span>set</span></time><div><strong>Luiz Arcanjo</strong><p>Duque de Caxias · RJ</p></div><small>Realizado</small></li>
        <li class="agenda-event is-past"><time datetime="2026-09-19"><b>19</b><span>set</span></time><div><strong>Trazendo a Arca</strong><p>Ponte Nova · MG</p></div><small>Realizado</small></li>
        <li class="agenda-event is-next"><time datetime="2026-09-23"><b>23</b><span>set</span></time><div><strong>Trazendo a Arca</strong><p>Tucano · BA</p></div><small>Próximo</small></li>
        <li class="agenda-event"><time datetime="2026-09-26"><b>26</b><span>set</span></time><div><strong>Trazendo a Arca</strong><p>Figueirópolis D’Oeste · MT</p></div><small>Confirmado</small></li>
        <li class="agenda-event"><time datetime="2026-09-30"><b>30</b><span>set</span></time><div><strong>Luiz Arcanjo</strong><p>Ilha do Governador · RJ</p></div><small>Confirmado</small></li>
      </ol><div class="agenda-month__action"><p>Para informações de acesso, consulte os canais oficiais do evento.</p><a class="text-link" href="#mensagem" data-contact-subject="Convite e agenda">Convidar Luiz Arcanjo <span aria-hidden="true">↓</span></a></div></div>
    </div></section>
    <section class="contact-channels section-pad" id="canais"><div class="shell"><div class="section-head" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Canais oficiais</p><h2 class="display-title">A conversa certa,<br>com a equipe <em>certa.</em></h2></div><div class="contact-channel-grid">
      <a class="contact-channel" href="mailto:assessorialuizarcanjo@gmail.com" data-reveal><span>01 / E-mail</span><strong>Assessoria e imprensa</strong><p>assessorialuizarcanjo@gmail.com</p><b aria-hidden="true">↗</b></a>
      <a class="contact-channel" href="https://wa.me/5521968315841?text=Ol%C3%A1%2C%20equipe%20do%20Luiz%20Arcanjo%21%20Gostaria%20de%20solicitar%20atendimento." target="_blank" rel="noopener" data-reveal><span>02 / WhatsApp</span><strong>Atendimento da equipe</strong><p>(21) 96831-5841</p><b aria-hidden="true">↗</b></a>
      <a class="contact-channel" href="#mensagem" data-contact-subject="Convite e agenda" data-reveal><span>03 / Convites</span><strong>Igrejas e eventos</strong><p>Envie contexto, data e local para análise.</p><b aria-hidden="true">↓</b></a>
    </div></div></section>
    <section class="contact-message section-pad section--blue" id="mensagem"><div class="shell invite-grid"><div class="invite-grid__intro" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Fale com a equipe</p><h2 class="display-title">Direcione sua mensagem para quem pode <em>responder.</em></h2><p class="lead-serif">Selecione o assunto e envie os dados necessários. A mensagem seguirá diretamente para a assessoria de Luiz Arcanjo.</p><div class="contact-direct"><span>Prefere escrever?</span><a href="mailto:assessorialuizarcanjo@gmail.com">assessorialuizarcanjo@gmail.com</a></div></div>
      <form class="invite-form contact-form" id="invite-form" action="/api/contact" method="post"><div class="contact-honeypot" aria-hidden="true"><label>Empresa <input name="company" tabindex="-1" autocomplete="off"></label></div><label>Assunto <select name="assunto" id="contact-subject" required><option value="">Selecione o assunto</option><option>Convite e agenda</option><option>Assessoria de imprensa</option><option>Parcerias</option><option>Academy · cursos e workshops</option><option>Academy · mentoria</option><option>Outros assuntos</option></select></label><div class="field-grid"><label>Seu nome <input name="nome" required autocomplete="name" placeholder="Nome e sobrenome"></label><label>E-mail <input name="email" required type="email" autocomplete="email" placeholder="voce@exemplo.com"></label></div><div class="field-grid"><label>Telefone / WhatsApp <input name="telefone" type="tel" autocomplete="tel" placeholder="+55 (00) 00000-0000"></label><label data-invite-field>Organização ou igreja <input name="organizacao" placeholder="Nome da organização"></label></div><div class="field-grid" data-invite-field><label>Tipo de convite <select name="tipo"><option value="">Selecione</option><option>Ministração</option><option>Apresentação musical</option><option>Conferência</option><option>Entrevista</option><option>Outro</option></select></label><label>Data prevista <input name="data" type="date"></label></div><label data-invite-field>Cidade e local <input name="local" placeholder="Cidade, estado e local do evento"></label><label>Mensagem <textarea name="mensagem" rows="6" required placeholder="Conte o contexto e como a equipe pode ajudar"></textarea></label><button class="button button--gold" type="submit"><span>Enviar para a assessoria</span><span aria-hidden="true">↗</span></button><p class="form-status" data-form-status aria-live="polite" hidden></p><small>Seus dados serão usados somente para responder a esta solicitação.</small></form>
    </div></section>
    <section class="contact-social shell social-grid" aria-label="Redes sociais"><a href="https://www.instagram.com/luiz_arcanjo/" target="_blank" rel="noopener">Instagram <span>↗</span></a><a href="https://www.youtube.com/luizarcanjo" target="_blank" rel="noopener">YouTube <span>↗</span></a><a href="https://open.spotify.com/artist/3jhaArlXRtYY9R7GJrvcZ2" target="_blank" rel="noopener">Spotify <span>↗</span></a></section>"""
)

redirect("agenda", "/contato/#agenda")
redirect("convites", "/contato/#mensagem")
