## 4.1 The DC-to-AC problem

The battery has a problem it does not know about. It is brimming with electricity of exactly the wrong kind.

Electricity comes in two temperaments. The kind in a battery is *direct current*, DC: it flows steadily in one direction, from minus to plus, like a river with a single current. It is calm and constant, which is perfect for storage. But the motor that is going to move the car — for reasons the next chapter will make vivid — cannot use calm and constant electricity at all. It runs on *alternating current*, AC: electricity that reverses direction over and over, surging one way and then the other, many times a second. Worse, it does not want one stream of alternating current but three, each rising and falling a third of a cycle apart, so that together they can conjure a magnetic field that appears to *rotate*. The whole trick of the motor, as we will see, is that rotating field, and the whole trick of making it is three neatly staggered AC waveforms.

So somewhere between the placid DC battery and the AC-hungry motor, something has to perform a conversion that sounds almost like alchemy: turn steady one-directional current into three smoothly surging, precisely staggered waves. That something is the inverter, and the delightful thing is that it does this with no cleverness of the analogue kind at all. It does not gently shape the current. It has, in fact, only the crudest possible tool — a set of switches that can do nothing but slam fully on or fully off — and it makes a smooth wave out of them by brute speed and impeccable timing.

Here is the idea, and it is genuinely counterintuitive. Imagine you want to fill a bath to exactly half-full-worth of *flow*, but your tap has no in-between setting: it is either fully open or fully shut. What do you do? You flick it on and off, fast, and you control the *average* by how much of the time it spends open. Open half the time, and on average you get half the flow. Open a lot of the time, and you get most of the flow; barely at all, and you get a trickle. If you flick fast enough, the person in the bath never notices the individual bursts — they feel only the smooth average. This is *pulse-width modulation*, universally shortened to PWM, and it is one of the most useful ideas in all of electronics.

The inverter does exactly this with the battery's DC. Its switches chop the steady voltage into a rapid train of pulses, and by making the pulses wider when the wave should be high and narrower when it should be low, it sculpts the *average* into any shape it likes — including the gentle rise and fall of a sine wave. The motor never sees the smooth wave drawn on the engineer's whiteboard; it sees a blur of full-voltage pulses of varying width. But the motor's own coils, being electrically sluggish, smooth those pulses out, averaging the blur into precisely the surging current the whiteboard promised. The crudeness is hidden by speed.

To make the three staggered phases the motor needs, the inverter simply runs three of these switch pairs at once — one per phase — and starts each one's wave a third of a cycle after the last. Six switches in all, arranged in three pairs, each pair feeding one of the motor's three connections. That is the whole hardware: six fast switches, some large capacitors to steady the supply, and a controller clever enough to choreograph the pulse widths in real time.

Everything else about the inverter — the speed of its switching, the material its switches are made from, the heat it must shed — is refinement of this single, slightly absurd, entirely successful idea: that the way to make a smooth wave, when all you have is an on/off switch, is to flick it faster than anyone can see and let physics do the smoothing. The next question is what happens when you change how fast, and how hard, you flick — because that, it turns out, is the same thing as changing the speed and the torque of the car.

---

**Sources**

- Union College capstone (three-phase PWM rectifier/inverter) and arXiv PWM inverter papers — PWM principle, chopping DC into variable-width pulses to synthesise a sine wave.
- EV Engineering & Infrastructure (evengineeringonline.com), "EV inverters: key to motor control" — three-phase inverter structure, DC-bus decoupling capacitors, IGBT/MOSFET switches.
- Three-phase (120°-offset) waveform generation is standard power-electronics practice; the rotating magnetic field it produces is developed in Chapter 5.
