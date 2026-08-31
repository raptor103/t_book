## 2.3 Trade-offs: density, cost, longevity, cold, cobalt

There is no such thing as the best battery, and anyone who tells you otherwise is selling one. There are only batteries that are good at some things by being bad at others, and the whole art of choosing a chemistry is deciding which virtues you can afford to sacrifice. It is less like shopping and more like negotiating: every gain is paid for somewhere else on the ledger. The two chemistries in most Teslas — a nickel-rich NMC or NCA in the longer-range cars, and lithium iron phosphate, LFP, in the standard ones — are a near-perfect illustration, because they sit at almost opposite corners of the same set of compromises.

Start with **energy density** — how much energy you can pack into each kilogram, which is really the question of how far the car goes before it gets too heavy to bother. Here the nickel chemistries win clearly. NMC and NCA cells hold something like **150 to 250 watt-hours per kilogram**, while LFP manages roughly **90 to 160**, with the best modern versions creeping toward 200. That gap is the single reason the long-range cars use nickel: for a given weight of battery, they simply carry more energy. If range were the only thing that mattered, the conversation would end here.

But range is never the only thing that matters, because of **cost**. Nickel and cobalt are expensive, mined in a few troubled places, and volatile in price. Iron and phosphate — the guts of LFP — are cheap and everywhere. The result, as of a 2024 industry survey, is LFP packs landing near **95 euros-worth per kilowatt-hour** against **130 to 150** for nickel packs, a difference that runs to thousands across a whole car. This is why LFP has swept the standard-range market: in 2024 it reached roughly 40 per cent of EV batteries globally, and around 60 per cent in China. When you are building millions of affordable cars, twenty per cent off the most expensive component is not a detail. It is the strategy.

Then **longevity**, and here the ledger flips again. LFP is the tortoise, and the tortoise wins the distance race. An LFP cell will typically survive **two to five thousand** full charge-discharge cycles, and sometimes far more, where a nickel cell may be tiring after **one to two thousand**. LFP is also relaxed about being charged all the way to 100 per cent, which nickel chemistries resent — one reason Tesla tells LFP owners to charge to full routinely and nickel owners to stop around 80 for daily use. The advice differs because the chemistry differs; it is not fussiness, it is physics, and Chapter 3 returns to why.

Now the two places nickel takes its revenge. The first is **cold**. LFP's chief weakness is a sluggishness in low temperatures — its usable energy and, especially, its willingness to accept a fast charge fall away more sharply in the cold than a nickel cell's. On a January morning an LFP car often needs to warm its own battery before it will charge quickly, which costs energy and time. Nickel chemistries suffer in the cold too, but less. This is not a fatal flaw — it is managed, as we will see, by the thermal systems in Part IV — but it is real, and northern-European owners feel it.

The second is **cobalt**, and this one is as much ethics as engineering. Cobalt is what makes older nickel chemistries stable, but it is expensive and much of it comes from mines with genuinely ugly human and environmental records. The entire trajectory of battery development has been a slow retreat from cobalt: from formulations that were a fifth cobalt by weight to high-nickel recipes that use around a tenth, and to LFP, which uses none at all. When you read that a battery is "cobalt-free," that is LFP's quiet moral advantage being advertised — bought, remember, at the cost of density and cold performance.

The whole negotiation, on one card:

```
              density   cost     cycle    cold     cobalt
              (range)   (cheap)  life     tolerance  free?
  NMC / NCA    HIGH      low      medium    better     no
  LFP          lower     HIGH     HIGH      worse      YES

  (HIGH = strong on that axis; there is no column that wins them all)
```

Read that grid and the market makes itself. The affordable, high-mileage, charge-it-to-full commuter car wants LFP and its cheapness and endurance. The long-range and performance car wants nickel and its density, and pays for it in money, in cobalt, and in a shorter cycle life it manages with careful charging. Neither is the "better" battery. They are answers to different questions — which is exactly why a single manufacturer builds cars with both, and why the next thing to understand is not a chemistry at all, but a container: the 4680.

---

**Sources**

- Ufine, evlithium.com, BSLBATT — LFP vs NMC energy density (LFP ~90–205 Wh/kg; NMC ~150–250), cycle life (LFP ~2,000–5,000+; NMC ~1,000–2,000).
- BloombergNEF 2024 pack-cost survey (via evlithium/GlobalSpec) — LFP ~$95/kWh vs NMC ~$130–150/kWh; LFP ~40% global / ~60% China EV share in 2024.
- Electronics360 / GlobalSpec and battery.mba — cobalt content trend (NMC 811 ~10% vs older ~20%), LFP cobalt-free; LFP cold-weather weakness.
- Charging advice by chemistry (LFP to 100%, nickel to ~80% daily) developed further in subchapter 3.4.
