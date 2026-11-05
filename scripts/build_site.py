"""Monta o site estático. Uso: python scripts/build_site.py (Python 3.9+)."""

from html import escape
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- INICIO_GALERIA -->"
END = "<!-- FIM_GALERIA -->"


def build(root=ROOT):
    root = Path(root)
    template = (root / "index.html").read_text(encoding="utf-8")
    if template.count(START) != 1 or template.count(END) != 1:
        raise ValueError("O index.html deve conter um par de marcadores da galeria.")
    before, rest = template.split(START)
    _, after = rest.split(END)
    pages = sorted((root / "pages").glob("*.html"), key=lambda p: p.name.lower())
    for page in pages:
        if page.is_symlink() or not page.is_file():
            raise ValueError(f"A página deve ser um arquivo HTML regular: {page.name}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*\.html", page.name):
            raise ValueError(f"Use letras minúsculas, números e hífens no nome: {page.name}")
        content = page.read_text(encoding="utf-8")
        if not re.search(r"<h1(?:\s[^>]*)?>.+?</h1>", content, re.I | re.S):
            raise ValueError(f"A página precisa de um h1 preenchido: {page.name}")
    links = "\n".join(
        f'        <li><a href="pages/{escape(p.name)}">{escape(p.stem)}</a></li>'
        for p in pages
    ) or "        <li>A primeira página da turma chegará em breve.</li>"
    output = root / "dist"
    if output.exists():
        shutil.rmtree(output)
    (output / "pages").mkdir(parents=True)
    for page in pages:
        shutil.copyfile(page, output / "pages" / page.name)
    (output / "index.html").write_text(
        before + START + "\n" + links + "\n        " + END + after,
        encoding="utf-8",
    )
    shutil.copyfile(root / "modelo.html", output / "modelo.html")
    (output / ".nojekyll").touch()
    print(f"Site pronto em {output}: {len(pages)} página(s).")
    return output


if __name__ == "__main__":
    build()
