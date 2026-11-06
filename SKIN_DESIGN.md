# Project ANIMA: Smart Skin Hardware & Peripheral Specifications v1.0

This specification serves as the primary engineering and design standard for Project ANIMA's modular peripheral ecosystem. It codifies the rigorous physical boundaries, electrical tolerances, and hardware execution states required for all snap-on "Smart Skins."

---

## 📐 Module 1: Physical Geometry & Mechanical Constraints

To guarantee universal cross-compatibility across all custom user-designed shells, every Smart Skin must structurally conform to the exact physical envelope of the Base Core.

```text
                 30 mm
         ┌─────────────────┐
         │  ┌───────────┐  │ ▲
         │  │           │  │ │
         │  │ Base Core │  │ │ 40 mm
         │  │  Vacated  │  │ │
         │  │  Chassis  │  │ │
         │  └───────────┘  │ ▼
         └────────┬────────┘
                  ▼ Keyring Loop Anchor
```

* **Internal Cavity Clearances:** The interior pocket of the skin must cleanly accept a 30 mm × 40 mm × 6 mm block with a tolerance window of +0.15 mm on the X and Y axes to prevent friction-jamming.
* **Mechanical Interlocking:** Structural retention is achieved via dual-sided physical guide rails running down the parallel edges of the Recycled Polycarbonate core casing. Skins must utilize negative indentations or pressure-fit detents to "click" and latch firmly into place.
* **Keyring Preservation:** The bottom 30 mm edge includes an integrated structural keyring loop anchor. The Smart Skin layout must feature a precise cutout profile to leave this loop fully exposed for functional deployment.

---

## ⚡ Module 2: Electrical Pin Diagnostics & Resistor Map

The Base Core reads an analog voltage profile on Pad 3 (`SKIN_ID`) to dynamically load peripheral firmware parameters. This setup bypasses expensive electronic handshakes, relying instead on low-cost internal resistors built into the skin shell.

| Skin Index Code | Target Resistor Value | Read Voltage Pool (At +3.3V Input) | Master Firmware Execution Index |
| :--- | :--- | :--- | :--- |
| **Skin 01** | 1.0 kΩ (±1%) | ~ 0.30 V - 0.35 V | `SKIN_PROFILE_BURL_BRASS` |
| **Skin 02** | 2.2 kΩ (±1%) | ~ 0.63 V - 0.69 V | `SKIN_PROFILE_MUD_FROG` |
| **Skin 03** | 4.7 kΩ (±1%) | ~ 1.15 V - 1.25 V | `SKIN_PROFILE_GRAVE_DIGGA` |
| **Skin 04** | 10.0 kΩ (±1%) | ~ 1.95 V - 2.05 V | `SKIN_PROFILE_NIMBUS` |
| **Skin 05** | 22.0 kΩ (±1%) | ~ 2.70 V - 2.85 V | `SKIN_PROFILE_SUB_STATION` |

---

## 🎨 Module 3: R&D Concept Lab — Advanced Peripheral Expansion

To build a diverse ecosystem, we need to push past our initial 5 configurations. Here are 3 brand new, distinct structural and aesthetic concept designs ready for open-source development.

### 1. The "Solar-Sailer" (Astro-Navigator ID | ID: 47 kΩ)
* **Material Aesthetic:** Clear frosted acrylic composite paired with lightweight, micro-thin flexible solar panel segments laminated along the top deck.
* **Peripheral Actuators:** Uses an ultra-thin electronic ink (E-ink) display panel driven by a shared data line, along with a low-current micro-magnetometer (compass).
* **Low Match State:** The E-ink panel shows a static, jagged broken line graph; an internal soft white LED stays dim.
* **High Match State:** The E-ink panel rapidly refreshes to display a sharp cosmic coordinate system. Concurrently, a subtle white ring array orbits smoothly underneath, mimicking a spinning radar line.

### 2. The "Foundry-Core" (Brutalist Cyberpunk ID | ID: 100 kΩ)
* **Material Aesthetic:** Heavy, raw cold-cast zinc alloy mixed with exposed copper trace routing wires weaving through a geometric grid chassis.
* **Peripheral Actuators:** Houses a dual-row red miniature LED ladder bar-graph display along with an array of three parallel Linear Resonant Actuators (LRAs) for nuanced physical thrumming.
* **Low Match State:** The bottom single indicator element blinks fitfully; a harsh, single jarring haptic pulse kicks in once every 4 seconds.
* **High Match State:** The twin LED bars charge rapidly to max value from bottom to top. The three internal LRA motors alternate operational cycles to transmit a deep, rhythmic heavy-machinery vibration.

### 3. The "Mycelium-Node" (Bio-Synthetic ID | ID: 220 kΩ)
* **Material Aesthetic:** Light, texturized shell grown organically out of an agricultural hemp-fiber mycelium matrix, featuring a raw, tactile surface feel.
* **Peripheral Actuators:** Uses multiple fiber-optic threads routed to diffuse deep, subterranean organic emerald green and warm mycelial white micro-LED glows, paired with a soft sub-audible physical transducer.
* **Low Match State:** Emits a faint, slow green organic breathing glow pattern; zero physical vibration output.
* **High Match State:** Fiber threads shift rapidly between vibrant green and amber pulses. The transducer introduces a soothing, deep low-frequency purr that makes the organic shell pulse comfortably in the user's hand.

---

## 🛠️ Module 4: Hardware Physical Validation Flowchart

Before any custom user-submitted skin profile can be officially merged into the main repository and assigned an active index ID, it must clear this safety engineering sequence:

1. **Pin Continuity Clearance:** Run a digital multimeter check across the contact pads. Verify there are no dead short circuits between Pad 1 (VCC) and Pad 2 (GND) to protect the internal LiPo cell from damage.
2. **Current Draw Evaluation:** Connect the system to an isolated workbench power supply set to 3.3 V. Trigger all onboard LEDs and haptic drives simultaneously; peak operational current draw must never exceed 45 mA to safeguard the battery.
3. **Voltage Signature Check:** Read the ADC voltage line output at Pad 3. Confirm that the voltage signature sits squarely within the targeted slot allocation boundaries without drifting into adjacent skin indices.