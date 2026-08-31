## 17.1 The camera suite, and dropping radar and ultrasonics

Walk around a Tesla and try to spot the cameras, and you will mostly fail, because they are small and tucked discreetly into the bodywork. But there are eight of them, and together they give the car a full three-hundred-and-sixty-degree view of its surroundings. Three look forward from behind the windscreen, at different focal lengths — a wide one for the near scene, a main one for the middle distance, and a narrow one for spotting things far down the road. Two look forward-and-sideways from the front flanks, watching for cross-traffic at junctions. Two more look backward along the sides, for lane changes and overtaking cars. And one looks straight back from above the rear plate. Between them, they see everything around the car at once, continuously, and it is this flood of eight video streams that the AI brain of Chapter 15 spends its life interpreting.

What is striking about this suite is not what it contains but what it *no longer* contains, because Tesla arrived at cameras-only by a deliberate campaign of removal. Most cars aiming at any kind of self-driving carry a mix of sensor types, on the sensible-sounding logic that different senses cover each other's weaknesses. Tesla started that way too, then began stripping the other senses out. In 2021 it removed the forward *radar* from the Model 3 and Model Y, and later from the Model S and X. In 2022 it went further and removed the *ultrasonic sensors* — the little proximity sensors around the bumpers that every modern car uses for parking — from its mainstream cars. What remained was vision alone: eight cameras and the neural networks that interpret them, a system Tesla calls Tesla Vision.

The subtraction, step by step:

```
   what Tesla progressively REMOVED to reach cameras-only:

   ~2021  radar (forward-looking) ....... gone from 3/Y, then S/X
   ~2022  ultrasonic parking sensors .... gone from mainstream cars
   remaining:  8 CAMERAS + neural networks = "Tesla Vision"

   the recurring instinct -- do more with less -- applied to SENSES
```

Why remove senses from a safety system? Tesla's reasons are a mix of the practical and the philosophical, and they are worth setting out plainly because they are the foundation of the whole bet. The practical ones are cost and simplicity: the sensors are not free — the ultrasonic set alone was reported to cost around a hundred euros' worth per car — and removing them saves money across millions of vehicles and simplifies the wiring and the software. The philosophical ones are more interesting and more contested. Tesla's argument, articulated by its engineers, is that combining fundamentally different senses is not the free lunch it appears to be. When a camera says one thing and a radar says another — and they sometimes disagree, because they sense the world in different ways — the car must decide which to believe, and that arbitration is itself a source of error and confusion. Tesla claimed that as its camera-based system improved, the radar started *subtracting* from its performance rather than adding to it, injecting conflicting signals that the vision system was better off without. Better, they argued, to have one excellent sense than several that quarrel.

Underneath all of it sits the logic of the last chapter. Tesla's deepest bet is that the path to self-driving runs through *data and neural networks*, not through more sensors — that a fleet of millions of camera cars, feeding the data flywheel, will produce better driving than a smaller fleet bristling with expensive lidar. Cameras are cheap enough to put on every car, which keeps the flywheel spinning; lidar, historically, was not. So the sensor decision and the data strategy are one and the same: cameras everywhere, on every car, gathering everything, and the intelligence made to live in the software rather than the hardware.

The honest immediate cost of this deletion was real and worth recording. When Tesla removed the ultrasonic sensors before its vision-based replacement was fully ready, cars shipped that *temporarily lost* familiar features — parking distance displays, automatic parking, the Summon function that creeps the car toward you — while the software caught up to do those jobs with cameras alone. Owners paid, in lost function, for the company's conviction that vision would eventually do everything the sensors had done and more. Some features returned; the episode showed both the boldness of the strategy and its willingness to make customers live on the promise.

So the car sees the world through eight eyes and nothing else — no radar humming through fog, no laser scanner building a precise three-dimensional map, no ultrasonic chirps judging the distance to a wall. Just cameras, and a brain trained to understand them. Whether that is enough — enough for the parking assistance owners noticed losing, and enough for the far grander goal of a car that drives itself anywhere — is the single most argued-over question in the field, and the next section lays out both sides of it as fairly as the state of knowledge in 2026 allows.

---

**Sources**

- Electrek, Repairer Driven News, Green Car Reports, AutoPilot Review — Tesla Vision eight-camera suite (three forward, two forward-side, two rearward-side, one rear); radar removed from 3/Y in 2021 and S/X in 2022; ultrasonic sensors removed from mainstream cars in 2022 (~$114/vehicle cited).
- Electrek / Not a Tesla App — Tesla/Musk and Andrej Karpathy rationale: cost, sensor-fusion complexity, radar reducing signal-to-noise, priority on fleet data over added sensors.
- CarExpert / Tesla support — temporary loss of Park Assist, Autopark, and Summon after ultrasonic removal. Vision-vs-sensor debate developed in 17.2.
