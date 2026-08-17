# SEEM · KFUPM Website

Official website of the **Smart Earth Exploration and Monitoring (SEEM)** research group at the College of Petroleum Engineering & Geosciences, King Fahd University of Petroleum and Minerals.

**Website:** [https://seem-kfupm.github.io/](https://seem-kfupm.github.io/)

This repository contains the production Quarto website, including the group's research themes, members, publications, public software projects, news, and contact information.

## Highlights

- Responsive Quarto site with search, light and dark themes, and accessible navigation.
- Member profiles, publications, public research software, news, and reproducible computational examples.
- Automated rendering and internal-link validation with GitHub Actions.

## Local development

Quarto 1.10.18 and Python 3.12 are the tested development environment.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
QUARTO_PYTHON=.venv/bin/python quarto preview
```

Render the complete static website with:

```sh
QUARTO_PYTHON=.venv/bin/python quarto render
```

Validate the rendered site with:

```sh
python scripts/check_internal_links.py _site
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for content locations, attribution metadata, bibliography updates, review expectations, and the contributor checklist.

The canonical address is configured in `_quarto.yml`. Pull requests are rendered and checked before publication.
