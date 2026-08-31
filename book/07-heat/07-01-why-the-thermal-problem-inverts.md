## 7.1 Why an EV's thermal problem inverts the combustion one

The engineer who used to design cooling systems for petrol engines had, in a sense, an easy brief. Make the heat go away. The engine was a furnace — recall from Chapter 1 that around seventy percent of the fuel's energy left as waste heat — and the job was disposal: a big radiator at the front, a pump pushing coolant through the block, a fan for when the car sat in traffic, and a fixed one-way flow of heat from a place that had far too much of it to the open air that would take as much as you gave. Warming the cabin was almost an afterthought, a matter of diverting a trickle of the engine's endless excess. Nobody worried about running out of heat. There was always more heat than anyone wanted.

The electric car tears this brief up and writes the opposite one. And the reason is the very efficiency the whole car is built around. A drivetrain that turns eighty-five or ninety percent of its energy into motion is, by definition, one that wastes only ten or fifteen percent as heat — a tenth of what an engine threw off. That is wonderful for range and catastrophic for anyone hoping to warm the cabin for free. The furnace is gone. The car that sips energy so carefully has, as a direct consequence, almost no spare warmth to give.

So the first inversion is scarcity: heat changes from something you frantically dispose of to something you carefully hoard. But there is a second inversion that makes the problem genuinely harder than the one it replaced, and it concerns the battery. An engine did not much care how warm it was, within wide limits, once it was running. A lithium battery cares enormously, and in *both* directions. When it is too cold — a frosty morning — it cannot deliver its full power, cannot be fast-charged without risking the damage described in Chapter 2, and offers reduced regenerative braking; it needs *warming*. When it is too hot — hard driving, or the fierce heat of DC fast charging — it ages rapidly and, at the extreme, risks the runaway the whole design works to prevent; it needs *cooling*. The very same component demands heating on some days and cooling on others, sometimes within the same journey, and it insists on being kept inside a fairly narrow band to do its best work.

Three tenants, three different demands:

```
   What each part wants, thermally:

   BATTERY ......... a narrow, mild band. WARMING when cold,
                     COOLING when hot or fast-charging. The
                     fussiest tenant -- and it changes its mind
                     within a single journey.

   MOTOR + POWER ... runs hot; almost always wants COOLING.
   ELECTRONICS       Its waste heat is a RESOURCE to be stolen.

   CABIN ........... whatever the humans want. WARMING through
                     a European winter, COOLING in summer.

   Three conflicting demands -- and only a tenth as much waste
   heat as an engine had, to satisfy all of them.
```

Put those together and the shape of the new problem appears. You have three consumers — battery, drivetrain, cabin — with conflicting and shifting needs, and only a meagre supply of waste heat to draw on. The old fixed, one-way flow is useless here. What you need instead is a system that can *reconfigure* itself: that can take the modest warmth coming off the motor and power electronics and, instead of dumping it out of a radiator, redirect it to warm a cold battery, or pipe it into the cabin. That can, on a hot day at a fast charger, do the reverse and pull heat *out* of the battery as fast as possible. That can connect and disconnect its various loops on demand, sending heat wherever the shortage is worst, moment by moment.

This is why the electric car's thermal system is not a scaled-down version of the petrol car's but a different kind of machine altogether — closer to a small, mobile district-heating network than to a radiator. It has to be a logistics operation, routing a scarce resource around a changing map of demand, and it has to do the routing while spending almost no energy, because every watt it burns keeping the battery or cabin comfortable is a watt stolen from range.

Two devices make this possible, and the rest of the chapter is largely about them. The first is a way to *manufacture* heat far more cheaply than a simple electric heater ever could, by moving it rather than making it — the heat pump. The second is a way to *route* heat and cooling around the car with a single, elegant component instead of a tangle of valves — the octovalve. Together they turn the daunting inverted problem of this section into one of the quiet triumphs of the modern EV. We take them in turn, starting with the device that seems, at first glance, to break the laws of arithmetic.

---

**Sources**

- E-Mobility Engineering, "Tesla Octovalve analysis" and TESLA.ROCKS — EVs have limited waste heat; thermal system must route heat between cabin, powertrain and ambient; battery's narrow temperature band.
- Chapter 1 efficiency figures (≈70% engine heat loss vs ~10–15% EV loss) and Chapter 2 (cold-battery charge limits, high-temperature ageing) underpin the inversion argument.
- Motronix / Tesla.rocks — battery needs both heating and cooling depending on conditions; reconfigurable coolant loops as the design response.
