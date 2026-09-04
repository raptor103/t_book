## 7.4 Preconditioning and the pack as thermal store

Here is a problem the last three sections have been circling. A cold battery charges slowly — Chapter 2 explained why: shove ions into cold, sluggish electrodes too fast and you risk plating lithium and damaging the cell, so the BMS wisely throttles the charging rate until the pack warms up. On a winter road trip this is maddening. You arrive at a fast charger with a battery chilled to near-freezing, and instead of the rapid charge you were promised, you get a trickle, while the pack slowly warms itself using some of the very energy you are trying to add. The fastest charger in the world is useless to a cold battery.

The solution is to warm the battery *before* you arrive, so it is already at its ideal temperature the moment you plug in — and this is called preconditioning. It is one of those features that sounds trivial and turns out to be the difference between a good and a wretched winter journey. In a Tesla it mostly happens invisibly: set a Supercharger as your destination in the navigation, and the car quietly begins warming the pack perhaps half an hour out, spending a little energy to heat the battery on the move so that it arrives primed. The reward is a charging session that starts at full speed instead of crawling while the pack thaws — often saving many minutes, sometimes cutting a session by ten minutes or more. You spent a little range warming the battery, but you bought back far more time at the charger, and the trade is almost always worth it.

The same idea works the other way, before you drive rather than before you charge. Using scheduled departure, you tell the car when you intend to leave, and it arranges to have both the cabin and the battery at the right temperature by that moment — de-iced, warmed, ready. And this is where a genuinely elegant point emerges, one that reframes the whole battery: you can do this warming *while the car is still plugged into the wall*. That means the energy to heat the cold pack comes from the grid, not from the battery's own range. You leave with a warm, efficient battery and a warm cabin, and you have spent none of your driving range to get them. The car has, in effect, done its shivering on someone else's electricity.

Preconditioning, both directions:

```
   BEFORE CHARGING                BEFORE DRIVING (plugged in)

   you navigate to a charger      you set a departure time
        |                              |
        v                              v
   the car warms the pack         the car warms the pack AND
   on the way there               the cabin from the WALL
        |                              |
        v                              v
   arrive warm, and charge at     leave warm: full range, full
   full speed from the first      regen, comfortable -- and none
   minute                         of it paid for out of range

   Warming from the wall is nearly free.
   Warming a frozen pack on the move costs real range.
```

Underneath both tricks lies a change in how to think about the battery, and it is the real insight of this section. We have treated the pack as a fuel tank — a store of *energy*. But a half-ton slab of cells is also an enormous store of *heat*, a thermal flywheel. It takes a lot of energy to change the temperature of five hundred kilograms of battery, which cuts both ways: it is slow and costly to warm from stone cold, but once warm it stays warm for a long time, coasting on its own thermal mass long after the heating stops. The car exploits this. It can warm the pack while plugged in and then live off that stored warmth for the first part of a drive. It can, on the octovalve's command, use the pack as a buffer — dumping the motor's waste heat into the battery's mass to save it for later, or leaning on the pack's coolness to absorb a burst of heat. The battery is not just where the energy lives; it is a great thermal reservoir the car can charge and draw down like any other store.

That reframing is why the thermal system and the battery are really one system, not two. The BMS that protects the cells, the heat pump that makes cheap warmth, the octovalve that routes it, and the driver's own schedule all cooperate to keep the pack's temperature — and therefore its charging speed, its power, its regeneration, and its aging — inside the narrow happy band it prefers. Preconditioning is the visible tip of that cooperation: the car thinking ahead, spending a little heat now, from the cheapest available source, so that it is ready for what you are about to ask of it.

There is a limit worth stating plainly. Preconditioning is not free when it must run from the battery itself — warming a frozen pack on the move does spend real range, and in deep cold that cost is noticeable. It is nearly free only when the car can draw from the wall. The art, which the software increasingly handles for you, is knowing when the warming is worth it and where the energy should come from. Get that right and the fussiest tenant in the car — the temperature-sensitive battery — is kept comfortable almost for free. Which leaves only the tenants who complain the most and pay the least attention to efficiency: the humans in the cabin.

---

**Sources**

- Tesla Motors Club, Lectron EV, JOWUA, Notebookcheck — automatic battery preconditioning via navigation to a Supercharger (~30 min/30 mi out); scheduled departure preconditioning; time saved at the charger.
- Tesla owner documentation — preconditioning warms battery to optimal ion-transfer temperature for charging; cabin preconditioning to last climate setting.
- Preconditioning from grid power while plugged in, and the pack's large thermal mass acting as a store, follow from the battery physics of Chapter 2 and standard EV operation.
