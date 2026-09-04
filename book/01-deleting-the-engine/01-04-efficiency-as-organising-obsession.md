## 1.4 Efficiency as the organizing obsession

For a hundred years, car engineers were allowed to be wasteful, and they knew it. Gasoline was cheap, extraordinarily energy-dense, and could be replenished in the time it takes to buy a coffee. If your engine threw away three-quarters of its fuel as heat — and it did — you simply carried a bit more fuel. Efficiency was a virtue, pursued when convenient, but it was never the thing the whole car was organized around. There was always slack in the system.

Take the engine out, and the slack vanishes overnight.

The reason is the battery, and it is worth being blunt about it. The battery is the single heaviest and most expensive object in an electric car — a slab that can weigh half a ton and cost as much as a small second-hand car all by itself. Every unit of energy it holds was expensive to buy and is heavy to carry. So the calculus flips completely. In a gasoline car, wasted energy cost you a little extra fuel. In an electric car, wasted energy costs you *range* — and to buy the range back you must add battery, and battery adds weight and cost, and the extra weight consumes yet more energy, and round the spiral goes. Efficiency stops being a virtue and becomes the master variable. Save a watt anywhere and you have, in effect, been handed free range, free weight and free money, all at once.

This is the single idea that explains almost every strange design choice in the rest of this book. Once you see it, you cannot unsee it.

Why does a Tesla have those flush door handles that pop out to greet you? To smooth the airflow. Why the near-total absence of a front grille? Because a hole in the front of a car is a hole that air falls into, and air is the enemy. Why the smooth belly pan under the floor, the small aerodynamic wheel covers that owners either love or quietly replace, the obsessive sculpting of every mirror and pillar? All of it is a war on drag — and drag matters ferociously because, as we will see in Part VII, the power needed to push air aside rises with the *cube* of speed, so a small gain in slipperiness at 120 km/h (75 mph) pays off out of all proportion where it counts. The result is a body with a drag coefficient of around **0.23** — and, in the latest version, **0.219** — numbers that put a family sedan into territory once reserved for the odd hand-built streamliner. Tesla's own engineers have said that this single aerodynamic improvement was the largest factor in an eight percent efficiency gain on the updated car. Eight percent, from shaping the air.

The obsession does not stop at the skin. It reaches into the tires, chosen and constructed to roll with less resistance. Into the heat pump, which we will meet later, whose entire reason for existing is to warm the cabin using a quarter of the electricity a simple heater would burn. Into the regenerative braking that scavenges back the energy of every slowing. Into the motor, tuned for efficiency across the speeds you actually drive, and into an oil pump for that motor that is itself electric, so it only runs when needed rather than being dragged along constantly. None of these is dramatic on its own. Each buys back a percent, or a fraction of a percent. Added together, across the whole car, they are the difference between a usable range and a disappointing one.

The payoff is a number that would have been science fiction to an engine designer. Where a gasoline car delivers perhaps a fifth of its fuel's energy to the road, an electric car delivers the great majority of it — commonly **80 to 90 percent**, measured from the battery to the wheels. A Model 3 will carry a person and their groceries using somewhere around **130 to 160 watt-hours per kilometer**, which is to say it travels the length of a football field on roughly the energy an electric kettle uses to not-quite-boil.

The contrast, drawn crudely:

```
   Where the energy goes  (tank or battery  ->  wheels)
   Both bars are the same 100 units.  # = reaches the wheels.

   GASOLINE  [########--------------------------------]  ~20%
   ELECTRIC  [##################################------]  ~85%

   Same bar, same scale: about one part in five, against
   four to four and a half.
```

This is why "efficiency as an obsession" is the right frame for the whole machine, and why it belongs at the end of the first chapter. Deleting the engine was only the opening move. Everything that follows — the chemistry of the cells, the switching of the inverter, the cleverness of the thermal system, the shortening of every wire — is the same obsession, followed relentlessly into every corner of the car. An electric car is not merely a vehicle that happens to be efficient. It is a machine in which efficiency has become the organizing principle, the thread you can pull to unravel every other decision.

Pull it, and let us begin with the place all the energy is kept: a single, humble cell.

---

**Sources**

- EVspecs / InsideEVs — Tesla Model 3 drag coefficient (0.23; facelift 0.219, cited as "lowest absolute drag of any Tesla").
- WLTP consumption data (EVspecs, wltpinfo.com) — Model 3 ~128–167 Wh/km depending on variant; RWD ~130 Wh/km.
- Mobility.ch, eufactcheck.eu, and battery-to-wheel efficiency literature — EV battery-to-wheel efficiency commonly cited at ~80–90%; gasoline engine ~20%.
- The cube-law relationship between speed and aerodynamic power is developed with sources in Chapter 12.
