## 10.3 Etherloop: gigabit Ethernet, power over the same wires

Every so often an engineering idea is elegant enough that describing it makes people smile, and Tesla's Etherloop is one of them. It answers three separate problems — data bandwidth, power delivery, and wiring resilience — with a single stroke, and the stroke is almost absurdly simple: run one high-speed cable in a loop around the whole car, and send both the data *and* the power down it together.

Start with the bandwidth problem the last section left open. The car needs a backbone that can carry video, audio, and the coordination of its central computers — far more than CAN can manage. Ethernet, the technology that networks the world's offices, provides it, and Tesla's implementation runs at *gigabit* speed: a thousand megabits per second, a thousandfold leap over the old party line. Down this single connection can flow the digital video from multiple cameras to the self-driving computer, digital audio out to each speaker, the signals from cabin microphones used for active noise cancellation, and the general chatter of the car's brains — all the data-heavy traffic that CAN could never dream of carrying.

Now the elegant part. Ordinarily, data wires carry only data, and power comes down its own separate, heavier cables — two parallel networks threading through the car, doubling the wiring. Etherloop collapses them into one. Borrowing an idea long used in office networks called Power over Ethernet, Tesla sends the car's forty-eight-volt electrical power down the *same* cable that carries the data. A device tapped into the loop gets both its instructions and its electricity from a single connection. This is where the chapters knit together: it is precisely because the low-voltage system moved to forty-eight volts (Chapter 8) that meaningful power can be pushed down slim Ethernet-style wiring, and it is precisely the zonal organisation (Chapter 9) that makes a single shared loop practical. The threads of the whole part come together in one cable.

And then the loop itself, which is the cleverest touch. The cable is not a line with two ends but a *ring*, running all the way around the car and back to where it started. Why a ring? For resilience. In a straight-line network, cutting the wire anywhere severs everything beyond the cut. In a loop, every device can be reached from *both* directions — so if the cable is damaged or cut at any single point, the signals simply travel the other way around the ring to reach their destination. The network heals around the break. For a car, where a wire might be severed in a collision or by a fault, this self-healing property is a genuine safety and reliability feature, not merely a neat trick.

One cable, three problems solved:

```
   ETHERLOOP: one gigabit cable, run as a RING around the car

     +=======================================================+
     |                                                       |
     |   carries DATA (cameras, audio, microphones)          |
     |   AND 48 V POWER, along the very same cable           |
     |                                                       |
     +==+==========+==========+==========+==========+========+
        |          |          |          |          |
      camera    speaker      zone       mic       camera
                            controller

   Each device taps the loop once, for both data and power.
   Cut the loop anywhere and the signals simply travel the
   other way round the ring -- it heals itself.
```

The payoff, when you combine Etherloop with everything else in this part, is measured in the currency the whole part has cared about: copper deleted. Reports credit the Cybertruck's combination of forty-eight volts, zonal controllers and the Etherloop backbone with cutting the number of cross-car wires by around two-thirds and the copper used by something like seventy per cent. That is not an incremental trim; it is a wholesale reimagining of the nervous system, and it attacks the harness problem of the first section from every angle at once — fewer wires, thinner wires, wires that carry two things instead of one, arranged so the whole thing is shorter and simpler and, crucially, closer to something a robot could install.

Honesty and this book's conventions both require the reminder that Etherloop, like the full forty-eight-volt architecture, is direction-of-travel rather than the state of every Tesla on the road. It debuted on the Cybertruck; the mainstream Model 3 and Y still rely on more conventional mixtures of CAN and Ethernet and twelve-volt-derived power. This chapter includes Etherloop not because it is in the reference car, but because it shows, more clearly than anything else, where the nervous system is heading — and because it is the natural endpoint of every trend in this part: shorten the wire, raise the voltage, merge the functions, distribute the intelligence, and tie it all together over a fast, resilient, shared backbone.

There is one more thing to say about a car that runs its whole nervous system on published, standard technologies like Ethernet — and about a company that, unusually, keeps taking its own hard-won designs and *giving them away*. That is not generosity for its own sake; it is a strategy, and understanding it explains why a Ford can now charge at a Tesla station and why the humble connectors in a car have become a battleground. Standardisation as strategy is where the chapter, and the part, conclude.

---

**Sources**

- Wikipedia (Etherloop), electrifynews, MachEforum, teslamagazine — Cybertruck Etherloop: single gigabit Ethernet loop carrying data and 48V power (Power over Ethernet); loop topology reroutes if cut; carries camera video, digital audio, ANC microphone signals.
- NextBigFuture / autoevolution — ~68% reduction in cross-car wires and ~70% less copper from the combined 48V + zonal + Etherloop approach.
- Dependencies on 48V (Chapter 8) and zonal architecture (Chapter 9) per those chapters; Etherloop stated as Cybertruck-first direction-of-travel per this book's convention.
