## 10.2 CAN bus and its limits

In 1986, an engineer at Bosch presented a new way for the electronic parts of a car to talk to each other, and it was so well-suited to the job that four decades later it is still, quietly, running inside almost every vehicle on earth. It is called the CAN bus — Controller Area Network — and before we watch it hit its limits, it deserves a moment of genuine admiration, because it solved a real problem with real elegance.

The problem it solved was wiring, the very problem of the last section. Before CAN, if a switch needed to talk to a device, you ran a wire between them, and as cars gained electronics the number of wires threatened to become unmanageable. CAN's insight was to let many devices share a single pair of wires — a *bus* — like party-line telephones sharing one line, rather than each pair having its own private connection. Every controller taps into the same two-wire bus, and messages are broadcast onto it for whoever needs them. It is robust almost to a fault: designed for the electrically filthy environment of a car, it shrugs off noise, keeps working if some messages are garbled, and has a clever scheme for deciding who talks when two devices try at once, so the most urgent message always wins without any collision or confusion. Cheap, tough, and reliable, CAN became the nervous system of the automobile and never really left.

The two-wire party line:

```
   CAN BUS: one shared pair of wires, many controllers tap in

     ==+==========+==========+==========+==========+==  (2 wires)
       |          |          |          |          |
     engine     brakes     doors      lights     sensor
     (messages broadcast to all; urgent ones get priority)

   robust, cheap, simple -- but SHARED, and slow by modern
   standards (~1 Mbit/s; a few Mbit/s for newer CAN variants)
```

But CAN was designed for a world of small messages. Its whole job was to carry short, urgent control signals: *this switch is on; that sensor reads forty degrees; apply the brakes.* For that, its modest speed — around one megabit per second, a few megabits in newer versions — is not merely enough but ideal, because control signals are tiny and what matters is that they arrive reliably and on time, not that they arrive in bulk. For its intended purpose, CAN remains excellent, and even the newest cars still use it for exactly this kind of low-level, must-not-fail control traffic.

The trouble is that a modern car is no longer only moving small messages. It is drowning in *data*. A ring of cameras watching the road produces a torrent of high-definition video. The self-driving computer must be fed that video in real time. Digital audio streams to every speaker; microphones stream back for noise cancellation; screens want high-resolution graphics; the car uploads and downloads great gulps of information. These are not tiny control signals; they are fire-hoses of data, and pushing them through a one-megabit party line is like trying to broadcast television down a telegraph wire. It simply cannot carry the volume.

For a while, carmakers coped by adding *more* buses — splitting the traffic across a powertrain CAN, a body CAN, a chassis CAN, and so on, until a complex car might have more than ten separate CAN networks, each handling its own district. But this is a patch, not a cure. It multiplies wiring — the very thing the last section was trying to reduce — and it does nothing to solve the fundamental ceiling: no matter how many one-megabit buses you add, none of them can carry a stream of camera video, because that stream needs far more bandwidth than any single CAN bus can provide. The party line is fine for a hundred short conversations; it cannot carry one enormous one.

So the industry has arrived at a familiar crossroads. CAN is not going away — for the low-level control traffic it was born to carry, it is still the right tool, and it will keep doing that job in the "nerve endings" of the car for a long time yet. But for the *backbone* — the high-volume trunk lines that must move video, coordinate the central computers, and carry the flood of data a software-defined car generates — something with vastly more capacity is needed. That something is automotive Ethernet: the same fundamental technology that networks the computers in an office, adapted for the car, offering hundreds or thousands of megabits per second and, crucially, a design where every connection can run at full speed rather than sharing one crowded line.

The move from CAN to Ethernet as the car's backbone is one of the quiet architectural shifts of this decade, and Tesla has pushed it about as far as anyone. In the Cybertruck it took the idea to an unusual and rather beautiful extreme — a single Ethernet loop carrying not just data but power, threaded around the whole car. That is the subject of the next section, and it is where the nervous system stops being a bundle of legacy wiring and becomes something genuinely new.

---

**Sources**

- CSS Electronics, Keysight, Copperhill, Excelfore, Electronic Design — CAN bus origin (Bosch, 1986), two-wire shared-bus topology, priority arbitration, robustness; ~1 Mbit/s (CAN FD/XL a few–tens of Mbit/s).
- Same sources — CAN's bandwidth ceiling versus ADAS/camera/infotainment data needs; proliferation of 10+ CAN buses per car; automotive Ethernet (100 Mbit/s+) replacing CAN as the backbone while CAN persists for low-level control.
- Ethernet-loop (Etherloop) extension developed in 10.3.
