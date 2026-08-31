## 6.1 The single-speed reduction gear

We have already met the reduction gear as an idea — the single fixed ratio, about nine to one, that stands in for a whole gearbox because the motor's range is wide enough not to need one. But it is worth looking at the actual lump of metal, because it is the last stubbornly mechanical thing in the drivetrain, and it quietly solves a problem that has nothing to do with gearing at all: the problem of corners.

Here is that problem. When a car goes round a bend, its outer wheels travel a longer path than its inner wheels, and so they must turn faster. If both driven wheels were locked to the same shaft, forced to spin at identical speeds, one of them would have to skid on every corner — chirping, scrubbing, fighting the road. Every car ever built, petrol or electric, needs a device that lets its two driven wheels turn at different speeds while still sharing the drive. That device is the *differential*, and it is genuinely old — a clever arrangement of gears, understood since the nineteenth century, that splits torque to both wheels but allows each to find its own speed.

In an electric drive unit, the differential does not disappear; it is simply folded into the same compact housing as the reduction gears, so tidily that from the outside you would never guess two separate jobs are being done. The motor's fast, gentle-torqued spin enters one end; a first pair of gears steps it down; a second pair steps it down again to reach the roughly nine-to-one total; and the final gear drives the differential, which hands the now-slow, now-powerful rotation out to the two driveshafts and lets each wheel turn at whatever speed the corner demands. Motor, reduction, and differential, all in one sealed aluminium box the size of a picnic hamper.

The one drive unit, doing three jobs:

```
   motor spin  (fast, modest torque)
        |
   [ gear pair 1 ]   step down
        |
   [ gear pair 2 ]   step down again -- about 9:1 in total
        |
   [ DIFFERENTIAL ]  splits the drive to both wheels, and lets
        |     |      them turn at different speeds in a corner
      left   right
      wheel  wheel

   All three jobs inside one sealed aluminium box.
```

A small elegance hides in the choice of gears. The teeth are cut at an angle — *helical* rather than straight — so that each pair of teeth rolls into contact gradually rather than meeting all at once with a slap. Straight-cut gears are marginally stronger and are what you hear whining in a racing car; helical gears are quieter, and quiet matters enormously in a car with no engine to mask other noises. In a petrol car a little gear whine vanishes under the general roar. In an electric car, where the cabin can be library-silent, the faint singing of the reduction gears is sometimes the loudest thing in the drivetrain, and engineers work hard to hush it — angling the teeth, tightening the tolerances, damping the housing.

Now a genuinely interesting consequence of going electric, and one the "no model comparisons" spirit of this book lets us treat as pure technology. In a petrol four-wheel-drive car, getting drive to both axles means a *third* differential and a driveshaft running the length of the car to connect front to back — heavy, complex, lossy. An electric car with a motor on each axle needs none of that. The two axles are not connected by any shaft at all; they are connected only by the road and by software. Each axle has its own motor and its own differential, and the car coordinates them electronically, deciding instant by instant how much torque each end should make. The long propshaft, the centre differential, the transfer case — an entire subsystem of traditional all-wheel drive — is simply absent, replaced by two independent drive units and a fast computer telling them what to do. That electronic coordination is not only lighter and simpler; it is the foundation of the torque-vectoring tricks at the end of this chapter.

So the reduction gear is more than a stand-in for a gearbox. It is the drive unit's quiet mechanical core — stepping the motor down, splitting the drive, letting the wheels breathe through corners, all while trying not to sing. It is also the boundary line in the car: on one side, the last of the old mechanical world of gears and shafts and differentials, refined but ancient; on the other, the new world of electronic control, where slowing the car no longer means rubbing metal on metal but running the whole machine in reverse to catch the energy. That new world is where we go next.

---

**Sources**

- InsideEVs, "Tesla Model 3/Model Y Modular Electric Drive Units" — integrated motor + two-stage reduction + differential in one drive-unit housing.
- General drivetrain engineering — differential function (allowing driven wheels to rotate at different speeds through corners); helical vs straight-cut gear noise trade-off.
- Dual-motor cars replacing the mechanical centre differential/propshaft with two independent, electronically coordinated axles is standard EV architecture; torque coordination developed in 6.4.
