## 4.2 Switching frequency as speed and torque

Once you understand that the inverter builds the motor's three waves out of fast on/off pulses, a rather thrilling consequence follows: whoever controls the pulses controls the car. Not loosely, not with the lag of a mechanical linkage, but completely, and in microseconds. The inverter is not merely a converter sitting quietly between battery and motor. It is the throttle, the gearbox, and the sense of instant response, all collapsed into one silent box. To see how, you have to see that the pulses carry two independent messages at once — one that sets the car's speed, and one that sets its force.

Start with speed. The motor turns because the three AC waves make a magnetic field that rotates, and the rotor chases that field around (Chapter 5 makes this concrete). So the speed of the motor is set by how fast the field rotates, and *that* is set by the frequency of the AC waves — how many times a second they complete a full cycle. Make the waves cycle faster and the field spins faster and the motor speeds up; slow the waves and the motor slows. The inverter can dial this output frequency anywhere it likes, smoothly, from a standstill to the motor's top speed, which is precisely why an electric car needs no gears. The "gearing" is done in software, by choosing how fast to cycle the waves, and it can be changed a thousand times a second without a clutch, a shift, or a pause.

Now force — torque, the twist that actually pushes the car. Torque comes not from how *fast* the field rotates but from how *strong* it is, which is to say from how much current is being driven through the motor's coils at each instant. And current, in the PWM scheme from the last section, is set by how much of the time the switches spend open — by the width of the pulses. Wide pulses, more current, more torque; narrow pulses, less. So the inverter has two knobs it can turn independently: the *frequency* of the waves for speed, and the *amplitude* — the pulse width — for torque. When you press the accelerator, you are commanding torque, and the inverter answers by fattening the pulses to pour more current into the motor, right now, this instant.

Two knobs on the same box of switches:

```
   Three different rates, doing three different jobs:

   1  OUTPUT FREQUENCY ..... how fast the three waves cycle
      (a few hundred Hz)      -> how fast the field spins
                              -> the car's SPEED

   2  PULSE WIDTH ........... how long each switch stays open
      (the duty cycle)        -> how much current in the coils
                              -> the car's TORQUE

   3  SWITCHING FREQUENCY ... how fast the switches chop
      (10,000-20,000 Hz)      -> smoothness against wasted heat
                              -> the designer's balancing act
```

This is the deep reason electric cars have that famous instant shove. In a petrol car, asking for more torque means air and fuel and spark and rising revs — a physical process with its own unavoidable delays. In an electric car, asking for more torque means telling the inverter to widen its pulses, and it can do that between one blink of its internal clock and the next. There is essentially no lag between your foot and the force at the wheels. The throttle response people rave about is really inverter response.

There is a third number lurking here, easy to confuse with the first, and worth separating cleanly: the *switching frequency* itself — how many times a second the switches flick on and off to build the waves. This is far faster than the waves it produces. The output waves might cycle a few hundred times a second at most; the switches underneath them chop away at something like **ten to twenty thousand** times a second, painting each smooth wave out of thousands of tiny pulses. Turn this rate up and the waves come out smoother and the motor runs quieter and more precisely — but every flick of a switch wastes a little energy as heat, so switching faster than you need is simply pouring efficiency away. Choosing the switching frequency is a balancing act between smoothness and loss, and it is one of the quiet arts of inverter design. It is also, incidentally, why an electric car sometimes emits a faint high-pitched whine that rises and falls: you are hearing the switching, or its effects in the motor, leaking into the range of human ears.

So three frequencies, doing three different jobs, all inside one box: the output frequency that sets speed, the current that sets torque, and the underlying switching frequency that trades smoothness against waste heat. Master all three and you have complete, instantaneous, gearless command of the car's motion from a device with no moving parts.

Which raises the obvious engineering question. If every flick of a switch costs a little heat, and you are flicking twenty thousand times a second through hundreds of amps at hundreds of volts, the switches themselves become the bottleneck — the hottest, most stressed, most loss-prone part of the whole chain. Make them even slightly better and the gains multiply across billions of flicks an hour. That is exactly the prize Tesla went after when it changed what its switches were made of, and it is the subject of the next section.

---

**Sources**

- evengineeringonline.com and Union College capstone — inverter output frequency sets motor speed; current (pulse width) sets torque; PWM carrier switching in the ~10–20 kHz range.
- General power-electronics principle — switching-frequency trade-off between waveform smoothness and switching losses; audible inverter/motor whine as a by-product.
- Instant torque response attributed to microsecond inverter current control (per Chapter 1 sources); rotating-field motor behaviour developed in Chapter 5.
