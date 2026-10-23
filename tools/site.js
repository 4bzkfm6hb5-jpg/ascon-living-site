/* Lightweight carousels and one lightbox. No dependencies. */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lb = document.querySelector('.lb');
  var lbImg, lbCap, lbIndex, lbSlides;

  function slidesOf(root) {
    return [].slice.call(root.querySelectorAll('.car-slide'));
  }

  function setup(root) {
    var slides = slidesOf(root);
    if (slides.length < 2) return;
    var view = root.querySelector('.car-viewport');
    var track = root.querySelector('.car-track');
    var dots = root.querySelector('.car-dots');
    var i = 0;
    var timer = 0;
    var auto = !reduced && parseInt(root.getAttribute('data-auto') || '0', 10);

    if (dots) {
      dots.innerHTML = '';
      slides.forEach(function (_, n) {
        var b = document.createElement('button');
        b.type = 'button';
        b.setAttribute('aria-label', String(n + 1));
        b.addEventListener('click', function () { go(n); user(); });
        dots.appendChild(b);
      });
    }

    function paint() {
      var w = view ? view.clientWidth : root.clientWidth;
      if (view && slides[i] && !root.classList.contains('hero')) view.style.height = slides[i].scrollHeight + 'px';
      if (track && w) track.style.transform = 'translateX(' + (-i * w) + 'px)';
      slides.forEach(function (s, n) { s.setAttribute('aria-hidden', n === i ? 'false' : 'true'); });
      if (dots) [].forEach.call(dots.children, function (d, n) {
        if (n === i) d.setAttribute('aria-current', 'true');
        else d.removeAttribute('aria-current');
      });
      [].forEach.call(root.querySelectorAll('.car-thumbs [data-go]'), function (t) {
        if (Number(t.getAttribute('data-go')) === i) t.setAttribute('aria-current', 'true');
        else t.removeAttribute('aria-current');
      });
      var count = root.querySelector('.car-count');
      if (count) count.textContent = (i + 1) + ' / ' + slides.length;
    }

    function go(n) {
      i = (n + slides.length) % slides.length;
      paint();
    }

    function stop() { if (timer) { clearInterval(timer); timer = 0; } }
    function start() {
      stop();
      if (!auto || document.hidden) return;
      timer = setInterval(function () { go(i + 1); }, auto);
    }
    function user() { stop(); }

    root.querySelectorAll('.car-btn.next').forEach(function (b) {
      b.addEventListener('click', function () { go(i + 1); user(); });
    });
    root.querySelectorAll('.car-btn.prev').forEach(function (b) {
      b.addEventListener('click', function () { go(i - 1); user(); });
    });
    root.querySelectorAll('.car-thumbs [data-go]').forEach(function (b) {
      b.addEventListener('click', function () { go(Number(b.getAttribute('data-go'))); user(); });
    });

    var x0 = null;
    var dragged = false;
    if (view) {
      view.addEventListener('pointerdown', function (e) {
        if (e.target.closest('a, button')) return;
        x0 = e.clientX; dragged = false; user();
      });
      view.addEventListener('pointerup', function (e) {
        if (x0 == null) return;
        var dx = e.clientX - x0;
        x0 = null;
        if (Math.abs(dx) > 40) { dragged = true; go(i + (dx < 0 ? 1 : -1)); }
      });
      view.addEventListener('pointercancel', function () { x0 = null; });
      if (root.hasAttribute('data-lightbox')) {
        view.addEventListener('click', function (e) {
          if (dragged) { dragged = false; return; }
          if (e.target.closest('button, a')) return;
          var img = e.target.closest('.car-slide') && e.target.closest('.car-slide').querySelector('img');
          if (!img) return;
          openLb(root, i);
        });
      }
    }
    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { go(i + 1); user(); }
      if (e.key === 'ArrowLeft') { go(i - 1); user(); }
    });
    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', start);
    root.addEventListener('focusin', stop);
    root.addEventListener('focusout', start);
    slides.forEach(function (s) {
      var img = s.querySelector('img');
      if (img && !img.complete) img.addEventListener('load', paint);
    });
    window.addEventListener('resize', paint);
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else start(); });
    go(0);
    start();
  }

  function openLb(root, index) {
    if (!lb) return;
    lbSlides = slidesOf(root).map(function (s) {
      var img = s.querySelector('img');
      var cap = s.querySelector('figcaption');
      return { src: img ? (img.currentSrc || img.src) : '', alt: img ? img.alt : '', cap: cap ? cap.textContent : '' };
    });
    lbIndex = index;
    showLb();
    lb.hidden = false;
    document.body.classList.add('lb-open');
    var close = lb.querySelector('.lb-x');
    if (close) close.focus();
  }

  function showLb() {
    if (!lb || !lbSlides.length) return;
    lbIndex = (lbIndex + lbSlides.length) % lbSlides.length;
    var item = lbSlides[lbIndex];
    lbImg = lb.querySelector('img');
    lbCap = lb.querySelector('figcaption');
    if (lbImg) { lbImg.src = item.src; lbImg.alt = item.alt; }
    if (lbCap) lbCap.textContent = item.cap;
  }

  function closeLb() {
    if (!lb) return;
    lb.hidden = true;
    document.body.classList.remove('lb-open');
    if (lbImg) lbImg.removeAttribute('src');
  }

  if (lb) {
    lb.querySelector('.lb-x').addEventListener('click', closeLb);
    lb.querySelector('.lb-prev').addEventListener('click', function () { lbIndex--; showLb(); });
    lb.querySelector('.lb-next').addEventListener('click', function () { lbIndex++; showLb(); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') closeLb();
      if (e.key === 'ArrowRight') { lbIndex++; showLb(); }
      if (e.key === 'ArrowLeft') { lbIndex--; showLb(); }
    });
  }


  // Photo grid: open any photo in the lightbox, browse the whole set.
  document.querySelectorAll('[data-pgrid]').forEach(function (block) {
    var items = [].slice.call(block.querySelectorAll('.pg-item'));
    function open(n) {
      if (!lb) return;
      lbSlides = items.map(function (f) {
        var img = f.querySelector('img'); var cap = f.querySelector('figcaption');
        return { src: f.getAttribute('data-full') || (img && img.src), alt: img ? img.alt : '', cap: cap ? cap.textContent : '' };
      });
      lbIndex = n; showLb(); lb.hidden = false; document.body.classList.add('lb-open');
      var x = lb.querySelector('.lb-x'); if (x) x.focus();
    }
    items.forEach(function (f, n) {
      f.addEventListener('click', function () { open(n); });
      f.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(n); } });
    });
  });
  // Close the mobile menu after choosing a link.
  document.querySelectorAll('nav.main a').forEach(function (a) {
    a.addEventListener('click', function () { var t = document.getElementById('navt'); if (t) t.checked = false; });
  });
  document.querySelectorAll('[data-carousel]').forEach(setup);
})();
