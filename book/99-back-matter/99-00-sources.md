# Sources and a note on method

This book was written against sources rather than from memory, in keeping with its own premise: that the component-level engineering of electric cars is knowable, but scattered, and that the honest thing is to ground each claim and flag what remains uncertain.

**Where the sources live.** Every subchapter ends with its own short source list, naming the specific material behind that subchapter's claims. That is the real bibliography of this book, distributed through it, and it is where to look to check any particular figure or statement. This page does not repeat all of it. Instead it names the recurring wells that the whole book drew from, and explains how their claims were weighted.

**The recurring sources.** A handful of sources appear again and again, because they are the places where component-level EV engineering is actually documented for a general-but-serious reader:

- **Munro & Associates / Munro Live (leandesign.com and associated teardowns).** Physical teardowns of real cars — the octovalve, the structural pack, the 4680 cell, the steer-by-wire system. When this book says something was "found by teardown," this is usually the source. Teardown findings are strong evidence for *what is physically in the car* and weaker for *why*, so they are often paired with the `[INFERENCE]` tag.
- **E-Mobility Engineering (emobility-engineering.com) and Battery Design (batterydesign.net).** Trade-press and specialist engineering analysis — pack architecture, the octovalve, thermal systems. Excellent for mechanism and reasoning.
- **U.S. Department of Energy / EPA (fueleconomy.gov).** The canonical, non-partisan source for energy-loss and efficiency figures, used throughout Chapter 1 and the synthesis chapters.
- **InsideEVs, Electrek, Not a Tesla App, Teslarati, CleanTechnica.** EV-focused journalism — useful for specifications, timelines, and reporting, weighted according to how well each individual claim was corroborated.
- **Patents (via the USPTO and freepatentsonline).** Tesla's own patents on drive-unit cooling, thermal management, and eFuses — authoritative for design *intent*, though a patent shows what was protected, not necessarily what shipped, hence frequent `[INFERENCE]` tagging.
- **Peer-reviewed and academic sources (ScienceDirect, IOPscience, IEEE Spectrum, arXiv, university course notes).** Used for the underlying physics — intercalation, rotating fields, degradation, aerodynamics — where the science is settled and citable.

**How claims were weighted.** Confirmed manufacturer specifications and government data were treated as firm. Trade-press engineering analysis was treated as reliable for mechanism. Teardown findings were treated as strong for physical fact and flagged where the *interpretation* was inference. Figures that drift year to year — pack voltages, cell counts, RPM ceilings, which cell is in which trim — were grounded where possible and flagged where they rest on teardown estimate rather than published spec. The label used throughout is:

- **`[INFERENCE]`** — a claim known from teardown or patent rather than confirmed by the manufacturer. These were deliberately kept as prose caveats, because knowing *how* something is known is part of the story.

**A closing caveat, restated.** This book is dated to 2026 on purpose. The fastest-aging material — Part IX, on perception and autonomy — was written with the most explicit uncertainty, and the reader is encouraged to treat all specification-level detail as a snapshot of a moving target. The conceptual scaffolding should age well; the exact numbers will not. That was understood from the outset, and it is why the sources are named at every step rather than trusted from memory.
