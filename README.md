# ASCON LIVING website
Static multilingual site, published from `docs/` via GitHub Pages.
- Add a language: create `content/<code>.json` (copy `content/en.json`), run `python3 build.py`. Only languages with a content file are published, linked in hreflang, picker and sitemap.
- Bilingual titles (HI, BN, UR, PA, DA, EL, FA, HE, KM, LO, MY): set `"title_suffix": " | Ho Chi Minh City villa"` in the content file.
- Fonts/RTL per language in `languages.json`. Shared facts in `facts.json`. Images: `tools/images.py` (real house photos only, EXIF stripped).
- `notes/keywords/` = keyword research (not published). Never use pool or parking wording.
