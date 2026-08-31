## 6.4 Multi-motor torque vectoring

A car corners on a knife-edge that most drivers never think about. In a turn, the four tyres are each doing slightly different work, each with a slightly different grip on the road, and the balance between them decides whether the car turns obediently, pushes wide, or slides its tail. For a century, managing that balance was a matter of suspension geometry, tyre choice, and — when things went wrong — a driver's reflexes and, later, electronic stability systems that could only ever *subtract* grip by pinching a brake on one wheel. An electric car with more than one motor can do something categorically different: it can *add* precisely metered thrust to individual wheels, faster than any human and faster than any brake, to steer the car with power itself. This is torque vectoring, and it is where multiple motors stop being about straight-line speed and start being about poise.

The principle is simple to state. If you drive the wheels on one side of the car, or one end of it, a little harder than the other, you create a twisting force that tends to rotate the car about its vertical axis — engineers call this rotation *yaw*. Push the outside of a corner harder and you help swing the nose *into* the turn; push the inside or the front harder and you *straighten* the car out of a slide. Because an electric motor's torque can be dialled up or down in millionths of a second, a car with independent motors can apply exactly the right nudge, exactly when needed, to keep itself pointed where the driver intends — trimming understeer, catching oversteer, all invisibly, many times a second.

In a dual-motor Tesla, the two axles are independent — recall from earlier in the chapter that there is no mechanical shaft joining them, only software. So the car can shift torque front-to-rear at will: more torque to the rear to sharpen the car's turn-in, more to the front to calm it and pull it straight. Tesla's own description of its performance mode is almost tactile — extra torque to the rear axle helps rotate the nose into a corner, torque to the front arrests that rotation and pulls the car straight. The highest-performance cars go further still, with a pair of motors at the rear that can be driven *independently of each other*, so the car can command the left and right rear wheels separately — the fullest form of the trick, biasing torque across the axle to rotate the car through a bend with a precision no mechanical differential could match.

Nudging the car with torque:

```
   Top-down view, car turning left:

            front
         [FL]   [FR]
           |     |
           |     |
         [RL]   [RR]
            rear

   more torque to the REAR axle ..... rotates the nose INTO
                                      the turn, sharpening it
   more torque to the FRONT axle .... arrests that rotation and
                                      pulls the car STRAIGHT

   On the fastest cars the two rear wheels have a motor each,
   so torque can be biased across the axle, left against right
   -- the finest form of the trick, and one no mechanical
   differential could match.
```

It is worth being clear about why doing this with motors is so much better than the older ways. Traditional stability control works only by braking — it can slow a wheel to arrest a slide, but it cannot speed one up, so its only tool is to take grip away, which also scrubs off speed and momentum. Torque vectoring by motor can *give* as well as take: it can add drive to the wheel that needs it, correcting the car's line without necessarily slowing it. And it is faster, because there is no hydraulic brake to pressurise, no mechanical clutch to engage — only a change in the inverter's command, which happens at the speed of electronics. The car can begin correcting a slide before the driver's inner ear has even registered that one is starting.

The safety dividend is the part that matters for an ordinary driver who will never see a racetrack. Most of the time, torque vectoring is not making the car exciting; it is making it quietly, boringly stable — keeping it planted on a wet motorway curve, straightening a twitch on a bumpy bend, ensuring the enormous instant torque of an electric car reaches the road as clean forward progress rather than a spun wheel. The same fast, fine motor control that lets a performance car dance through corners lets an everyday car simply refuse to misbehave.

This is the final and most sophisticated form of "motion management," and it closes the loop the chapter opened. The motor began as a source of thrust. Through regeneration it became a brake. Through blending it became a brake you rarely have to press. And now, in multiples, it becomes a way to steer the car with power — the machine coordinating itself, thousands of times a second, into something more surefooted than the sum of its wheels. We have stored the energy, converted it, delivered it, and learned to manage it. It is time to confront the by-product of all this activity, the thing every one of these systems has quietly been fighting or hoarding: heat.

---

**Sources**

- Tesla, "Introducing Plaid Track Mode" and InsideEVs (Model 3 Performance Track Mode) — front/rear torque bias to control yaw; independent rear-wheel torque control on tri-motor Plaid.
- ScienceDirect (dual-motor torque-vectoring drive system, 2025) and Tesla Owners Online — torque vectoring definition (differential torque generating a yaw moment) and speed advantage over brake-based systems.
- Contrast with brake-only stability control is standard chassis-control engineering; the independent-axle basis was established in 6.1.
