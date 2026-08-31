## 8.4 From lead-acid to 16V lithium to 48V

The low-voltage world is the most conservative corner of the car, and for a strange reason: its very universality made it hard to change. For over a century, "twelve volts" and "lead-acid battery" were so standard that an entire planet's worth of components — every bulb, motor, relay and switch a car might use — was built to that assumption. To change the low-voltage system was to break compatibility with the whole ecosystem. So even the most radical electric cars, for years, kept a perfectly ordinary twelve-volt lead-acid battery under the bonnet, the same lump of lead and acid your grandfather's car used, sitting incongruously inside the most advanced vehicle of its age. It is a good reminder that even revolutions carry their ancestors around for a while.

The first change was to the battery's chemistry, and it addressed the weakness we met two sections ago: lead-acid batteries are heavy, they dislike being deeply discharged, and they die relatively young — and when the low-voltage battery dies, the whole car is stranded. So Tesla, around the turn of 2022, began replacing the lead-acid unit with a small *lithium-ion* low-voltage battery. Confusingly to newcomers, these have often run at around sixteen volts rather than twelve — close enough to keep the twelve-volt ecosystem happy, but chosen to suit the lithium chemistry — and some newer cars have moved to a small LFP low-voltage battery instead. The details matter less than the direction: the ancient lead-acid battery, the last truly Victorian component in the car, is being retired in favour of a lithium one that is lighter, longer-lived, and less likely to leave you stuck. It is the same logic as the main pack, applied to its small cousin.

The second change is far bigger, and it is the one this section is really about: abandoning twelve volts altogether in favour of *forty-eight*. The reasoning is the same physics that gave us two voltages in the first place, now turned on the low-voltage world itself. Power is voltage times current, and current is the expensive, wire-thickening, heat-making part. Raise the low-voltage system's voltage from twelve to forty-eight — a factor of four — and you can deliver the same power at a *quarter* of the current. A quarter of the current means much thinner wires can carry it, because there is far less heat to shed, which means dramatically less copper.

Why 48 volts saves so much wire:

```
   The same power, delivered at two different voltages:

   at 12 V   current [############################]
                     thick, heavy, expensive copper

   at 48 V   current [#######]
                     one quarter the current, and a small
                     fraction of the copper

   Four times the voltage = one quarter the current for the
   same power. And 48 V is still safely below the ~60 V
   threshold at which electricity becomes a shock hazard.
```

That copper is not trivial. The low-voltage wiring harness of a modern car is one of its heaviest, most sprawling, most labour-intensive components — kilometres of wire threaded through the whole body, which the next chapter is devoted to. Cutting the current fourfold lets that harness slim down substantially, saving weight, cost, and the sheer effort of building it. And forty-eight volts sits at a sweet spot: high enough to bring these savings, but still comfortably below the roughly sixty-volt threshold at which electricity becomes a shock hazard to a human, so it remains part of the "safe" low-voltage world, needing none of the isolation and armour of the high-voltage side. It is the highest voltage you can use without inheriting the dangers of high voltage.

Tesla introduced a full forty-eight-volt low-voltage architecture on the Cybertruck, and — in a move worth noting for a company not famous for openness — published the specification and offered it to the rest of the industry, hoping to break the century-old twelve-volt standard by making its replacement freely available. The reason for the generosity is self-interested but sound: forty-eight volts only pays off fully when the whole ecosystem of components moves with it, so encouraging rivals to adopt the same standard makes those components cheaper for everyone, Tesla included. The change also *enables* things twelve volts struggled to, because some of the newest features — the steer-by-wire and rear-wheel steering of Chapter 14 — want to drive small motors with meaningful power, and doing that at forty-eight volts rather than twelve means thinner wires to each, exactly where thin wires are most welcome.

This is a piece of "direction of travel" rather than the state of every car on the road today, and this book flags it as such: the mainstream Model 3 and Y still live largely in the twelve-volt (now sixteen-volt lithium) world, while forty-eight volts is the architecture the newest designs point toward. But the trajectory is clear, and it is all of a piece with everything in this chapter. The low-voltage backbone — the least glamorous, most conservative part of the car — is being modernised on the same principles as the rest of the machine: lighter batteries, less copper, fewer kilograms, every watt and every wire treated as something to be trimmed. Which is the perfect cue for the next chapter, because once you start caring this much about wire, you start rethinking the entire nervous system that the wire is part of.

---

**Sources**

- Tesla Motors Club, Tesla service bulletins, evseekers — transition from 12V lead-acid to ~16V lithium-ion low-voltage battery (~late 2021–early 2022); some newer cars using ~12.8V LFP.
- The Driven, InsideEVs, Munro/leandesign, Vicor — Cybertruck 48V low-voltage architecture; 4× voltage → ¼ current → thinner/lighter wiring and less copper; 48V below the shock-hazard threshold; Tesla open-sourcing the 48V spec.
- InsideEVs / carbuzz — 48V enabling steer-by-wire and rear-wheel steering (developed in Chapter 14). 48V as direction-of-travel, not yet universal across the 3/Y, is stated per this book's convention.
