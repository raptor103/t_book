## 11.4 When the energy flows backwards

Here is a number that ought to be more famous than it is. A typical house in Europe gets through something like ten kilowatt-hours of electricity a day. A Cybertruck carries a battery of roughly a hundred and twenty. Park one on your driveway and you have, sitting there doing nothing, about *twelve days* of household electricity — a domestic power station with wheels, spending twenty-three hours a day as an extremely expensive paperweight. Every electric car on every street is a similar store, and until very recently the entire industry treated the plug as a one-way valve. This chapter has so far described energy going in. It is time to admit that the wire works in both directions, and that this may turn out to be the most consequential thing about electric cars that has nothing to do with driving them.

The idea goes by an ugly family of names, all of them variations on the same theme: *vehicle-to-load* (V2L) means running a tool or a kettle off the car; *vehicle-to-home* (V2H) means running your house off it; *vehicle-to-grid* (V2G) means selling power back to the utility. Tesla's implementation of the family is called **Powershare**, and it arrived with the Cybertruck. What matters for a book about how the machine works is that these are not software features. They are a hardware capability, and to understand why, we need to go back to the box from Chapter 8.

Recall the PCS, the Power Conversion System bolted under the rear seat in its compartment nicknamed the penthouse. Section 8.3 introduced it as a combined onboard charger and DC-DC converter: it takes alternating current from the wall and rectifies it into direct current the pack can drink. Now look at that description again with the last few chapters in mind, and something ought to nag. Turning DC into AC by switching very fast is *exactly* what Chapter 4 spent its entire length describing, because that is what an inverter does. The onboard charger is a power-electronics bridge between an AC world and a DC one — and a bridge, in principle, does not care which way traffic crosses it. The very switches that turn mains AC into pack DC can also run the other way, turning pack DC back into mains AC — provided they are designed and controlled to work in both directions.

That qualifier — *designed and controlled to work in both directions* — is doing real work. Making a charger run backwards is not free: the switching devices must conduct and block in both directions, and the control software must synchronise its output with the grid's own fifty-hertz rhythm, matching frequency and phase, rather than simply following whatever the wall provides. Above all it must satisfy a safety rule called *anti-islanding* — the absolute obligation to shut down the instant the grid goes dead, so that a car on a suburban driveway cannot quietly electrify a length of cable that a lineman upstream believes is safely disconnected. Which is why vehicle-to-home is never just a cable. Powershare needs a **Powershare Gateway** at the house, a box whose job is to sense the outage, physically disconnect the home from the street, and only then let the car take over the household circuits.

The energy, running the other way:

```
   CHARGING  (sections 11.1 to 11.3)

     grid AC ---> [ onboard charger ] ---> DC ---> the pack

   DISCHARGING  (the same silicon, running backwards)

     the pack ---> DC ---> [ the same switches, inverting ] ---> AC
                                                          |
                        V2L  a socket: tools, a kettle <--+
                        V2H  the house, through a gateway <-+
                        V2G  the grid, sold back <----------+

   The gateway's real job is not conversion but disconnection:
   it cuts the house off from the street FIRST, so the car can
   never backfeed a line someone believes is dead.
```

With that plumbing in place the numbers become domestic rather than theoretical. Powershare Home Backup delivers up to **11.5 kilowatts** to a house — comfortably more than a home draws at its busiest — and Tesla's claim is that a Cybertruck can carry a household through a blackout for **more than three days**. The simpler modes need less apparatus: the truck's own sockets supply up to **9.6 kilowatts** for tools or a campsite, which is enough to run a building site, and the car can also charge another electric car, roadside, from its own pack. Somewhere in there the car stops being a consumer of the energy system and becomes a participant in it.

The caveats matter, and this book's convention is to state them rather than let the excitement run. As of 2026 Powershare Home Backup — the version that matters in a blackout — is a Cybertruck feature and a Cybertruck feature alone. Tesla does not offer it on the Model S, 3, X or Y, which were not built with the outlets or the bidirectional hardware it requires. What the Model Y has gained instead is the campsite version: the higher trims can take a roughly eighty-euro adapter that turns the car into a 2.4-kilowatt household socket — enough for tools, a kettle or a fridge, and about a fifth of what the Cybertruck can push into a house. The distinction is worth holding onto, because the word "bidirectional" is doing a great deal of work in the marketing of both. [INFERENCE — the underlying hardware capability of past model years is not published by Tesla, and the widespread assumption that older cars could run backwards if only the software allowed rests on the charger topology being inherently bidirectional, not on any confirmation.] And there is a cost the brochures underplay, which readers of Chapter 3 will anticipate immediately: cycling the pack to power a house is still cycling the pack. Every kilowatt-hour sent to the fridge is a kilowatt-hour of the battery's finite life spent on something other than driving.

Still, step back and look at what the architecture implies. A country that replaces its cars with electric ones does not merely acquire cleaner transport; it acquires, incidentally, an enormous distributed battery — tens of gigawatt-hours of storage, already paid for, already installed, sitting idle on driveways at exactly the hours when a grid full of solar and wind most needs somewhere to put its surplus or somewhere to draw its shortfall. That is a genuinely large idea, and it arrives almost as an accident of having put a very good inverter in every car. The last section of this chapter turns from what flows through the plug to the far more quarrelsome question of what the plug should look like.

---

**Sources**

- Tesla (tesla.com/powershare and Powershare support pages), Electrek, Green Car Reports, Wikipedia (Tesla Powershare) — Powershare split into Home Backup (V2H), Outlets, and Mobile; up to 11.5 kW continuous to a home and backup for over three days; up to 9.6 kW across the vehicle's outlets; vehicle-to-vehicle charging; requires a Powershare Gateway plus a Universal/bidirectional Wall Connector.
- tesla.com/powershare and Not a Tesla App, "Tesla Powershare Explained" — Home Backup is listed as unavailable on Model S, 3, X and Y, which lack the outlets and bidirectional hardware it requires; it remains a Cybertruck feature.
- Electrek (August 2026) — Tesla's ~$80 vehicle-to-load adapter for Model Y Premium and Performance, giving a 20 A / ~2.4 kW household outlet. This is V2L, not home backup.
- Anti-islanding as a mandatory grid-protection requirement, and the transfer-switch role of the gateway, are standard distributed-generation engineering (IEEE 1547 and equivalent European practice).
- Household consumption figure (~10 kWh/day) is a rounded European average used here as a scale anchor, not a Tesla specification; Cybertruck pack capacity ~123 kWh. [INFERENCE — pack capacity is a teardown/EPA-derived estimate, not an official Tesla figure.]
- The bidirectionality of the onboard charger's power-electronics topology follows from the inverter principles of Chapter 4 and the PCS description in 8.3; pack-cycling degradation cross-references 3.4.
