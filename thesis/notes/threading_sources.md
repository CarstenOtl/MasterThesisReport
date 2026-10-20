# Threaded joints: textbook sources for Section 1.1

Purpose: back the motivation paragraph on threaded joints with one standard German and one standard English machine elements textbook. Only claims I could verify are kept.

## The two textbooks

| | German | English |
|---|---|---|
| Book | Maschinenelemente 1: Konstruktion und Berechnung von Verbindungen, Lagern, Wellen | Shigley's Mechanical Engineering Design |
| Authors | G. Niemann, H. Winter, B.-R. Höhn, K. Stahl | R. G. Budynas, J. K. Nisbett |
| Edition | 5th, Springer Vieweg, Berlin, Heidelberg, 2019. Print ISBN 978-3-662-55481-4, eBook ISBN 978-3-662-55482-1, DOI 10.1007/978-3-662-55482-1 | 11th, McGraw-Hill Education, New York, 2020 (catalogs list Jan 2019 as the release date; the book says © 2020), ISBN 978-0-07-339821-1 |
| Threaded joint chapter | Ch. 10 "Schraubenverbindungen, Gewinde", DOI 10.1007/978-3-662-55482-1_10 | Ch. 8 "Screws, Fasteners, and the Design of Nonpermanent Joints" |
| What I could read | The chapter abstract on Springer Professional | The chapter title, and the official McGraw-Hill lecture slides for Ch. 8 |

Niemann is on Springer Link through TUM, so page numbers can be added from there.

## Verified claims

| Claim for the thesis | Source | Evidence |
|---|---|---|
| Screws divide into fastening screws (Befestigungsschrauben) and motion screws (Bewegungsschrauben). A nut on a bolt is a fastening joint | Niemann Ch. 10 | Abstract, first sentence |
| A thread converts a large circumferential motion into a small axial motion and a small circumferential force into a large axial force | Niemann Ch. 10 | Abstract: "Wegübersetzung" and "Kraftübersetzung" |
| Assembling and securing threaded joints are design topics of their own | Niemann Ch. 10 | Abstract: "Montage und Sichern von Schraubenverbindungen" |
| Threaded fasteners make joints nonpermanent, for field assembly, disassembly, maintenance, and adjustment | Shigley Ch. 8 | Chapter title; reasons listed in the publisher's slides |
| Threads are standardized (ISO metric M series), and pitch is the distance between adjacent threads | Shigley Ch. 8 | Thread standards and definitions in the publisher's slides |

## Dropped claims

These were in the earlier list but couldn't be verified, so they stay out of the thesis:

- "Most widely used machine element"
- Mixed materials, no heat input, reusability, load capacity
- Preload control by tightening torque. Both books very likely cover it, but I haven't read the passage.

## Draft paragraph for Section 1.1

> Threaded fasteners join parts so that the joint can be released again, which enables field assembly, disassembly, maintenance, and adjustment~\cite{Budynas2020}. Their threads are standardized, so a metric nut fits any bolt of the same size and pitch~\cite{Budynas2020}. The thread converts a large rotation into a small axial travel and a small circumferential force into a large axial force~\cite{Niemann2019}, and assembling such a joint means turning the nut along the thread until it is seated~\cite{Niemann2019}.

The last clause leads into the automation question (how threading is automated today, and why dexterous hands).

## BibTeX (ready for `literature.bib`)

```bibtex
@book{Niemann2019,
  author    = {Niemann, Gustav and Winter, Hans and H{\"o}hn, Bernd-Robert and Stahl, Karsten},
  title     = {Maschinenelemente 1: Konstruktion und Berechnung von Verbindungen, Lagern, Wellen},
  edition   = {5},
  publisher = {Springer Vieweg},
  address   = {Berlin, Heidelberg},
  year      = {2019},
  isbn      = {978-3-662-55481-4},
  doi       = {10.1007/978-3-662-55482-1},
  language  = {german}
}

@book{Budynas2020,
  author    = {Budynas, Richard G. and Nisbett, J. Keith},
  title     = {Shigley's Mechanical Engineering Design},
  edition   = {11},
  publisher = {McGraw-Hill Education},
  address   = {New York},
  year      = {2020},
  isbn      = {978-0-07-339821-1}
}
```
