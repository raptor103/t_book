# How a Tesla Works — Project Brief
*Working title. Master spec for the book. Re-upload this file at the start of every working session.*

---

## 1. What this book is

A high-level but genuinely technical overview of how a modern electric car works, using Tesla as the worked example. It explains real components by name — battery chemistries, the inverter, the octovalve, the zone controllers, the low-voltage battery — at a level a curious, intelligent non-engineer can follow and enjoy.

**Why it exists:** this book does not currently exist. Books about Tesla are business and biography. Books about EV engineering are university textbooks (Husain et al.). Component-level Tesla engineering lives almost entirely in teardown journalism, scattered across articles and YouTube. Nothing sits in the middle. That gap is the entire premise.

**Reader:** technically curious, no engineering degree, comfortable with a diagram, allergic to equations. Someone who wants to understand the machine well enough to explain it at dinner, not well enough to build one.

**Not in scope:** Musk, company history, stock price, culture-war material. Business context appears only where it explains an engineering decision.

---

## 2. Decisions locked

| Decision | Choice |
|---|---|
| Language | English |
| Voice | Warm, story-driven, Bryson-ish |
| Length target | No hard cap. Author reviewed Chapter 1 and confirmed the length is good; nothing is to be cut at the end (decision updated 2026-08-28, supersedes the original 150-page cap) |
| Drafting strategy | Draft full and keep it all. The original "cut ~30% at the end" plan is CANCELLED per author instruction |
| Units | Metric, EU context |
| Vehicle spine | Model 3 / Model Y as the default reference car |
| Model comparisons | None. No model-vs-model contrast sections |
| Knowledge cutoff for the text | State explicitly as 2026; the book dates itself rather than pretending to be timeless |
| Diagrams | ASCII only, inline in the text. No rendered figures, no image assets |
| Source files | One markdown file per subchapter, in a per-chapter folder |
| Final artefact | All markdown concatenated into a single PDF |
| Distribution | Sold as an ebook (Amazon). No free-to-read or donation framing in the text |
| Editions | English only. No Czech edition |

**Note on dropping model comparisons:** this removes the *framing*, not the technology. Several genuinely important systems first appeared on models other than the 3/Y — 48V architecture, steer-by-wire, Etherloop, the shift from lead-acid to lithium low-voltage batteries. These stay in the book, written as technology and as direction of travel, not as "the Cybertruck does X while the Model 3 does Y." Subchapters 8.4, 10.3 and 14.4 are affected by this and should not be deleted on a future read of this brief.

**UPDATE 2026-08-28 — no final cut.** The author reviewed Chapter 1, approved the voice and the length, and instructed that nothing be cut at the end. The full ~90-subchapter structure below is drafted and kept in its entirety. The paragraphs that follow describe the original (now-cancelled) plan and are retained only as a record of the decision that was reversed.

**UPDATE 2026-08-29 — three coverage gaps closed.** A component-coverage audit of the completed draft found three significant systems with no dedicated treatment. All three have been researched, drafted and inserted, and later subchapters renumbered accordingly:

- **14.3 The computer that referees the brakes.** The manuscript described blended braking (6.3) purely as software and never named the hardware; the Chapter 14 opener promised a computer "refereeing" the brakes that never appeared, and 16.2 cited a brake-by-wire discussion that did not exist. Now covers the electromechanical brake booster (iBooster), the hydraulic control unit, and ABS/traction/stability control. Former 14.3–14.5 shifted to 14.4–14.6.
- **11.4 When the energy flows backwards.** Part VI treated charging as strictly one-directional; V2L/V2H/V2G and Powershare were absent entirely. Former 11.4 (connector wars) shifted to 11.5.
- **13.4 The silence problem.** NVH was touched three times in passing (tyre foam, active noise cancellation, "the cabin is silent") but never developed, despite being a genuinely EV-specific consequence of deleting the engine.

Remaining known gaps, judged subchapter-sized or deliberately out of scope, recorded here so a future session does not re-derive them: occupant restraints (explicitly scoped out by the Chapter 19 opener); exterior lighting; glass and closures, including the electronic door releases; TPMS; halfshafts and CV joints; suspension hardware (subframes, knuckles, bushings); HVIL and isolation monitoring; the pyrofuse; busbars and the cell contact system.

**Original consequence of "draft full, cut at the end" (CANCELLED):** the full structure below is ~90 subchapters. At 700–800 words each that is roughly 65,000–70,000 words, or ~200 pages with figures. Reaching 150 would have meant cutting ~30% of finished prose at the end.

**Original cut candidates (NO LONGER CUT):** Part IX (Perception and Autonomy) was flagged as the fastest-ageing, least verifiable material and the natural first cut. Per the 2026-08-28 decision it stays in full, like everything else.

---

## 3. Voice

Bryson-ish means specific things. Not decoration — structure.

