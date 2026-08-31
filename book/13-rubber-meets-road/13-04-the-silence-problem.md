## 13.4 The silence problem

There is a complaint about electric cars that sounds, at first hearing, like a joke at the complainer's expense: they are too noisy. Not the cars themselves — they are famously, eerily quiet — but the *inside* of them, which a surprising number of drivers coming from petrol cars report as louder than what they left behind. They are not imagining it, and they are not wrong. They are experiencing one of the most elegant unintended consequences in the whole book: the electric car did not make more noise. It removed the noise that was hiding all the other noise.

An internal-combustion engine is, among its many other functions, a magnificent masking device. It sits a metre in front of you producing a broad, continuous roar, and that roar conveniently occupies the same acoustic territory as the sound of tyres on tarmac and air tearing past the mirrors. For a century, car engineers got the suppression of road and wind noise partly for free, because the engine drowned it out. Psychoacousticians call this masking, and it is the same reason you cannot hear a dripping tap while the shower is running. Delete the engine — the whole triumphant subtraction of Chapter 1 — and you turn the shower off. The tap was always dripping. Now it is all you can hear.

The effect is worse than merely revealing what was there, because two of the electric car's defining traits actively make road noise louder. The car is heavy, as Chapter 13 has been insisting throughout, and a heavier car presses its tyres into the road harder, exciting more vibration from every joint and stone chip. And it is stiff: the structural pack of Chapter 3, that magnificently rigid slab bolted into the floor, is an outstanding conductor of vibration, transmitting road roar into the cabin through a large flat surface that sits directly beneath the occupants. The very decisions that made the car efficient, safe and rigid all conspire to make it hum. So the engineers, having deleted one noise problem, inherit a subtler one — and this is why an electric car's cabin is quietly full of acoustic engineering that a petrol car never needed.

The counter-measures work at every stage of the sound's journey. At the source, the tyre itself is quietened from within: the sound-absorbing foam bonded inside the carcass, which section 13.2 met as a curiosity, is really the first line of defence, damping the drumming of the air cavity inside the tyre before it ever reaches the body. At the path, the suspension bushings that connect wheel to body are tuned as much for what they *block* as for how they handle — the Model 3's 2024 revision, for instance, adopted softer rubber in both the suspension and the subframe-to-body mounts, trading a sliver of directness for isolation. At the boundary, the body is sealed with an obsessiveness that would seem excessive on a noisier car: revised weatherstrips at the beltline and around the mirrors, and door edges reshaped specifically so that air cannot get into the gaps between door, fender and quarter panel and howl there.

And then the glass, which is where the story becomes properly clever. Ordinary side windows are a single sheet of toughened glass — cheap, strong, and acoustically hopeless, because a stiff panel is an efficient loudspeaker. *Acoustic laminated* glass is instead a sandwich: two thinner sheets bonded around a soft plastic interlayer. The interlayer is the point. Sound arriving at the outer pane tries to flex it, the flexing shears the soft middle layer, and the shearing turns the sound into a tiny amount of heat. The window eats the noise. Tesla progressively extended this from the windscreen alone, to the front side windows, and finally — on the revised Model 3 — to every piece of glass in the car, which is the single change the company credits most for that car's markedly quieter cabin. Independent testing found it cruising at around **67 decibels** at motorway speed, some **three decibels** below the previous car. Three decibels sounds trivial and is not: the decibel scale is logarithmic, and three of them is *half* the sound energy.

Where the quiet comes from:

```
   SOURCE            PATH              BOUNDARY         CABIN
   ------            ----              --------         -----
   tyre cavity  -->  bushings     -->  acoustic    -->  active
   drumming          + subframe        laminated        noise
      |              mounts            glass            cancel.
      v                 |                 |                |
   foam inside       softer rubber     2 panes +        mics hear
   the tyre          absorbs the       soft inter-      the boom,
   (13.2)            vibration         layer that       speakers
                                       shears sound     play its
                                       into heat        opposite

   the engine used to MASK all of this for free
```

The last stage is the one that would have been science fiction in a car with an engine. Because the cabin is now quiet enough for it to work, some Teslas run *active noise cancellation* on road noise: microphones listen for the low-frequency boom coming up through the structure, and the audio system plays a precisely inverted waveform through the speakers so the two cancel. This is the same trick as a pair of noise-cancelling headphones, applied to a room, and it is only feasible because it needs serious real-time computation and a network fast enough to carry the microphone signals — which is exactly why the Etherloop of section 10.3 lists cabin-microphone traffic for noise cancellation among the reasons the car outgrew the CAN bus. The car's data backbone exists, in small part, to make the car quieter.

It is a satisfying place to end a chapter about tyres, because it shows the whole book's pattern turning back on itself. The engine was deleted for efficiency; its deletion unmasked road noise; the fix for road noise runs through the tyre, the suspension, the glass, and finally through the car's computers and its gigabit network. Nothing in a machine this integrated stays in its own chapter. Which is the right thought to carry upward, out of the contact patch and into the chassis that holds it all together.

---

**Sources**

- Teslarati and Electrek — Tesla's noise-reduction strategy; double-pane (acoustic laminated) glass extended to all windows on the 2024 Model 3, credited by Tesla as the principal source of the quieter cabin; earlier Tesla work on door and window seals and on tyre insulation with tyre manufacturers; active road-noise cancellation introduced on Model S/X.
- Go-Parts (Model 3 quarter glass, "Highland" acoustic versions) and Tesla Motors Club — acoustic laminated glass as two panes bonded around a damping interlayer; previously only the windscreen and front side glass were laminated.
- Car and Driver via Notebookcheck — 2024 Model 3 measured ~67 dB at a 70 mph cruise, ~3 dB below the previously tested 2019 Model 3. The observation that 3 dB represents half the sound energy is the definition of the logarithmic decibel scale.
- Revised weatherstrips at the beltline and mirror area, reshaped door edges to prevent air entering the door/fender/quarter gaps, and softer suspension and subframe-to-body bushings are reported changes to the 2024 Model 3. [INFERENCE — enthusiast and press teardown reporting rather than a published Tesla engineering specification.]
- Acoustic masking by engine noise, and the greater road-noise excitation caused by vehicle mass and a stiff structural floor, are standard NVH engineering; the structural pack is described in 3.3 and the tyre's internal foam in 13.2.
- Active noise cancellation depending on cabin microphone traffic over the car's high-bandwidth network cross-references 10.3.
