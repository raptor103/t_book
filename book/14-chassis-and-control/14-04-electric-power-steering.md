## 14.4 Electric power steering

Power steering is one of those conveniences so total that we have forgotten it is there. Turn the wheel of any modern car and it responds with an ease that has no relation to the real forces involved — the actual effort of twisting two heavily-laden tyres against the road, which without assistance would demand a genuine heave, especially when parking. Something is multiplying your effort many times over. For most of automotive history that something was hydraulic, and its quiet replacement by an electric system is both a small efficiency story and the hidden foundation of everything the car is learning to do by itself.

The old way was hydraulic power steering, and it was effective but wasteful in a way that should now sound familiar. A pump, driven by a belt off the engine, kept a supply of oil under high pressure at all times, and when you turned the wheel, valves directed that pressure to help shove the steering rack in the right direction. The catch is that the pump ran *constantly*, dragging on the engine and consuming energy every moment the engine turned, whether you were steering or driving dead straight down an empty motorway. Like the mechanical oil pump of Chapter 5, it was chained to the engine and could not switch itself off, so it wasted energy whenever it was not needed — which was most of the time.

Electric power steering throws the hydraulics away. In its place sits an electric motor, mounted on the steering system, that provides the assistance directly — when a sensor detects you turning the wheel, the motor spins to help push the rack over. Its first virtue is the efficiency one: the motor only draws power *when you actually steer*, and sits idle and lossless when you are going straight. There is no pump running for nothing, no fluid to leak or replace, no belt, no constant drag. For an electric car with no engine to drive a pump anyway, and with its obsessive care for every watt, this is the obvious choice, and it is universal on electric cars.

Hydraulic versus electric assistance:

```
   HYDRAULIC POWER STEERING      ELECTRIC POWER STEERING
   ------------------------------------------------------------
   a pump driven by the engine   an electric motor assists
   runs constantly, always on    only when you actually steer
   pressurised fluid and valves  a sensor reads your input,
                                 and the motor helps
   wastes energy going straight  draws nothing going straight
   the assist is mechanical      SOFTWARE sets the assistance
   ------------------------------------------------------------

   And the consequence that matters most: a motor that can
   turn the rack is a motor that can steer the car ITSELF.
   Every self-driving feature rests on this one fact.
```

But the efficiency is almost the smaller point. The larger one is that an electric motor is a thing a computer can command, and this quietly transforms what steering can be. Because software now sits between your hands and the assistance, the car can vary how much help it gives according to the situation — lots of assistance at parking speed, so the wheel turns with a fingertip, and less at motorway speed, so the steering feels firm, planted and precise. It can add a gentle self-centring, nudging the wheel back to straight. And — this is the profound part — because the motor can push the steering rack on its own, the car can *steer itself*. Every self-parking manoeuvre, every gentle correction that keeps the car in its lane, every wheel movement made by Autopilot or Full Self-Driving, is the electric power steering motor turning the wheels in response to a computer rather than a pair of hands.

This is why electric power steering, dull as it sounds, is one of the true enabling technologies of the automated car. You cannot have a car that steers itself if steering requires a human muscle pulling on a hydraulic valve; you can the moment steering is done by a motor a computer can address. The same substitution we have watched everywhere — a mechanical action replaced by an electronically commandable one — here opens the door to autonomy, because a steering system the software can move is a steering system the software can drive. Everything Part IX describes about a car perceiving and navigating the world would be inert without a hand on the wheel that answers to code, and EPS is that hand.

Note, though, what electric power steering still keeps: the mechanical column. In an ordinary electric car there is still a physical shaft connecting the steering wheel in your hands to the rack that turns the front wheels — the electric motor merely *assists* the turning of that shaft, and if the electronics failed entirely you could still, with real effort, steer the car through the surviving mechanical link. The connection between your hands and the road is augmented by electronics but not yet replaced by them. That last mechanical link — the steering column that has connected wheel to wheels since the dawn of the motor car — is the final one to go, and cutting it is the boldest substitution in the whole book. It is called steer-by-wire, and it is next.

---

**Sources**

- General automotive engineering and Tesla design — electric power steering (EPS) replaces engine-driven hydraulic pumps; motor assists on demand (efficiency), enables variable assist, self-centring, and software-commanded steering for parking/lane-keeping/autonomy.
- Parallel to the on-demand electric oil pump of Chapter 5; EPS retaining a mechanical steering column (assist, not replacement) is standard, distinguishing it from steer-by-wire in 14.5.
- EPS as the enabler of self-steering features connects to the autonomy discussion in Part IX.
