## 11.2 Onboard charger vs. Supercharger

The last section left us with two converters — a small one the car carries and a giant one at the roadside — and an obvious question a sensible person immediately asks: why not just carry the giant one? If a DC fast charger can refill a battery in twenty minutes, why does every car not simply have that capability built in, so you could get a rapid charge from any socket? The answer is a lovely lesson in engineering trade-offs, and it explains the whole peculiar division of labour in EV charging.

Consider what it would take to carry a Supercharger's worth of converting power around with you. A 250-kilowatt converter is not a scaled-up version of the 11-kilowatt one in the car; it is a different beast entirely. It is bulky — a substantial cabinet, not a shoebox. It is heavy, and by now you know what this book thinks of dead weight: every kilogram carried is range lost forever, so hauling a fridge-sized converter around on the off-chance you might fast-charge would quietly cost you range on every single journey. It runs hot at those power levels and needs serious liquid cooling. And it is expensive — the converting hardware is one of the pricier parts of a fast charger. To build all that into every car would mean every owner paying for, and carrying, and cooling, a massive converter that sits idle ninety-nine per cent of the time.

So the engineering does the obvious economical thing: it splits the job by how often each kind of charging is actually needed. Most charging, by far, happens slowly and predictably — overnight at home, or during the hours a car sits parked at work or a hotel. For that, a small, cheap, light onboard charger is perfect, because time is abundant when you are asleep. The car carries only what it needs for the common case. The rare case — needing a lot of energy fast, on a long journey — is handled by putting the giant, expensive converter *at the roadside*, where it does not have to be carried, can be as big and well-cooled as necessary, and, crucially, is **shared**. One Supercharger cabinet serves car after car after car, so its cost is spread across thousands of charging sessions rather than borne by a single vehicle.

The division of labour:

```
   ONBOARD CHARGER               SUPERCHARGER
   (you carry it everywhere)     (you visit it)
   -------------------------------------------------------------
   small, light, cheap           huge, heavy, expensive, cooled
   converts AC->DC in the car    converts AC->DC in the cabinet
   ~7-11 kW                      up to 250 kW and beyond
   for the COMMON case:          for the RARE case:
   slow, overnight, time to      fast, mid-journey, in a hurry
   spare
   anywhere there is a socket    only at dedicated stations
   you carry its weight even     its cost is SHARED across
   when it is idle               every car that visits
   -------------------------------------------------------------

   Not rivals: one car, two doors into the same battery.
```

This is why the Supercharger network matters as much as the car itself, and why it deserves a word here even in a book about engineering rather than business. A fast charger is useless in isolation; what makes it valuable is that there are many of them, reliably working, spaced along the routes people actually drive. Tesla's decision to build that network itself — rather than wait for others to — is one of the reasons its cars became practical for long journeys years before many rivals, and it is the network, as much as the plug, that every other carmaker wanted access to when they adopted Tesla's connector in the story of Chapter 10. The car and the network are two halves of one system; neither is much use without the other.

There is a subtlety worth adding, because it prevents a common misunderstanding. The two converters are not rivals; a car uses *both*, on different occasions, and the same battery accepts energy from either. When you AC-charge at home, the onboard charger is working and the Supercharger circuitry is irrelevant. When you DC fast-charge on a trip, the onboard charger sits idle and the roadside cabinet feeds the pack directly. The car simply routes the incoming power appropriately: through its own converter for AC, or straight to the pack for DC. It is not two kinds of car but one car with two doors into its battery — a small one it carries for everyday use, and a large one it borrows from the roadside when speed matters.

And yet even the mightiest roadside converter cannot make a battery charge at full speed all the way to full. Plug into a 250-kilowatt charger with a nearly-full battery and you will not get anything like 250 kilowatts, no matter how big the cabinet is — because the limiting factor is no longer the converter at all, but the battery's own changing appetite. That appetite, and why it fades as the battery fills, is one of the most useful things a driver can understand, and it is the subject of the next section.

---

**Sources**

- ChargePoint / Wevolver / Ekoenergetyka — onboard charger (small, in-vehicle, ~7–11 kW) vs DC fast charger (large external cabinet, hundreds of kW); a 150 kW DC charger delivers ~10× an 11 kW AC charger.
- Supercharger V3 (~250 kW) and higher V4 figures are Tesla's published network specs; weight/cost/cooling trade-offs of carrying a large converter follow from the AC/DC distinction in 11.1 and this book's efficiency framing.
- Battery-side limits at high state of charge developed in 11.3.
