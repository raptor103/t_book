## 9.1 VCFRONT, VCLEFT, VCRIGHT — controllers by geography, not function

Imagine you are wiring a car and you have to connect a hundred small devices — lights, motors, switches, sensors — scattered throughout the body, to the computers that control them. There are two ways to organize the job, and the choice between them turns out to be one of the most consequential decisions in the whole design.

The traditional way organizes by *function*. You build a controller for each job — one for the body electronics, one for the doors, one for the climate system, and so on — and then each controller runs its own wires out to every device it needs, wherever in the car that device happens to sit. The door controller reaches out to all four doors; the lighting controller reaches out to every lamp front and rear; the climate controller threads wires to sensors in the cabin, the vents, the outside. Every controller is a specialist with tentacles stretching across the entire car, and the tentacles overlap and criss-cross into an enormous woven mass. This is how cars were wired for a century, and it grew more tangled every year as features multiplied.

Tesla's Model 3 does something that, once you hear it, seems obvious — though obvious ideas are often the hardest to adopt, because they require throwing out the accumulated habits of an industry. It organizes by *geography*. Instead of a controller per function, there are a few controllers per *region* of the car, and each one takes charge of everything nearby, regardless of what that thing does. There are three main ones. **VCFRONT** sits at the front, behind the frunk, and looks after the things at the front — the lights, many of the thermal components, whatever lives up there. **VCLEFT** sits in the left footwell and handles the devices down the driver's side of the car. **VCRIGHT** sits in the right footwell and handles the passenger side. The names are refreshingly literal: front controller, left controller, right controller.

Function versus geography:

```
   BY FUNCTION (the old way)      BY GEOGRAPHY (zonal)

   door module --> all 4 doors    VCFRONT --> all things up front
   light module -> every lamp     VCLEFT  --> all things on the left
   climate mod. -> every vent     VCRIGHT --> all things on the right

   each module reaches right      each controller handles only
   across the whole car           what is physically NEAR it

   long wires crossing and        short local drops, plus one
   overlapping everywhere         thin shared data backbone
```

The liberating part is that a zone controller does not care what a device *is*. To VCLEFT, a driver's-door window motor, a driver's-side puddle lamp, a left-side temperature sensor and a nearby pump are all just "things near me that need power and control." It provides them power, switches them on and off, reads their sensors, and reports up to the car's central brain over a shared network. The controller is a general-purpose local agent — domain-agnostic, in the jargon — rather than a specialist. And because it is general-purpose, the same basic controller design can be dropped anywhere, which simplifies the parts list too.

What makes this work is that the zone controllers do not each need their own long wires back to a central computer. They connect to one another and to the main computers over a shared communications network — the car's data backbone, which the next chapter examines — so that VCLEFT can tell the central computer "the driver just pressed the window switch," and the central computer can tell VCRIGHT "raise the passenger window," all over a few shared data wires rather than dedicated point-to-point runs. The intelligence is distributed to the edges of the car, near the things being controlled, and only *decisions and messages* travel long distances, not raw power to every device.

It helps to think of it as the difference between two ways of running a country's post. The old, functional way is like every government department maintaining its own private courier network to reach every citizen — hopelessly duplicated. The zonal way is like having one local post office in each town that handles all the mail for everyone nearby, whatever it concerns, and a single trunk route connecting the post offices. Vastly less infrastructure, and far easier to extend: add a new device near a zone, and you simply connect it to the local controller rather than running a fresh wire across the whole car.

This reorganization is the foundation for the two sections that follow. Because each zone controller is the local hub for power distribution, it can also *become* the fuse box for its region — but a fuse box without any fuses, as the next section explains. And because devices now connect to a nearby controller instead of a distant one, the total length of wire in the car can fall dramatically, which is the payoff the chapter builds toward. It all flows from one deceptively simple decision: to stop asking "what does this device do?" and start asking "where is it?"

---

**Sources**

- Go-Parts and Jalopnik — Tesla Model 3 zonal body controllers VCFRONT (behind frunk), VCLEFT and VCRIGHT (footwells); each handles components by location (front / driver's side / passenger side).
- S&P Global Automotive Insights — zonal architecture reduces the number of ECUs and wiring by using domain-agnostic hardware managing local functions; potential wiring reduction cited (up to ~50%, developed in 9.3).
- Zone controllers acting as fuse boxes (MOSFETs/current detectors, no physical fuses) per Go-Parts; developed in 9.2. Data-backbone communication developed in Chapter 10.
