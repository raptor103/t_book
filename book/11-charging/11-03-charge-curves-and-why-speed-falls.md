## 11.3 Charge curves and why speed falls

Ask someone how long an electric car takes to charge and they will usually quote a single number — "twenty minutes," "an hour" — as though charging happened at a steady rate, like filling a bath. It does not, and the belief that it does is the source of more road-trip frustration than any other misunderstanding. Charging is fast at first and slows down as the battery fills, sometimes dramatically, and the shape of that slowdown — the *charge curve* — is one of the most useful things a driver can carry in their head.

Picture the curve. You arrive at a fast charger with a fairly empty battery, plug in, and the power leaps up — perhaps to the charger's full rated speed, a couple of hundred kilowatts, energy pouring in. This is the fast part, and it typically holds from a low state of charge up to somewhere around the halfway mark. Then, as the battery fills past roughly fifty per cent and heads toward eighty, the power begins to ease off. Past eighty per cent it falls away sharply, so that the final climb from eighty to a hundred can take almost as long as everything before it combined. The battery that gulped its first half in fifteen minutes may take another forty to sip its way to completely full. The curve starts high and tapers, like a sprinter slowing to a walk.

Why? The reasons reach straight back to the chemistry of Chapter 2 and the watchful BMS of Chapter 3, and they are all really the same reason wearing different clothes. Remember that charging means forcing lithium ions into the graphite anode's parking spaces. When the battery is nearly empty, those spaces are plentiful and the ions slot in easily, so you can push hard and fast. As the battery fills, the easy spaces are taken, and the remaining ions must be crammed into a structure that is increasingly full — pushed somewhere they are progressively less willing to go. Force them in too fast at that point and you risk exactly the damage the BMS exists to prevent: lithium plating out as metal, heat building up, cells straying toward danger. So the BMS deliberately throttles the charging rate as the battery fills, trading speed for the battery's safety and longevity. It is not the charger giving up; it is the car's guardian easing off the throttle to protect the pack.

Two other effects from the same family pile on near the top. Heat: fast charging warms the pack, and a warm pack near full charge is doubly stressed, so the BMS slows things to keep temperatures in the safe band. And balancing: as the battery approaches full, the BMS slows down to let the weaker cells catch up to the stronger ones, that levelling act from Chapter 3. All of it conspires to make the last stretch slow.

The shape of a fast charge:

```
   charging power (kW)
    high |####
         |########
         |############
         |################          <- fast: plenty of empty
         |####################         parking spaces, push hard
         |########################
         |##############################
         |####################################  <- tapering as
    low  |__________________________________########  it fills
         0%    20%    40%    60%    80%    100%
              (peak)          |----- slow crawl -----|
```

Out of this comes the single most valuable piece of practical charging advice, and it is delightfully simple: on a road trip, **charge to about eighty per cent and drive on.** The stretch from eighty to a hundred is the slowest, least rewarding part of the curve — you spend a long time gaining relatively little range — so you almost always cover more distance in less total time by charging to eighty, driving, and stopping again briefly, than by waiting at each stop for a full battery. The "0 to 100 per cent" time that people quote is nearly meaningless for journey planning; the number that matters is something like "10 to 80 per cent," the fast part of the curve, where fast charging earns its name.

Two useful footnotes tie the chapter together. First, this is exactly why preconditioning from Chapter 7 matters so much: arriving with a warm, ready battery lets the car sit up at the top of the fast part of the curve from the moment you plug in, instead of crawling while the pack warms. A cold battery has a low, sad charge curve; a preconditioned one has a tall, fast one. Second, the taper explains the apparent paradox that a bigger, more powerful charger does not always charge much faster — because past a certain point the limit is the battery's appetite, not the charger's power, and a 350-kilowatt charger cannot force a nearly-full pack to accept 350 kilowatts any more than a fire hose can fill an almost-full glass faster than a tap.

Understand the curve and you understand charging. It is not a bath filling at a constant rate; it is a battery accepting energy eagerly when empty and reluctantly when full, refereed the whole time by a BMS that would always rather protect the pack than shave a minute off your stop. Which leaves two questions, one surprising and one merely overdue. The surprising one first: everything this chapter has described so far assumes the energy is flowing *into* the car — and there is no law of physics that says it must.

---

**Sources**

- Recharged, InsideEVs, Elinta Charge, chargingadvisor — charge tapering controlled by the BMS to prevent overvoltage/overheating; peak charging roughly 10–50%, sharp slowdown past 80%; contributing factors of chemistry (filling parking spaces), temperature, cell balancing, efficiency.
- Practical "charge to ~80% on trips" and "10–80% is the meaningful metric" follow directly from the curve; preconditioning link from Chapter 7; charger-power-vs-appetite point from 11.2.