- **Curiosity before explanation.** Open a subchapter with the question, the oddity, or the problem an engineer faced. Never open with a definition.
- **The ordinary made astonishing.** The reader should finish a section slightly amazed that something they walk past every day works at all.
- **Concrete over abstract.** Not "high switching frequency" but "flipping a switch twenty thousand times a second, without ever getting it wrong."
- **Numbers made vivid.** A number that isn't given a human referent is wasted. Anchor it to something the reader can picture.
- **Analogy carries the load.** One strong analogy per concept, sustained. Don't stack three weak ones.
- **Permission to digress**, briefly, when the digression earns its place. This is the main thing 500-word subchapters would have killed.
- **Dry humour, sparingly.** Understatement rather than jokes. Never at the reader's expense, never at the engineers'.
- **Honesty about uncertainty.** Where something is teardown inference rather than published fact, say so in the prose. It builds trust and it's more interesting than false confidence.

**Avoid:** breathless marketing register, "revolutionary" and "game-changing," hero narratives about the company, and the textbook tic of defining a term before establishing why anyone should care.

**Length per subchapter:** 700–800 words. Some will justify 1,000. None should fall below 500 — if a subchapter can't earn 500 words it should be folded into its neighbour.

---

## 4. Working method

One subchapter at a time. Complete the full cycle before moving on.

1. **Research.** Search for the specific subchapter's content. Prioritise: Munro Live teardowns, E-Mobility Engineering, patents, published specs, peer-reviewed papers. Do not draft from memory.
2. **Write.** Full prose at target length, in voice.
3. **Refine.** Second pass for rhythm, analogy strength, and cutting throat-clearing. First drafts always open too slowly.
4. **Validate.** Every hard number and component-specific claim checked against a source, or tagged `[VERIFY]`. Flag anything that is inference rather than confirmed fact.
5. **Append and hand back.** Then next subchapter.

**Why this order matters:** the conceptual scaffolding is the reliable part of the work. Exact figures — pack voltages, kWh, which cell is in which trim, RPM ceilings, octovalve operating modes — drift year to year and are frequently teardown inference rather than published spec. These get grounded against sources rather than trusted from memory. This is not optional caution; it is the known failure mode of the project.

---

## 5. Conventions

- **`[VERIFY]`** — inline tag on any claim not yet grounded in a source. Nothing ships with these unresolved.
- **`[INFERENCE]`** — inline tag where the best available knowledge is teardown-derived or patent-derived, not confirmed by the manufacturer. Many of these should survive into the final text as prose caveats.
- **Sources** — a short source list at the end of each subchapter, not footnotes in the body. Footnotes fight the reading voice.
- **Diagrams** — ASCII only, written inline inside a fenced code block, with a caption line above it. Pure ASCII characters only (`+ - | / \ < > * =`), no Unicode box-drawing, so the PDF build cannot break on font substitution. Keep them under 76 characters wide so they survive A4 with margins at a readable monospace size.
- **Numbers** — concentrate hard figures in a few reference pages or tables rather than scattering them through prose. Cheaper to verify, cheaper to update, and it keeps the narrative clean.

---

## 6. Files, repository, and build

### One file per subchapter

Every subchapter is its own markdown file. Subchapter files live inside a folder for their chapter. Filenames carry their own numbering so a plain alphabetical sort produces correct book order — this is what the PDF build depends on.

```
how-a-tesla-works/
  README.md                          <- landing page
  PROJECT-BRIEF.md                   <- this file
  build.sh                           <- concatenate + render
  book/
    00-front-matter/
      00-00-title.md
      00-01-preface.md
      00-02-how-to-read-this-book.md
    01-deleting-the-engine/
      01-00-chapter-opener.md
      01-01-what-an-ice-car-actually-is.md
      01-02-five-jobs-every-car-must-do.md
      01-03-why-electric-changes-all-five.md
      01-04-efficiency-as-organising-obsession.md
    02-inside-a-single-cell/
      02-00-chapter-opener.md
      02-01-how-lithium-ion-stores-energy.md
      ...
    99-back-matter/
      99-00-sources.md
      99-01-glossary.md
  out/
    how-a-tesla-works.pdf
```

**Rules:**

- Folder name: `NN-chapter-slug`, chapter number zero-padded.
- File name: `NN-MM-subchapter-slug`, chapter then subchapter, both zero-padded.
- `NN-00-chapter-opener.md` is optional — use it where a chapter benefits from a page of framing before the first subchapter.
- Each subchapter file contains its own heading, body, ASCII diagrams, and its end-of-file source list. Nothing else.
- No image files anywhere in the repo.

### Build

Final step, once drafting and cutting are done: concatenate every markdown file in sort order and render one PDF to `out/how-a-tesla-works.pdf`. Pandoc with a monospace font that preserves ASCII diagram alignment, A4 page size, and a generated table of contents. `build.sh` should be reproducible from a clean checkout.

### Session logistics

The manuscript does not persist between conversations. The container filesystem resets and each session starts with no memory of the last one.

- George holds the repository.
- At the start of each session: upload this brief, plus any subchapter files relevant to the session's work.
- At the end of each session: save the new files into the repo.
- This brief is the single source of truth for structure, voice, and conventions. Update it when a decision changes.

---

## 7. Structure

### Part I — A Different Kind of Machine

**1. The car that deletes the engine**
1.1 What an internal-combustion car actually is
1.2 The five jobs every car must do
1.3 Why electric changes all five at once
1.4 Efficiency as the organising obsession

