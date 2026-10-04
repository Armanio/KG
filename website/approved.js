(() => {
  const group = document.querySelector('.cards');
  const cards = [...group.querySelectorAll('.card')];
  const desktop = matchMedia('(min-width: 761px) and (hover: hover)');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let timer, index = -1, hovered = null, focused = null, visible = false;
  function paint(card) {
    cards.forEach(item => item.classList.toggle('is-active', item === card));
  }
  function sync() {
    clearInterval(timer);
    if (!desktop.matches) { paint(null); return; }
    if (hovered || focused) { paint(hovered || focused); return; }
    if (reduced.matches || !visible || document.hidden) { paint(null); return; }
    paint(index < 0 ? null : cards[index]);
    timer = setInterval(() => {
      index = (index + 1) % cards.length;
      paint(cards[index]);
    }, 2000);
  }
  cards.forEach(card => {
    card.addEventListener('pointerenter', () => { hovered = card; sync(); });
    card.addEventListener('pointerleave', () => { hovered = null; sync(); });
    card.addEventListener('focusin', () => { focused = card; sync(); });
    card.addEventListener('focusout', () => { focused = null; sync(); });
  });
  new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting;
    sync();
  }, {threshold: 0.1}).observe(group);
  desktop.addEventListener('change', sync);
  reduced.addEventListener('change', sync);
  document.addEventListener('visibilitychange', sync);
})();

(() => {
  const scene = document.querySelector('.scene');
  const stage = scene.querySelector('.banner-stage');
  const dots = [...scene.querySelectorAll('[data-slide]')];
  const pause = scene.querySelector('.banner-pause');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const mobile = matchMedia('(max-width: 1100px)');
  const frames = [
    ['111', 'Эвейна с книгой, Эриан, Вирт и Каэль в кабинете.'],
    ['333', 'Эвейна показывает документ Вирту. Каэль наблюдает за разговором.'],
    ['222', 'Вирт осторожно касается волос Эвейны.'],
    ['444', 'Эриан прикрывает рот Эвейны в тёмном коридоре. Позади — Каэль.'],
    ['555', 'Каэль держит Эвейну за запястье. Эриан стоит рядом.']
  ];
  const slides = [stage.querySelector('picture')];
  let index = 0, timer, visible = false, paused = false, request = 0;
  function slideAt(i) {
    if (slides[i]) return slides[i];
    const picture = document.createElement('picture');
    picture.className = 'banner-slide';
    picture.setAttribute('aria-hidden', 'true');
    const source = document.createElement('source');
    source.media = '(max-width: 1100px)';
    source.srcset = `assets/banner-${frames[i][0]}m.webp`;
    const img = document.createElement('img');
    img.alt = frames[i][1]; img.width = 4000; img.height = 2000;
    picture.append(source, img);
    img.src = `assets/banner-${frames[i][0]}.webp`;
    stage.append(picture);
    slides[i] = picture;
    return picture;
  }
  function sync() {
    clearTimeout(timer);
    pause.setAttribute('aria-pressed', String(paused));
    pause.setAttribute('aria-label', paused ? 'Продолжить смену кадров' : 'Приостановить смену кадров');
    pause.textContent = paused ? '▶' : 'Ⅱ';
    pause.hidden = reduced.matches;
    if (!paused && !reduced.matches && visible && !document.hidden) {
      timer = setTimeout(() => show((index + 1) % frames.length), 5000);
      // Load only the next frame, using the browser-selected mobile or desktop source.
      slideAt((index + 1) % frames.length);
    }
  }
  async function show(next) {
    clearTimeout(timer);
    const ticket = ++request;
    const picture = slideAt(next);
    try { await picture.querySelector('img').decode(); }
    catch { if (ticket === request) sync(); return; }
    if (ticket !== request) return;
    slides.forEach((slide, i) => {
      slide.classList.toggle('is-current', i === next);
      slide.setAttribute('aria-hidden', String(i !== next));
    });
    index = next;
    dots.forEach((dot, i) => dot.setAttribute('aria-pressed', String(i === index)));
    sync();
  }
  dots.forEach((dot, i) => dot.addEventListener('click', () => show(i)));
  pause.addEventListener('click', () => { paused = !paused; ++request; sync(); });
  let start;
  stage.addEventListener('pointerdown', event => { start = [event.clientX, event.clientY]; });
  stage.addEventListener('pointercancel', () => { start = null; });
  stage.addEventListener('pointerup', event => {
    if (!start) return;
    const dx = event.clientX - start[0], dy = event.clientY - start[1];
    start = null;
    if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) show((index + (dx < 0 ? 1 : frames.length - 1)) % frames.length);
  });
  new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting;
    if (!visible) ++request;
    sync();
  }, {threshold: .15}).observe(stage);
  document.addEventListener('visibilitychange', () => { ++request; sync(); });
  reduced.addEventListener('change', () => { ++request; sync(); });
  mobile.addEventListener('change', () => { ++request; sync(); });
})();

// End the desktop shade at the actual right edge of the first title line.
(() => {
  const hero = document.querySelector('.hero-final');
  const title = hero.querySelector('.title-first');
  const stage = hero.querySelector('.banner-stage');
  function alignFade() {
    hero.style.setProperty('--title-fade-end', `${Math.max(0, title.getBoundingClientRect().right - stage.getBoundingClientRect().left)}px`);
  }
  const observer = new ResizeObserver(alignFade);
  observer.observe(hero);
  observer.observe(title);
  document.fonts.ready.then(alignFade);
})();
