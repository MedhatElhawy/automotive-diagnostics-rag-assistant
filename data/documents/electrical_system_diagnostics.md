# Electrical System Diagnostics: Battery, Alternator, Starter

The battery, alternator, and starter work together but fail in
different, mostly distinguishable ways. The battery provides the initial
power to crank the engine and backs up the electrical system; the
alternator recharges the battery and powers accessories once the engine
is running; the starter motor physically turns the engine over for the
few seconds it takes to fire up. Because these systems are
interconnected, replacing the wrong part on a guess is a common source of
wasted money — proper testing matters more than intuition here.

## Battery
**Function:** Stores energy to start the engine and stabilizes voltage for
electronics when the engine is off or the alternator output is
insufficient.

**Common symptoms of a failing battery:**
- Failure to start at all — if you turn the key/press the button and
  nothing happens, the battery is a good first suspect.
- A clicking sound with no crank often signals a battery that's just
  about dead.
- Very slow cranking, especially in cold weather (low temperatures stiffen
  engine components and drop battery voltage at the same time).
- Battery warning light illuminated, or dashboard lights flickering when
  starting.
- Corrosion visible on the terminals.
- A car that won't start after sitting for a few days (parasitic drain or
  a battery near end of life).

**Diagnostic steps:**
1. Visually inspect terminals for corrosion; clean if present.
2. Measure resting voltage with a multimeter (should read roughly 12.6V
   with the engine off, fully charged).
3. Perform a load test; a battery that drops sharply under load likely
   needs replacement even if resting voltage looks normal. Many parts
   stores (e.g. AutoZone) offer free battery/alternator testing if you
   don't have your own tester.
4. Check the age — most batteries last roughly 3–5 years depending on
   climate and usage; heat shortens battery life more than cold does.

## Alternator
**Function:** Charges the battery and powers the electrical system while
the engine runs, converting the engine's mechanical energy into
electrical energy.

**Common symptoms of a failing alternator:**
- Battery warning light illuminated *while driving* (as opposed to only
  at startup).
- Dimming or flickering headlights/interior lights, especially at idle.
- Battery repeatedly dies despite being in good condition — a failing
  alternator can't keep it charged.
- On-board accessories (radio, power windows) working erratically or
  underpowered.
- Whining or growling noise from the alternator pulley/bearing.
- A car that stalls shortly after starting, or dies the moment jumper
  cables are removed after a jump-start.

**Diagnostic steps:**
1. Measure charging voltage at the battery with the engine running
   (typically ~13.5–14.8V; consult spec for the exact range).
2. Test under load (headlights, blower, rear defroster on) — voltage
   should not drop excessively.
3. Inspect the drive belt for wear, glazing, or slipping.
4. Listen for a whining or growling bearing noise, which tends to worsen
   as more accessories are used.

## Starter Motor
**Function:** Engages the flywheel to crank the engine at startup, drawing
power from the battery for the few seconds it operates.

**Common symptoms of a failing starter:**
- A single click with no crank (often the starter solenoid specifically,
  once the battery itself has been confirmed good).
- The engine cranks over slowly or not at all.
- Grinding noise when starting (worn starter drive gear or flywheel).
- Dashboard lights stay bright when you turn the key, but nothing else
  happens — this pattern points toward the starter rather than the
  battery, since a weak battery usually also dims the dash lights.

**Diagnostic steps:**
1. Confirm battery voltage and connections are good first — a weak
   battery is a far more common cause of a no-crank condition than a
   failed starter.
2. Perform a voltage drop test across the starter circuit while cranking.
3. Test the starter relay/solenoid by listening for and confirming the
   click, or bench-test the starter if removed.

## Quick Field Test: Battery vs. Alternator vs. Starter
Jump-start the vehicle from a known-good battery/jump box, then remove
the cables:
- **Doesn't start at all**, even with the jump → suspect the **starter**
  (no amount of charge helps if the starter itself can't turn the
  engine).
- **Starts, then dies** the moment the cables are removed → suspect the
  **alternator** (it isn't sustaining the electrical load on its own).
- **Starts and keeps running normally** → the original **battery** was
  likely the problem.

## Charging System Quick Reference

| Symptom | Likely Culprit |
|---|---|
| Battery light on while driving, voltage below spec | Alternator or belt |
| Battery light on, voltage reads normal | Faulty warning circuit/sensor |
| Dies overnight, charges fine when driven | Parasitic draw or an aging battery |
| Won't crank at all, dash lights dim severely | Weak/dead battery |
| Won't crank, dash lights stay bright, single click | Starter solenoid |
| Grinding noise on start attempt | Worn starter drive gear |
| Starts, dies immediately after jump-start cables removed | Alternator |

## Parasitic Draw Testing
A parasitic draw is current pulled from the battery when the vehicle is
off. Normal draw is typically under 50 mA. Testing involves placing a
multimeter in series with the negative battery terminal after allowing
modules to enter sleep mode (often 20–40 minutes after the last door
close), then pulling fuses one at a time to isolate the offending
circuit.

## Sources
This document paraphrases and organizes information from the following
real, publicly available references (consulted for accuracy, not quoted
verbatim):
- AutoZone — [Battery vs. Alternator: Which Is the Problem?](https://www.autozone.com/diy/battery/battery-vs-alternator-which-is-the-problem)
- AutoZone — [Signs of a Bad Battery vs. Bad Alternator](https://www.autozone.com/diy/battery/bad-battery-vs-bad-alternator)
- AutoZone — [Alternator vs Starter](https://www.autozone.com/diy/alternator/alternator-vs-starter)
- Tires Plus — [How to Tell if Battery, Alternator, or Starter is Bad](https://www.tiresplus.com/blog/maintenance/starter-battery-or-alternator/)
- AAA — [8 Signs Of A Bad Alternator Vs Bad Battery](https://cluballiance.aaa.com/the-extra-mile/articles/prepare/car/bad-alternator-vs-bad-battery)
