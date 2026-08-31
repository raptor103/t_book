## 2.4 The 4680 and the tabless idea

In 2020, at an event Tesla called Battery Day, the company unveiled a new cell with the unglamorous name 4680 and made a set of promises about it grand enough to move the share price. Six years on it is one of the more instructive stories in the whole book — not because it failed, and not because it triumphed, but because it did neither cleanly, and the gap between what was promised and what arrived tells you more about real engineering than any success story could.

Recall from earlier that 4680 is a *format*, not a chemistry — a cylinder 46 millimetres across and 80 tall, roughly the size of a small tin of tomato purée, and about five times the volume of the 2170 cells it was meant to supersede. Making the can bigger sounds trivial, even backward; surely more, smaller cells give you more control? But bigger cells mean fewer of them for the same pack — thousands instead of tens of thousands — and fewer parts to make, weld, wire and monitor is fewer chances to get something wrong and less cost in the assembling. The 4680's first argument for existing is simply arithmetic: a big cell is a cheap cell to build with, if you can build the cell itself.

The clever part, though, is not the size. It is a change to the internals with the faintly comic name *tabless*, and it revives an idea older than the hype around it. Inside any cylindrical cell the electrodes are not stacked but rolled — two long ribbons of foil wound up like a Swiss roll. In a conventional cell, the current is collected by a little metal tab welded to that ribbon at one point, which means every electron produced anywhere along the metre-long foil has to travel the whole winding length to reach the tab before it can leave. That is a long, resistive journey, and resistance means heat, and heat is the thing that limits how hard you can charge and discharge a cell.

The tabless design does away with the single tab and instead folds the entire edge of the foil into the connection, so the whole rim of the roll becomes one giant contact. Now an electron only has to cross the short width of the ribbon — the height of the cell — rather than run its entire length.

The difference, drawn crudely:

```
   The electrode foil, unrolled -- a ribbon about a metre long.

   CONVENTIONAL: one tab, welded at a single point
                                                     [tab]
     +---------------------------------------------------+
     |  . . . . . . . . . . . . . . . . . . . . . . . >  |
     +---------------------------------------------------+
       every electron runs the FULL LENGTH to reach it
       = long path, more resistance, more heat

   TABLESS: the whole edge is folded into the contact
      | | | | | | | | | | | | | | | | | | | | | | | | |
     +---------------------------------------------------+
     |  ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^    |
     +---------------------------------------------------+
       each electron crosses only the SHORT WIDTH
       = short path, less resistance, runs cooler
```

Shorten the path and you lower the cell's internal resistance, and a lower-resistance cell runs cooler, which in principle lets it accept and deliver current harder without cooking itself. That was the pitch: a bigger cell, cheaper to make, that could also charge nearly as fast as the small ones despite holding far more energy. Add to it Tesla's parallel bet on a "dry" electrode process — coating the foils without the toxic solvents and long drying ovens the industry has always needed, saving energy, space and money — and Battery Day painted the 4680 as the cell that would make electric cars decisively cheaper.

Here honesty is required, because this is where the story gets interesting rather than triumphant. The 4680 shipped, first in the Cybertruck and in limited Model Y production, and independent teardowns and lab tests — the careful outside scrutiny this book leans on throughout — found a more mixed picture than the promises. Sandy Munro's teardown team measured a later revision with a respectable energy-density gain of around **12 per cent** over its predecessor, real but hardly revolutionary. And the headline claim — that tabless would let the big cell fast-charge almost like a small one — has not clearly borne out; real-world DC fast-charging data has been, if anything, underwhelming, and reporting through 2026 described Tesla still struggling to make its own 4680 cells as good as the cells it buys from suppliers. The dry-electrode process, the quietly more important bet, appears to be edging toward viability at scale but has been genuinely hard to master.

So what is the 4680, in the end? Not the miracle of the keynote, and not the flop of the sceptics. It is a sane, incremental format change — fewer cells, a smarter current path, a hard manufacturing bet attached — that is delivering some of what was promised, more slowly and less completely than advertised. Which is, if you have spent any time near real engineering, the most normal outcome imaginable. The lesson worth carrying out of this chapter is not about one cell. It is that the distance between a bold announcement and a shipped product is where nearly all the actual work lives, and that the trustworthy way to know how a technology is really doing is to wait for someone to saw one open and measure it.

---

**Sources**

- Munro / leandesign.com, "Cybertruck's 4680 Battery: Inside Tesla's Gen 2 Cell" — ~12% energy-density gain on later revision; tabless design characterisation.
- InsideEVs, "Tesla's 4680-Type Battery Cell Teardown: Specs Revealed" and IOPscience teardown (2024) — 4680 dimensions (46×80 mm) and internal construction.
- notateslaapp.com and evlithium.com — dry-cathode/dry-electrode process goals; tabless current-path and lower internal resistance explanation.
- Electrek (May 2026), "Tesla's 4680 battery cells are underperforming" — real-world DC fast-charging shortfall vs Battery Day claims; in-house vs supplier cell performance. Some figures are teardown-derived [INFERENCE] rather than manufacturer-confirmed.
