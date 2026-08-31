## 2.1 How lithium-ion stores and releases energy

Here is a small mystery to start with. A charged battery and a flat one weigh exactly the same. Not almost the same — the same, to the precision of any scale you could bring to bear. Whatever energy is, it has no weight worth mentioning, and yet a charged phone battery can burn your hand and a flat one cannot. So where does the energy actually *go* when you charge a battery? What changes inside it?

The answer is one of the loveliest ideas in engineering, and it is almost entirely about geography.

A lithium-ion cell has two electrodes — two solid structures — held a hair's breadth apart and kept from touching by a thin porous membrane called the separator. One electrode, the one engineers call the anode, is almost always made of graphite: the same soft grey carbon that is in a pencil, arranged in microscopic sheets stacked like the pages of a book. The other, the cathode, is a metal-oxide crystal — a compound of lithium with metals such as nickel, cobalt, manganese or iron, and the exact recipe is the subject of the next few sections. Filling the space between them is the electrolyte, a liquid that lithium ions can swim through freely but electrons cannot.

Now the trick. Both electrodes are riddled with microscopic parking spaces — vacancies in their crystal structure, exactly the right size and shape to hold a lithium ion. The engineers call the act of slotting an ion into one of these spaces *intercalation*, which is a forbidding word for a homely idea: it is shelving. A lithium ion arrives, finds an empty slot in the lattice, and settles into it like a book pushed into a gap on a shelf. It changes nothing about the structure; it just occupies a space that was there waiting.

When you charge the cell, you use an external supply of electricity to force lithium ions out of the cathode, across the electrolyte, and into the graphite anode — cramming the pages of that carbon book full of lithium that would, left to itself, rather be back in the metal oxide. This is the paying-the-price moment from the chapter opener. The energy you put in is stored as a kind of chemical tension: a great many ions parked somewhere they do not want to be, held there only because the circuit is now open and they have no way home.

Driving the car opens the door. Connect the two electrodes through a load — the motor, ultimately — and the lithium ions rush back from the graphite to the metal oxide, where they are more comfortable. But here is the crucial part. The ions travel through the electrolyte, and the electrolyte will not let electrons follow. So each departing lithium ion leaves its electron behind at the anode, and that electron, desperate to rejoin its ion on the other side, can only get there the long way round — out through the wire, through the car, doing work every step of the way, before arriving at the cathode to reunite with the ion that has been waiting. That forced detour of electrons *is* the electric current. That is the whole secret.

A simple picture of the two directions:

```
        CHARGING (energy in)              DISCHARGING (energy out)

   anode                cathode      anode                cathode
 (graphite)          (metal oxide) (graphite)          (metal oxide)
     |   Li+  ---->    |               |    <----  Li+     |
     |  (through electrolyte)          |  (through electrolyte)
     |                 |               |                   |
     +<---- e- (forced by charger) ----+    +---- e- ----> + through
       the wire, storing energy             the wire = the CAR runs
```

Two things fall out of this picture immediately, and both matter for the rest of the book. First, nothing is burned, nothing is consumed, nothing moves except ions and electrons shuttling back and forth. That is why the same cell can be charged and drained hundreds or thousands of times: it is the same lithium, rocking between the same two shelves, over and over. Engineers sometimes call it the "rocking-chair" battery, and it is a good name. Second, because the ions physically have to travel through the electrolyte and squeeze into their slots, there are limits to how fast you can rush them. Push too hard, too cold, or too full, and the tidy shelving turns messy — ions pile up, plate out as metal, or damage the lattice they are meant to slot into. Almost every rule you have ever heard about looking after a battery — don't charge it in the freezing cold, don't leave it at 100 per cent, don't fast-charge it to the brim — is a direct consequence of what you have just seen. It is all about keeping the rocking gentle.

Energy stored as geography; current as electrons taking the scenic route. Hold that, and every battery in the book becomes legible.

---

**Sources**

- ScienceDirect, "Intercalation-based electrode materials for lithium-ion batteries: structure, chemistry, and performance" (2026) — intercalation mechanism, electrode/electrolyte/separator structure.
- Stanford PH240, "Lithium-Ion Batteries and Graphite" — graphite anode, charge/discharge ion and electron flow.
- Standard electrochemistry of Li-ion cells (graphite anode; NMC/NCA/LFP cathodes) as developed in later subchapters of this chapter.
