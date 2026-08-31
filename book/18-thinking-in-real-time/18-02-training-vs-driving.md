## 18.2 Training vs. driving — where the heavy compute lives

Here is a misconception worth dismantling, because almost everyone holds it: that the car is where the artificial intelligence "happens." It is natural to imagine the clever computer in the car as the seat of its intelligence, learning and thinking as it drives. But the truth is stranger and more interesting. The car does relatively little of the real computational heavy lifting. The vast, staggering, power-hungry effort of *creating* the intelligence happens somewhere the car will never go — in enormous data centres, on machines the size of buildings, long before a single line of the result is sent to a car. To understand self-driving, you have to understand this division of labour, because it is where most of the confusion lives.

Think of it as the difference between an education and a job. *Training* a neural network is the education — the long, expensive, effortful process of teaching it, from scratch, using the mountains of real-world driving data gathered by the fleet in Chapter 16. You show the network millions upon millions of examples — this is a pedestrian, this is a lane, in this situation the human braked — and through an enormous amount of repetitive computation, the network gradually adjusts itself until it can recognise these things reliably. This is the heavy compute, and it is heavy almost beyond imagining: it takes weeks or months, on purpose-built supercomputers consuming *megawatts* of power — the electricity of a small town — grinding through numbers day and night. It is done offline, in advance, with no car anywhere near it.

*Driving* is the job — the trained network actually doing its work, the inference of the last section. Once the education is complete, the finished network is a fixed thing that can be copied and sent, over the air, to every car in the fleet. And running it, as we saw, takes only a modest computer drawing a light-bulb's worth of power, because applying what you have learned is vastly cheaper than learning it. The car does the job; the data centre did the education.

Two kinds of thinking, two very different places:

```
   TRAINING                      DRIVING
   building the intelligence     using it
   ------------------------------------------------------------
   in giant data centres         in the car
   MEGAWATTS of power            80 to 160 watts
   weeks or months, offline      real time, right now
   grinds through millions       runs the finished network
   of examples                   once, per frame
   done ONCE, then copied        done constantly, in every
   to every car                  car, forever
   ------------------------------------------------------------

   The heavy thinking is NOT in the car. It happens in a
   building the car will never visit.
```

Tesla built specialised machinery for this training side, most famously a supercomputer project called Dojo, designed specifically to chew through the fleet's video data and train the driving networks. The story of Dojo is itself a lesson in how fast this field moves and how provisional even big bets can be: after years of development, Tesla wound the Dojo project down around 2025, judging it an evolutionary dead-end, and shifted its focus to new-generation chips (called AI5 and AI6) intended to handle both the training in the data centre and the inference in the car. This book flags that as very much a moving story — the specific hardware names will date quickly — but the underlying division does not change: whatever machine does it, *training* is a colossal offline effort, and *driving* is a small real-time one.

Why does this distinction matter to someone just trying to understand their car? Because it clarifies what is and is not happening as you drive. Your car is not learning from your driving in the moment — it is running a network that was trained elsewhere, weeks ago, on the aggregated experience of the whole fleet. Your car's *contribution* to the intelligence is the data it sends back (the shadow-mode divergences of Chapter 16), which feeds the next round of training in the data centre, whose result is then sent back to you as an update. The intelligence flows in a great loop between the fleet and the data centre, and the car is a node in that loop — a collector of experience and a user of the trained result — but not, itself, the place where the learning happens. The car applies; the data centre teaches; the loop connects them.

This also quietly reframes the vision-versus-sensors debate of the last chapter. Tesla's whole bet rests on the belief that the *training* side — enough data, poured into big enough networks, on powerful enough supercomputers — can teach a network to drive on camera images alone, compensating for the physical limits of the cameras with sheer learned intelligence. The critics' doubt is, at bottom, a doubt that any amount of training can overcome those physical limits. So the argument about sensors is really an argument about how far the education can be pushed — which is why the training machinery, invisible and far away, is as much a part of "how a Tesla works" as anything under the bonnet.

We have now traced the thinking from the camera to the roadside brain to the distant data centre and back. Only one question remains, and it is the one that matters most for the person actually sitting in the driver's seat: when all this perception and computation is switched on, what does the car actually *do* — and what do its famous, contested names really promise?

---

**Sources**

- Wikipedia (Tesla Dojo), TechCrunch, SemiAnalysis, Not a Tesla App — Dojo supercomputer built for training FSD neural networks on fleet video; Dojo wound down ~2025 in favour of AI5/AI6 chips for training and inference.
- The training-vs-inference distinction (offline, data-centre, megawatt-scale training vs in-car real-time inference) is a standard machine-learning concept; power figures from 18.1 sources.
- The fleet↔data-centre learning loop references Chapter 16; the connection to the vision-only bet references Chapter 17. Specific chip roadmap items are noted as fast-dating direction-of-travel.
