# OBD-II Diagnostic Trouble Codes (DTC) Reference

## Overview
On-Board Diagnostics II (OBD-II) is a standardized system used by all modern
vehicles (1996 and newer in the US) to monitor engine, transmission, and
emissions performance. When a fault is detected, the Engine Control Unit
(ECU) stores a Diagnostic Trouble Code (DTC) and illuminates the
Malfunction Indicator Lamp (MIL), commonly known as the "Check Engine"
light. DTCs are generated from data collected by the vehicle's onboard
diagnostics system and help identify which vehicle system has a problem
and roughly where it is located.

DTC format: a letter (P = Powertrain, B = Body, C = Chassis, U = Network)
followed by four digits. The first digit after the letter indicates whether
the code is generic (0) or manufacturer-specific (1).

## Common Powertrain Codes

### P0300 — Random/Multiple Cylinder Misfire Detected
P0300 means the computer detected a misfire that it cannot attribute to
one specific cylinder, typically because a cylinder fails to produce
power when combustion doesn't occur due to a lack of spark, fuel, or
compression. Related single-cylinder codes P0301–P0308 point to a
specific cylinder instead.
**Symptoms:** Rough idle, hesitation on acceleration, flashing check engine
light, reduced fuel economy, lack of acceleration.
**Common causes:** Worn spark plugs, ignition coils, or spark plug wires;
vacuum leaks; low fuel pressure; a rich or lean fuel mixture (often
alongside a related P0171/P0174 code); low compression.
**Diagnostic steps:** Scan for additional codes first (misfire codes
often appear alongside lean/rich codes), retrieve freeze-frame data,
visually inspect spark plugs/coils/wires for damage or wear, perform a
vacuum leak test with a smoke machine, check fuel pressure at the rail,
and reproduce the original operating conditions (temperature, load, RPM)
recorded with the code, since a fault that only shows up under specific
conditions can be missed otherwise.
**Typical fix:** Replace spark plugs/coils, repair the vacuum leak, or
correct the fuel trim issue causing the misfire.

### P0171 — System Too Lean (Bank 1)
P0171 means the engine is getting too much air relative to fuel on Bank 1
(Bank 2 on V6/V8 engines is P0174).
**Symptoms:** Rough idle, hesitation, reduced power, occasional stalling.
**Common causes:** A vacuum leak from a cracked or disconnected hose is
the most common cause; also a dirty mass airflow (MAF) sensor or a weak
fuel pump.
**Diagnostic steps:** Check fuel trims in live data, inspect intake boots
and vacuum lines, clean the MAF sensor with an appropriate cleaner, check
fuel pressure.
**Typical fix:** Repair the vacuum leak, clean/replace the MAF sensor, or
replace the fuel filter/pump if fuel delivery is insufficient.

### P0420 — Catalyst System Efficiency Below Threshold (Bank 1)
P0420 means the powertrain control module (PCM) found the catalytic
converter's efficiency below its programmed threshold on Bank 1 (P0430
is the Bank 2 equivalent); it does not by itself prove the converter is
the failed part.
**Symptoms:** Often no drivability symptoms; can trigger rough idle,
reduced performance, or lack of acceleration in some cases; failed
emissions test; occasionally a rotten-egg smell from the tailpipe.
**Common causes:** A genuinely degraded catalytic converter; but also
misfires (P0300 series) or a lean/rich condition (P0171/P0174 series)
that stresses a healthy converter until it reads as inefficient; an
exhaust leak near the oxygen sensors; a failing downstream O2 sensor.
**Diagnostic steps:** Resolve any active misfire or lean/rich condition
*first* — a converter can't be judged fairly while the engine is feeding
it the wrong air/fuel mixture. Then compare upstream vs. downstream O2
sensor waveforms on a scan tool and inspect the exhaust for leaks.
**Typical fix:** Replace the catalytic converter only after ruling out
misfires, sensor faults, and exhaust leaks as the root cause.

### P0128 — Coolant Thermostat Below Regulating Temperature
**Symptoms:** Poor fuel economy, cabin heater blowing cool air, slow warm-up.
**Common causes:** Thermostat stuck open, faulty coolant temperature
sensor.
**Diagnostic steps:** Monitor coolant temperature on a scan tool during a
drive cycle, compare to the expected warm-up curve.
**Typical fix:** Replace the thermostat.

### P0442 — Evaporative Emission Control System Leak Detected (Small Leak)
**Symptoms:** Check engine light only; usually no drivability impact.
**Common causes:** Loose or damaged fuel cap, cracked EVAP hose, faulty
purge valve.
**Diagnostic steps:** Check the fuel cap seal first, then smoke-test the
EVAP system to locate the leak.
**Typical fix:** Replace the fuel cap or repair the leaking hose/component.

### P0500 — Vehicle Speed Sensor Malfunction
**Symptoms:** Speedometer inaccuracy, erratic transmission shifting,
cruise control disabled.
**Common causes:** Faulty VSS, damaged wiring/connector, worn tone ring.
**Diagnostic steps:** Check VSS signal on a scan tool while driving,
inspect wiring for damage.
**Typical fix:** Replace the vehicle speed sensor or repair the wiring.

### P0700 — Transmission Control System Malfunction
This is a "pointer" code — the actual fault is stored in the
transmission control module (TCM) and requires a TCM-specific scan tool
to retrieve.
**Symptoms:** Harsh or delayed shifting, transmission in limp mode.
**Diagnostic steps:** Retrieve TCM-specific codes with a capable scan
tool.
**Typical fix:** Depends on the underlying TCM code.

## Body and Chassis Codes

### B0001 — Driver Frontal Stage 1 Deployment Control
Indicates an airbag deployment circuit fault; requires professional SRS
system diagnosis.

### C0035 — Left Front Wheel Speed Sensor Circuit
A common ABS-related code; check the wheel speed sensor and tone ring for
damage or debris.

## Diagnostic Workflow (General)
1. Retrieve all stored and pending codes with an OBD-II scan tool.
2. Record freeze-frame data for the first code that set.
3. Research the code, likely causes, and known technical service bulletins
   (TSBs) for the specific make/model/year.
4. Perform a visual inspection before replacing any parts.
5. Test components rather than assuming; many codes share overlapping
   causes, and misfire/lean codes should generally be resolved before
   chasing a P0420-style catalyst code that they can cause on their own.
6. Failing to reproduce the original temperature, load, and RPM
   conditions recorded with the code is a common reason a "fixed" fault
   returns.
7. Clear codes and perform a test drive to confirm the repair.

## Sources
This document paraphrases and organizes information from the following
real, publicly available references (consulted for accuracy, not quoted
verbatim):
- O'Reilly Auto Parts — [Check Engine Light Code P0300](https://www.oreillyauto.com/how-to-hub/check-engine-light-code-p0300-random-or-multiple-cylinder-misfire-detected)
- O'Reilly Auto Parts — [Check Engine Light DTC Code P0420 and P0430](https://www.oreillyauto.com/how-to-hub/check-engine-light-codes-p0420-and-p0430-catalyst-system-efficiency-below-threshold)
- Identifix — [P0300 Code: The Guide to Diagnostics and Repair](https://www.identifix.com/blogs/p0300-code-the-guide-to-diagnostics-and-repair/)
- Identifix — [P0420 Code: The Guide to Diagnosis and Fast Fixes](https://www.identifix.com/blogs/p0420-code-the-guide-to-diagnosis-and-fast-fixes/)
- checkenginelightexplained.com — [Common Check Engine Light Codes / Complete OBD-II Code Directory](https://checkenginelightexplained.com/codes/)
