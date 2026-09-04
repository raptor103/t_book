## 17.1 The camera suite, and dropping radar and ultrasonics

Walk around a Tesla and try to spot the cameras, and you will mostly fail, because they are small and tucked discreetly into the bodywork. There are eight of them looking outward, plus a ninth inside the cabin that watches the driver rather than the road — and the exact arrangement varies by model and by generation of hardware. On the reference car it runs roughly like this. Two look forward from behind the windshield: a main camera covering the broad middle-distance view, and beside it a wide fisheye that takes in traffic lights overhead and anything cutting in close. The earlier cars had a third here, a narrow long-range lens for reading the road far ahead; it was dropped once the sensors jumped from about one megapixel to five, and the main camera had pixels enough to do that work itself. One looks forward from low in the front bumper, a recent addition — the Cybertruck had it first, then the refreshed Model Y, and by 2026 the whole range — and it sees what the windshield cameras cannot: the curb, the bollard, the ground immediately ahead. Two look sideways and slightly forward from the tops of the B-pillars, watching for cross-traffic at junctions and for cars sliding into the lane. Two more sit in the front fenders, behind the turn-signal repeaters, looking backward along the flanks for lane changes and overtaking traffic. And one looks straight back from above the rear plate. Between them they cover every direction at once, continuously — not perfectly, since there are still blind spots low and close to the body, and the ultrasonic sensors that once filled them were deleted in 2022 — and it is this flood of camera streams that the AI brain of Chapter 15 spends its life interpreting.

What is striking about this suite is not what it contains but what it *no longer* contains, because Tesla arrived at cameras-only by a deliberate campaign of removal. Most cars aiming at any kind of self-driving carry a mix of sensor types, on the sensible-sounding logic that different senses cover each other's weaknesses. Tesla started that way too, then began stripping the other senses out. In 2021 it removed the forward *radar* from the Model 3 and Model Y, and later from the Model S and X. In 2022 it went further and removed the *ultrasonic sensors* — the little proximity sensors around the bumpers that every modern car uses for parking — from its mainstream cars. What remained was vision alone: cameras and the neural networks that interpret them, a system Tesla calls Tesla Vision.

One honest complication belongs here, because the campaign of removal was not quite the one-way street the story usually implies. From 2023 Tesla quietly fitted a *new* high-definition radar — a 76-to-77-gigahertz unit known internally as Phoenix — to the Model S and Model X built on the newer computer hardware, and to the Cybertruck. It is not the old radar returning; it is a far more capable sensor, and Tesla has been notably quiet about how much, if at all, the driving software actually leans on it. The mainstream Model 3 and Model Y — the reference cars of this book — remain camera-only. But "Tesla is vision-only" is a claim about most Teslas rather than all of them, and a company that removed radar as a matter of principle putting a better one back on its most expensive cars is exactly the kind of detail this book would rather report than tidy away.

The subtraction, step by step:

```
   What Tesla progressively REMOVED on the way to
   cameras-only:

   around 2021   forward-looking RADAR
                 dropped from Model 3/Y, then S/X
   around 2022   ULTRASONIC parking sensors
                 dropped from the mainstream cars

   what remains:  CAMERAS + neural networks
                  -- branded "Tesla Vision"

   and one wrinkle:
   from 2023     a NEW high-definition radar quietly
                 appears on HW4 Model S/X and Cybertruck.
                 Not on the Model 3 or Model Y.

   The book's recurring instinct -- do more with less --
   applied, boldly, to the car's senses themselves.
```

Why remove senses from a safety system? Tesla's reasons are a mix of the practical and the philosophical, and they are worth setting out plainly because they are the foundation of the whole bet. The practical ones are cost and simplicity: the sensors are not free, and removing them saves money across millions of vehicles and simplifies the wiring and the software. The philosophical ones are more interesting and more contested. Tesla's argument, articulated by its engineers, is that combining fundamentally different senses is not the free lunch it appears to be. When a camera says one thing and a radar says another — and they sometimes disagree, because they sense the world in different ways — the car must decide which to believe, and that arbitration is itself a source of error and confusion. Tesla claimed that as its camera-based system improved, the radar started *subtracting* from its performance rather than adding to it, injecting conflicting signals that the vision system was better off without. Better, they argued, to have one excellent sense than several that quarrel.

Underneath all of it sits the logic of the last chapter. Tesla's deepest bet is that the path to self-driving runs through *data and neural networks*, not through more sensors — that a fleet of millions of camera cars, feeding the data flywheel, will produce better driving than a smaller fleet bristling with expensive lidar. Cameras are cheap enough to put on every car, which keeps the flywheel spinning; lidar, historically, was not. So the sensor decision and the data strategy are one and the same: cameras everywhere, on every car, gathering everything, and the intelligence made to live in the software rather than the hardware.

The honest immediate cost of this deletion was real and worth recording. When Tesla removed the ultrasonic sensors before its vision-based replacement was fully ready, cars shipped that *temporarily lost* familiar features — parking distance displays, automatic parking, the Summon function that creeps the car toward you — while the software caught up to do those jobs with cameras alone. Owners paid, in lost function, for the company's conviction that vision would eventually do everything the sensors had done and more. Some features returned; the episode showed both the boldness of the strategy and its willingness to make customers live on the promise.

So the reference car of this book sees the world through its cameras and nothing else — no radar humming through fog, no laser scanner building a precise three-dimensional map, no ultrasonic chirps judging the distance to a wall. Just cameras, and a brain trained to understand them. Whether that is enough — enough for the parking assistance owners noticed losing, and enough for the far grander goal of a car that drives itself anywhere — is the single most argued-over question in the field, and the next section lays out both sides of it as fairly as the state of knowledge in 2026 allows.

---

**Sources**

- Electrek, Repairer Driven News, Green Car Reports, AutoPilot Review — Tesla Vision eight-camera suite; radar removed from 3/Y in 2021 and S/X in 2022; ultrasonic sensors removed from mainstream cars in 2022 (~$114/vehicle cited).
- Not a Tesla App ("Tesla Guide: Number of Cameras"), Drive Tesla, Tesla Oracle, Notebookcheck — the current HW4 suite: two forward windshield cameras rather than the earlier three, plus a front bumper camera introduced on the Cybertruck and the 2025 Model Y, for eight in total.
- InsideEVs, Teslarati, autoevolution, Go-Parts — teardown confirmation of the 76–77 GHz "Phoenix" high-definition radar fitted to HW4 Model S/X from 2023 and to the Cybertruck, and absent from the HW4 Model 3/Y. Whether and how far the driving software uses it is not published. [INFERENCE]
- Electrek / Not a Tesla App — Tesla/Musk and Andrej Karpathy rationale: cost, sensor-fusion complexity, radar reducing signal-to-noise, priority on fleet data over added sensors.
- CarExpert / Tesla support — temporary loss of Park Assist, Autopark, and Summon after ultrasonic removal. Vision-vs-sensor debate developed in 17.2.
