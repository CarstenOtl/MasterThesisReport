# Master's Thesis — Documentation

Documentation repository for my master's thesis. Contains the expose and (later) the thesis itself, both written against the AIR LaTeX templates.

## Structure

- `expose/` — expose document (AIRStudentExpose template).
  - `main.tex` — root LaTeX file.
  - `source/` — chapter/section sources.
  - `figures/` — figures used in the document.
  - `AIRlatex.cls` — AIR class file (vendored from the template).

The `thesis/` folder will be added once expose work is underway.

## Building

The expose builds with a standard LaTeX toolchain (e.g. `latexmk -pdf main.tex` from `expose/`).
