## 16.1 Over-the-air updates

The mechanism behind the car-that-improves-overnight is simple to describe and radical in its consequences. Like your phone, a Tesla can receive new software wirelessly — over Wi-Fi at home, or over its built-in cellular connection — download it quietly in the background, and, once you approve, install it while the car sits parked and idle. Tesla rolls these updates out in waves, so not every car gets a given update on the same day, and the process is designed to be as unremarkable as a phone update: a notification, a tap to accept, a short wait, and the car reboots into a new version of itself. The engineering to do this *safely* is considerable — you very much do not want an update to fail halfway and leave a car unable to boot — but from the owner's side it is mundane, which is precisely the point.

What arrives in those updates is where it stops being mundane. Over-the-air updates have delivered three quite different kinds of change, and each rewrites an old assumption about cars.

The first is *new features*. Cars have received entirely new capabilities long after leaving the factory — new interface layouts, games, streaming apps, dashcam functions, improvements to navigation and climate control, and refinements to Autopilot. A feature that did not exist when you bought the car simply appears one morning, free, because the hardware was always capable of it and the software finally arrived to use it.

The second, and more startling, is *performance and behaviour*. Tesla has used software updates to change how the physical car performs — improving acceleration, refining the regenerative braking, optimising energy management to extend range, smoothing the driving experience. The car's hardware did not change; the code controlling that hardware did, and the car became meaningfully quicker or more efficient as a result. Because, as this whole book has shown, so much of the car is now controlled by software — the inverter's switching, the thermal system's logic, the blend of regeneration and friction braking — improving that software improves the physical machine. The car you own is, in a real sense, partly made of code, and better code makes a better car.

The third is the humble but valuable one: *fixes*. Bugs get corrected, quirks smoothed, problems that would once have required a recall and a trip to the dealer resolved with a download. A fault discovered across the fleet can be patched everywhere, overnight, without anyone lifting a spanner.

What an update can change:

```
   An update downloads while the car is parked, and installs
   only once you approve it. What arrives:

   NEW FEATURES .... apps, interface, dashcam, navigation,
                     driver-assistance behaviour
   PERFORMANCE ..... acceleration, range, regeneration, thermal
                     behaviour -- same hardware, better code
   FIXES ........... bugs patched across the whole fleet at
                     once, with no visit to a dealer

   The car stops being a fixed object bought once, and becomes
   a platform that keeps changing.
```

The consequence is a reversal of the oldest fact about owning a car: that it is all downhill from the showroom. A software-defined car can be *newer*, in capability, three years into its life than it was on the day it was bought — running the same software as a car fresh off the line, gaining features its original buyers never imagined. The car stops being a depreciating fixed asset and becomes something closer to a device that is supported, updated, and improved over time. That is a genuinely new relationship between a person and their car, and it is one of the things owners cite most warmly.

But this book insists on the other side, and here it is a real one. When a car is defined by software that the manufacturer controls, the manufacturer can change it in ways you do not want, as well as ways you do. Features can be altered or removed by an update as easily as added. Behaviour you relied on can shift beneath you. Capabilities can be placed behind new paywalls, or a car's functions made dependent on a subscription. And because the software is controlled centrally, your car's behaviour is, to a degree no mechanical car ever was, in someone else's hands. The same mechanism that lets a car improve overnight lets it change overnight, and not always in your favour. The power to reprogram the car from afar is a power, and it does not belong to you.

None of this would be possible, or safe, without the architecture of the last chapter — the isolation that ensures an update touching one system cannot endanger another, so that the car can be reprogrammed on your driveway without risking the systems that keep you alive. Over-the-air updating is the visible payoff of that careful separation of concerns. And it is only the most obvious expression of a much deeper change, one that has been building quietly through every chapter of this book: the steady conversion of the car from a machine of mechanical linkages into a machine of signals that software can command. That deeper change is worth naming directly.

---

**Sources**

- Recharged, MakeUseOf, tesevo — Tesla OTA updates via Wi-Fi/cellular, background download, install while parked, staged rollout; new features, performance/efficiency/acceleration improvements, and bug fixes delivered over the air.
- tesevo / trendingcar — examples of Autopilot, energy-management, and regenerative-braking improvements via software; a car gaining capability years after purchase.
- The ownership/control caveats (feature removal, paywalls, central control) are widely reported and follow from the software-defined model; dependence on the isolation architecture references Chapter 15.
