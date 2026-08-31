## 14.6 Rear-wheel steering

We assume, without ever thinking about it, that a car steers with its front wheels and the back ones simply follow. For a small car this is fine. For a large one it is the source of a familiar frustration: the wide, lumbering turning circle that makes a long vehicle a misery to manoeuvre in a car park, forcing the three-point turns and careful shuffling that anyone who has driven a big estate or a van knows well. The problem is geometric and, until recently, unavoidable — but let the *rear* wheels steer too, even by a few degrees, and it largely disappears. That is rear-wheel steering, and the steer-by-wire technology of the last section is what makes it practical.

The trick has two modes, and they are cleverly opposite depending on how fast you are going. At low speed — parking, tight turns, U-turns — the rear wheels turn in the *opposite* direction to the front ones. Picture it: the front wheels swing left, and the rear wheels swing right. This effectively shortens the car, pivoting it around a much tighter point than its length would suggest, so that a large vehicle can swing round in an arc that ought to belong to something much smaller. The Cybertruck, a genuinely huge vehicle, can execute U-turns and park in spaces that would defeat a conventional truck, because at low speed its rear wheels are actively helping to rotate it, cutting the effective wheelbase and the turning circle dramatically.

At high speed the logic flips. Now the rear wheels turn in the *same* direction as the front ones, by a smaller amount. This does not tighten the turn — at speed you do not want tightness, you want stability. Steering all four wheels the same way lets the car change lanes and take motorway curves in a smoother, more planted way, the whole car shifting together rather than the tail following the nose a beat later. The same system that makes the car nimble in a car park makes it steady on the motorway, simply by reversing which way the rear wheels point.

Opposite at low speed, together at high speed:

```
   LOW SPEED -- parking, U-turns

     front wheels   turn LEFT
     rear wheels    turn RIGHT -- the opposite way

     the car pivots about its middle and takes a much
     tighter circle, as though it were a shorter car

   HIGH SPEED -- lane changes, motorway curves

     front wheels   turn LEFT
     rear wheels    turn LEFT too, but only slightly

     the whole car slides across as one: stable and planted,
     with none of the tail-swing of a sharp turn-in

   Same hardware, opposite behaviour -- chosen by software,
   according to how fast you are going.
```

On the Cybertruck the rear wheels move only a few degrees — around three, with the potential for more via a software update, since the angle is set in software rather than fixed in metal — but even that small movement transforms how a large vehicle behaves, because turning circle is exquisitely sensitive to rear-wheel angle. A handful of degrees at the back is worth an enormous improvement in manoeuvrability at the front.

Rear-wheel steering is not new in itself — a few cars have offered mechanical versions over the decades — but doing it this way, as part of an all-electronic, by-wire steering system, is what makes it clean and flexible. Because the rear wheels are turned by their own actuators taking electrical commands, the car can decide exactly how much rear steer to apply, in which direction, at any speed, purely in software. There is no mechanical linkage to the front wheels dictating the relationship; the computer chooses it, moment by moment, blending low-speed agility into high-speed stability as the car accelerates. It is the same theme one final time: a behaviour that mechanical engineering could only approximate crudely becomes fluid and precise once it is placed under software control.

And so this chapter, and Part VII, close on the frontier of the book's central idea. We began the part with the tyre — rubber pressed on tarmac, about as physical and mechanical as a car gets — and we end it with a car whose wheels, front and rear, are pointed not by shafts and hands but by motors answering to code, with the sacred mechanical links deleted and rebuilt as redundant electronics. The chassis, the most stubbornly mechanical region of any car, has been drawn into the same transformation as everything else: springs that adjust themselves, brakes that barely engage, steering with no column, wheels at both ends turned by wire.

It is the natural bridge to the rest of the book. If the car's very steering is now a computer's decision, then the computers themselves — how many there are, how they are divided, how they think — become the most important components of all. We have spent fourteen chapters on the machine. It is time to meet the mind.

---

**Sources**

- InsideEVs, Not a Tesla App, e-vehicleinfo, Notebookcheck — Cybertruck rear-wheel steering: opposite-phase at low speed (shorter effective wheelbase, tighter turning circle), same-phase at high speed (stability); ~3° now, up to ~10° via software.
- Rear-wheel steer angle set in software via by-wire actuators (dependent on the steer-by-wire system of 14.5); mechanical rear-steer predecessors are general automotive history.
- Turning-circle sensitivity to rear-wheel angle is standard vehicle geometry; stated as Cybertruck-first direction-of-travel per this book's convention.
