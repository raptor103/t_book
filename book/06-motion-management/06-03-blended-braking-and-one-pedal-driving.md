## 6.3 Blended braking and one-pedal driving

Ask a Tesla driver what surprised them most in their first week, and a striking number will say the same odd thing: they almost stopped using the brake pedal. Not out of recklessness — the car slows down beautifully — but because most of the slowing had quietly migrated to the *other* pedal, the one they used to think of as "go." This is one-pedal driving, and it is the most immediately noticeable behavioural change of switching to electric. Underneath it sits a piece of software cleverness called blended braking, and the two are worth taking apart carefully, because the way they fit together is a small masterpiece of hiding complexity from the user.

Begin with the pedal you *do* still have. When you press the brake pedal in an electric car, you are not — as you might assume — simply clamping the friction brakes. You are making a request: *slow the car by this much.* The car then decides how to honour it. For all but the hardest stops, it will honour it with regeneration alone, running the motor backwards to slow the car and harvest the energy, exactly as the last section described. Only when you ask for more deceleration than the motor can supply, or when regeneration is unavailable because the battery is full or cold, does the car quietly bring the friction brakes into play — and it does so smoothly, feeding them in underneath the regeneration so that the total slowing matches what your foot asked for. This is *blended braking*: two utterly different mechanisms, one electrical and one mechanical, seamlessly mixed so that the pedal feels like a single consistent thing.

The blending is genuinely hard to do well, which is why it is a point of pride. The friction brakes and the regenerating motor have completely different characters — different response times, different force curves, different behaviour when cold or wet — and yet the handover between them must be imperceptible. If the driver could feel the moment the friction brakes cut in, the car would feel lumpy and untrustworthy. Getting it invisible, across every temperature and state of charge, is the sort of unglamorous refinement that separates a car that merely works from one that feels polished. There is even a safety dividend: because the friction brakes remain fully independent and mechanically capable, they can stop the car entirely on their own if the electronics ever fail, so the clever blending never compromises the fundamental ability to stop.

Now the other pedal, and the real revolution. In an electric car, lifting off the accelerator does not just cut the power — it actively brakes, hard, through strong regeneration. Ease off, and the car slows noticeably, as if you had gently pressed a brake; lift off entirely, and it slows firmly enough to handle most everyday deceleration without the brake pedal ever being touched. With a little practice you learn to modulate the car's speed entirely through the accelerator: press for faster, lift for slower, and reserve the actual brake pedal for hard or unexpected stops. Hence one pedal. Some Teslas take it to the logical end with a "Hold" mode that brings the car to a complete standstill and keeps it there, blending in the friction brakes automatically at walking pace — below around **6.5 km/h**, where regeneration fades to nothing — so the car comes to a clean, held stop without any pedal at all.

The two pedals, reimagined:

```
   ACCELERATOR                   BRAKE PEDAL

   press -> the motor drives     press -> "slow me by THIS much"

   lift  -> the motor            the car then chooses:
            regenerates, and       regeneration first,
            the car slows          friction added only as needed

   does most of the everyday     kept for hard stops and
   braking on its own            emergencies

   Hold mode: below about 6.5 km/h regeneration fades away, so
   the friction brakes are blended in to bring the car to a
   clean, held standstill -- no pedal at all.
```

Two footnotes keep it honest. First, one-pedal driving is beloved but not automatically more *efficient*, a subtlety often missed. Its regeneration recovers energy handsomely, but the driving style it encourages — squeezing the accelerator harder to overcome the strong lift-off braking — can burn energy too, and a smooth driver coasting toward a stop can sometimes do as well or better. What one-pedal driving reliably delivers is not maximum efficiency but a calmer, more relaxed way of driving, and far less use of the friction brakes.

That last point has a lovely material consequence, which Chapter 14 returns to: the friction brakes on an electric car barely wear out. Because regeneration does the great majority of the slowing, the pads and discs are used so lightly that they can last the life of the car, and the main hazard becomes not wear but rust from disuse. A brake that is too rarely used to wear down — it is a small, perfect emblem of the whole electric project, in which the old hard problem is not solved but sidestepped, and the leftover parts are left with almost nothing to do.

---

**Sources**

- Not a Tesla App, "How Tesla's Regenerative Braking Works" — brake pedal requests deceleration; car blends regen and friction; friction blended in below ~4 mph (~6.5 km/h) in Hold mode.
- Tesla patents on one-pedal drive, blended braking, and brake-light control (USPTO 11794715, 11745737, 11724642) — grade-compensated one-pedal torque, regen/friction blend management.
- arXiv (haptic pedal feel, 2019) and Shop4Tesla — one-pedal driving does not guarantee higher efficiency; independence of friction brakes for emergency stopping. Reduced brake wear developed in 14.2.
