## 20.2 Gigacasting

Imagine the back third of a car's underbody — the complex structure beneath the rear seats and boot that holds the suspension, absorbs crash loads, and ties the body together. In a traditional car this is an assembly of *dozens* of separate pieces: sheets of steel stamped into shape, then welded, bolted and glued together in a long, carefully-sequenced dance involving hundreds of robots, each weld a step that must be done right and then checked. It is one of the most complex and labour-intensive regions of the whole car body. Now imagine deleting all of it — all seventy-odd parts, all those welds — and replacing it with a *single* piece, cast in one shot like a toy soldier poured from a mould. That is gigacasting, and it is the boldest manufacturing idea in the modern car.

The machine that does it is called a Giga Press, and it is genuinely enormous — one of the largest die-casting machines ever built, a device the size of a small house that clamps a mould shut with thousands of tonnes of force and injects molten aluminium into it under tremendous pressure. The aluminium fills every cavity of the mould, cools, and is lifted out as a single, finished, intricate part that would otherwise have been an assembly of seventy. Tesla pioneered this at automotive scale, first casting a single-piece rear underbody for the Model Y that replaced around seventy stamped-and-welded parts with one, and has pushed toward casting the front and eventually larger portions of the body the same way.

Seventy parts, one shot:

```
   TRADITIONAL REAR UNDERBODY    GIGACASTING
   ------------------------------------------------------------
   about 70 stamped steel parts  1 aluminium casting
   hundreds of welds             poured in a single shot
   many robots, a long           about 300 fewer robots,
   sequence of operations        by Tesla's own account
   variable fit, much            consistent, with little
   inspection needed             left to inspect
   ------------------------------------------------------------
   heavy, slow, costly           around 30% lighter and 40%
                                 cheaper, by Tesla's estimates

   And the same consolidation that makes it cheap to build
   is what makes it expensive to repair. One see-saw.
```

The benefits, when it works, are exactly the design-for-manufacturing wins of the last section, delivered at spectacular scale. Consolidating seventy parts into one eliminates all the welding between them, and with it the hundreds of robots that did the welding — Tesla has claimed the change removed something like three hundred robots from the line. It eliminates the variability of lining up many parts, so the finished structure is more consistent and dimensionally accurate. It removes a small mountain of logistics — seventy part numbers, their suppliers, their storage, their sequencing — replaced by one casting. And by Tesla's own estimates the approach can cut the underbody's weight by around thirty percent and its cost by up to forty. Fewer parts, less labour, less weight, lower cost, better consistency: it is the manufacturing dream made metal, and it is why much of the rest of the industry scrambled to copy it.

But this book always tells you the price, and gigacasting's price is steep and worth understanding, because it echoes a warning from earlier in the book. The first cost is capital: a Giga Press is a multi-million-euro machine, and the moulds ("dies") for it are hugely expensive too, which means the whole approach only makes economic sense at very high production volumes — you must build a great many identical cars to spread that colossal fixed cost. It also demanded a new aluminium alloy, developed specially, that could be cast into so large and complex a shape and still have the right strength — a metallurgical problem in its own right. And there is the drawback that connects directly to the next chapter: *repairability*. When a car's rear underbody is a single giant casting, a collision that would once have crumpled a few replaceable stamped parts can instead damage the one enormous casting — which cannot be unwelded and patched, only replaced whole, at great cost, if it can be replaced at all. A part designed to eliminate assembly is, almost by definition, a part designed to resist disassembly.

This is the same tension we met with the structural battery pack in Chapter 3, and it is not a coincidence — it is the deep signature of the whole design-for-manufacturing philosophy. Every act of consolidation that makes the car cheaper and simpler to *build* tends, by the same logic, to make it harder and more expensive to *repair*. Integration and repairability are two ends of one see-saw: press down on the cost of manufacturing and the cost of repair rises at the other end. Tesla has consistently chosen the manufacturing end, betting that cars built this way are cheap enough, and crash-safe enough, that the repair penalty is worth it. Whether that bet is right for the owner, as opposed to the maker, is one of the questions the next chapter takes up.

Gigacasting is the most visible face of "the factory is the product" — a car body reconceived around the capabilities of one gigantic machine. But a casting must be made of *something*, and the choice of what to cast, stamp, and fold a car from is its own set of trade-offs, which the next section explores.

---

**Sources**

- Electrek, InsideEVs, alcircle, HotCars — Giga Press casts a single-piece rear underbody replacing ~70 parts; ~300 fewer robots; ~30% weight and ~40% cost reduction (Tesla estimates); requires a specially developed aluminium alloy.
- Automotive Manufacturing Solutions, Notebookcheck, Sunrise Metal — Giga Press scale and capital cost (~$18–25M per press), economic viability only at high volume (~100,000+ units/die); repairability and high repair-cost concerns.
- The manufacturing-vs-repairability trade-off references the structural pack of Chapter 3 and is developed in Chapter 21.
