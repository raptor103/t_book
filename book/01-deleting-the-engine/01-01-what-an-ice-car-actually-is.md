## 1.1 What an internal-combustion car actually is

Set fire to a cup of gasoline and it simply burns — a hot, useless, faintly alarming flame. To make that same cupful move a ton and a half of metal down a highway, you need one of the most quietly deranged machines humans have ever built: a device that takes the explosion, that most uncontrollable of events, and arranges to have it happen in a sealed metal chamber several thousand times a minute, on schedule, forever, without ever blowing itself apart. That machine is the internal-combustion engine, and once you look at it clearly, the strangest thing about it is how much of the car exists only to cope with it.

Start with what it is. A gasoline engine is a set of cylinders — usually four in an ordinary car — in each of which a piston slides up and down. Fuel and air are squeezed into the top of the cylinder, a spark lights them, and the resulting bang shoves the piston down. That downward shove is the entire point; everything else is plumbing. The pistons turn a crankshaft, the crankshaft spins, and that spin, eventually, reaches the wheels. To keep the bangs coming in the right order you need camshafts, valves, springs, a timing chain. To stop the whole thing seizing solid you need oil pumped everywhere under pressure. To stop it melting you need a cooling system — a radiator, a water pump, liters of coolant circulating constantly. To start it at all you need a separate electric motor, because an engine cannot begin turning itself. Count the moving parts and you arrive somewhere around two hundred in the powertrain alone [INFERENCE — commonly cited industry figure, not a single audited count], every one of them wearing, needing lubrication, and eventually failing.

And here is the part that should genuinely astonish you: for all that machinery, most of the fuel is wasted. Not a little of it — most of it. The figures are not controversial; they come from the United States Department of Energy, which has measured them exhaustively. Of the energy in a tank of gasoline, only somewhere between **18 and 25 percent** actually reaches the wheels. The rest is lost, and the largest share by far — around **68 to 72 percent** — is simply thrown away as heat: out of the exhaust pipe, into the radiator, off the engine block into the air. You have, in effect, a very expensive heater that produces motion as a side effect.

Concise diagram of where a tankful of gasoline actually goes:

```
   100 units of energy in a tank of gasoline
   -------------------------------------------------------
    -70   engine losses, mostly heat, out of the
          exhaust pipe and the radiator
    - 3   idling at traffic lights
    - 4   drivetrain friction
    - 5   pumps, alternator, accessories
   -------------------------------------------------------
     18   reaches the wheels
          (18-25 in practice, and the only part you
           actually wanted to buy)
```

There is worse. The engine only works well within a narrow band of speeds — too slow and it stalls, too fast and it tears itself up — and that band does not match the range of speeds a car actually needs, from crawling in a parking lot to cruising at 130 km/h (80 mph). So you bolt on a gearbox: a heavy, precise, oil-filled box of cogs whose entire job is to keep translating between the engine's fussy comfort zone and the road's demands. Every gear change is a small confession that the power source cannot do what is asked of it directly. Add the clutch, the driveshafts, the differential, and you have a second complicated machine that exists purely to manage the failings of the first.

Now step back and look at the car as a whole. The engine is heavy, so it sits low and forward, and the chassis is built around it. It is hot, so the front of the car becomes a giant air scoop feeding the radiator. It vibrates, so the whole thing floats on rubber mounts. It breathes, so there is an intake, a filter, an exhaust, a catalytic converter, a silencer running the length of the underbody. It needs feeding, so there is a fuel tank, lines, a pump, injectors. A conventional car is not a passenger box with an engine added. It is an engine with a passenger box wrapped around it, and nearly every design decision — the long hood, the transmission tunnel running between the front seats, the grille — is a scar left by the thing under the hood.

Hold that picture in your head, because the entire premise of an electric car is a single, radical act of subtraction. Take the engine out. Take the gearbox, the exhaust, the fuel system, the cooling of the block, the two hundred moving parts, the whole apparatus of coping — and simply delete it. What is left, and what has to be reinvented in its place, is the subject of everything that follows.

---

**Sources**

- U.S. Department of Energy / EPA, *Where the Energy Goes: Gasoline Vehicles*, fueleconomy.gov — energy-loss breakdown (18–25% to wheels; ~68–72% engine/heat losses).
- ScienceDirect, "Estimation of tank-to-wheel efficiency functions based on type approval data" (2020) — tank-to-wheel efficiency figures for ICE vehicles.
- Industry teardown commentary comparing ICE powertrain (~200 moving parts) with EV drivetrain (~17–20 moving parts); figure marked [INFERENCE] as a widely cited approximation rather than an audited count.
