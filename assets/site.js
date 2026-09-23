(function () {
  "use strict";

  var path = window.location.pathname;
  var home = path === "/" || path === "/index.html";
  var lightHeroHeader = ["livro", "conteudos"].some(function (slug) {
    return path === "/" + slug + "/" || path === "/" + slug + "/index.html";
  });
  var spotifyLuiz = "https://open.spotify.com/artist/3jhaArlXRtYY9R7GJrvcZ2";
  var youtube = "https://www.youtube.com/luizarcanjo";
  var instagram = "https://www.instagram.com/luiz_arcanjo/";
  var email = "assessorialuizarcanjo@gmail.com";

  var headerTarget = document.getElementById("site-header");
  if (headerTarget) {
    headerTarget.innerHTML = [
      '<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>',
      '<header class="site-header', home || path === '/musica/' || path === '/musica/index.html' || path === '/cursos/' || path === '/cursos/index.html' || path === '/contato/' || path === '/contato/index.html' ? ' site-header--hero' : '', '" id="header">',
      '<div class="site-header__inner shell">',
      '<a class="brand" href="/" aria-label="Luiz Arcanjo — página inicial"><img class="brand__image" src="', lightHeroHeader ? '/assets/images/signature-dark.png' : '/assets/images/signature-light.png', '" alt="Luiz Arcanjo"></a>',
      '<nav class="desktop-nav" aria-label="Navegação principal">',
      '<a href="/">Início</a><a href="/historia/">Biografia</a><a href="/musica/">Discografia</a><a href="/cursos/">Academy</a><a href="/livro/">Loja</a><a href="/conteudos/">Devocionais</a><a href="/igreja/">Igreja</a>',
      '</nav><a class="header-cta" href="/contato/">Agenda &amp; contato <span aria-hidden="true">↗︎</span></a>',
      '<button class="menu-toggle" type="button" aria-label="Abrir menu" aria-controls="mobile-menu" aria-expanded="false"><span></span><span></span></button>',
      '</div><nav class="mobile-menu" id="mobile-menu" aria-label="Navegação móvel" inert><div class="mobile-menu__inner shell">',
      '<a href="/">Início</a><a href="/historia/">Biografia</a><a href="/musica/">Discografia</a><a href="/cursos/">Academy</a><a href="/livro/">Loja</a><a href="/conteudos/">Devocionais</a><a href="/igreja/">Sobre as Águas Church</a><a href="/contato/">Agenda &amp; Contato</a>',
      '<div class="mobile-menu__social"><a href="', instagram, '" target="_blank" rel="noopener">Instagram ↗︎</a><a href="', youtube, '" target="_blank" rel="noopener">YouTube ↗︎</a></div>',
      '</div></nav></header>'
    ].join("");
  }

  var footerTarget = document.getElementById("site-footer");
  if (footerTarget) {
    footerTarget.innerHTML = [
      '<footer class="site-footer">',
      '<div class="shell footer-top"><a class="footer-signature" href="/" aria-label="Luiz Arcanjo — página inicial"><img src="/assets/images/signature-light.png" alt="Luiz Arcanjo"></a><p>Uma vida dedicada a <em>servir.</em></p></div>',
      '<div class="shell footer-middle"><nav class="footer-map" aria-label="Mapa do site"><a href="/">Início</a><a href="/historia/">Biografia</a><a href="/musica/">Discografia</a><a href="/cursos/">Academy</a><a href="/livro/">Loja</a><a href="/conteudos/">Devocionais</a><a href="/igreja/">Sobre as Águas</a><a href="/contato/">Agenda &amp; Contato</a></nav>',
      '<div class="footer-channels"><span>Acompanhe e ouça</span><div class="footer-channels__icons">',
      '<a href="', instagram, '" target="_blank" rel="noopener" aria-label="Instagram"><img src="/assets/images/instagram-icon.svg" alt=""></a>',
      '<a href="', youtube, '" target="_blank" rel="noopener" aria-label="YouTube"><img src="/assets/images/youtube-icon.svg" alt=""></a>',
      '<a href="', spotifyLuiz, '" target="_blank" rel="noopener" aria-label="Spotify"><img src="/assets/images/spotify-icon.svg" alt=""></a>',
      '<a href="https://music.apple.com/us/artist/luiz-arcanjo/1506654862" target="_blank" rel="noopener" aria-label="Apple Music"><img src="/assets/images/applemusic-icon.svg" alt=""></a>',
      '<a href="https://music.amazon.com.br/artists/B004YRIFEI/luiz-arcanjo" target="_blank" rel="noopener" aria-label="Amazon Music"><img src="/assets/images/amazonmusic-icon.svg" alt=""></a>',
      '</div></div></div>',
      '<div class="shell footer-bottom"><div><small>© ', new Date().getFullYear(), ' Luiz Arcanjo. Todos os direitos reservados.</small><small>Desenvolvido na França por <a href="https://www.fulllifeweb.fr/br" target="_blank" rel="noopener">Full Life Agency</a>.</small></div><a class="footer-toplink" href="#topo">Voltar ao topo <span aria-hidden="true">↑︎</span></a></div></footer>'
    ].join("");
  }

  var platformLinks = [
    ["https://open.spotify.com/artist/3jhaArlXRtYY9R7GJrvcZ2", "Spotify", "spotify-icon.svg"],
    ["https://www.deezer.com/artist/5162481", "Deezer", "deezer-icon.svg"],
    ["https://music.apple.com/us/artist/luiz-arcanjo/1506654862", "Apple Music", "applemusic-icon.svg"],
    ["https://music.amazon.com.br/artists/B004YRIFEI/luiz-arcanjo", "Amazon Music", "amazonmusic-icon.svg"],
    ["https://music.youtube.com/channel/UCUAmzBqyLwVIneS-sEGQVTQ", "YouTube Music", "youtubemusic-icon.svg"]
  ];
  document.querySelectorAll(".platform-bar__inner").forEach(function (bar) {
    bar.innerHTML = '<span>Ouça nas plataformas</span>' + platformLinks.map(function (platform) {
      return '<a class="music-platform" href="' + platform[0] + '" target="_blank" rel="noopener" aria-label="Ouvir Luiz Arcanjo no ' + platform[1] + '"><img src="/assets/images/' + platform[2] + '?v=2" alt=""><span>' + platform[1] + '</span></a>';
    }).join("");
  });

  // Keep short Portuguese connectors attached to the word that follows them.
  // This prevents typographic orphans such as a line containing only "de".
  var protectHeadingLineBreaks = function (heading) {
    var walker = document.createTreeWalker(heading, NodeFilter.SHOW_TEXT);
    var nodes = [];
    var node;
    while ((node = walker.nextNode())) nodes.push(node);
    nodes.forEach(function (textNode) {
      textNode.nodeValue = textNode.nodeValue.replace(/\u00a0/g, " ").replace(
        /(^|\s)(a|as|ao|aos|à|às|com|da|das|de|do|dos|e|em|na|nas|no|nos|o|os|ou|para|por|sem|sob)\s+(?=\S)/gi,
        function (_, before, connector) { return before + connector + "\u00a0"; }
      );
    });
    if (heading.clientWidth && heading.scrollWidth > heading.clientWidth + 1) {
      nodes.forEach(function (textNode) {
        textNode.nodeValue = textNode.nodeValue.replace(/\u00a0/g, " ");
      });
    }
  };
  var refreshHeadingLineBreaks = function () {
    document.querySelectorAll("h1, h2, h3").forEach(protectHeadingLineBreaks);
  };
  refreshHeadingLineBreaks();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(refreshHeadingLineBreaks);
  window.addEventListener("resize", refreshHeadingLineBreaks, { passive: true });

  var header = document.getElementById("header");
  if (header) {
    var updateHeader = function () {
      var scrolled = window.scrollY > 45;
      header.classList.toggle("is-scrolled", scrolled);
      if (lightHeroHeader) {
        var logo = header.querySelector(".brand__image");
        if (logo) logo.src = scrolled || document.body.classList.contains("menu-open") ? "/assets/images/signature-light.png" : "/assets/images/signature-dark.png";
      }
    };
    updateHeader();
    window.addEventListener("scroll", updateHeader, { passive: true });
    if (footerTarget && "IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        header.classList.toggle("is-over-footer", entries[0].isIntersecting && window.scrollY > 200 && !document.body.classList.contains("menu-open"));
      }, { rootMargin: "-80px 0px 0px 0px" }).observe(footerTarget);
    }
  }

  var menuButton = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  if (menuButton && menu) {
    var closeMenu = function () {
      menuButton.setAttribute("aria-expanded", "false");
      menuButton.setAttribute("aria-label", "Abrir menu");
      menu.classList.remove("is-open");
      menu.inert = true;
      document.body.classList.remove("menu-open");
      updateHeader();
    };
    menuButton.addEventListener("click", function () {
      var open = menuButton.getAttribute("aria-expanded") !== "true";
      menuButton.setAttribute("aria-expanded", String(open));
      menuButton.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
      menu.classList.toggle("is-open", open);
      menu.inert = !open;
      document.body.classList.toggle("menu-open", open);
      updateHeader();
    });
    menu.querySelectorAll("a").forEach(function (link) { link.addEventListener("click", closeMenu); });
    document.addEventListener("keydown", function (event) { if (event.key === "Escape") closeMenu(); });
  }

  var current = path.replace(/index\.html$/, "");
  document.querySelectorAll(".desktop-nav a").forEach(function (link) {
    if (link.getAttribute("href") === current || (home && link.getAttribute("href") === "/")) {
      link.setAttribute("aria-current", "page");
    }
  });

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  document.querySelectorAll("[data-family-slideshow]").forEach(function (slideshow) {
    var slides = Array.from(slideshow.querySelectorAll(".family-slideshow__slide"));
    var markers = Array.from(slideshow.querySelectorAll(".family-slideshow__progress span"));
    var activeSlide = 0;
    var slideTimer = 0;
    var showFamilySlide = function (index) {
      activeSlide = index;
      slides.forEach(function (slide, slideIndex) {
        var active = slideIndex === activeSlide;
        slide.classList.toggle("is-active", active);
        slide.setAttribute("aria-hidden", String(!active));
      });
      markers.forEach(function (marker, markerIndex) { marker.classList.toggle("is-active", markerIndex === activeSlide); });
    };
    var stopFamilySlideshow = function () {
      if (slideTimer) window.clearInterval(slideTimer);
      slideTimer = 0;
    };
    var syncFamilySlideshow = function () {
      stopFamilySlideshow();
      if (reducedMotion.matches) {
        showFamilySlide(0);
        return;
      }
      if (document.visibilityState === "visible") {
        slideTimer = window.setInterval(function () { showFamilySlide((activeSlide + 1) % slides.length); }, 5200);
      }
    };
    showFamilySlide(0);
    syncFamilySlideshow();
    reducedMotion.addEventListener("change", syncFamilySlideshow);
    document.addEventListener("visibilitychange", syncFamilySlideshow);
  });
  var imageRevealItems = document.querySelectorAll(".image-feature__visual, .church-feature__image, .book-feature__visual, .book-inside__visual, .book-final__cover, .music-panel__image, .church-story__photo, .church-visit__photo");
  if (!reducedMotion.matches && "IntersectionObserver" in window) {
    imageRevealItems.forEach(function (item) { item.classList.add("image-reveal"); });
  }
  var revealItems = document.querySelectorAll("[data-reveal]");
  if (!reducedMotion.matches && "IntersectionObserver" in window) {
    document.documentElement.classList.add("motion-ready");
    var revealObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: .08, rootMargin: "0px 0px 50px 0px" });
    revealItems.forEach(function (item) { revealObserver.observe(item); });
    var imageObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.querySelectorAll(".image-reveal").forEach(function (photo) { photo.classList.add("is-visible"); });
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: .08, rootMargin: "0px 0px 50px 0px" });
    imageRevealItems.forEach(function (item) { imageObserver.observe(item.parentElement); });
  }

  var journey = document.querySelector(".story-journey");
  if (journey) {
    var journeyChapters = Array.from(journey.querySelectorAll("[data-story-chapter]"));
    var journeyPhotos = Array.from(journey.querySelectorAll(".story-journey__frame img"));
    var journeyCounter = journey.querySelector(".story-journey__counter");
    var activeJourney = -1;
    var journeyScheduled = false;
    var updateJourney = function () {
      journeyScheduled = false;
      if (window.innerWidth <= 700) return;
      var focusY = window.innerHeight * .52;
      var closest = 0;
      var distance = Infinity;
      journeyChapters.forEach(function (chapter, index) {
        var box = chapter.getBoundingClientRect();
        var current = Math.abs(box.top + box.height / 2 - focusY);
        if (current < distance) { distance = current; closest = index; }
      });
      if (closest === activeJourney) return;
      activeJourney = closest;
      journeyChapters.forEach(function (chapter, index) { chapter.classList.toggle("is-active", index === closest); });
      journeyPhotos.forEach(function (photo, index) { photo.classList.toggle("is-active", index === closest); });
      if (journeyCounter) journeyCounter.firstChild.textContent = String(closest + 1).padStart(2, "0") + " ";
    };
    var scheduleJourney = function () {
      if (journeyScheduled) return;
      journeyScheduled = true;
      window.requestAnimationFrame(updateJourney);
    };
    updateJourney();
    window.addEventListener("scroll", scheduleJourney, { passive: true });
    window.addEventListener("resize", scheduleJourney);
  }

  var heroVideo = document.getElementById("hero-video");
  var heroProgress = document.getElementById("hero-progress");
  var heroToggle = document.getElementById("hero-toggle");
  if (heroVideo) {
    var hero = heroVideo.closest(".hero");
    var phrases = Array.from(hero.querySelectorAll("[data-hero-phrase]"));
    var phraseIndex = 0;
    var showPhrase = function (index) {
      if (phraseIndex === index || !phrases[index]) return;
      var previous = phrases[phraseIndex];
      previous.classList.remove("is-active");
      previous.classList.add("is-leaving");
      window.setTimeout(function () { previous.classList.remove("is-leaving"); }, 680);
      phraseIndex = index;
      phrases[index].classList.remove("is-leaving");
      phrases[index].classList.add("is-active");
    };
    heroVideo.addEventListener("loadeddata", function () { heroVideo.classList.add("is-ready"); });
    heroVideo.addEventListener("loadedmetadata", function () {
      if (heroVideo.duration) hero.style.setProperty("--hero-phase-duration", (heroVideo.duration / 3).toFixed(2) + "s");
    });
    heroVideo.addEventListener("timeupdate", function () {
      var t = heroVideo.currentTime;
      var index = heroVideo.duration ? Math.min(2, Math.floor(t / heroVideo.duration * 3)) : 0;
      showPhrase(index);
      if (heroProgress && heroVideo.duration) heroProgress.style.width = Math.min(100, t / heroVideo.duration * 100) + "%";
    });
    if (heroToggle) heroToggle.addEventListener("click", function () {
      if (heroVideo.paused) {
        heroVideo.play().catch(function () {});
        heroToggle.innerHTML = 'Pausar <span aria-hidden="true">Ⅱ</span>';
        heroToggle.setAttribute("aria-label", "Pausar vídeo");
      } else {
        heroVideo.pause();
        heroToggle.innerHTML = 'Reproduzir <span aria-hidden="true">▶︎</span>';
        heroToggle.setAttribute("aria-label", "Reproduzir vídeo");
      }
    });
    var videoSource = heroVideo.querySelector("source[data-src]");
    var syncVideoPlayback = function () {
      var staticMode = reducedMotion.matches;
      if (heroToggle) heroToggle.hidden = staticMode;
      if (staticMode) {
        heroVideo.pause();
        showPhrase(0);
      } else {
        if (videoSource && !videoSource.getAttribute("src")) {
          videoSource.setAttribute("src", videoSource.getAttribute("data-src"));
          heroVideo.load();
        }
        heroVideo.play().catch(function () {});
      }
    };
    syncVideoPlayback();
    reducedMotion.addEventListener("change", syncVideoPlayback);
  }

  document.querySelectorAll(".inner-hero__video").forEach(function (video) {
    var mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    var syncInnerHeroVideo = function () {
      if (mediaQuery.matches) {
        video.pause();
      } else {
        var playback = video.play();
        if (playback && playback.catch) playback.catch(function () {});
      }
    };
    syncInnerHeroVideo();
    mediaQuery.addEventListener("change", syncInnerHeroVideo);
    video.addEventListener("canplay", syncInnerHeroVideo);
    video.addEventListener("pause", function () {
      if (!mediaQuery.matches && document.visibilityState === "visible") syncInnerHeroVideo();
    });
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "visible") syncInnerHeroVideo();
    });
    window.addEventListener("pageshow", syncInnerHeroVideo);
    window.addEventListener("focus", syncInnerHeroVideo);
  });

  var biographyDialog = document.querySelector("[data-biography-dialog]");
  if (biographyDialog) {
    document.querySelectorAll("[data-biography-open]").forEach(function (button) {
      button.addEventListener("click", function () {
        biographyDialog.showModal();
        document.body.classList.add("dialog-open");
        var scrollArea = biographyDialog.querySelector(".biography-dialog__scroll");
        if (scrollArea) scrollArea.scrollTop = 0;
      });
    });
    biographyDialog.querySelectorAll("[data-biography-close]").forEach(function (button) {
      button.addEventListener("click", function () { biographyDialog.close(); });
    });
    biographyDialog.addEventListener("click", function (event) {
      if (event.target === biographyDialog) biographyDialog.close();
    });
    biographyDialog.addEventListener("close", function () { document.body.classList.remove("dialog-open"); });
  }

  document.querySelectorAll("[data-discography]").forEach(function (section) {
    var artist = "solo";
    var type = "all";
    var rail = section.querySelector("[data-release-rail]");
    var dialog = section.querySelector("[data-discography-dialog]");
    var status = section.querySelector("[data-discography-status]");
    var dialogTitle = section.querySelector("[data-discography-dialog-title]");
    var dialogMeta = section.querySelector("[data-discography-dialog-meta]");
    var artistButtons = Array.from(section.querySelectorAll("[data-artist-filter]"));
    var typeButtons = Array.from(section.querySelectorAll("[data-type-filter]"));
    var allCards = Array.from(section.querySelectorAll("[data-release]"));
    var labels = { solo: "Luiz Arcanjo", band: "Trazendo a Arca" };
    var typeLabels = { all: "lançamentos", album: "álbuns e EPs", single: "singles" };

    var matches = function (card) {
      return card.dataset.artist === artist && (type === "all" || card.dataset.type === type);
    };
    var render = function () {
      var count = 0;
      allCards.forEach(function (card) {
        var visible = matches(card);
        card.hidden = !visible;
        if (visible && card.dataset.releaseContext === "rail") count += 1;
      });
      artistButtons.forEach(function (button) { button.setAttribute("aria-pressed", String(button.dataset.artistFilter === artist)); });
      typeButtons.forEach(function (button) { button.setAttribute("aria-pressed", String(button.dataset.typeFilter === type)); });
      var message = count + " " + typeLabels[type] + " · do mais recente ao mais antigo";
      if (status) status.textContent = message;
      if (dialogTitle) dialogTitle.textContent = labels[artist];
      if (dialogMeta) dialogMeta.textContent = message;
      if (rail) rail.scrollLeft = 0;
    };

    artistButtons.forEach(function (button) {
      button.addEventListener("click", function () { artist = button.dataset.artistFilter; render(); });
    });
    typeButtons.forEach(function (button) {
      button.addEventListener("click", function () { type = button.dataset.typeFilter; render(); });
    });
    section.querySelectorAll("[data-rail-prev], [data-rail-next]").forEach(function (button) {
      button.addEventListener("click", function () {
        if (!rail) return;
        var direction = button.hasAttribute("data-rail-prev") ? -1 : 1;
        rail.scrollBy({ left: direction * Math.max(280, rail.clientWidth * .78), behavior: "smooth" });
      });
    });
    var openButton = section.querySelector("[data-discography-open]");
    var closeButton = section.querySelector("[data-discography-close]");
    if (openButton && dialog) openButton.addEventListener("click", function () { dialog.showModal(); document.body.classList.add("dialog-open"); });
    if (closeButton && dialog) closeButton.addEventListener("click", function () { dialog.close(); });
    if (dialog) {
      dialog.addEventListener("close", function () { document.body.classList.remove("dialog-open"); });
      dialog.addEventListener("click", function (event) { if (event.target === dialog) dialog.close(); });
    }
    render();
  });

  document.querySelectorAll("[data-embed]").forEach(function (container) {
    var button = container.querySelector("button");
    if (!button) return;
    button.addEventListener("click", function () {
      var frame = document.createElement("iframe");
      frame.src = container.getAttribute("data-embed");
      frame.title = container.getAttribute("data-embed-title") || "Player oficial do Spotify — Luiz Arcanjo";
      frame.loading = "lazy";
      frame.allow = "autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture";
      container.classList.add("is-loaded");
      container.replaceChildren(frame);
    });
  });

  document.querySelectorAll("[data-current-month]").forEach(function (label) {
    var month = new Intl.DateTimeFormat("pt-BR", { month: "long", year: "numeric" }).format(new Date());
    label.textContent = "Agenda de " + month.charAt(0).toUpperCase() + month.slice(1);
  });

  document.querySelectorAll("[data-post-like]").forEach(function (button) {
    var storageKey = "luiz-arcanjo-like-" + button.getAttribute("data-post-like");
    var icon = button.querySelector("span");
    var syncLike = function (liked) {
      button.setAttribute("aria-pressed", String(liked));
      if (icon) icon.textContent = liked ? "♥" : "♡";
    };
    var liked = false;
    try { liked = window.localStorage.getItem(storageKey) === "1"; } catch (error) {}
    syncLike(liked);
    button.addEventListener("click", function () {
      liked = !liked;
      syncLike(liked);
      try { window.localStorage.setItem(storageKey, liked ? "1" : "0"); } catch (error) {}
    });
  });

  document.querySelectorAll("[data-post-share]").forEach(function (button) {
    button.addEventListener("click", async function () {
      var title = button.getAttribute("data-share-title") || document.title;
      var rawUrl = button.getAttribute("data-share-url") || window.location.href;
      var url = new URL(rawUrl, window.location.origin).href;
      try {
        if (navigator.share) {
          await navigator.share({ title: title, url: url });
        } else {
          await navigator.clipboard.writeText(url);
          var original = button.lastChild.textContent;
          button.lastChild.textContent = " Link copiado";
          window.setTimeout(function () { button.lastChild.textContent = original; }, 1800);
        }
      } catch (error) {
        if (error && error.name !== "AbortError") window.location.href = url;
      }
    });
  });

  var inviteForm = document.getElementById("invite-form");
  if (inviteForm) {
    var subject = inviteForm.querySelector('[name="assunto"]');
    var invitationFields = Array.from(inviteForm.querySelectorAll("[data-invite-field]"));
    var subjectAliases = { cursos: "Academy · cursos e workshops", formacao: "Academy · cursos e workshops", mentoria: "Academy · mentoria", convite: "Convite e agenda" };
    var syncContactFields = function () {
      var invitation = subject && subject.value === "Convite e agenda";
      invitationFields.forEach(function (field) {
        field.hidden = !invitation;
        field.querySelectorAll("input, select").forEach(function (control) { control.disabled = !invitation; });
      });
    };
    var requestedSubject = new URLSearchParams(window.location.search).get("assunto");
    if (subject && requestedSubject) subject.value = subjectAliases[requestedSubject.toLowerCase()] || requestedSubject;
    if (subject) subject.addEventListener("change", syncContactFields);
    document.querySelectorAll("[data-contact-subject]").forEach(function (link) {
      link.addEventListener("click", function () {
        if (subject) subject.value = link.getAttribute("data-contact-subject") || "";
        syncContactFields();
      });
    });
    syncContactFields();
    inviteForm.addEventListener("submit", async function (event) {
      event.preventDefault();
      if (!inviteForm.reportValidity()) return;
      var button = inviteForm.querySelector('button[type="submit"]');
      var buttonLabel = button && button.querySelector("span");
      var status = inviteForm.querySelector("[data-form-status]");
      var initialLabel = buttonLabel ? buttonLabel.textContent : "Enviar para a assessoria";
      var payload = Object.fromEntries(new FormData(inviteForm).entries());
      if (status) {
        status.hidden = true;
        status.className = "form-status";
      }
      if (button) button.disabled = true;
      if (buttonLabel) buttonLabel.textContent = "Enviando…";
      try {
        var response = await fetch(inviteForm.action, {
          method: "POST",
          headers: { "Content-Type": "application/json", "Accept": "application/json" },
          body: JSON.stringify(payload)
        });
        var result = await response.json().catch(function () { return {}; });
        if (!response.ok) throw new Error(result.error || "Falha no envio");
        inviteForm.reset();
        syncContactFields();
        if (status) {
          status.textContent = "Mensagem enviada com sucesso. Nossa equipe retornará em breve pelo e-mail ou telefone informado.";
          status.classList.add("is-success");
          status.hidden = false;
        }
      } catch (error) {
        if (status) {
          status.textContent = "Não foi possível enviar agora. Tente novamente ou fale com a equipe pelo WhatsApp.";
          status.classList.add("is-error");
          status.hidden = false;
        }
      } finally {
        if (button) button.disabled = false;
        if (buttonLabel) buttonLabel.textContent = initialLabel;
      }
    });
  }
})();
