"""Helpers for the city-guide pages merged by build.py."""

def page(title, description, h1, lead, sections, related):
    return {
        "title": title,
        "description": description,
        "h1": h1,
        "lead": lead,
        "toc": True,
        "book": True,
        "related": related,
        "sections": [{"h2": h, "p": ps if isinstance(ps, list) else [ps]} for h, ps in sections],
    }

def ui(toc, book_line, book_btn, related_h):
    return {"toc_label": toc, "book_line": book_line, "book_btn": book_btn, "related_h": related_h}
