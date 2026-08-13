# SEEM website — Quarto prototype

This branch is a from-scratch Quarto implementation of the Smart Earth Exploration and Monitoring group website. It starts from the repository's minimal `main` branch and reuses only the approved SEEM/KFUPM logos, Omnes fonts, and high-level content concept from the parallel HugoBlox prototype.

## What this prototype demonstrates

- The agreed navigation: Home, Research, People, Publications, Projects & Software, News, and Join / Contact.
- Metadata-driven Quarto listings for people, projects, and news.
- Site search, RSS, responsive cards, accessible focus states, and descriptive image text.
- A shared BibTeX source for project, publication, and notebook citations.
- An executable Python/Jupyter page with a generated figure, computed table, cross-references, folded code, callouts, and tabsets.
- A build-check workflow for the `quarto` branch. It uploads the rendered site as an artifact but does **not** deploy over the live organization site.

All unapproved people, news, recruitment, and contact content is explicitly labeled as placeholder material.

## Local setup

Quarto 1.10.18 is the tested renderer.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
QUARTO_PYTHON=.venv/bin/python quarto preview
```

Render the static site:

```sh
QUARTO_PYTHON=.venv/bin/python quarto render
```

The output is written to `_site/`. Quarto's `freeze: auto` stores notebook results in `_freeze/`, which should be committed so normal CI builds do not need to re-execute older computational pages.

## Content workflow

- Add a profile under `people/profiles/`.
- Add a project listing record under `projects/items/` and, when needed, a longer project page under `projects/`.
- Copy `news/posts/prototype-workflow.qmd` for a short update.
- Add reviewed bibliographic records to `publications.bib` and cite them as `[@citation-key]`.
- Put research teaching examples under `examples/`; declare every dependency in `requirements.txt` and use a deterministic random seed.

Every substantive change should be reviewed in a pull request. People, projects, positions, and institutional language should include an owner and review date before launch.

## Publishing decision

The included GitHub Action validates and preserves a rendered artifact. It intentionally does not publish to `gh-pages`, because this experimental branch should not replace the current organization site without an explicit decision. When the Quarto version is selected for production, configure the repository's Pages source and add the official Quarto publish action as a separate reviewed change.
