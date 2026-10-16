# Master's Thesis — Documentation

**Author:** Carsten Oertel
**University:** Technical University of Munich (TUM)
**Chair:** Robotics, Artificial Intelligence and Real-time Systems (I6/AIR)
**Supervisor:** Prof. Knoll | **Advisor:** Chi Zhang
**Industry Partner:** Antonio Gonzales Marin

Documentation repository for my master's thesis, written against the AIR LaTeX templates. The thesis builds on the NUTS paper (*Learning Long-Horizon Cyclic Nut Threading via Hybrid-Teacher Policy Distillation*). The code lives in the separate [forgeUltra](https://github.com/CarstenOtl/forgeUltra) repository (`~/code/forgeUltra/`).

## Structure

- `expose/`: expose document (`AIRStudentExpose` template). **Finished and frozen; do not edit.**
- `thesis/`: master's thesis (`AIRStudentThesis` template). **Work in progress.**
  - `main.tex`: root LaTeX file.
  - `source/`: abstract, chapters (`chapterNN.tex`), appendix, and the bibliography files:
    - `literature.bib`: the thesis bibliography (registered in `main.tex`).
    - `library.bib`: my full reading library. Not registered; cited entries are copied into `literature.bib`.
  - `figures/`: figures used in the document.
  - `AIRlatex.cls`: AIR class file (vendored from the template).
- `additional/`: reference material, each PDF with a plain-text `.md` conversion next to it:
  - `SemesterThesis`: my semester thesis (DAgger-based distillation of a privileged grasping policy). Structure reference.
  - `chi_master_thesis_final_signed`: Chi Zhang's master's thesis. Structure reference for a full master's report.
  - `NUTS`: the conference paper submitted on this project. Main content source.

## Latest PDFs

- Expose (final): [`expose/main.pdf`](expose/main.pdf)
- Thesis (draft): [`thesis/main.pdf`](thesis/main.pdf)

## Building from Source

Requires a TeX Live installation with `pdflatex` and `biber`.

```bash
cd thesis
latexmk -pdf main.tex
```

Or manually:

```bash
cd thesis
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Build artifacts are ignored by `.gitignore`; only sources and `main.pdf` are tracked.

## Reference PDFs → Markdown

Reference PDFs in `additional/` get a plain-text sibling for searching and for AI-assisted writing (reading the PDFs directly is too expensive):

```bash
pdftotext -layout additional/<name>.pdf additional/<name>.md
```

## Editor Setup

### Option A — VSCode (recommended)

1. Install [TeX Live](https://tug.org/texlive/) (full installation)
2. Install the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension
3. Create `.vscode/settings.json` (ignored by git, so it stays local) with the build recipe `pdflatex → biber → pdflatex × 2`, auto-build on save, and PDF-in-tab viewing.
4. Open `thesis/main.tex`. The PDF builds automatically on save (`Ctrl+S`).
   View the PDF with `Ctrl+Alt+V`. Click in the PDF to jump to source (SyncTeX).

### Option B — TeXstudio

1. Install [TeX Live](https://tug.org/texlive/) (full installation)
2. Install [TeXstudio](https://www.texstudio.org/)
3. Enable `-shell-escape`:
   *Options → Configure TeXstudio → Commands*
   Set **PdfLaTeX** to:

   ```text
   pdflatex -synctex=1 -shell-escape -interaction=nonstopmode %.tex
   ```

4. Set biber as bibliography backend:
   *Options → Configure TeXstudio → Build*
   Set **Default Bibliography Tool** to `txs:///biber`
5. **Optional — autocomplete for AIRlatex commands:** Copy `AIRlatex.cwl` from the AIR templates repo (`AIRlatex/AIRTemplates/AIRlatex.cwl`) to:
   - Windows: `%APPDATA%\texstudio\completion\user\`
   - Linux/Mac: `~/.config/texstudio/completion/user/`

   This adds completions for commands like `\vec{}`, `\diff{}{}`, `\mat{}`, etc.
   *(VSCode does not need this — LaTeX Workshop scans the `.cls` file automatically.)*

6. Open `thesis/main.tex` and compile with `F5`.
