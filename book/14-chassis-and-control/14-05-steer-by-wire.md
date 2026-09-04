## 14.5 Steer-by-wire: no column, triple redundancy

For as long as there have been motor cars, one thing has been sacred: the physical connection between the steering wheel and the road wheels. A shaft — the steering column — runs from your hands down to the mechanism that turns the front tires, so that when you turn the wheel, metal moves metal, and you are, quite literally, mechanically linked to the road. Every other control has been allowed to become a signal — the throttle, the gear selector, the brakes largely so — but the steering kept its hard mechanical spine, because the idea of trusting your ability to *point the car* to nothing but electronics felt like a step too far. Steer-by-wire is that step, and it is the most radical single substitution in this entire book.

In a steer-by-wire system there is no column. Nothing physical connects the steering wheel to the front wheels at all. The steering wheel becomes a pure input device — sensors read how far and how fast you turn it — and that reading is sent, as an electrical signal, to motors down on the steering rack that do the actual turning. Your hands talk to a computer; the computer talks to the wheels. The sacred mechanical link is replaced by wires and software, and Tesla's Cybertruck became the first production car in the United States to do this with *no mechanical backup* — no emergency shaft waiting in reserve, nothing to fall back on if the electronics fail. That is a genuinely bold, and to some engineers genuinely alarming, thing to do.

Which means the entire viability of steer-by-wire rests on one thing: it must not fail. And since no single component can ever be trusted absolutely, the system is built on *redundancy* — the discipline of making everything more than once, so that no single failure can leave you unable to steer. The Cybertruck's implementation, as teardown engineers found, is a small masterclass in the art. There are *two* electric motors turning the steering rack, so that if one dies the other carries on. There are *three* position sensors reading the steering input, with a tie-breaker rule to decide what to do if they ever disagree — because with three opinions, two can outvote a faulty one. And the signals travel over a *dual-redundant* forty-eight-volt Ethernet loop — two independent communication paths, using the resilient looped network of Chapter 10, so that a single severed wire cannot cut the wheel off from the rack. Everything critical exists at least twice.

Redundancy, so no single failure disconnects you:

```
   STEER-BY-WIRE -- no mechanical column at all

   the steering wheel
        |
        v
   THREE position sensors ...... if one disagrees, the other
        |                        two outvote it
        v
   DUAL-redundant 48 V ......... two independent paths, so one
   Ethernet loop                 severed wire changes nothing
        |
        v
   TWO rack motors ............. if one dies, the other still
        |                        steers the car
        v
   the front wheels

   Everything critical exists at least twice. The sacred
   mechanical link is replaced by wires and built-in backups.
```

Notice how many threads of the book converge here. Steer-by-wire leans on the forty-eight-volt architecture of Chapter 8, because turning a steering rack takes real power, and doing it at forty-eight volts rather than twelve means thinner wires to the steering motors — one of the specific features that pushed Tesla toward the higher voltage in the first place. It leans on the resilient Ethernet loop of Chapter 10 for its fail-operational communication. And it is the ultimate expression of the substitution we have traced from the very first chapter: the last mechanical linkage, the one everyone thought untouchable, finally converted into a signal.

What do you gain for taking such a leap? Because the steering ratio is now defined in software rather than fixed by mechanical gearing, the car can change how much the wheels turn for a given turn of the wheel — and change it with speed. At parking speed it can be extremely aggressive, so that a tiny movement of the wheel swings the front tires hard over: the Cybertruck goes from lock to lock in a little under one full turn of the wheel — around 340 degrees — where an ordinary car needs about three, and a U-turn takes roughly a third of a rotation, so you never have to shuffle your hands to park. At highway speed the same system calms right down, so the steering is relaxed and stable and a nervous twitch of the hands does not dart the car across a lane. A mechanical steering rack could never do both; a software-defined one simply chooses the ratio to suit the moment. It also frees the designer from routing a hard steering shaft through the car, which opens up packaging and crash-safety possibilities.

Honesty demands the caveat this section has been circling, and it is a serious one. Removing the mechanical backup means placing absolute trust in the electronics and their redundancy, and reasonable people disagree about whether that trust is yet warranted for something as safety-critical as steering. The redundancy is impressive, but it is not the same as a steel shaft that cannot crash, hang, or receive a bad software update. This is why steer-by-wire remains, in 2026, a frontier feature — present on the Cybertruck, absent from the mainstream Model 3 and Y, and written here, per this book's convention, as a direction of travel rather than a settled norm. It is one of the boldest bets in the car, and whether it becomes universal will depend on years of accumulated evidence that the wires really are as trustworthy as the shaft they replaced. But the direction, as with so much else, is unmistakable — and it enables one more trick that a fixed mechanical column never could, which is to let the *rear* wheels steer as well.

---

**Sources**

- The Autopian, Munro/leandesign, Go-Parts, Wikipedia (steer-by-wire) — Cybertruck steer-by-wire: no steering column, first US production car with no mechanical backup; two rack motors, three position sensors with tie-breaker, dual-redundant 48V Ethernet loop.
- Not a Tesla App / e-vehicleinfo, The Drive, Cybertruck Owners Club — software-defined variable steering ratio: roughly 340° lock-to-lock (about ±170°) against a conventional car's ~1,080°, and about 120° of input for a U-turn; more aggressive at low speed, calmer at high speed.
- Dependencies on 48V (Chapter 8) and the Ethernet loop (Chapter 10) per those chapters; steer-by-wire stated as Cybertruck-first direction-of-travel. The safety debate over removing mechanical backup is reported industry/engineering commentary.
