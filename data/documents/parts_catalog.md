# Parts Catalog — Common Replacement Parts

## How Real Part Numbers & Fitment Work
Real-world parts lookup is VIN-based: a vehicle's 17-character Vehicle
Identification Number encodes the model year, assembly plant, body
style, engine size, transmission type, and factory-installed options —
all of which affect exactly which part fits. Two trims of the same
model and year (e.g. a base engine vs. a larger optional engine) can
require completely different parts, so professional catalogs decode the
VIN rather than relying on year/make/model alone. Platforms differ in
how they use it: some (e.g. NAPA Online, OEM dealer parts sites)
support full VIN-based lookup for both OEM and aftermarket parts; others
rely on manual year/make/model/engine selection instead. When VIN lookup
isn't available, a technician can fall back to the part's own casting
number, an OEM label, or the vehicle's emissions decal (which lists
engine displacement, calibration code, and sometimes spark plug type).
Cross-referencing the OEM part number against aftermarket equivalents is
the standard way to confirm a correct substitute. Because of this,
**professionally you should always confirm fitment by VIN or by the
old part's own casting/OEM number — never by year/make/model alone.**

Real manufacturer part numbers and cross-references live behind
commercial parts-catalog databases (e.g. RockAuto, NAPA, dealer parts
systems, or industry data providers like Epicor and Hollander) that
aren't freely redistributable in bulk. **The table below is therefore an
illustrative example catalog for this project's demo RAG system, not
real manufacturer part numbers** — the part *categories*, typical
compatibility notes, and the general shape of a parts catalog are
realistic, but the specific example part numbers are placeholders
invented for this dataset.

## Brakes

| Part | Example Part No. | Fits (example) | Notes |
|---|---|---|---|
| Front brake pad set (ceramic) | BP-CER-1042 | Sedan compact class, 2015–2022 | Includes wear sensor clip |
| Front brake pad set (semi-metallic) | BP-SM-1042 | Sedan compact class, 2015–2022 | Higher noise, better heat resistance |
| Rear brake pad set | BP-CER-2087 | Sedan compact class, 2015–2022 | |
| Front rotor (vented) | RT-V-3305 | Sedan compact class, 2015–2022 | 280 mm diameter |
| Rear rotor (solid) | RT-S-3306 | Sedan compact class, 2015–2022 | 262 mm diameter |
| Brake caliper (front, left) | CAL-FL-4410 | Sedan compact class, 2015–2022 | Remanufactured option available |
| Brake fluid DOT 4 (1L) | FLD-DOT4-01 | Universal | |

## Ignition & Engine

| Part | Example Part No. | Fits (example) | Notes |
|---|---|---|---|
| Iridium spark plug | SP-IR-5521 | 4-cyl 1.6–2.0L gasoline engines | Gap: 0.7 mm pre-set |
| Ignition coil pack | IGN-COIL-6630 | 4-cyl 1.6–2.0L gasoline engines | One per cylinder |
| Engine air filter | AF-PANEL-7710 | Sedan compact class, 2015–2022 | Replace every 20,000–30,000 km |
| Cabin air filter | AF-CABIN-7711 | Sedan compact class, 2015–2022 | Replace every 15,000–20,000 km |
| Oil filter (spin-on) | OF-SPIN-7712 | 4-cyl gasoline engines | |
| Fuel filter (in-tank) | FF-TANK-7810 | Sedan compact class, 2015–2022 | Sold with fuel pump assembly |
| Thermostat (88°C) | THM-88-8801 | 4-cyl gasoline engines | |
| Timing belt kit | TB-KIT-8905 | 4-cyl 1.6–2.0L (belt-driven cam) | Includes tensioner and idler |

## Sensors

| Part | Example Part No. | Fits (example) | Notes |
|---|---|---|---|
| Mass airflow sensor (MAF) | MAF-9010 | 4-cyl 1.6–2.0L gasoline engines | |
| Oxygen sensor (upstream) | O2-US-9111 | 4-cyl gasoline engines | 4-wire heated type |
| Oxygen sensor (downstream) | O2-DS-9112 | 4-cyl gasoline engines | 4-wire heated type |
| Vehicle speed sensor | VSS-9220 | Sedan compact class, 2010–2020 | |
| Wheel speed sensor (front) | WSS-F-9330 | Sedan compact class, 2015–2022 | |
| Coolant temperature sensor | CTS-9410 | 4-cyl gasoline engines | |

## Electrical

| Part | Example Part No. | Fits (example) | Notes |
|---|---|---|---|
| Starter motor | STR-1120 | 4-cyl gasoline engines | Reman/new options |
| Alternator (120A) | ALT-120A-1220 | 4-cyl gasoline engines | |
| Battery (Group 35, AGM) | BAT-AGM-35-1310 | Sedan compact/mid-size | 650 CCA |
| Battery (Group 35, flooded) | BAT-FLD-35-1311 | Sedan compact/mid-size | 600 CCA |

## Tires & Wheels

| Part | Example Part No. | Fits (example) | Notes |
|---|---|---|---|
| All-season tire 205/55R16 | TIRE-205-55-16 | Sedan compact class | |
| Wheel lug nut (M12x1.5) | LUG-M12-1410 | Most sedans/hatchbacks | Sold individually |
| TPMS sensor | TPMS-1510 | 2012 and newer | Requires relearn procedure |

## OEM vs. Aftermarket
Aftermarket parts are made by a third-party manufacturer with no direct
connection to the vehicle's original manufacturer beyond a licensing
agreement, and they're often cheaper than OEM — though a lower price
doesn't automatically mean lower quality. As a rule of thumb, stick with
OEM for safety-critical systems (airbags, ABS modules) and powertrain
components (timing belts, fuel pumps), and consider aftermarket for
lower-stakes wear items (air filters, wiper blades, some suspension
bushings) where cost savings are less likely to matter.

## Ordering Notes
- Always confirm compatibility using the vehicle's VIN, not just the
  general "fits" description, since trim-level and engine variants change
  part numbers.
- If VIN lookup isn't available, the old part's casting number or the
  vehicle's emissions decal can serve as a fallback identifier.
- Remanufactured parts (calipers, alternators, starters) typically carry a
  core charge, refunded when the old part is returned.
- Wear parts (pads, filters) should be checked against the maintenance
  schedule interval, not only replaced on failure.

## Sources
The illustrative table above uses invented example part numbers built
for this project (see note above); the "How Real Part Numbers & Fitment
Work" and "OEM vs. Aftermarket" sections paraphrase and organize
information from the following real, publicly available references:
- CounterMan Magazine — [Tech Talk: VIN Look Up — Decoding Parts Sales](https://www.counterman.com/tech-talk-vin-look-up-151-decoding-parts-sales/)
- ScrapCarComparison — [How to Find OEM Car Part Numbers](https://www.scrapcarcomparison.co.uk/blog/how-to-find-oem-car-part-numbers/)
