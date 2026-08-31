## 5.4 Small efficiencies: the electric oil pump and other invisible wins

If Chapter 1 had a moral, it was that efficiency in an electric car is not won in one grand stroke but accumulated in a hundred small ones, each too minor to notice on its own. Nowhere is this clearer than inside the drive unit, where the headline components — motor, inverter, gear — are already so good that the remaining gains have to be scavenged from the margins. This section is about those margins: the unglamorous refinements that no advertisement mentions and that, added together, are worth real kilometres of range.

Start with a component so humble it sounds like a joke in a book about electric cars: the oil pump. Yes, an electric car has oil, and a pump to move it. Not engine oil — there is no engine — but a light synthetic fluid that lubricates the reduction gears and, cleverly, also cools the motor from the inside. And here is the small, characteristic piece of intelligence. In a petrol car the oil pump is driven mechanically by the engine itself, which means it runs flat out whenever the engine runs, pumping hard even when hardly any oil flow is needed, dragging on the engine and wasting energy the entire time. It cannot do otherwise; it is chained to the crankshaft.

Tesla's drive unit instead uses an *electric* oil pump — a small independent pump with its own motor, controlled by the car's computers, that speeds up, slows down, or switches off according to what the drive unit actually needs at that moment. Gentle cruising on a cool day needs barely any flow, so the pump barely runs, and the energy that a mechanical pump would have wasted stays in the battery. Push the car hard until the motor heats up, and the pump spins up to pour cooling oil exactly where it is wanted. The pump is sized and run to minimise its own losses — flow on demand, rather than flow regardless. It is the same principle as the whole car: never spend energy on something you are not currently using.

The oil's double life is itself a small elegance. The same fluid that keeps the gears from grinding is flung onto the spinning rotor to carry its heat away, then drips down into a sump, passes through a heat exchanger to hand its warmth to the main coolant, and returns to do it again. Tesla's own patents describe fussing over details most people would never imagine mattering — an elevated sump that lets gravity feed oil straight onto the specific bearings and gear teeth that need it, rather than the traditional method of letting the gears splash through a bath of oil and drag against it. Splashing wastes energy churning the oil; targeted feeding does not. It is a fraction of a percent, chased deliberately.

Where the invisible wins hide:

```
   The drive unit's quiet efficiencies. Each is tiny.
   Added up, they are worth real kilometres.

   electric oil pump ..... runs only as needed, never always-on
   one fluid, two jobs ... the same oil lubricates AND cools
   targeted oil feed ..... gravity onto the bearings and teeth
                           that need it, instead of letting the
                           gears splash through a bath and drag
   dragless idle ......... the induction motor switches fully off
   low-friction seals .... less rubbing where the shafts come out
   warm oil on purpose ... thinner oil is cheaper to pump, so a
                           slightly hotter unit can be the
                           efficient one -- held on a knife-edge
                           by software, since too hot stops cooling
```

And there are more of the same kind, scattered through the car. The induction motor from two sections ago, able to switch fully off and freewheel with almost no drag when it is not needed, is one of these wins wearing a bigger coat. The bearings and shaft seals are chosen and shaped to rub as little as possible, because a seal that grips a spinning shaft too tightly costs energy every second of every journey. Even the temperature of the oil is played as an efficiency card: warm oil is thinner and easier to pump, so the car will sometimes tolerate a slightly hotter drive unit precisely because the thinner oil wastes less energy in pumping and churning — a balance held on a knife-edge by software, since oil that gets *too* hot stops cooling properly.

None of this is the sort of thing that sells a car. You cannot feel the electric oil pump modulating its flow, or the sump feeding a bearing by gravity, or the seals rubbing a little less. That is precisely the point. These are the wins the driver never notices, which is why they are so easily overlooked and so genuinely important. A car is not made efficient by one miracle. It is made efficient by an engineering culture that treats every half-percent as worth chasing, everywhere, all the time — in the shape of a sump, the control of a pump, the tightness of a seal.

Add them up across the drive unit and they are the difference between a car that goes far and one that goes a little further. Which is the whole game. We have now stored the energy, converted it, and delivered it to a single gear. What remains is to *manage* that motion — to slow the car, to split the drive between wheels, to turn the motor's talents into control — and that is the business of the next chapter.

---

**Sources**

- Tesla, Inc. patents (freepatentsonline US2019/0003572; USPTO 12162343, 11114921) — electric oil pump with variable speed/duty cycle; oil lubricating gears and cooling the rotor; heat exchanger to coolant; elevated/targeted oil sump vs splash lubrication.
- Teslarati, "Tesla is designing an electric pump system" — variable-flow electric pump to minimise pumping losses.
- Lectron EV — synthetic drive-unit fluid; no engine oil. Some design specifics are patent-derived [INFERENCE] and may vary across drive-unit revisions.
