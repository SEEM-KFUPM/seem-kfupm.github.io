# SEEM — KFUPM website prototype

This repository contains a HugoBlox prototype for the Smart Earth Exploration Monitoring (SEEM) Group at King Fahd University of Petroleum and Minerals.

The site is intentionally a **prototype**: the public organization description, selected SeisReconNO project, and publication record are verified from SEEM’s public GitHub presence. People, news, contact details, and recruitment text that await approval are visibly marked as samples.

The header uses the KFUPM logo supplied in the associated SEEM website decision package. No SEEM logo has been invented.

## Technology

- Hugo Extended `0.165.0` locally; the HugoBlox starter pins its CI build version in [`hugoblox.yaml`](hugoblox.yaml).
- HugoBlox kit module `v0.12.0`, based on starter commit `66efb1916bd62287ea2fef3caacb1245b2f34da2`.
- Node dependencies are recorded in `package.json` and `pnpm-lock.yaml`.
- GitHub Pages workflows are present but deployment remains disabled until a reviewed prototype is merged to `main` and Pages is explicitly enabled in GitHub settings.

## Local preview

Install the frontend dependencies once after cloning the repository:

```sh
pnpm install --frozen-lockfile
```

Run this command again only when `package.json` or `pnpm-lock.yaml` changes.

For everyday development, start the local server:

```sh
hugo server --disableFastRender
```

Open the local address Hugo reports, normally <http://localhost:1313/>. To make a production build and refresh the static search index:

```sh
pnpm run build
```

## Content workflow

| Content | Location | Normal update |
| --- | --- | --- |
| Homepage and landing pages | `content/**/_index.md` | Edit block-based YAML front matter. |
| People | `data/authors/*.yaml` | Add an approved profile and matching photo in `assets/media/authors/`. |
| Projects/software | `content/projects/<slug>/index.md` | Add a short public explanation and Code/Paper/Demo/Data links. |
| Publications | `publications.bib` and `content/publications/<slug>/` | Update BibTeX, import, review the generated bundle, then commit it. |
| News | `content/blog/<slug>/index.md` | Add a dated Markdown update and approved visual when available. |

### Import publications

The `academic` CLI is installed separately through Pipx. It converts the shared source file into reviewable Hugo content; do not edit bibliography text in two places.

```sh
academic import publications.bib /tmp/seem-publication-import --compact
```

Review the generated folder, merge the intended `index.md` and `cite.bib` into `content/publications/`, then test with `pnpm run build`.

## Before publication

- Replace the prototype team card, news post, and contact/recruitment placeholders with approved content.
- Add approved imagery and confirm KFUPM brand use.
- Check keyboard navigation, text alternatives, contrast, and the layout at phone, tablet, and desktop widths.
- Push the reviewed work to a pull request; only then enable GitHub Pages with the GitHub Actions source.
