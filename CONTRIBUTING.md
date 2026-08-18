# Contributing to the SEEM Website

Thank you for helping maintain the SEEM website. Content should be accurate, publicly approved, clearly attributed, and supported by stable links or bibliographic records.

## Website update workflow

All work is done in this public repository; contributors do not need forks. An authorized contributor must be a member of the [SEEM-KFUPM organization](https://github.com/SEEM-KFUPM) and must be given **Write** access so they can push their own branch. Protected-branch rules prevent contributors from updating `dev` or `main` directly.

| Role | Responsibility |
| --- | --- |
| Contributor | Is a SEEM-KFUPM organization member who creates a branch in this repository and opens a pull request (PR) to `dev`. |
| [**SEEM Website Team**](https://github.com/orgs/SEEM-KFUPM/teams/seem-website-team) | Reviews and merges contributor PRs into `dev`, may update `dev` directly, checks the integrated website, and opens release PRs from `dev` to `main`. |
| SEEM Website admins / owner | Gives final approval to a release PR to `main` to actually update the website. |

The complete update path is:

1. Contributor branch → PR to `dev`.
2. A SEEM Website Team member approves and merges the PR.
3. The team checks the combined website on `dev`.
4. A SEEM Website Team member opens a `dev` → `main` PR.
5. The designated administrator or owner approves it.
6. A SEEM Website Team member merges it, and GitHub Pages deploys `main`.

Contributors must never push directly to `dev` or `main`, and their PRs must not target `main`. SEEM Website Team members may update `dev` directly when necessary. Nobody may push directly to `main`; every production update must use a reviewed `dev` → `main` PR. Because the repository is public, GitHub may still allow a non-member to open a PR from a fork; such PRs are outside this contribution workflow and should be closed without merging.

### Archived prototypes

The `quarto` and `hugoblox` branches contain earlier website prototypes built with [Quarto](https://quarto.org/) and [HugoBlox](https://hugoblox.com/), respectively. They are retained as read-only archives and are not part of the production workflow. Either may be used as the starting point for a separate website. New work for the current website must branch from `dev`.

## Contributor steps

Before starting, accept the invitation to join the SEEM-KFUPM organization and confirm that you have Write access to this repository. Then clone the repository and create a clearly named branch from the latest remote `dev` branch. Do not modify `dev` itself.

### 1. Create your branch

In the examples below, `content/update-people-page` is the name of a new branch. It is not a folder or a special Git command. Choose a name that briefly describes your change, and use that same name in each later command.

A branch name should:

- start with a category such as `content/`, `fix/`, or `design/`;
- use lowercase words separated by hyphens;
- contain no spaces; and
- describe one specific change.

Examples include:

- `content/update-people-page`
- `content/add-research-project`
- `fix/publication-link`
- `fix/member-photo`
- `design/improve-mobile-menu`

The following example creates a branch for updating the People page:

```sh
git clone https://github.com/SEEM-KFUPM/seem-kfupm.github.io.git
cd seem-kfupm.github.io
git fetch origin
git switch -c content/update-people-page origin/dev
```

These commands perform the following steps:

1. `git clone` downloads a working copy of the repository.
2. `cd` enters the downloaded repository directory.
3. `git fetch origin` downloads the latest branch information from GitHub without changing any files.
4. `git switch -c content/update-people-page origin/dev` creates and switches to the new `content/update-people-page` branch, using the latest remote `dev` branch as its starting point. The `-c` option means “create a new branch.”

`origin` is the name Git automatically gives to the GitHub repository from which it was cloned. `origin/dev` means the current `dev` branch stored on GitHub.

You can confirm which branch is active with `git branch --show-current`. It should print your new branch name, not `dev` or `main`.

### 2. Save and push your change

Make and validate one focused change, then push the branch:

```sh
git add <changed-files>
git commit -m "Describe the website change"
git push -u origin content/update-people-page
```

Here, `git add` selects files for the change, `git commit` records the selected changes locally with a short description, and `git push` uploads the new branch and its commits to GitHub.

Replace `<changed-files>` with the files you changed, for example:

```sh
git add people/index.qmd
```

The first push must use the same branch name created above. The `-u` option connects the local branch to its GitHub branch; after that, additional commits can be uploaded with the shorter command `git push`.

### 3. Open the pull request

Open a PR with the contributor branch as the **compare** branch and `dev` as the **base** branch. The compare branch contains the proposed changes; the base branch is where the changes will go after approval. Describe what changed, identify pages requiring visual review, and cite sources used to verify factual content. Address review comments by pushing more commits to the same branch.

The contributor branch is deleted from GitHub after the PR is merged. This does not delete the completed changes, because they have already been added to `dev`. Ask the Website Team to merge only when all planned work for that PR is complete, all review comments have been addressed, and the final checks pass. If another change is needed after the merge, create a new branch from the latest `origin/dev` instead of trying to reuse the deleted branch.

## Review and publication

For a contributor PR to `dev`, a SEEM Website Team member checks the content and layout, waits for the Quarto build check, requests any necessary corrections, and confirms that the contributor's work is complete. The team member then **squash merges** the approved PR and deletes its contributor branch.

A Website Team member who updates `dev` directly must complete the same review and validation locally before pushing, because the direct-push bypass skips the PR approval and required checks.

When `dev` is ready for publication, a SEEM Website Team member opens a PR with `main` as the base and `dev` as the compare branch. After the required administrator or owner approves it and all checks pass, a team member uses **Create a merge commit**. Do not squash or rebase this release PR; keeping the `dev` commits as ancestors of `main` prevents published changes from reappearing in later release PRs.

After merging, the team confirms that the GitHub Pages deployment succeeded and checks the production website.

## Administrator setup

### Access and teams

1. Keep the repository **Public** and `main` as its default branch.
2. Add each contributor as a member of the **SEEM-KFUPM** organization; do not use the outside-collaborator role for this workflow.
3. Give each contributor **Write** access, directly or through an organization team. Write access is necessary to push branches inside the repository.
4. Give **SEEM Website Team** **Write** access and add the editors who may review and merge into `dev` or `main`.
5. Create **SEEM Website Approvers**, add the designated administrator or owner, and give the team **Write** access so its approval can satisfy a required-review rule. The person may retain Admin or organization Owner permissions separately.
6. Allow both **squash merging** and **merge commits** under **Settings > General > Pull Requests**.
7. Enable **Automatically delete head branches** so merged contributor branches are removed from the repository.

The final approver cannot approve their own PR. A different Website Team member should therefore open the `dev` → `main` PR when the designated approver is also a Website Team member.

### Protect `dev`

Under **Settings > Rules > Rulesets**, create an active branch ruleset named `Protect dev` that targets only `dev`:

- Add **SEEM Website Team** to the bypass list with **Always allow** so its members may update `dev` directly.
- Require a pull request and one approval from **SEEM Website Team** for the `**` file pattern.
- Dismiss approvals when new commits are pushed and require all conversations to be resolved.
- Require the `render` job from **Quarto build check** to pass and require the branch to be up to date.
- Allow only squash merges.
- Restrict deletion and block force pushes.

Because contributors have Write access, also create a classic branch protection rule for `dev` and set **Restrict who can push to matching branches** to **SEEM Website Team**. This makes the team the only group that can complete a merge into `dev`; the ruleset still requires its review and checks.

### Protect `main`

Create an active branch ruleset named `Protect main` that targets only `main`:

- Do not add any bypass actors; the rule must also apply to administrators and organization owners.
- Require a pull request and one approval from **SEEM Website Approvers** for the `**` file pattern.
- Dismiss approvals when new commits are pushed and require all conversations to be resolved.
- Require the `render` job to pass and require the branch to be up to date.
- Allow only merge commits; do not require linear history.
- Restrict deletion and block force pushes.

Also create a classic branch protection rule for `main` and set **Restrict who can push to matching branches** to **SEEM Website Team**. This lets the team merge only after the designated approver and required checks have approved the release.

GitHub does not provide a native rule limiting who may open a PR. “Only a Website Team member opens a PR to `main`” is therefore a team policy. Safety is still enforced because only the team can merge into `main` and the designated approver must approve. A required GitHub Actions check can additionally reject any PR to `main` whose compare branch is not `dev`.

### GitHub Pages

The deployment must run only after a merge to `main`. Under **Settings > Pages > Build and deployment**, select **GitHub Actions** and use a deployment workflow triggered by pushes to `main`.

The existing `.github/workflows/quarto-check.yml` validates PRs but does **not** deploy Pages. A deployment job or workflow must still be added. Follow the [GitHub Pages custom Actions guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) and the [Quarto GitHub Pages guidance](https://quarto.org/docs/publishing/github-pages.html).

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
