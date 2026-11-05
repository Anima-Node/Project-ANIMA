# Project ANIMA: System Glossary & Lexicon

This living document defines the core technical vocabulary, acronyms, and hardware concepts used across the Project ANIMA ecosystem. It ensures absolute alignment between software developers, hardware engineers, industrial designers, and community creators.

---

## 🔌 Hardware & Electrical Engineering Terms

* **ADC (Analog-to-Digital Converter):** A hardware peripheral inside the ESP32-C3 SoC that translates variable analog voltage levels into digital numbers. In Project ANIMA, the ADC samples the voltage signature on Pad 3 (`SKIN_ID`) to instantly index and identify the attached Smart Skin archetype.
* **Base Core:** The standardized, pocket-sized 30 mm × 40 mm × 6 mm electronic "pod" containing the ESP32-C3 SoC, NAND Flash array, and LiPo battery. It serves as the universal open-source processor for the ecosystem.
* **BMS (Battery Management System):** The micro-circuitry responsible for safely charging the internal 3.7V 150mAh LiPo battery, protecting it from overcharging, deep discharge, and short circuits while managing power delivery down the USB-C rail.
* **ESD Protection (Electrostatic Discharge):** Transient Voltage Suppression (TVS) diode arrays placed near exposed copper pads to absorb static electricity shocks from human interaction, redirecting high-voltage spikes safely to the ground plane before they reach sensitive microchips.
* **PCB (Printed Circuit Board):** The structural 4-layer FR4 substrate that mechanically supports and electrically connects all electronic components using etched copper trace pathways.
* **Pogo Pads:** The six flush, gold-plated mechanical contact interface boundaries located on the underside of the Base Core chassis. They establish a temporary, reliable electrical connection to a Smart Skin via spring-loaded pins.
* **Smart Skin:** Custom-molded, user-fabricated external peripheral shells (such as the *Nimbus* cloud or *Grave-Digga* skull) that dock with the Base Core to translate mathematical personality vector matches into localized physical light, sound, and touch feedback loops.
* **SMD (Surface Mount Device):** Micro-electronic components designed to be soldered directly onto the outer surface planes of a PCB rather than through drilled holes, allowing our core hardware thickness to remain strictly under 6 mm.

---

## 💻 Firmware, Cryptography & Math Terms

* **CERN-OHL-W (CERN Open Hardware Licence - Weakly Reciprocal):** The governance framework protecting the physical hardware designs of Project ANIMA. It ensures blueprints remain public, allowing anyone to modify them, while requiring all derivative layout improvements to be openly published to protect against predatory patenting.
* **Ephemeral Token (`eID`):** A temporary, rotating digital signature broadcast over BLE by the Hub. Because it automatically changes in volatile RAM every 15 minutes, it acts as an anti-tracking safeguard, preventing stationary Bluetooth sniffers from mapping user movements.
* **ESP-IDF (Espressif IoT Development Framework):** The official, low-level professional C/C++ development workspace environment optimized for writing high-performance firmware, aggressive deep-sleep configurations, and register-level operations on the ESP32-C3 chip.
* **Human Manifest Schema:** The compiled, standardized 10-byte integer array output generated on-device based on the 10-Question Trial Schema. It acts as an offline, cross-compatible personality matrix profile.
* **Quantization:** The optimization process of shrinking a massive Artificial Intelligence model's mathematical weights (e.g., compressing an 8-billion parameter LLM down to 4-bit configurations) so it can run entirely offline on low-cost edge nodes like a Raspberry Pi.
* **Venue Hub:** High-performance, offline single-board computer gateway installations placed in physical third-spaces. They use `llama.cpp` to run local AI inference pipelines and directly drive 58mm TTL ESC/POS thermal receipt printers on verified match milestones.
* **Venue Salt ($\text{VenueSalt}_{24h}$):** Random cryptographic data updated at 00:00 UTC daily across local nodes. It adds dynamic entropy to validation strings, preventing malicious actors from pre-calculating or spoofing interaction inputs to game the local reward system.
* **Vector Dot-Product Engine:** The mathematical calculation method ($\text{Score} = \sum A_i \cdot B_i$) executed entirely on-chip within the ESP32-C3’s secure memory partition. It multiplies overlapping components of two intersecting profile arrays over a line-of-sight IR blast to calculate compatibility percentages without transmitting raw text answers.

---

## 📝 How to Add Terms to This Glossary

We encourage all contributors to help preserve the accessibility of this project. If you introduce a complex acronym, unique peripheral component, or technical calculation layer inside an active Pull Request, you are required to update this ledger:

1. Locate the correct categorical section matching your term.
2. Format the term using a bullet point, bold text, and a concise, beginner-accessible description:
   * **TERM (Acronym):** Clear, educational definition.
3. Submit the addition as part of your feature branch Pull Request for maintainer review and repository merging.
