# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to a simple date-based versioning.

## 2026-08-18

### Added

- Added retrospective blog stories covering SEEM research releases, workshops, presentations, visitors, collaborations, and student achievements.
- Added automatic hero images to Blog post pages using each post's existing image metadata.
- Added a CC BY 4.0 license for original website text and illustrations, with attribution guidance and explicit exclusions.
- Added official KFUPM undergraduate and research-based graduate study pathways to the homepage and Join / Contact page.
- Added a “How to find us” section with an embedded map, Google Maps link, and official CPG campus directions for Building 76.

### Changed

- Replaced the Blog grid with a framed chronological list that displays image thumbnails and groups posts automatically by year.
- Activated the Blog listing, author profile associations, and RSS feed, renamed the section source folder to `blog/`, and linked the AI Coding Agents Workshop project page to its event recap.
- Renamed “Projects & Software” to “Projects,” divided the catalog into Research and Education sections, moved the AI Coding Agents Workshop into Education, added quick-navigation buttons, and replaced the repository-centric introduction.
- Renamed the visitor-facing News section to Blog in the navigation, page title, introductory copy, and member profile headings.
- Updated the GitHub Actions workflow to use Node.js 24-compatible actions and run on pushes to `quarto`, `dev`, and `main`.
- Added GitHub Pages deployment after successful `main` branch rendering and link validation.
- Documented the code/content dual-license model in the README and added CC BY 4.0 and “Powered by Quarto” footer links beside GitHub.
- Expanded the contribution guide with the organization-member branch workflow, `dev` review and `main` approval rules, repository protection settings, archived prototype branches, beginner Git instructions, and post-merge branch cleanup.
- Refined the explainable AI illustration by removing stray diagram nodes and aligning the P- and S-wave bands with the first two arrivals.
- Renamed the homepage “Selected work” section to “Selected projects,” summarized its four research examples, and linked to the full project catalog.
- Refocused the “Work with SEEM” and Join / Contact introductions on study pathways, the SEEM team, and the group's CPG affiliation.

## 2026-08-17

### Added

- Added profiles for Dr. Umair bin Waheed and Dr. Denis Anikiev, with portraits, biographies, links, and member-specific news listings.
- Added linked author metadata and stable member identifiers for associating posts with profiles.
- Added cards and detail pages for public, visitor-facing SEEM-KFUPM repositories, with project-specific illustrations and provenance notes.
- Expanded the bibliography to project-linked and recent SEEM-member publications.
- Added contributor guidance for content, attribution, publications, reproducibility, and review.

### Changed

- Made Quarto's full-width page layout the site-wide default so inner-page content uses the same wider layout as the homepage.
- Improved People cards with circular portraits and explicit profile ordering.
- Updated the projects catalog and navigation to represent the complete public repository collection.
- Reworked the README as concise production-site documentation and moved authoring guidance to `CONTRIBUTING.md`.
- Hid prototype notebook, sample-news, editorial, and recruitment content from the production render while retaining the options in source.
- Replaced homepage prototype cards with public projects and limited the build to visitor-facing website pages.
- Updated the News page and navigation with an “updates coming soon” placeholder.
- Rebuilt the Research and homepage themes around Monitoring, Imaging, Sensing, and Modeling, supported by current projects and publications.
- Expanded homepage selected work to one representative project for each research topic.
- Organized the People page into senior researchers, students, and alumni, with verified public profile links and a hidden postdocs placeholder.

## 2026-08-16

### Added

- Added Quarto's native light/dark theme switch beside the GitHub icon, with a custom SEEM dark palette, system-theme detection, and persistent visitor preference.
- Added the CPG logo to the centered footer on every page, using the black version in light mode and the white version in dark mode.

### Changed

- Linked the footer's College of Petroleum Engineering & Geosciences and KFUPM labels to their corresponding official websites.
- Updated the homepage eyebrow to read “Smart Earth Exploration and Monitoring · CPG · KFUPM”.

## 2026-08-13

### Added

- Initial prototype of the quarto-based website
