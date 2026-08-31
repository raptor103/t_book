## 6.2 Regenerative braking

Every time an ordinary car slows down, it commits a small act of waste so routine that no one thinks about it. The car has energy of motion — the whole tonne-and-a-half of it, moving — and to slow down it must get rid of that energy. A friction brake does this by clamping pads onto a spinning disc and turning the energy of motion into heat, which then simply blows away into the air. All that effort the engine made to get the car moving, all that fuel, is scrubbed off as warmth on a brake disc and lost forever. A petrol car throws away its speed, quite literally, as hot air.

An electric car does not have to. And the reason is the single most satisfying fact about electric motors: a motor and a generator are the same machine. Feed electricity into a motor and it produces rotation. Force a motor to rotate and it produces electricity. It runs both ways with equal ease. So when an electric car wants to slow down, it does not have to reach for the friction brakes at all. It simply tells the inverter to run the motor as a generator — to let the wheels, still turning with the car's momentum, spin the motor and be resisted in doing so. The motor fights the rotation, which slows the car, and the energy of that slowing, instead of becoming waste heat, becomes electricity that flows back into the battery. This is *regenerative braking*, and it is the closest thing a car has to getting something for nothing.

The elegance is total. The very same device that spent battery energy to speed the car up now refills the battery as the car slows down. The motor pushes, then catches. Over a journey full of the ordinary slowings of real driving — for corners, for junctions, for traffic — this clawing-back adds up, and a car that uses its regeneration well can extend its range by something on the order of **ten per cent**. That is ten per cent of range recovered not by a bigger battery or a slipperier body, but simply by refusing to throw away energy the car already had.

Waste versus recovery, side by side:

```
   FRICTION BRAKE (petrol car)      REGEN (electric car)
   motion --> pads clamp disc        motion --> motor spun backwards
          --> HEAT --> gone                 --> ELECTRICITY
                                            --> back into battery
   the car's speed is thrown away    the car's speed is banked
```

But this book prefers the honest version, and regeneration has real limits that shape how the car behaves. The first is the battery's willingness to accept charge. If the pack is completely full — say you have just charged to 100 per cent and set off downhill — there is nowhere for the recovered energy to go, and regeneration has to be dialled back or switched off, handing the job to the friction brakes after all. The same is true when the battery is very cold, because, as Chapter 2 explained, a cold battery cannot accept a fast charge without risking damage; on a freezing morning a Tesla will often show reduced regeneration until the pack has warmed, and the car warns you that braking will feel different. This is not a fault. It is the BMS from Chapter 3 protecting the cells, and it is one of the reasons the car works so hard to keep the battery in its comfortable temperature range — a theme Part IV takes up in full.

The second limit is power. A motor asked to generate has a ceiling on how much it can push back, and that ceiling is generally lower than its ceiling for driving — so gentle and moderate slowing can be handled entirely by regeneration, but a genuine emergency stop demands far more braking force than the motor can provide. For that you still need the old friction brakes, clamping hard. Regeneration handles the everyday; friction handles the extremes and the emergencies.

Which raises an obvious question. If some slowing is done by the motor and some by the friction brakes, and the changeover depends on the battery's temperature, its state of charge, and how hard you are braking — who manages the handover? If the driver had to think about it, the car would be undriveable. The answer is that they never do: a layer of software silently blends the two kinds of braking together, moment by moment, so that the pedal feels the same whether the car is regenerating, rubbing, or both. That blending, and the peculiar pleasure of a car you can drive with one pedal, is the next section.

---

**Sources**

- Not a Tesla App and Shop4Tesla — regenerative braking principle (motor as generator, energy returned to battery); range benefit "as much as ~10%."
- EVKX.net, "Regenerative braking calculations" — power and energy limits of regen; recovery dependent on conditions.
- Tesla owner documentation and CleanTechnica/ArenaEV — reduced regeneration when the battery is full or cold; friction brakes required for hard/emergency stops. Regen power-ceiling point is standard EV behaviour.
