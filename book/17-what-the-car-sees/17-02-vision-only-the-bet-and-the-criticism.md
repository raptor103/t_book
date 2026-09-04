## 17.2 Vision-only: the bet and the criticism

The question is simple to state: can a car drive itself safely using cameras alone, or does it need other senses — radar, and especially the laser scanners called lidar — to be truly safe? Tesla has bet its entire self-driving program on the first answer. Much of the rest of the industry, and many independent experts, believe the second. Both sides have real arguments, and honesty requires laying them out fairly, without a thumb on the scale.

Start with the case *for* vision-only, because it is more elegant than critics often admit. The headline argument is an appeal to biology: human beings drive using two eyes and a brain, and nothing else — no radar, no laser scanner — and we manage it well enough that most journeys end uneventfully. If a human can drive with vision and intelligence alone, the reasoning goes, then a machine with good enough cameras and a good enough neural network should be able to as well; the problem is not a lack of senses but a lack of brain, and the brain is exactly what improves with the data flywheel of Chapter 16. The supporting arguments follow: cameras are cheap enough to put on every car, which keeps that flywheel spinning with data from millions of vehicles; a single kind of sensor avoids the arbitration problem of a car receiving conflicting reports from different senses; and cameras capture the rich detail — color, text, the exact shape of things, brake lights, hand signals — that radar and lidar simply cannot. The bet is that intelligence, fed by scale, beats a pile of sensors.

Now the case *against*, which is equally serious and comes from equally informed people. It rests on the things cameras are genuinely bad at. A camera sees a flat image and must *infer* depth — how far away things are — indirectly, by clever reasoning, whereas lidar and radar *measure* distance directly, by timing reflected light or radio waves. Direct measurement is more reliable than inference, and depth is exactly the thing you most want to get right when deciding whether to brake. Cameras also struggle badly in conditions where radar and lidar shrug: thick fog, heavy rain, snow, blinding low sun, the darkness of an unlit road. A human copes with these by slowing down and using judgement, but a camera in fog is simply half-blind. And the deepest objection is about *redundancy*: relying on one kind of sensor means that when it is fooled — by glare, by an unusual object, by a reflection — there is no independent second sense to catch the error. Many safety experts hold that genuine, unsupervised self-driving *requires* redundant, diverse sensors precisely so that no single failure can go unchecked, and that a camera-only system, however clever, cannot reach the necessary safety on its own.

The argument, fairly stated:

```
   THE BET (vision only)         THE CRITICISM (not enough)
   ------------------------------------------------------------
   humans drive on eyes and      cameras INFER depth; radar
   a brain, so cameras and AI    and lidar MEASURE it
   ought to be sufficient        directly, which is safer

   cameras are cheap, so every   cameras fail in fog, rain,
   car carries them -- more      snow, glare and darkness.
   data, and a better AI         Radar and lidar do not.

   one sense means no            one sense means no
   conflicting signals to        redundancy: a fooled camera
   arbitrate between             has nothing to check it

   rich detail: color, text,     many experts hold that safe
   brake lights, gestures        autonomy REQUIRES diverse
                                 sensors, and lidar is now
                                 far cheaper than it was
   ------------------------------------------------------------
```

The evidence, as of 2026, is genuinely mixed and does not hand victory to either side. Tesla's vision system has improved markedly and, by some measures of active safety, its cars perform well. At the same time, camera-only driving has shown persistent weaknesses — including the unnerving phenomenon of "phantom braking," where the car brakes hard for a hazard that is not there, a classic symptom of a vision system misreading a shadow or a reflection — and independent assessments of how often a human must take over still fall well short of what unsupervised autonomy would demand. Meanwhile the economic ground has been shifting under the debate: one of Tesla's strongest original arguments, that lidar was hopelessly expensive, has weakened as lidar prices have fallen, softening the cost case for going without it.

So where does that leave an honest reader in 2026? With a real question, genuinely open. It is entirely possible that Tesla is right, and that a sufficiently trained vision system will cross the gap to safe autonomy, vindicating the boldest subtraction in the car. It is equally possible that the critics are right, and that no amount of neural-network cleverness can compensate for the physical limits of a single sense, so that the camera-only path tops out at excellent *assistance* but never reaches true self-driving. This book takes no side, because taking a side would be dishonest about the state of knowledge. What it can say is that the bet is real, the stakes are enormous, and the answer will be written not in marketing claims but in years of accumulated road evidence — the very evidence the next chapter's computers are built to gather and act upon.

---

**Sources**

- IEEE Spectrum, Not a Tesla App, basenor — the pro-vision case: human vision analogy, camera cost/scalability feeding the data flywheel, avoiding sensor-fusion conflicts, rich visual detail.
- Fast Company, InsideEVs, engineering.com, whatisrecal — the criticism: cameras infer depth vs direct lidar/radar measurement; poor performance in fog/rain/snow/glare/darkness; lack of redundancy; expert view that safe unsupervised autonomy needs diverse sensors; falling lidar costs.
- Phantom braking and disengagement-rate concerns per InsideEVs/reporting. The chapter deliberately reaches no verdict, consistent with the unsettled 2026 state and this book's honesty convention.
