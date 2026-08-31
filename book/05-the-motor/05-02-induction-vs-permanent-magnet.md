## 5.2 Induction vs. permanent-magnet — why both

The last section left a gap on purpose. The sweeping magnetic field drags the rotor round — but what *is* the rotor, the thing being dragged? It turns out there are two good answers, two whole families of motor built on the same rotating-field principle, and they have opposite personalities. Tesla, rather than choosing between them, has often built cars that use one of each, and the reason is one of the neatest pieces of pragmatism in the car.

The first kind is the **induction motor**, and it is the one Tesla started with — a design so associated with the physicist Nikola Tesla that the company is named after him. Its rotor carries no magnets at all. Instead it is a cage of conducting bars, the so-called squirrel cage, and it works by a lovely piece of physical jujitsu. The stator's sweeping field, passing over the bars, *induces* electric currents in them — this is the same Faraday induction that runs the whole electrical world — and those induced currents create their own magnetism, which the sweeping field then grabs and drags along. The rotor makes its own magnetism to order, out of the field that is chasing it. There is a catch built into the physics: the rotor must always turn slightly slower than the field, because if it ever caught up, the field would stop sweeping past the bars and the induction would cease. That deliberate lag is called slip, and an induction motor lives on it.

The second kind is the **permanent-magnet motor**, and it does the obvious thing the induction motor pointedly avoids: it puts actual magnets on the rotor. Now the stator's field has something permanently magnetic to grab, and it drags the rotor round in perfect lockstep — no slip, no lag; the rotor turns exactly as fast as the field sweeps, which is why this type is called synchronous. Tesla's version, used in the Model 3 and Y, is a sophisticated variant that also exploits the shape of the rotor's iron to add extra pull, and goes by the mouthful of names IPM-SynRM. The details matter less than the headline: because the magnets are always there, providing their magnetism for free, this motor does not have to spend energy magnetising its own rotor the way the induction motor does.

That single difference — free magnetism versus made-to-order magnetism — sets up the whole trade-off. The permanent-magnet motor is more efficient, especially at the low and medium speeds where a car actually spends most of its life, because it gets its rotor field gratis; independent figures put the Model 3's permanent-magnet motor around **96 per cent** efficient against roughly **94 per cent** for a comparable induction motor. But that free magnetism has to be bought elsewhere: the magnets are made of rare-earth metals, expensive and geopolitically awkward, and — more subtly — they never switch off. Even when you are coasting and want the motor to do nothing, the magnets keep sweeping past the stator coils, generating a drag you must actively cancel.

The induction motor is the mirror image. It is a little less efficient in gentle everyday driving because of the energy spent magnetising its rotor, and it uses no rare-earth magnets — just cheap, robust copper or aluminium and iron. Its special virtue is that when you do not need it, it can be switched fully off and left to freewheel with almost no drag at all, because with no current in the stator there is no magnetism anywhere and nothing to cancel. It is also happy being pushed hard at high speed.

Now the punchline, for a dual-motor car with a motor on each axle:

```
   REAR motor: permanent-magnet (synchronous)
     - efficient at low/medium speed = your daily commute
     - does the everyday work, most of the time

   FRONT motor: induction (asynchronous)
     - can idle with near-zero drag when not needed
     - wakes up for hard acceleration and high speed
     - no rare-earth magnets

   Result: the efficient one runs constantly; the muscular one
   only joins in when it earns its keep -- best of both.
```

This is why Tesla builds cars with two different kinds of motor rather than two of the same. The permanent-magnet motor on one axle handles the ordinary business of driving efficiently. The induction motor on the other axle sits idle and dragless for most of a journey, then springs to life when you ask for real acceleration or reach high speed, contributing muscle exactly when the permanent-magnet motor's efficiency advantage matters least. Each motor covers the other's weakness. The car gets the everyday economy of the magnet motor and the on-demand power and dragless coasting of the induction motor, and pays the full cost of neither.

It is a very characteristic kind of cleverness — not a single brilliant machine, but two ordinary ones arranged so their flaws cancel. And it only works because, as the next section explains, an electric motor is so untroubled by having to cover a huge range of speeds that you can bolt one straight to the wheels through a single, unchanging gear.

---

**Sources**

- Tesmanian and lesics.com — Model 3 rear IPM-SynRM permanent-magnet motor; front AC induction motor on AWD; efficiency ~96% (PM) vs ~94% (induction).
- Tesla Owners Online / Tesla Motors Club — rationale for dual motor types: PM efficiency at low/medium speed, induction dragless idling and high-speed strength.
- Squirrel-cage induction and slip; permanent-magnet synchronous operation — standard machine theory (Tutorialspoint, Electrical4U); rare-earth magnet cost/supply is widely reported industry context.
