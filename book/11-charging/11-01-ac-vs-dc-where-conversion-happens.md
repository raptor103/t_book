## 11.1 AC vs. DC — where the conversion happens

Here is the one idea that unlocks the entire subject of charging, and it is worth reading twice because everything else in this chapter hangs from it. The electricity in the wall — indeed, in the entire grid — is *alternating* current, AC, the kind that surges back and forth. The electricity a battery can store is *direct* current, DC, the steady one-directional kind from Chapter 2. So charging an electric car *always*, without exception, involves converting AC into DC somewhere between the grid and the battery. The only question — and it is the question that separates a trickle from a torrent — is **where that conversion happens.**

There are exactly two possible answers, and they correspond to the two worlds of charging that so confuse newcomers.

The first answer: the conversion happens *inside the car*. When you plug into an ordinary home socket or a public "AC" charging point, what arrives at the car is raw grid AC. The car then converts it to DC itself, using the onboard charger we met in Chapter 8 — that half of the PCS box whose job is exactly this. The wall simply hands the car alternating current; the car does the rest. This is often called Level 2 charging, and it is what you use overnight at home or topping up at a car park. Its speed is limited by the size of the converter the car can reasonably carry: a Model 3's onboard charger handles somewhere around 7 to 11 kilowatts, enough to refill the battery comfortably over a night's sleep, but no faster.

The second answer: the conversion happens *outside the car*, in the charging station. A DC fast charger — a Supercharger is one — is a large, heavy, powerfully-cooled cabinet that contains its own enormous AC-to-DC converter. It does the conversion itself and sends *DC straight into the car's battery*, bypassing the little onboard charger entirely. Because the converter now lives in a big roadside cabinet with no weight or size limit and proper cooling, it can be vastly more powerful than anything a car could carry — pushing hundreds of amps at hundreds of volts, delivering ten, twenty, thirty times the power of home charging, and refilling a battery in the time it takes to drink a coffee.

The whole distinction, in one picture:

```
   AC CHARGING (home / destination)
     grid AC --> [ car's onboard charger does AC->DC ] --> battery
     conversion is INSIDE the car -> limited by what the car
     can carry -> ~7-11 kW -> hours

   DC FAST CHARGING (Supercharger)
     grid AC --> [ big roadside cabinet does AC->DC ] --> battery
     conversion is OUTSIDE the car -> no size limit, well cooled
     -> hundreds of kW -> minutes
```

That is the whole thing. Slow charging and fast charging are not two different technologies so much as two different *places* to put the same converter — in the car, where it must be small and light, or in a roadside cabinet, where it can be enormous. Every other difference follows from this one. The home charger is cheap and can be anywhere there is a socket, because the expensive converting hardware is the modest one you carry with you. The fast charger is costly and lives only at dedicated stations, because the expensive converting hardware is the giant one bolted to the ground — but you get to *share* that giant with every other car that visits, which is what makes it economic.

It also explains a common source of confusion: the numbers. A home AC charger might be rated at 7 or 11 kilowatts; a fast DC charger at 150 or 250. People assume the car is somehow "accepting" charging differently, but the bottleneck in the two cases sits in completely different places. On AC, the limit is the little converter *in the car*. On DC, the car's own converter is out of the loop entirely, and the limits become the charger's power, the cables, and — as the third section will explain — the battery's own willingness to be filled quickly, which changes as it fills.

So whenever you approach any charger, anywhere in the world, you can ask the one clarifying question and know immediately what you are dealing with. *Where does this conversion happen — in my car, or in that cabinet?* If it happens in your car, you are AC charging, and the speed is set by what you carry. If it happens in the cabinet, you are DC charging, and the speed can be enormous. Two answers to one question, and the fog begins to lift. The next section looks more closely at the two devices this distinction creates — the modest charger you carry and the mighty one you visit — and why the car cannot simply carry the mighty one everywhere.

---

**Sources**

- ChargePoint, Wevolver, Ekoenergetyka, evbattery.us — grid is AC, batteries store DC; AC (Level 2) charging converts inside the vehicle via the onboard charger (~7.2–19.2 kW); DC fast charging converts in the station and bypasses the onboard charger, delivering far higher power.
- Onboard-charger figures for the Model 3 (~7.7–11.5 kW) from Chapter 8 sources; the shared-cabinet economics and battery-side limits are developed in 11.2 and 11.3.
