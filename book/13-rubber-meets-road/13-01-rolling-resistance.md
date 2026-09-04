## 13.1 Rolling resistance and why EVs care more

A tire looks, from a distance, like a rigid hoop rolling smoothly along. It is not. Where it meets the road it is squashed flat into that hand-sized contact patch, and as the wheel turns, each part of the tire is squashed flat and then springs back, over and over, hundreds of times a minute. Rubber, being rubber, does not spring back perfectly — some of the energy of squashing it is lost as heat each time, in a phenomenon engineers call hysteresis. Multiply that small loss by four tires, each flexing continuously for every meter traveled, and you have a steady, unavoidable drag on the car that persists whenever the wheels are turning. This is *rolling resistance*, and it is the price of using soft rubber tires at all.

Most drivers have never heard of it, because in a gasoline car it was buried in the noise. But it has a crucial property that makes it the mirror image of the air resistance from the last chapter: rolling resistance stays roughly *constant* with speed, rising only gently, whereas aerodynamic drag climbs steeply with the square of speed. This means the two forces trade dominance depending on how fast you are going. At high highway speeds the air wins overwhelmingly, as we saw. But at the lower speeds of town and city driving — where the air is barely a factor — rolling resistance becomes the single largest force the car is fighting. Stop-start urban driving, the daily reality for most cars, is a regime ruled not by the wind but by the flexing of the tires.

Two forces, two regimes:

```
   Which force is the car actually fighting?

   force
        |                                              ##
        |                                            ##
        |                                          ##
        |                                       ###
        |                                     ##
        |                                  ###
        |                               ###
        |                           ####
        |================================================
        |                  #####
        |           #######
        |###########
        +------------------------------------------------
         0      40     80     120    160 km/h

   #  aerodynamic drag -- tiny in town, EXPLODES on the highway
   =  rolling resistance -- roughly constant at any speed

   They cross at around 80 km/h. Below it the tires are the
   main enemy; above it, the air. An electric car has to win
   both battles to have good range everywhere.
```

Now, why does an electric car care about this more than a gasoline car did? Three reasons, and they are the same three that run through the whole chapter. The first is the one from Chapter 1: an electric drivetrain is so efficient that there are very few *other* losses left, so the losses that remain — chiefly rolling resistance and air — loom proportionally much larger. In a gasoline car, where the engine was throwing away three-quarters of the fuel anyway, the drag of the tires was a rounding error lost among far bigger wastages. In an electric car, where almost nothing else is wasted, the tires' flexing becomes one of the biggest remaining leaks, and plugging it matters.

The second reason is weight. Rolling resistance rises with the load a tire must carry, and an electric car is heavy — several hundred kilograms of battery heavier than an equivalent gasoline car. More weight pressing down means more flexing, means more rolling resistance, means more energy lost every meter. The battery that gives the car its range also, through sheer mass, taxes that range through the tires.

The third reason is simply that range is scarce and anxiously watched, so every source of loss is worth attacking. And so the tire industry developed *low-rolling-resistance* tires — tires with special rubber compounds and constructions that flex with less hysteresis, losing less energy to heat as they roll. Fitting them can meaningfully extend an electric car's range, particularly in the city where rolling resistance dominates, and most electric cars come on such tires as standard.

But — and this book always looks for the but — low rolling resistance is not free, because it fights against two other things a tire must do. A tire that flexes less and loses less energy also tends to *grip* less, especially in the wet, and tends to be made of harder rubber that wears differently. Grip, efficiency, and durability pull against one another: make a tire slippery-rolling for range and you risk compromising its hold on the road; make it grippy and hard-wearing and you pay in rolling resistance. Every EV tire is a negotiated settlement between these demands, and the settlement is harder to reach than it was for gasoline cars precisely because the electric car pushes so hard on all three fronts at once — wanting maximum range, maximum grip for its instant torque, and maximum life despite its weight.

That collision of demands is exactly what the next section is about, because it turns out that the same qualities that make an electric car care so much about its tires also make it destroy them faster than anyone expected.

---

**Sources**

- Continental, Michelin, Apollo, Tire Pte Ltd — rolling resistance from tire hysteresis; low-rolling-resistance tires extend EV range; rolling resistance more significant in efficient EV drivetrains and rises with load/weight.
- BB Wheels / eleport — rolling resistance roughly constant with speed vs aerodynamic drag rising steeply; the low-rolling-resistance vs grip vs wear trade-off.
- The two-regime (city vs highway) framing cross-references the cube law of Chapter 12; EV weight from the battery mass of Chapter 3.
