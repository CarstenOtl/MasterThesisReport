# Master's Thesis — Documentation

**Author:** Carsten Oertel
**University:** Technical University of Munich (TUM)
**Chair:** Robotics, Artificial Intelligence and Real-time Systems (I6/AIR)
**Supervisor:** Prof. Knoll | **Advisor:** Chi Zhang
**Industry Partner:** Antonio Gonzales Marin

Documentation repository for my master's thesis. Contains the expose and (later) the thesis itself, both written against the AIR LaTeX templates.

## Structure

- `expose/` — expose document (`AIRStudentExpose` template).
  - `main.tex` — root LaTeX file.
  - `source/` — chapter/section sources.
  - `figures/` — figures used in the document.
  - `AIRlatex.cls` — AIR class file (vendored from the template).

The `thesis/` folder will be added once expose work is signed off.

## Latest PDF

The most recent compiled version of the expose can be found at:

[`expose/main.pdf`](expose/main.pdf)

## Building from Source

Requires a TeX Live installation with `pdflatex` and `biber`.

```bash
cd expose
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Or, with `latexmk`:

```bash
cd expose
latexmk -pdf main.tex
```

## Editor Setup

### Option A — VSCode (recommended)

1. Install [TeX Live](https://tug.org/texlive/) (full installation)
2. Install the [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension
3. Open the repo in VSCode — the workspace settings in [`.vscode/settings.json`](.vscode/settings.json) already configure the build recipe (`pdflatex → biber → pdflatex × 2`), auto-build on save, and PDF-in-tab viewing.
4. Open `expose/main.tex` — the PDF will build automatically on save (`Ctrl+S`).
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
5. **Optional — autocomplete for AIRlatex commands:** Copy `AIRlatex.cwl` from the AIR templates repo (`..\AIRlatex\AIRTemplates\AIRlatex.cwl`) to:
   - Windows: `%APPDATA%\texstudio\completion\user\`
   - Linux/Mac: `~/.config/texstudio/completion/user/`

   This adds completions for commands like `\vec{}`, `\diff{}{}`, `\mat{}`, etc.
   *(VSCode does not need this — LaTeX Workshop scans the `.cls` file automatically.)*

6. Open `expose/main.tex` and compile with `F5`.
