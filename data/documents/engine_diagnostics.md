# Engine Diagnostics Guide

## Warning Signs and Their Meaning

### Check Engine Light (Steady)
Indicates a stored emissions- or performance-related fault that is not
immediately dangerous to keep driving with, but should be diagnosed soon.
Retrieve the code with a scan tool as the first step.

### Check Engine Light (Flashing)
Indicates an active, severe misfire that can damage the catalytic
converter within minutes of continued driving. Reduce load and have the
vehicle inspected immediately.

### Oil Pressure Warning Light
Indicates insufficient oil pressure. Stop the engine as soon as it is safe
to do so — continuing to run a low-oil-pressure engine can cause bearing
damage within seconds. Check oil level first; if the level is correct, the
oil pump, pressure sensor, or bearings may be at fault.

### Temperature Warning Light / Gauge in Red
Indicates engine overheating. Common causes: low coolant, failed
thermostat, failed water pump, radiator fan not engaging, head gasket
failure. Pull over and let the engine cool before checking coolant level;
never open a hot radiator cap.

## "Won't Crank" vs. "Cranks but Won't Start"
These are two different problems with mostly different causes, so it's
worth identifying which one you actually have before diagnosing further.

### Engine Won't Crank at All (or cranks very slowly)
A dead or weak battery is the single most common reason a car won't
crank. If you turn the key and get a single click with no crank, that
often points to the starter solenoid; a rapid repeated clicking is more
often a weak battery that can't supply enough current. Very slow cranking
is also common in cold weather, where low temperatures stiffen engine
components and drop battery voltage. If the dashboard lights stay bright
and you get a single click, suspect the starter specifically rather than
the battery.
| Possible Cause | How to Confirm |
|---|---|
| Dead/weak battery | Load test the battery; jump-start test |
| Faulty starter motor | Voltage drop test across starter; grinding noise on crank attempt |
| Bad starter relay/solenoid | Listen for the click, test the relay |
| Blown fuse in starting circuit | Check the fuse box |
| Jammed/broken ignition switch | Dash lights work but nothing happens at the key/button |

**Quick field test:** jump-start the vehicle from a known-good battery.
If it won't start at all, suspect the starter. If it starts but dies the
moment the jumper cables are removed, suspect the alternator (it isn't
sustaining the electrical load). If it starts and keeps running
normally, the original battery was likely the problem.

### Engine Cranks but Won't Start
If the engine turns over normally but doesn't fire, the fault is almost
always spark, fuel, or timing related — since cranking itself confirms
the battery and starter are basically functional.
| Possible Cause | How to Confirm |
|---|---|
| No spark | Spark tester on a plug wire/coil |
| No fuel delivery | Listen for the fuel pump prime at key-on, check fuel pressure |
| Failed crankshaft position sensor | Often causes an intermittent or heat-soaked no-start with no stored code; check for wiring damage near the sensor |
| Timing belt/chain failure | Check cam/crank sync, compression test |
| Blown fuse (EFI/ignition relay) | Check fuses and relays before assuming a sensor or wiring fault |
| Immobilizer fault | Check for a security light, scan for codes |

**Diagnostic order:** check fuses and relays first (fast and cheap to
rule out), then confirm spark and fuel delivery separately — a no-start
with both missing at once often points to a shared relay or wiring fault
rather than two coincidental part failures.

## Common Symptom-to-Cause Tables

### Rough Idle
| Possible Cause | How to Confirm |
|---|---|
| Vacuum leak | Smoke test, listen for hissing |
| Dirty throttle body | Visual inspection, idle relearn after cleaning |
| Worn spark plugs | Inspect electrode gap and condition |
| Failing idle air control valve | Monitor idle RPM in scan tool live data |

### Loss of Power / Hesitation on Acceleration
| Possible Cause | How to Confirm |
|---|---|
| Clogged fuel filter | Check fuel pressure under load |
| Failing fuel pump | Compare fuel pressure at idle vs. under load |
| Clogged air filter | Visual inspection |
| Faulty MAF or MAP sensor | Compare live data to expected values |
| Restricted catalytic converter | Backpressure test |

## Compression Testing
A dry compression test measures the sealing ability of each cylinder.
Typical healthy readings are within 10% of each other across all
cylinders and meet the manufacturer's minimum spec (commonly 120–180 psi
depending on engine design). A cylinder reading significantly lower than
the others suggests a worn ring, valve, or head gasket problem. A wet
test (adding a small amount of oil to the cylinder) that raises the
reading points to worn piston rings; no change points toward valve or
head gasket issues.

## Routine Diagnostic Tools
- OBD-II scan tool (code reading + live data)
- Multimeter (voltage, resistance, continuity)
- Fuel pressure gauge
- Compression tester
- Smoke machine (vacuum/EVAP leak detection)
- Timing light (on older non-coil-on-plug systems)

## Sources
This document paraphrases and organizes information from the following
real, publicly available references (consulted for accuracy, not quoted
verbatim):
- AutoZone — [Why Won't My Car Start?](https://www.autozone.com/diy/engine/why-wont-my-car-start)
- YourMechanic — [Engine cranks but won't start (Q&A)](https://www.yourmechanic.com/question/engine-cranks-but-won-t-start-by-robert-h)
- YourMechanic — [Crank but no start: No spark or fuel](https://www.yourmechanic.com/question/crank-but-no-start-no-spark-or-fuel-all-quit-at-the-same-time-by-ron-r)
- YourMechanic — [Engine cranks, ignition is slow, and car won't start](https://www.yourmechanic.com/question/engine-cranks-ignition-is-slow-and-car-won-t-start)
