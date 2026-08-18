# SEEM · KFUPM Website

Official website of the **Smart Earth Exploration and Monitoring (SEEM)** research group at the College of Petroleum Engineering & Geosciences, King Fahd University of Petroleum and Minerals.

**Website:** [https://seem-kfupm.github.io/](https://seem-kfupm.github.io/)

This repository contains the production Quarto website, including the group's research themes, members, publications, public software projects, blog, and contact information.

## Highlights

- Responsive Quarto site with search, light and dark themes, and accessible navigation.
- Member profiles, publications, public research software, blog posts, and reproducible computational examples.
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

## Licensing

This repository uses separate licenses for software and website content:

- **Software — MIT License.** Source code, scripts, stylesheets, Quarto configuration, templates, and other software are licensed under the [MIT License](LICENSE). It permits reuse, modification, redistribution, and commercial use while requiring preservation of the copyright and license notice.
- **Original content — CC BY 4.0.** Original website text and original SEEM illustrations are licensed under the [Creative Commons Attribution 4.0 International License](CONTENT-LICENSE.md). It permits sharing and adaptation, including commercial use, provided that SEEM · KFUPM is credited, the license is linked, and modifications are identified.

The content license excludes institutional names, logos, trademarks and branding; portraits, photographs and personal information unless explicitly marked; third-party figures, media, quotations and publication content; linked external material; and content, software or data governed by another project's license. These materials remain subject to their respective rights and may require separate permission.

See [CONTENT-LICENSE.md](CONTENT-LICENSE.md) for the complete scope, attribution guidance, and exclusions. The two licenses apply by material type: CC BY 4.0 does not replace the MIT License for code, and the MIT License does not grant rights to excluded website media or institutional branding.
