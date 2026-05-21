# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

LaTeX documentation repo for a master's thesis. It holds writing deliverables (expose now, thesis later) — there is no application code, no test suite, no lint config. Treat tasks here as document authoring, not software engineering.

## Build

The expose builds with `latexmk` from inside the document folder (biber + alphabetic bibliography style):

```powershell
cd expose
latexmk -pdf main.tex
```

There is no top-level build script — each document folder is self-contained (each carries its own `AIRlatex.cls`). Build artifacts (`.aux`, `.log`, `.bbl`, `.out`, `.toc`, …) are currently **not** ignored by `.gitignore`; `expose/main.pdf` is intentionally committed for now.

## Architecture

### Per-document folders, seeded from AIR templates

Each document type lives in its own top-level folder (currently only `expose/`; `thesis/` will be added later). Folders are seeded by copying the **contents** of the matching template from the sibling repo `..\AIRlatex\AIRTemplates\` — student variants for this master's thesis:

| Folder           | Template source                                         |
| ---------------- | ------------------------------------------------------- |
| `expose/`        | `..\AIRlatex\AIRTemplates\AIRStudentExpose\`            |
| `thesis/` (TBD)  | `..\AIRlatex\AIRTemplates\AIRStudentThesis\`            |

Each folder vendors its own `AIRlatex.cls`, so the document is self-contained after copy. When scaffolding a new document, copy contents into the new folder (not the template folder as a subdir).

### The AIRlatex class drives document type

`main.tex` selects the document style via a class option on `\documentclass{AIRlatex}`:

- `AIRstudentexpose` — expose layout (current)
- `AIRstudentthesis` — thesis layout
- `AIRstudentpresentation` — beamer-style presentation

Bibliography tool and style are also class options (`optBiber`, `optBibstyleAlphabetic`); language is `optEnglish` or its German counterpart.

### Bilingual content macro

Content uses `\AIRlangGerEng{<German>}{<English>}` so the same source compiles in either language — only the `optEnglish` class option switches output. When editing prose, preserve both arms of these macros even if only one is being actively written; do not collapse them to one language.

### Title page is type-specific

The title page comes from a typed macro chosen for the work being submitted, e.g. `\AIRstudentexposeTitlePageMastersThesis{...}` for this expose (other variants for Bachelor / Semester / IDP are commented in `main.tex`). Switching work type means switching this macro, not editing arguments of a generic one.

### Figures and bibliography

- `figures/` mixes `.png`, `.pdf`, `.tikz`, and Inkscape `.pdf_tex` figures — each has its own inclusion pattern in `main.tex` worth copying when adding new figures.
- Bibliography is a single `.bib` file at `source/literature.bib`, registered via `\addbibresource`.

## Conventions when extending the repo

- New document type → new top-level folder seeded from the matching `AIRStudent*` template (contents-into-folder).
- Keep `AIRlatex.cls` vendored per-document-folder; do not deduplicate to a shared location.
- Author bilingually via `\AIRlangGerEng{}{}` rather than hard-coding one language.
