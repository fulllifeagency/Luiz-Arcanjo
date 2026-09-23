"""Verified Spotify discography used by the Música page.

The source records are stored in catalog_audit.json. They were checked against
the public Spotify release pages on 2026-09-22. Playback editions are excluded.
"""
from html import escape
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RECORDS = json.loads((ROOT / "catalog_audit.json").read_text(encoding="utf-8"))


PLATFORMS = (
    ("Spotify", "spotify-icon.svg", "https://open.spotify.com/artist/3jhaArlXRtYY9R7GJrvcZ2"),
    ("Deezer", "deezer-icon.svg", "https://www.deezer.com/artist/5162481"),
    ("Apple Music", "applemusic-icon.svg", "https://music.apple.com/us/artist/luiz-arcanjo/1506654862"),
    ("Amazon Music", "amazonmusic-icon.svg", "https://music.amazon.com.br/artists/B004YRIFEI/luiz-arcanjo"),
    ("YouTube Music", "youtubemusic-icon.svg", "https://music.youtube.com/channel/UCUAmzBqyLwVIneS-sEGQVTQ"),
)


def platform_bar():
    links = "".join(
        f'''<a class="music-platform" href="{url}" target="_blank" rel="noopener" aria-label="Ouvir Luiz Arcanjo no {escape(name, quote=True)}"><img src="/assets/images/{icon}" alt=""><span>{escape(name)}</span></a>'''
        for name, icon, url in PLATFORMS
    )
    return f'''<nav class="platform-bar platform-bar--music" aria-label="Luiz Arcanjo nas plataformas digitais"><div class="shell platform-bar__inner"><span>Ouça nas plataformas</span>{links}</div></nav>'''


def _type_label(record):
    return {"single": "Single", "ep": "EP", "album": "Álbum"}.get(record["kind"], "Lançamento")


def _card(record, context):
    title = escape(record["title"])
    kind = "album" if record["kind"] in {"album", "ep"} else "single"
    meta = f'{_type_label(record)} · {record["year"]}'
    return f'''<a class="release-card release-card--{context}" data-release data-release-context="{context}" data-artist="{record["group"]}" data-type="{kind}" data-date="{record["date"]}" href="{record["url"]}" target="_blank" rel="noopener" hidden>
      <span class="release-card__visual"><img class="release-card__cover" src="/assets/images/discography/{record["id"]}.jpg" alt="Capa de {title}" loading="lazy"><span class="release-card__listen">Ouvir no Spotify <span aria-hidden="true">↗︎</span></span></span>
      <span class="release-card__info"><span>{escape(meta)}</span><strong>{title}</strong></span>
    </a>'''


def selection():
    records = [record for record in RECORDS if not record.get("playback")]
    records.sort(key=lambda record: record["date"], reverse=True)
    rail_cards = "".join(_card(record, "rail") for record in records)
    dialog_cards = "".join(_card(record, "dialog") for record in records)
    return f'''
    <section class="section-pad discography-section" data-discography><div class="shell">
      <div class="discography-section__head" data-reveal><p class="eyebrow"><span class="eyebrow__rule"></span>Discografia</p><h2 class="display-title">Uma trajetória em cada <em>lançamento.</em></h2><p>Álbuns, EPs e singles organizados do mais recente ao mais antigo. Selecione uma trajetória e explore no seu ritmo.</p></div>
      <div class="discography-toolbar">
      <div class="discography-controls" aria-label="Filtros da discografia">
        <div class="discography-control"><span>Trajetória</span><div class="discography-segmented"><button type="button" data-artist-filter="solo" aria-pressed="true">Luiz Arcanjo</button><button type="button" data-artist-filter="band" aria-pressed="false">Trazendo a Arca</button></div></div>
        <div class="discography-control"><span>Formato</span><div class="discography-segmented"><button type="button" data-type-filter="all" aria-pressed="true">Todos</button><button type="button" data-type-filter="album" aria-pressed="false">Álbuns e EPs</button><button type="button" data-type-filter="single" aria-pressed="false">Singles</button></div></div>
      </div>
      <button class="discography-show-all" type="button" data-discography-open>Ver tudo <span aria-hidden="true">↗︎</span></button>
      </div>
      <div class="discography-rail-head"><p class="discography-status" data-discography-status aria-live="polite"></p><div class="discography-rail-arrows" aria-label="Navegar pelos lançamentos"><button type="button" data-rail-prev aria-label="Lançamentos anteriores">←︎</button><button type="button" data-rail-next aria-label="Próximos lançamentos">→︎</button></div></div>
      <div class="release-rail" data-release-rail>{rail_cards}</div>
      <div class="discography-section__foot"><p>Capas, títulos, formatos e datas conferidos nas páginas públicas do Spotify. Edições de playback foram removidas.</p><a class="text-link" href="https://open.spotify.com/artist/3jhaArlXRtYY9R7GJrvcZ2" target="_blank" rel="noopener">Luiz Arcanjo no Spotify <span aria-hidden="true">↗︎</span></a><a class="text-link" href="https://open.spotify.com/artist/1KJkhqZNLx1JY9vXkBhGV5" target="_blank" rel="noopener">Trazendo a Arca no Spotify <span aria-hidden="true">↗︎</span></a></div>
    </div>
    <dialog class="discography-dialog" data-discography-dialog aria-labelledby="discography-dialog-title"><div class="discography-dialog__panel">
      <div class="discography-dialog__head"><div><span>Discografia completa</span><h3 id="discography-dialog-title" data-discography-dialog-title>Luiz Arcanjo</h3><p data-discography-dialog-meta></p></div><button type="button" data-discography-close aria-label="Fechar discografia">×</button></div>
      <div class="release-grid" data-release-grid>{dialog_cards}</div>
    </div></dialog>
    </section>'''
