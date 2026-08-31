## 18.1 The inference computer (HW3 → HW4/AI4)

The word to learn for this section is *inference*, because it names precisely what the car's brain does and distinguishes it from the thing people usually imagine. In the world of artificial intelligence, "inference" means *running* a neural network that has already been built and taught — feeding it a fresh input, here the current camera images, and getting its answer, here a decision about the road. It is the opposite of *training*, which is the slow, heavy business of building and teaching the network in the first place, and which the next section shows happens somewhere else entirely. The computer in the car is an *inference* computer. It does not learn while it drives; it applies, at high speed, what was learned beforehand.

That distinction shapes everything about the hardware, because inference in a moving car has a brutal set of constraints that training does not. It must be *fast* — the answer is useless if it arrives after the collision, so the whole cycle of taking in eight camera streams, running them through the networks, and producing a driving decision must complete many times a second, every second, without fail. It must be *small and cool enough* to live in a car, drawing modest power and shedding modest heat, unlike the room-sized machines that do the training. And it must be *reliable* to a degree ordinary computers never are, because a crash of this computer is not a lost document but a car that has stopped perceiving the road. Fast, compact, and utterly dependable — that is the demanding brief the inference computer must meet.

Tesla's answer has evolved through generations, each a response to wanting more of the one thing that always runs short: the ability to run bigger, cleverer networks on more camera data, faster. The earlier generation, Hardware 3, was a custom Tesla chip drawing a modest amount of power — on the order of eighty watts, about the same as a bright old-fashioned light bulb, which is remarkable for what it does. The current Hardware 4 (also called AI4) is substantially more capable, with far more memory and much greater bandwidth for shovelling camera data through the networks, at the cost of roughly double the power draw. Further generations, aimed at the still-heavier demands of the driving software, are on the way.

The inference computer's brief:

```
   INFERENCE = running an already-trained network.
   The car applies what was learned elsewhere. It does not
   learn anything here.

   The brain in the car must be:

     FAST ......... decide many times a second, before the
                    moment to decide has passed
     COMPACT ...... small and low-power, because it rides
                    in a car (HW3 ~80 W, HW4 ~160 W)
     REDUNDANT .... TWO chips, cross-checking each other, so
                    that if one is wrong or fails outright,
                    the other catches it

   A single chip deciding whether to brake for a child would
   be a single point of failure, in the most literal sense.
```

One design feature deserves special note because it embodies a principle from earlier in the book: redundancy. The Hardware 4 computer contains not one but *two* self-driving chips, and this doubling is deliberate. The two can work on the same problem and cross-check each other, so that if one produces a wrong answer or fails outright, the other is there — the same "make everything at least twice" logic we met in the steer-by-wire system of Chapter 14, applied now to the brain rather than the steering. A single chip deciding whether to brake for a child would be a single point of failure in the most literal and unacceptable sense; two chips checking each other is how you make a safety-critical decision trustworthy. The car's perception, like its steering, is built to survive the failure of any one part.

There is a tension here that connects back to Chapter 15's bittersweet note, and it is worth restating because owners feel it sharply. The capability of the driving software is bounded by the inference computer installed in the car, and that computer cannot be improved by an over-the-air update — it is physical silicon. So a car with an older-generation brain can be improved by software only up to what its chip can run; beyond that it needs a hardware upgrade, which is expensive, sometimes offered and sometimes not, and occasionally the source of real grievance from owners who bought on the promise that their specific car would one day drive itself. The software-defined car can update its code freely, but the inference computer is the hard floor beneath the software, and where that floor sits is fixed the day the car is built.

So the car carries a small, fast, redundant brain whose whole job is to run — not build — the neural networks, fast enough and reliably enough to drive. But those networks had to come from somewhere, and the effort of *building* them dwarfs anything happening in the car by a factor of thousands. To understand the whole system you have to leave the car entirely and visit the place where the intelligence is actually made — which reveals, cleanly, where the heavy thinking really lives.

---

**Sources**

- SemiAnalysis, Not a Tesla App, Tesla Oracle, Electrek — HW3 (~80 W) vs HW4/AI4 (two FSD chips, ~160 W, 16 GB GDDR6, ~224 GB/s, ~3.3× bandwidth over HW3); dual-chip redundancy for inference.
- Definition of inference vs training and the real-time/low-power constraints are standard AI-systems concepts; the hardware-ceiling/upgrade tension references Chapter 15 and widely reported owner experience.
- Redundancy parallel to steer-by-wire references Chapter 14; training infrastructure developed in 18.2.
