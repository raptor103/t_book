## 3.4 Degradation, and why charging advice differs by chemistry

Every battery is dying from the moment it is made, and there is nothing to be done about it except slow it down. This sounds gloomy, and owners often find it faintly alarming, so it is worth saying clearly at the outset: modern car batteries die *very* slowly — most will still hold the large majority of their original capacity after more than a decade — and the whole point of understanding how they age is that the aging is partly in your hands. The advice printed in the owner's manual, the numbers on the charging screen, the folklore traded at charging stations: nearly all of it is downstream of two simple mechanisms, and once you know them, the advice stops being arbitrary and starts being obvious.

Batteries age in two ways at once, and engineers give them two names. The first is *cycle aging* — the wear from actually using the battery, from each charge and discharge. Every time lithium ions shuttle in and out of those crystal shelves from Chapter 2, they do a little violence: the lattice swells and shrinks, tiny cracks form, and a microscopic amount of lithium gets permanently trapped and taken out of circulation. Do this a few thousand times and the losses add up. The second is *calendar aging* — the wear from merely existing, from time itself, whether the battery is used or not. Sitting on a shelf, a lithium cell slowly corrodes itself: a thin, self-made film called the SEI, the solid-electrolyte interphase, keeps very gradually thickening on the anode, consuming a little lithium as it grows. A battery locked in a garage for a year and never touched will still have aged.

Here is the crucial part, the part that turns theory into advice: both kinds of aging are made dramatically worse by two conditions — *heat* and *a high state of charge*. Heat speeds up most chemical reactions, including the destructive ones, which is one more reason the thermal system in Part IV matters so much. And a battery held at or near 100 percent full sits under a kind of chemical tension — the electrodes are at their most reactive, and the self-corroding SEI reaction runs faster. The research is stark: a nickel cell left resting at 100 percent charge can lose capacity several times faster than one kept nearer the middle, and warmth compounds it savagely. In one study a cell held full at 40 degrees degraded to worn-out in a fraction of the time it took at ordinary temperature.

That single fact — that the top of the charge range is where the damage concentrates — is the whole reason behind the famous advice to charge a nickel-chemistry car to only about 80 percent for everyday use, and to fill it to 100 only when you genuinely need the range and preferably just before you set off. You are not "wasting" the top twenty percent. You are declining to store your battery in its most stressful state.

And now the chemistry from Chapter 2 pays off, because this is exactly where LFP and nickel part company. The advice differs by chemistry because the *physics* differs by chemistry. LFP's cathode is built around an extraordinarily stable phosphate structure — the bond holding it together is so strong that sitting at 100 percent charge simply does not stress an LFP cell the way it stresses a nickel one. So LFP cars are not only permitted but positively encouraged to charge to 100 percent regularly — partly because it is harmless, and partly for a practical second reason: LFP's flat voltage makes it hard for the BMS to estimate state of charge accurately, and an occasional trip to a known, definite 100 percent lets the supervisor from the last section recalibrate its gauge.

The two rules of thumb, and why:

```

                        NICKEL (NMC / NCA)       LFP
   ----------------------------------------------------------------------

    daily charge to     about 80%                100%, routinely

    charge to 100%      before a long trip       any time you like

    why                 the top 20% causes       the phosphate cathode
                        most of the aging        shrugs a full charge off

    bonus               --                       a full charge recalibrates
                                                 the BMS gauge

   ----------------------------------------------------------------------

   Both chemistries dislike the same two things:
   heat, and being left sitting at 100% for weeks.
```

Two caveats keep this honest. First, even LFP would rather not be *parked* at 100 percent for weeks on end in the heat; charging to full is fine, marinating at full is not. Second, all of this is guidance about the margins. The difference between careful and careless charging is real, but it is measured in a few extra percent of capacity over many years, not in the survival of the battery. You will not destroy a modern EV battery by charging it wrong. You will, at most, slightly hasten a decline that is already slow.

Which is a fitting place to close the battery chapters. We began with a single cell storing energy as geography, and end with a half-ton structural machine that ages gracefully if treated with a little understanding. The energy is now stored, supervised, and built into the car. It is time to turn it into motion — and for that we need the strangest and most elegant device in the whole vehicle: the inverter.

---

**Sources**

- ScienceDirect and IOPscience — calendar vs cycle aging; SEI growth on the graphite anode; acceleration by high temperature and high state of charge.
- ECS webinar (Wittman & Preger) and Chargie degradation guide — nickel cells degrade ~20–30% faster held at 100% vs 80%; damage concentrated in the top of the SOC range; example of accelerated fade at 40 °C / 100% SOC.
- Eleport, Techflare, Sunrich Energy, Notebookcheck — LFP tolerance of routine 100% charging (strong P–O phosphate bond); 100% charge used to recalibrate LFP state-of-charge estimation; caution against prolonged storage at 100%.
