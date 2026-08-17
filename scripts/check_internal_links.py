"""Fail when rendered HTML references a missing local file."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlparse


SITE = Path(__file__).resolve().parents[1] / "_site"


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.references.append(("href", values["href"] or ""))
        if tag in {"img", "script", "source"} and values.get("src"):
            self.references.append(("src", values["src"] or ""))
        if tag == "link" and values.get("href"):
            self.references.append(("href", values["href"] or ""))


def target_for(page: Path, reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:")):
        return None

    path = unquote(parsed.path)
    if not path:
        return None

    target = SITE / path.lstrip("/") if path.startswith("/") else page.parent / path
    if target.is_dir() or path.endswith("/"):
        target /= "index.html"
    return target.resolve()


def main() -> None:
    missing: list[str] = []
    pages = sorted(SITE.rglob("*.html"))
    for page in pages:
        parser = ReferenceParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for kind, reference in parser.references:
            target = target_for(page, reference)
            if target is not None and not target.exists():
                missing.append(f"{page.relative_to(SITE)}: {kind}={reference}")

    stylesheets = sorted(SITE.rglob("*.css"))
    for stylesheet in stylesheets:
        css = stylesheet.read_text(encoding="utf-8")
        for raw_reference in re.findall(r"url\(([^)]+)\)", css):
            reference = raw_reference.strip().strip("\"'")
            target = target_for(stylesheet, reference)
            if target is not None and not target.exists():
                missing.append(f"{stylesheet.relative_to(SITE)}: url={reference}")

    if missing:
        raise SystemExit("Missing internal references:\n" + "\n".join(missing))

    print(
        f"Checked {len(pages)} HTML pages and {len(stylesheets)} stylesheets: "
        "all local targets exist."
    )


if __name__ == "__main__":
    main()
