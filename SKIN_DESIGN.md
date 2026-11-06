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


### 1. The "Burl & Brass" (Steampunk Botanist ID | ID: 1.0 kΩ)
*   **Material Aesthetic:** Reclaimed walnut timber shell accented with raw knurled brass structural gears and an external glass-encased vintage vacuum tube assembly.
*   **Peripheral Actuators:** Driven by a miniature internal 5V micro-stepper motor linked to the gear train and a high-intensity warm orange filament LED running up the center of the vacuum tube.
*   **Low Match State:** The filament LED flashes fitfully at long, irregular intervals; the stepper motor remains completely unpowered to keep the gears locked.
*   **High Match State:** Activates an amber strobe light sequence inside the vacuum tube while the micro-stepper motor drives the gear array into a steady rotation, accompanied by a looping mechanical clockwork arpeggio generated via the `AUDIO_PWM` line.

### 2. The "Mud-Frog" (Wetland Organic ID | ID: 2.2 kΩ)
*   **Material Aesthetic:** Flexible, squishy matte-green vulcanised silicone housing with a rough texture, featuring integrated low-resolution monochrome pixel-art frog design elements.
*   **Peripheral Actuators:** Houses a high-mass Eccentric Rotating Mass (ERM) haptic vibration motor alongside a rugged, low-frequency 20mm resonant piezoelectric buzzer element.
*   **Low Match State:** The buzzer emits a slow, deep acoustic croaking pattern while the ERM motor delivers a single shuddering vibration pulse every 6 seconds.
*   **High Match State:** The ERM motor switches to a high-frequency skittering vibration pattern, accompanied by a rapid, high-pitched digital chirp audio sequence looping continuously over the speaker rail.

### 3. The "Grave-Digga" (Gothic Skeptic ID | ID: 4.7 kΩ)
*   **Material Aesthetic:** Injection-moulded charcoal-grey polymer skull with deep, hollow mechanical eye sockets and a textured bone-ash matte surface finish.
*   **Peripheral Actuators:** Features two pinpoint crimson micro-LED elements aligned deep within the eye cavities and a bass-heavy dual-chamber acoustic piezo buzzer.
*   **Low Match State:** The crimson eye LEDs remain locked in a static, low-intensity state while the bass buzzer generates a continuous, low-frequency mechanical drone.
*   **High Match State:** The crimson LEDs are overridden by a rapid-fire white strobe light pulsing through the skull casing, while the buzzer launches into an upbeat, syncopated retro game victory melody.

### 4. The "Nimbus" (Fluffy Optimist ID | ID: 10.0 kΩ)
*   **Material Aesthetic:** Ultra-lightweight, needle-felted white merino wool cloud casing wrapped securely around an internal semi-rigid light-diffusing acrylic frame.
*   **Peripheral Actuators:** Contains an integrated flexible strip of 6 addressable RGB NeoPixels (`LED_DATA`) and a specialized bone-conduction flat audio transducer.
*   **Low Match State:** The internal NeoPixels shift into a dim, static deep purple hue while the transducer produces a soft, irregular digital static rumble.
*   **High Match State:** Loops a bright pastel rainbow cascade pattern moving across the NeoPixel array, paired with a sweeping, polyphonic chiptune chord sequence transmitted directly through the shell via the audio transducer.

### 5. The "Sub-Station" (Industrial Off-Grid ID | ID: 22.0 kΩ)
*   **Material Aesthetic:** High-impact, thick yellow industrial ABS plastic casing stencilled with high-contrast black hazard striping and textured non-slip grip steps.
*   **Peripheral Actuators:** Built with a precise Linear Resonant Actuator (LRA) haptic pulse motor and a front-facing, 8-segment green/red LED bar-graph display component.
*   **Low Match State:** The LED bar-graph zeroes out completely with only the single bottom red element blinking, while the haptic drive remains unpowered.
*   **High Match State:** Drives the LED bar-graph directly to maximum green illumination while the LRA motor transmits a heavy, structural rhythmic hum through the entire casing to simulate industrial machinery under load.

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