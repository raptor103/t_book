## 20.5 Vertical integration

Most carmakers are, at heart, assemblers. They design a car and then buy the pieces — the seats from one supplier, the chips from another, the battery cells from a third, the software from a fourth — and their factories exist mainly to bolt these bought-in parts together. It is an efficient division of labour, and it worked for a century. Tesla broke with it, choosing instead to make an unusually large share of its own car in-house: the battery cells, the motors, the power electronics, the seats, the giant castings, the chips that run the self-driving system, the software from top to bottom, and — reaching all the way back up the supply chain — even the refining of the lithium that goes into the cells. This is *vertical integration*, and it is the strategy that quietly underpins everything else in this part.

Why would a company take on so much? Buying parts from specialists is usually cheaper and simpler, so making them yourself needs a strong reason. Tesla's reasons are several, and they compound.

The first is *cost and control at the parts that matter*. The battery is the most expensive component in an electric car, so controlling its production means controlling the car's single biggest cost, and being able to push that cost down and its quality up directly, rather than negotiating with a supplier who has their own margins to protect. Own the expensive, critical thing, and you own the economics of the whole car.

The second is *speed of innovation*, and this is subtler. When you make the cells, the castings, the chips and the software yourself, you can design them *together* — co-optimising the battery for the car, the car for the factory, the software for the chip. Every integrated marvel in this book depended on exactly this. The structural pack works because Tesla controls both the cells and the body. The custom self-driving chip works because Tesla writes the software that runs on it and designs the chip for that software. You cannot deeply integrate components you buy as sealed boxes from separate suppliers; integration requires ownership. The whole design philosophy of this book — delete parts, merge functions, co-design everything — is only *possible* for a company that makes the parts it is merging.

Why make it yourself:

```
   ASSEMBLER                     VERTICALLY INTEGRATED
   (buy the parts)               (make the parts)
   ------------------------------------------------------------
   design the car, buy the       make the cells, motors,
   pieces, bolt them together    chips, software, castings --
                                 even refine the lithium

   cheaper per part, and         controls the cost of the
   far simpler to run            biggest components

   BUT cannot deeply co-design,  CAN co-design everything
   and is bound by suppliers'    together, and adapt fast
   limits and priorities         when the world breaks
   ------------------------------------------------------------

   The integration described all through this book is only
   available to a company that owns the pieces it is fusing.
```

The third reason is *resilience*, and it was proven dramatically in the semiconductor shortage that paralysed the car industry in the early 2020s. When the chips that carmakers depended on suddenly became unavailable, most manufacturers simply stopped — they could not build cars without parts they did not control and could not substitute. Tesla, because it wrote its own software, could rewrite that software to work with *different*, available chips, and keep building. That is the deep payoff of owning your capabilities: when you control something, you can *adapt* it when the world changes; when you merely buy it, your ability to adapt is bounded by your supplier's capacity, priorities, and problems. Vertical integration trades some everyday efficiency for the ability to bend rather than break when things go wrong.

This book insists on the costs, and vertical integration has real ones. It is enormously capital-hungry — building your own cell factories, chip designs, casting machines and refineries costs staggering sums, and ties up money that an assembler would leave to suppliers. It is risky: do it badly and you have simply become a worse version of the specialist you could have bought from, and Tesla's own history is littered with in-house efforts that were painful, delayed, or abandoned. And it sacrifices the flexibility of being able to switch suppliers when a better or cheaper part appears. It is not obviously the right strategy for everyone, and much of the industry has deliberately not followed Tesla down this road.

But for understanding *how a Tesla works*, vertical integration is the keystone, because it is what makes the integrated design possible in the first place. Every chapter of this book has described a car in which the usual boundaries between components are dissolved — battery into structure, functions into single boxes, hardware co-designed with software, the car co-designed with its factory. That kind of integration is not a styling choice; it is only available to a company that controls the pieces it is fusing. The reason a Tesla can be built the way it is built is that Tesla makes, to an unusual degree, the things it is building with. The factory is the product, the components are the factory's, and the whole is designed as one — which is the note on which the making of the car can rest, and the book can turn, finally, to what happens when a car so tightly integrated reaches the end of its life.

---

**Sources**

- FourWeekMBA, Logistics Viewpoints, Supplychain360, dtadetayo (Medium) — Tesla's vertical integration: in-house cells, motors, seats, chips, software, castings, and lithium refining; rationale of cost control, quality, innovation speed, and resilience.
- Same sources — the chip-shortage example: Tesla rewriting firmware to use alternative chips because it controlled its own software; resilience-over-margin argument.
- The link between ownership and deep co-design synthesises this part with the integrated designs throughout the book (structural pack, custom FSD chip, PCS, octovalve); repairability/end-of-life consequences developed in Chapter 21.
