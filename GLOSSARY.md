# Project ANIMA: System Glossary & Lexicon

This living document defines the core technical vocabulary, acronyms, and hardware concepts used across the Project ANIMA ecosystem. It ensures alignment between software developers, hardware engineers, and designers.

---

## 🔌 Hardware & Electrical Engineering Terms

* **BMS (Battery Management System):** The circuitry responsible for safely charging the 150mAh LiPo battery, protecting it from overcharging, short circuits, and managing safe power delivery.
* **Pogo Pins:** Spring-loaded, gold-plated mechanical contact pins used to establish a temporary, reliable electrical connection between the Base Core and the modular Smart Skins without requiring semi-permanent plugs.
* **ADC (Analog-to-Digital Converter):** A hardware peripheral inside the ESP32-C3 that reads variable voltage levels. In Project ANIMA, it checks the resistance value on Pad 3 to instantly identify which Smart Skin is attached.
* **ESD Protection (Electrostatic Discharge):** Tiny diodes placed near exposed copper pads (like the pogo interface) to absorb static electricity shocks from human fingers, preventing the internal microchips from frying.
* **PCB (Printed Circuit Board):** The structural green (or custom-colored) board that holds and connects all electronic components like the microchip, battery circuit, and resistors.
* **SMD (Surface Mount Device):** Electronic components designed to be soldered directly onto the surface of a PCB, rather than through holes, which allows our Core to remain under 6mm thick.

---

## 💻 Firmware, Cryptography & Math Terms

* **ESP-IDF (Espressif IoT Development Framework):** The official, professional coding framework used to configure and write deep system software for the ESP32-C3 chip.
* **Vector Dot-Product:** A mathematical operation that takes two lists of numbers (your profile parameters vs. another person's profile parameters) and multiplies them to generate a single final score representing how closely aligned they are.
* **Quantization:** The process of shrinking a massive Artificial Intelligence model (like a Large Language Model) so it can run smoothly on cheap, offline microchips (like a Raspberry Pi) without needing massive cloud servers.
* **Ephemeral Token:** A temporary, randomized digital signature broadcast by the keyring core over Bluetooth. Because it changes every 15 minutes, it prevents bad actors from tracking a user's location across a room.
* **Dynamic Salt (Salting):** Random data injected into a cryptographic calculation. The Venue Hub changes its daily salt key so users cannot predict the exact data inputs needed to cheat the matchmaking score.

---

## 📝 How to Add Terms to This Glossary

We encourage all contributors to maintain the accessibility of this project. If you introduce a complex acronym or technical component in a Pull Request, please add its definition here:

1. Locate the correct alphabetical or categorical section.
2. Format the term using a bullet point and bold text: `* **TERM (Acronym):** Clear, beginner-accessible definition.`
3. Submit the addition as part of your feature branch Pull Request for admin review.
