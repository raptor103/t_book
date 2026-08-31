## 3.1 Thousands of cells, one machine

Suppose you have four thousand little cells and you want to build a car battery out of them. You cannot just throw them in a box and run a wire out of each end. You have two problems, and they pull in different directions, and the way engineers solve both at once is the hidden grammar behind every battery pack ever made.

The first problem is *pressure*. A single cell pushes at a little under four volts, and voltage is the electrical equivalent of pressure — the shove behind the current. A motor that is going to move a car wants a great deal more shove than one cell can give: a few hundred volts, not a few. The fix is to connect cells in a chain, positive to negative, positive to negative, so their voltages add up. Engineers call this wiring cells *in series*, and it is exactly like stacking batteries end to end in a torch. Stack enough of them and the pressure climbs to something a motor can use.

The second problem is *quantity*. A single cell holds only a mug's worth of energy, and you want a car's worth. Chaining cells in series does not help here — a chain of cells has the voltage of the whole chain but still only the capacity of one cell's worth of current at a time. To get more capacity you connect cells side by side instead, all their positives together and all their negatives together, so they share the load and their capacities add up. This is wiring *in parallel*, and it is like widening a river rather than lengthening it: same height of water, far more of it flowing.

Every battery pack is therefore built on two axes at once — some cells in series to build the voltage, many more in parallel to build the capacity — and the shorthand engineers use captures both in a few characters. A Tesla Model 3 pack is described as **96s46p**, and once you can read that, you can read any pack. The "96s" means ninety-six groups wired in series, which sets the voltage. The "46p" means each of those groups is itself forty-six cells wired in parallel, which sets the capacity. Multiply them out — ninety-six times forty-six — and you get **4,416 cells** in a long-range car, all working as one. A standard-range pack is **96s31p**: the same ninety-six-high stack for voltage, but only thirty-one cells wide, so **2,976 cells** and less capacity.

Notice what stays fixed and what changes. Both packs are ninety-six cells "tall," because both need the same voltage. Each series group — Tesla calls one a *brick* — sits at a shade over 3.6 volts, and ninety-six of them in a chain give a pack of very roughly **350 volts** nominal. That number is a constant of the car; it is set by the "96s" and nothing else. What the car varies to make a bigger or smaller battery is the *width* — how many cells are ganged in parallel in each brick — because that, and only that, is what changes how much energy the pack holds.

The structure, drawn as a ladder:

```
   Each BRICK = 46 cells side by side in PARALLEL  -> capacity
   96 BRICKS stacked in SERIES                     -> voltage

        +---------------------------------------------+   ^
   96   | [o][o][o][o] .... 46 cells .... [o][o][o][o] |   |
   95   | [o][o][o][o] .... 46 cells .... [o][o][o][o] |   |
    :   |                     :                       |   | 96 x 3.6 V
    2   | [o][o][o][o] .... 46 cells .... [o][o][o][o] |   | = ~350 V
    1   | [o][o][o][o] .... 46 cells .... [o][o][o][o] |   v
        +---------------------------------------------+
         <----------- width sets ENERGY ------------->

   96s46p = 96 x 46 = 4,416 cells   (long range)
   96s31p = 96 x 31 = 2,976 cells   (standard range)
   The height never changes: every pack needs the same voltage.
```

These bricks are then grouped into a handful of larger blocks — historically four *modules* in a Model 3 — for ease of building and wiring, though the newest structural packs, which the chapter comes to shortly, blur the modules away entirely. However they are grouped, the principle is unchanged: height for pressure, width for quantity.

One consequence of parallel wiring is worth pausing on, because it explains why the whole scheme is trustworthy at all. When forty-six cells are ganged in parallel, they are forced to share a single voltage — they lean on one another, the strong ones quietly propping up the weak. A brick behaves like one enormous, reliable super-cell rather than forty-six temperamental small ones, and the failure or fade of any single cell is diluted almost to nothing across its forty-five neighbours. It is strength in numbers in the most literal sense: the pack is more dependable than any cell in it, precisely because no cell is ever asked to stand alone.

Height for voltage, width for energy, and safety in the crowd. That is the entire architecture. What it still lacks is a brain — something to watch all ninety-six bricks and make sure none of them drifts into trouble. That brain is the battery management system, and it is next.

---

**Sources**

- batterydesign.net and Electrek (2017) — Model 3 pack architecture: 96s configuration, 96s46p (4,416 cells) long-range, 96s31p (2,976 cells) standard-range; ~3.6 V nominal cell → ~350 V pack.
- Tesla Motors Club and Drive Quip — module/brick grouping (historically 4 modules); "brick" = parallel group terminology.
- Parallel-group self-balancing behaviour is standard battery-engineering principle; developed further in 3.2.
