## 2.2 Chemistry vs. format — the axis everyone conflates

Listen to people talk about electric-car batteries for any length of time and you will hear two kinds of names used as if they were the same kind of thing. Someone will say a car has "LFP batteries," and someone else will say it has "4680 batteries," and the conversation rolls on as though these were rival answers to the same question. They are not. They are answers to two completely different questions, and keeping them apart is the single most clarifying move you can make in this whole subject. Almost every muddle about EV batteries comes from collapsing these two axes into one.

Think of it like coffee. "Espresso" and "a takeaway cup" both describe your morning coffee, but one is about *what is in it* and the other is about *what it is packaged in*. You can have espresso in a takeaway cup, or in a china cup, or in a tiny glass. The drink and the container vary independently. Batteries are exactly the same, and the two axes are called chemistry and format.

**Chemistry** is what the cell is made of — specifically, the recipe of the cathode, that metal-oxide electrode from the previous section. This is where names like NMC, NCA and LFP come from, and they are just shorthand for which metals are in the mix. NMC is nickel, manganese and cobalt. NCA is nickel, cobalt and aluminum. LFP is lithium iron phosphate — no cobalt, no nickel, just iron. The chemistry decides the things that matter most to a driver: how much energy the cell packs into each kilogram, how much it costs, how it behaves in the cold, how long it lasts, and how it fails when abused. Change the chemistry and you change the soul of the cell.

**Format** is the physical shape and size the chemistry is packaged in — the cup, not the coffee. Here the names are different in character: they are numbers describing dimensions, or words describing shape. Tesla's cells have mostly been cylindrical, like slightly overgrown AA batteries, and named for their measurements in millimeters: the old 18650 (18 mm across, 65 mm tall), the 2170 that arrived with the Model 3 and Model Y (21 by 70), and the much-discussed 4680 (46 by 80). Other cars use flat rectangular *prismatic* cells, or soft flat *pouch* cells like a vacuum-packed slice of ham. The format decides how the cells pack together, how they shed heat, how easily they can be made, and — as we will see later — whether they can help hold the car together structurally.

And here is the point the whole section is built to make: **the two axes are independent.** A 4680 is a size, not a chemistry. You can build a 4680 cell with a nickel-rich chemistry or, in principle, with LFP; Tesla has used the 4680 format with a high-nickel NCM (a close cousin of NMC) cathode, while also making 4680-format cells for stationary storage with different recipes inside. Likewise LFP is a chemistry, not a shape: the LFP cells in many standard-range cars are large prismatic blocks bought from suppliers such as CATL and BYD, while nothing stops LFP being rolled into a cylinder. When a car is described as having "4680 batteries," you have been told the container and nothing about the coffee. When it is described as having "LFP batteries," you have been told the coffee and nothing about the container.

A simple grid makes the independence obvious:

```
                          +---------------------------------------+
                          |        CHEMISTRY (the coffee)         |
   +----------------------+--------------------+------------------+
   |  FORMAT (the cup)    |  NMC / NCA         |  LFP             |
   +----------------------+--------------------+------------------+
   |  cylindrical         |  2170, 4680        |  possible, but   |
   |  (18650, 2170, 4680) |  -- most Teslas    |  rare in cars    |
   +----------------------+--------------------+------------------+
   |  prismatic or pouch  |  used by some      |  large blocks    |
   |                      |  other makers      |  (CATL, BYD)     |
   +----------------------+--------------------+------------------+

   "4680" names the cup. "LFP" names the coffee.
   Neither one, on its own, tells you the other.
```

Why labor the distinction? Because the two axes are chosen for different reasons and traded off against different things, and the rest of this chapter needs them kept separate. The next section, on trade-offs, is almost entirely a chemistry story — density, cost, cold, cobalt. The section after, on the 4680, is almost entirely a format story — how making the container bigger and smarter changes the economics of building millions of them. Confuse the two and neither story lands. Keep them apart and you have a mental filing system that will serve you through every battery announcement you ever read, including the ones that have not happened yet.

So whenever someone tells you a car's battery in a single word, ask yourself the quiet follow-up: *is that the coffee, or the cup?* You will be surprised how often even the experts have only told you one of the two.

---

**Sources**

- InsideEVs, "What Batteries Are Tesla Using In Its Electric Cars?" and Shop4Tesla / teslabs.de — chemistries NMC, NCA, LFP and their attributes.
- Torque News, "Tesla 18650, 2170 and 4680 Battery Cell Comparison" — cylindrical format dimensions and naming.
- InsideEVs, "Tesla To Use 4680-Type Battery Cells" and Yeslak (2026 Tesla battery guide) — 4680 format used with NCM-class chemistry; LFP supplied as prismatic cells by CATL/BYD. Independence of format and chemistry is inferred from these combined sources.
