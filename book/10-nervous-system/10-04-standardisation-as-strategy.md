## 10.4 Standardisation as strategy (NACS, LVCS)

There is a puzzle in this chapter that a business-minded reader will have spotted. A company spends years and fortunes engineering a superior charging plug, or a cleaner scheme of low-voltage connectors, and then — instead of guarding these advantages jealously — it publishes the specifications and invites its rivals to copy them for free. Why would anyone do that? The answer turns standardisation from a piece of dull housekeeping into one of the sharpest strategic moves in the whole industry, and it is a fitting note to end the electrical backbone on, because it is about the connectors and standards that are the backbone's physical vocabulary.

The clearest case is the charging plug. For years North America had a messy standoff of competing connectors, with Tesla using its own slim design and most other makers using a bulkier one called CCS. Tesla's plug was smaller, neater, and — because Tesla had built the largest and most reliable fast-charging network in the world to go with it — attached to something everyone else wanted access to. In late 2022 Tesla did something telling: it published its connector's design, renamed it the North American Charging Standard, and offered it to the entire industry. What followed was a rout. Through 2023, Ford, then General Motors, then seemingly every major carmaker — Rivian, Volvo, Mercedes, Hyundai, Kia, Honda, Toyota and more — announced they would adopt the plug, and a standards body formally blessed it as an official standard. In the space of about a year, one company's proprietary connector became the connector the whole continent would use.

Look at what Tesla gained by giving something away. Its plug design became the industry default, which entrenches Tesla's engineering choices at the heart of every rival's car. Its charging network, already dominant, gained a flood of new paying customers driving other brands. And the sheer scale of a single shared standard drives down the cost of every connector, adapter and charger for everyone — Tesla included — because the whole industry now buys the same parts. Generosity and self-interest turn out to be the same act: by making its standard free, Tesla made its standard *win*, and a winning standard is worth far more than a jealously guarded one that stays niche.

The same logic reaches inside the car, to the humble low-voltage connectors — the little plugs where every wire meets every device. Here the enemy is not a rival standard but sheer chaos: a typical car uses a bewildering variety of different connector types, hundreds of them, a legacy of decades of each supplier and each system doing its own thing. That variety is expensive, complicated to manufacture, and hostile to automation — every different connector is a different part to stock and a different motion for a robot to learn. Tesla's response was to publish a Low Voltage Connector Standard, a deliberately small, rationalised set of connector types meant to cover the whole car, and — as with the charging plug — to offer it to the industry rather than hoard it.

Standardisation working in Tesla's favour:

```
   The move: publish your own standard, then invite rivals in.

   CHARGING PLUG (NACS)          LOW-VOLTAGE CONNECTORS (LVCS)

   a proprietary plug ...        hundreds of connector types ...
        |                             |
        v                             v
   published, and adopted        cut down to one small
   across the industry           standard set
        |                             |
        v                             v
   Tesla's design becomes        fewer parts, cheaper, and far
   the default; its network      friendlier to ROBOT assembly
   gains customers; costs        -- the harness goal from the
   fall for everyone at scale    start of this chapter
```

The connective tissue between these two examples is the theme of the whole part: fewer, simpler, cheaper, more automatable. Reducing a car to a handful of standard connectors serves exactly the same end as zonal wiring and forty-eight-volt power and the Etherloop — it shortens the harness, simplifies the factory, and inches the car toward being something a machine can build. Standardisation is not separate from the engineering; it is the engineering, pursued at the level of the parts catalogue rather than the circuit.

And there is a larger lesson here that echoes beyond wiring, one worth carrying into the rest of the book. Tesla's habit of publishing standards — the charging plug, the connector set, the forty-eight-volt architecture of Chapter 8 — reflects a company that often competes less by keeping secrets than by *setting the terms* everyone else must build to. When your design becomes the industry's default, you no longer merely make a good product; you shape the ground on which every competitor stands. That is a different and more durable kind of advantage than any single clever component, and it is one reason the influence of these cars runs well beyond the number of them on the road.

With that, the electrical backbone is complete: two voltages, zonal controllers, eFuses, a shrinking harness, a fast and resilient data loop, and a set of open standards binding it together. The car now has a body, a drivetrain, a thermal system, and a nervous system. What it still needs is to be *refuelled* — and charging, it turns out, is its own rich and frequently misunderstood story. That is Part VI.

---

**Sources**

- CNBC, TechCrunch, Bloomberg, The Auto Channel — Tesla published its connector as NACS (2022), standardised as SAE J3400; Ford, GM, Rivian, Volvo, Mercedes, Hyundai, Kia, Honda, Toyota and others adopted it through 2023.
- Tesla's "Low Voltage Connector Standard" publication — rationalising the large variety of automotive low-voltage connectors into a small standard set to cut cost and aid automation. Some LVCS specifics are treated as [INFERENCE] where not fully confirmed in the sources retrieved.
- Strategic analysis (network effects, cost-at-scale, standard-setting) synthesised from the above reporting; links to harness/automation goals from earlier in this chapter and Chapter 20.