### Part II — Storing the Energy

**2. Inside a single cell**
2.1 How lithium-ion stores and releases energy
2.2 Chemistry vs. format — the axis everyone conflates
2.3 Trade-offs: density, cost, longevity, cold, cobalt
2.4 The 4680 and the tabless idea

**3. From cell to pack**
3.1 Thousands of cells, one machine
3.2 The BMS as nervous system
3.3 The structural pack
3.4 Degradation, and why charging advice differs by chemistry

### Part III — Turning Energy Into Motion

**4. The inverter**
4.1 The DC-to-AC problem
4.2 Switching frequency as speed and torque
4.3 Silicon carbide and why Tesla bet on it

**5. The motor**
5.1 Torque from a rotating magnetic field
5.2 Induction vs. permanent-magnet — why both
5.3 Instant torque, one gear, no transmission
5.4 Small efficiencies: the electric oil pump and other invisible wins

**6. Motion management**
6.1 The single-speed reduction gear
6.2 Regenerative braking
6.3 Blended braking and one-pedal driving
6.4 Multi-motor torque vectoring

### Part IV — Managing Heat

**7. Heat as enemy and resource**
7.1 Why an EV's thermal problem inverts the combustion one
7.2 The heat pump: moving heat uphill
7.3 The octovalve — one valve, many paths
7.4 Preconditioning and the pack as thermal store
7.5 Cabin climate: filtration and the energy cost of comfort

### Part V — The Electrical Backbone

**8. Two voltages, one car**
8.1 The high-voltage world and the low-voltage world
8.2 The low-voltage battery — and why the big pack can't start itself
8.3 The PCS: onboard charger and DC-DC converter in one box
8.4 From lead-acid to 16V lithium to 48V

**9. Zonal architecture and the disappearing fuse box**
9.1 VCFRONT, VCLEFT, VCRIGHT — controllers by geography, not function
9.2 Solid-state eFuses replacing the fuse box
9.3 Why zoning shortens wire

**10. The nervous system**
10.1 The wiring harness as a mass and cost problem
10.2 CAN bus and its limits
10.3 Etherloop: gigabit Ethernet, power over the same wires
10.4 Standardisation as strategy (NACS, LVCS)

### Part VI — Filling It Up

**11. Charging, demystified**
11.1 AC vs. DC — where the conversion happens
11.2 Onboard charger vs. Supercharger
11.3 Charge curves and why speed falls
11.4 When the energy flows backwards — V2L, V2H, V2G and Powershare
11.5 The connector wars

### Part VII — Air, Road, and Chassis

**12. Fighting the air**
12.1 Drag rises with the cube of speed
12.2 Where drag actually comes from — wheels, wells, underbody
12.3 Aero wheels and the styling-vs-range tax

**13. Where rubber meets road**
13.1 Rolling resistance and why EVs care more
13.2 EV-specific tyres and faster wear
13.3 Wheel size trade-offs
13.4 The silence problem — NVH once the engine stops masking it

**14. Chassis and control**
14.1 Suspension, air springs, adaptive damping
14.2 The friction brakes that barely wear
14.3 The computer that referees the brakes — iBooster, ABS, ESC
14.4 Electric power steering
14.5 Steer-by-wire: no column, triple redundancy
14.6 Rear-wheel steering

### Part VIII — The Car as a Computer

**15. Three computers, three jobs**
15.1 The FSD/AI computer
15.2 The MCU — infotainment, deliberately separate
15.3 The zone controllers
15.4 Why the separation matters

**16. Software-defined driving**
16.1 Over-the-air updates
16.2 Drive-by-wire and the vanishing mechanical linkage
16.3 Connectivity: cellular modem, phone-as-key, Sentry Mode
16.4 The fleet data loop

### Part IX — Perception and Autonomy *(first cut candidate)*

**17. What the car sees**
17.1 The camera suite, and dropping radar and ultrasonics
17.2 Vision-only: the bet and the criticism

**18. Thinking in real time**
18.1 The inference computer (HW3 -> HW4/AI4)
18.2 Training vs. driving — where the heavy compute lives
18.3 What Autopilot and FSD do and don't mean

### Part X — Surviving the Crash

**19. Safety by architecture**
19.1 No engine block: the crumple zone you get for free
19.2 Low centre of gravity and rollover
19.3 Protecting the pack
19.4 High-voltage safety: contactors, isolation, first responders

### Part XI — Building It

**20. Manufacturing as engineering**
20.1 Why how it's built is how it works
20.2 Gigacasting
20.3 Materials: aluminium, steel, stainless
20.4 Harnesses designed for robots
20.5 Vertical integration

**21. The end of the life**
21.1 Repairability and the cost of integration
21.2 Second-life packs and recycling

### Part XII — The Whole Car

**22. Everything talking to everything**
22.1 A drive, traced through every system
22.2 Following the energy from plug to pavement
22.3 Where the real marvels are — and where marketing outran engineering

**23. What comes next**
23.1 Solid-state and the battery frontier
23.2 How much efficiency is left to win
