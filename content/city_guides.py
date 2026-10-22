"""Assemble en/de/ko/ja city guides for build.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from guides_en import ALSO as EN_ALSO
from guides_en import HUB as EN_HUB
from guides_en import PAGES as EN_PAGES
from guides_en import UI as EN_UI
from guides_en import cards as en_cards
from guides_de import ALSO as DE_ALSO
from guides_de import HUB as DE_HUB
from guides_de import PAGES as DE_PAGES
from guides_de import UI as DE_UI
from guides_de import cards as de_cards
from guides_ko import ALSO as KO_ALSO
from guides_ko import HUB as KO_HUB
from guides_ko import PAGES as KO_PAGES
from guides_ko import UI as KO_UI
from guides_ko import cards as ko_cards
from guides_ko_more import MORE as KO_MORE
from guides_ko_rest import REST as KO_REST
from guides_ko_tail import TAIL as KO_TAIL
from guides_ko_last import LAST as KO_LAST
from guides_ja import ALSO as JA_ALSO
from guides_ja import HUB as JA_HUB
from guides_ja import PAGES as JA_PAGES
from guides_ja import UI as JA_UI
from guides_ja import cards as ja_cards
from guides_ja_b import MORE as JA_MORE
from guides_ja_c import REST as JA_REST

KO_PAGES.update(KO_MORE)
KO_PAGES.update(KO_REST)
KO_PAGES.update(KO_TAIL)
KO_PAGES.update(KO_LAST)
JA_PAGES.update(JA_MORE)
JA_PAGES.update(JA_REST)

_REL = ["guide-sights", "guide-coffee", "guide-arrival", "home"]


def _pack(ui, hub, cards, pages, also):
    return {
        "ui": ui,
        "hub_h2": hub,
        "hub_cards": cards,
        "hub_related": list(_REL),
        "also": also,
        "pages": pages,
    }


GUIDES = {
    "en": _pack(EN_UI, EN_HUB, en_cards(), EN_PAGES, EN_ALSO),
    "de": _pack(DE_UI, DE_HUB, de_cards(), DE_PAGES, DE_ALSO),
    "ko": _pack(KO_UI, KO_HUB, ko_cards(), KO_PAGES, KO_ALSO),
    "ja": _pack(JA_UI, JA_HUB, ja_cards(), JA_PAGES, JA_ALSO),
}
