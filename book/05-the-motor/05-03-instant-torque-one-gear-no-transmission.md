## 5.3 Instant torque, one gear, no transmission

A petrol car has a gearbox because its engine is fussy. As we saw in Chapter 1, an engine makes useful power only within a narrow band of speeds, and that band is far too small to cover everything from pulling away at a junction to cruising on a motorway. So the gearbox exists to keep swapping ratios, endlessly re-matching the engine's little comfort zone to the road's wide demands. Five, six, seven gears; a clutch; a lever; the whole ritual of shifting. It is all a workaround for one shortcoming: the engine cannot cover the range on its own.

An electric motor can. And that single fact deletes the entire gearbox.

Remember the two things a motor does effortlessly that an engine cannot. It makes its full torque from zero revolutions — maximum shove available the instant it starts to turn, without needing to build up speed first. And it keeps turning usefully across an enormous span of speeds: a Tesla motor spins happily from a standstill all the way to around **eighteen thousand revolutions a minute**, roughly three times the redline of a typical petrol engine. One device, covering from nothing to eighteen thousand, with strong torque available throughout. There is simply no gap for a gearbox to bridge, because there is no range the motor cannot cover by itself.

So instead of a gearbox, an electric car has a *reduction gear* — a single, fixed set of cogs that does one unchanging job. The motor spins fast and with modest torque; the wheels need to spin slower and with far more torque. A fixed reduction of about **nine to one** trades one for the other: it divides the motor's speed by nine and multiplies its torque by nine, once, permanently, with no choices to make. In a Model 3 the exact ratio is a shade over 9:1, achieved with two pairs of gears, and it lets the motor's eighteen thousand rpm become a top road speed north of 250 km/h with no shifting at any point in between.

The whole "transmission," end to end:

```
   ENGINE CAR                        ELECTRIC CAR
   engine: narrow usable band        motor: 0 to ~18,000 rpm, strong
      |                                 throughout
   clutch (disconnect to shift)        |
      |                              (no clutch -- never disconnects)
   gearbox: 5-7 ratios, always         |
   swapping to stay in the band     reduction gear: ONE fixed ratio
      |                              ~9:1, divides speed x9,
   driveshafts -> wheels             multiplies torque x9
                                        |
                                     driveshafts -> wheels
```

The consequences ripple outward. There is no clutch, so the drive is never interrupted — the motor stays connected to the wheels at all times, which is part of why regenerative braking (next chapter) is even possible. There is no gear-change, so there is no shift shock, no pause, no hunting for the right ratio on a hill; acceleration is one seamless surge from zero to top speed, uninterrupted, the way a single long note differs from a scale. There is no gear lever and, increasingly, no obvious "transmission" at all — just a compact housing bolting the motor to the wheels. And there are far fewer parts to build, lubricate and break: a handful of gears instead of a dozen synchronised ratios, a clutch, and their hydraulics.

It is worth dwelling on how much *engineering history* is quietly discarded here. The multi-speed automatic gearbox is one of the great achievements of twentieth-century mechanical engineering — a marvel of hydraulics and control, refined over decades by thousands of clever people. The electric car does not improve on it. It renders it unnecessary. That is a different and slightly ruthless kind of progress: not building a better version of the hard thing, but changing the problem so the hard thing is no longer needed at all. We saw it with the engine, and here it is again with the gearbox.

A small honest caveat keeps the enthusiasm in check. A very small number of high-performance electric cars have experimented with two-speed gearboxes, to squeeze out both fierce acceleration and a high top speed, and there are efficiency arguments for a second ratio at the extremes. But for the overwhelming majority of electric cars, including every mainstream Tesla, the single reduction gear is not a compromise. It is simply enough. The motor's range is so wide and its torque so flat that a second gear would add cost, weight and complexity to solve a problem the car does not have.

One gear. No clutch. No shifting. A hundred and forty years of transmission engineering, politely set aside. And all of it made possible by a motor that makes its full effort the instant you ask and never runs out of range — which leaves only the small matter of the invisible refinements that turn a good drive unit into an excellent one.

---

**Sources**

- Tesla Motors Club (Highland Model 3 deep dive) and Fellten/ampREVOLT drivetrain listings — Model 3 overall reduction ratio ≈9.036:1 (two gear pairs, 81/31 × 83/24), motor to ~18,000–18,447 rpm, ~262 km/h top speed.
- InsideEVs, "Tesla Model 3/Model Y Modular Electric Drive Units" — single-speed reduction drive-unit design.
- Motor speed range and instant-torque behaviour from Chapters 1 and 4; two-speed EV gearbox exceptions are general industry context.
