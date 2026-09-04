## 12.1 Power rises with the cube of speed

Most things in life scale in a comfortable, proportional way. Drive twice as far and you use roughly twice the fuel; buy twice as much and you pay twice the price. Our intuition is built for this kind of straightforward arithmetic, and it serves us well almost everywhere — except when it comes to pushing a car through air, where the numbers behave in a way so steep and so punishing that it genuinely surprises people who ought to know better.

Here are the two facts, and they are worth stating carefully because everything about high-speed range follows from them.

The first: the *force* of air resistance rises with the **square** of your speed. Double your speed, and the air pushes back not twice as hard but *four* times as hard. Triple it, and the force is *nine* times greater. The air resists gently at a crawl and viciously at speed, and the transition between the two is not gradual but accelerating.

The second fact is the one that really matters for range, and it is worse. The *power* your car must spend to overcome that force rises with the **cube** of speed. Double your speed and you need not four but *eight* times the power to keep going against the air. The reason is a neat piece of physics: power is force multiplied by speed, so if the force is already going up with the square of speed, and you then multiply by speed again, you get the cube. Force scales with speed squared; power scales with speed cubed. That extra multiplication is the difference between an inconvenience and a catastrophe for range.

The cube law, made concrete:

```
   Double the speed. What happens to the fight against air?

   speed          drag FORCE      power needed to overcome it
   ------------------------------------------------------------
    x1  base         x1                     x1
    x2  double       x4                     x8
    x3  triple       x9                    x27
   ------------------------------------------------------------

   that power, drawn to scale:

     x1   #
     x2   ########
     x3   ###########################

   Going faster costs power wildly out of proportion to the
   speed -- which is also why easing off buys back so much.
```

Abstract numbers do not persuade, so here is what the cube law does to a real electric vehicle. Take a van cruising at 80 km/h (50 mph) with a certain range. Speed up to roughly 95 km/h (60 mph) and the range noticeably shrinks. Push on to 110 (70 mph), and it shrinks again. By the time you are traveling at around 130 km/h (80 mph) instead of 80, the range can have collapsed by something approaching *forty percent* — the same battery, the same road, the same weather, carrying you barely more than half as far, purely because you chose to hurry. That is not a gentle penalty for speed; it is a cliff, and every electric-car driver who has watched their predicted range evaporate on a fast highway has felt it directly.

There is a threshold hidden in all this that explains why aerodynamics dominates the chapter. At low, around-town speeds, air resistance is minor — the car spends most of its energy on other things, chiefly the rolling resistance of the tires, which is the next chapter's subject. But because air resistance grows so explosively with speed while those other losses grow only gently, there comes a point — somewhere in the range of ordinary main-road speeds — where the air overtakes everything else and becomes the single largest force the car is fighting. Above that point, on a highway, well over half of all the energy the car uses can be going to push air aside. The faster you go, the more totally the air dominates, until at high speed almost nothing else matters.

This is the physics that justifies the entire war described in the chapter opener. If range at highway speed is mostly a battle against air, and if the cost of that battle rises with the *cube* of speed, then shaving even a small amount off a car's aerodynamic drag pays off enormously at exactly the speeds where range is scarcest and most anxiously watched. A car that is ten percent slipperier is not ten percent better only at the margins; it is meaningfully better on every long, fast journey, which is precisely where electric cars have most needed to prove themselves. The cube law is why a family sedan is sculpted with the obsessive care once reserved for aircraft, and why the drag coefficient figures from Chapter 1 — the 0.23, the 0.219 — are quoted with such pride.

It also hands the driver a piece of free advice that no software update can beat: if you want more range on a long trip, slow down a little. Because the penalty is cubic, easing off from 130 to 115 km/h (80 to 70 mph) buys back a surprisingly large slice of range for a very small cost in journey time. The same physics that punishes haste so severely rewards a gentle lift of the foot just as generously. The air is an unforgiving opponent, but it is an honest one — and it fights hardest exactly where, and when, the car can least afford it. The next question is *where*, physically, on the car this fight is happening, and the answer is not where most people would guess.

---

**Sources**

- The Truth About Cars, AirShaper, InsideEVs, evchargingstations.com — drag force scales with speed squared; power to overcome drag scales with speed cubed (double speed → 8× power); over half of highway energy goes to aerodynamic drag.
- Fleet News — real-world example of EV range dropping ~39% between 50 and 80 mph (≈80–130 km/h), converted to metric here.
- Rolling resistance dominating at low speed and drag overtaking it at higher speed is standard vehicle dynamics; rolling resistance is the subject of Chapter 13. Drag-coefficient figures cross-reference Chapter 1.
