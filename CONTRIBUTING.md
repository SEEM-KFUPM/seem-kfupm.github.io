# Contributing to the SEEM Website

Thank you for helping maintain the SEEM website. Content should be accurate, publicly approved, clearly attributed, and supported by stable links or bibliographic records.

## Content locations

- Add or update member profiles in `people/profiles/`.
- Add project cards in `projects/items/` and full project pages in `projects/`.
- Add news posts in `news/posts/`.
- Add reviewed bibliographic records to `publications.bib` and cite them as `[@citation-key]`.
- Put reproducible teaching or research examples in `examples/`.
- Store reusable images and illustrations in `assets/` and provide descriptive alternative text wherever they appear.

## People and post attribution

Profile filenames act as stable member identifiers. Attribute a news post with a linked public byline and the corresponding member identifier:

```yaml
author:
  - name: Dr. Denis Anikiev
    url: /people/profiles/denis-anikiev.html
members: [denis-anikiev]
```

Use `author` for the reader-facing byline and `members` for automatic profile listings. Supply multiple authors and identifiers for collaborative posts.

## Projects and publications

Each public project should have a short listing record and a detail page explaining the problem, intended audience, key result or capability, and public links. Preserve upstream provenance for forked repositories and state publication or software status accurately.

Use one stable key per entry in `publications.bib`. Prefer DOI metadata from the publisher or Crossref, avoid duplicate preprint and final-paper records, and identify proceedings, preprints, software releases, and accepted or in-press work clearly.

## Reproducible content

Declare Python dependencies in `requirements.txt`, use deterministic random seeds where appropriate, and keep reviewed notebook output in `_freeze/`. Do not commit secrets, API keys, private datasets, or generated `_site/` output.

## Review checklist

Before opening a pull request:

1. Confirm names, affiliations, dates, links, publication status, and image permissions.
2. Render the complete website with `QUARTO_PYTHON=.venv/bin/python quarto render`.
3. Run `python scripts/check_internal_links.py _site`.
4. Review the affected pages in both light and dark themes and at narrow and wide screen sizes.
5. Update `CHANGELOG.md` when the change is notable to website visitors or maintainers.

Content changes should be submitted through a pull request and reviewed before publication.
