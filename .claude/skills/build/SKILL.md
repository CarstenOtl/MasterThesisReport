---
name: build
description: Build the thesis PDF with latexmk and report only a compact summary (errors, undefined refs/citations, overfull boxes). Use when the user types "build" or asks to compile the thesis.
---

Run the build script and relay its output verbatim. Do not read `main.log` or `main.pdf` yourself unless the summary shows an error you need to locate.

```bash
.claude/skills/build/build.sh
```

Optional argument: a document folder other than `thesis` (default). `expose/` is frozen and the script refuses it.

Output format:
- `BUILD OK: main.pdf, N pages` followed by one line of counts, plus up to 10 undefined refs/citations and the 5 worst overfull boxes.
- `BUILD FAILED` followed by the first LaTeX error and up to 5 biber errors.

After relaying the summary, stop. Only fix problems if the user asks.
