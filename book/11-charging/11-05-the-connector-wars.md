## 11.5 The connector wars

Of all the ways the early electric-car era made life harder than it needed to be, none was as petty or as maddening as the argument over the shape of the plug. For years, an electric car could arrive at a working, powered charging station and be unable to use it, for the sole reason that the plug was the wrong shape — the automotive equivalent of arriving at a full petrol station whose nozzles did not fit your filler neck. This was the "connector wars," and it is worth understanding both because it shaped the experience of early owners and because it is, at last, resolving.

The mess had an innocent origin: different regions and companies standardised at different times, in different ways, before anyone knew which approach would win. The result was a small zoo of incompatible connectors. For everyday AC charging, North America settled on a plug called J1772 and Europe on one called Type 2. For fast DC charging, a Japanese-led standard called CHAdeMO appeared first, then a European-and-American alliance produced CCS — the Combined Charging System — and Tesla, impatient with all of them, simply built its own slim connector and the network to match. China, meanwhile, went its own way entirely with a family called GB/T. A driver crossing regions, or shopping across brands, faced a bewildering compatibility matrix.

Amid the chaos, one genuinely good idea deserves singling out, because it is a small piece of elegant engineering hiding in a bureaucratic story. Early cars needed *two* separate sockets — one for AC charging and one for DC — because the two used different plugs. CCS's insight, right there in its name, was to *combine* them: take the existing AC connector and simply add two extra high-current pins below it for DC. Now a single port on the car accepts both — ordinary AC charging through the top part, fast DC charging through the whole thing — with no need for two holes in the bodywork. Tesla's connector does the same trick even more neatly, using the *same* pins for both AC and DC. One slim port, both kinds of charging: it is the same consolidating instinct that runs through this whole book, applied to a socket.

The regional picture, roughly as it stands in 2026:

```
   REGION          AC plug        DC fast plug
   Europe          Type 2         CCS2 (Type 2 + 2 DC pins)  [mandated]
   North America   J1772 -> NACS  CCS1 / CHAdeMO -> NACS (winning)
   Japan           Type 1         CHAdeMO (fading)
   China           GB/T AC        GB/T DC
```

For a European reader, there is a happy simplicity worth stating plainly, because it is the context this book is written in. Europe largely avoided the worst of the war by regulating early: Type 2 for AC and CCS2 for DC were effectively mandated as the common standards, and — crucially — Tesla went along with it. European Teslas do not use a proprietary Tesla plug; they use the same Type 2 and CCS2 connectors as everyone else, and Tesla opened its European Supercharger network to other brands' CCS cars. So the continent where this book is set is the one where the connector wars barely happened: a European EV driver, whatever the badge, mostly plugs the same standard connector into mostly compatible chargers. The tidiness was bought by regulation acting before the fragmentation could set, a reminder that sometimes the way to win a standards war is to prevent it.

North America is the region where the war actually raged, and where it is now ending — through the story told in Chapter 10. Tesla's connector, opened up and rechristened NACS, has swept the field: nearly every carmaker has agreed to adopt it, and the older CCS1 and the ageing CHAdeMO are on their way out. The continent that suffered the most fragmentation is converging, belatedly, on a single plug — Tesla's. It took a decade and a great deal of wasted effort, but the destination is the same one Europe reached years earlier by decree: one connector, both kinds of charging, cars and chargers that simply work together.

The deeper point, and the reason this belongs in a book about engineering rather than politics, is that a charging connector is *infrastructure*, and infrastructure is only as good as its universality. The finest fast charger in the world is worthless if your plug does not fit it, and the value of a charging network grows with the square of how many cars can use it. The connector wars were a decade-long, expensive demonstration that the *shape of the plug* was never really the point — the point was agreement, and the technical merits of any one connector mattered far less than getting everyone to use the same one. That both major markets have now, by very different routes, arrived at a single standard is arguably better news for electric cars than any improvement to the connectors themselves.

With that, filling the car up is demystified: convert the electricity somewhere, in the car or the cabinet; carry a small charger and visit big ones; respect the taper and charge to eighty on trips; and plug in a connector that, at long last, mostly fits. The car is now stored, driven, cooled, wired, and refuelled. It is time to send it out into the world and see what fights back — beginning with the air.

---

**Sources**

- Wevolver, Power Sonic, ChargePoint, bp pulse — connector landscape: J1772/Type 2 (AC), CCS1/CCS2, CHAdeMO, NACS, GB/T; CCS "combines" AC plus two DC pins; regional standards.
- ChargePoint / usevchargingstations — Europe standardised on Type 2 + CCS2; Tesla uses Type 2/CCS2 in Europe and NACS in North America; NACS (SAE J3400) adoption across North American automakers (2025+).
- NACS adoption narrative cross-references Chapter 10; "value grows with universality" is the network-effect argument applied to physical connectors.
