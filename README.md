
# Project ANIMA: Core Hardware Specifications v1.0
### Open-Source Tangible Social Interface (TSI) & Local AI Handshake Proxy

Project ANIMA is a privacy-first, zero-cloud physical "StreetPass" system designed to reclaim real-world human connection using open hardware and edge computing.

This repository contains the physical dimensions, internal layout, and electrical specifications for the ANIMA Base Core. 

* **Hardware License:** CERN Open Hardware Licence (CERN-OHL-W)
* **Firmware/Software License:** MIT
* **Project Discord Hub:** https://discord.gg/WgPyJf3bv
* **Development Blog:** [Insert Hackaday.io Link]

---

## 1. Physical Form Factor & Dimensions
The Base Core is designed to be an ultra-rugged, pocket-sized electronic "pod" that seamlessly slides into modular, expressive "Smart Skins."

* **Width:** 30 mm
* **Length:** 40 mm (including integrated keyring loop anchor)
* **Thickness:** 6 mm
* **Chassis Material:** Translucent or clear Recycled Polycarbonate (PC)
* **Mounting System:** Dual-sided guide rails with mechanical snap-detents for tactile locking into Smart Skins.

---

## 2. Internal Hardware Componentry

```text
┌──────────────────────────────────────────────┐
│          [KEYRING EXTENSION LOOP]            │
├──────────────────────────────────────────────┤
│          3.7V 150mAh LiPo BATTERY            │
├──────────────────────────────────────────────┤
│            PCB (BOARD CIRCUITS)              │
│  ┌─────────────────┐ ┌───────────────────┐   │
│  │    ESP32-C3     │ │  8MB FLASH VAULT  │   │
│  │   (Micro-SoC)   │ │ (Encrypted Local) │   │
│  └─────────────────┘ └───────────────────┘   │
├──────────────────────────────────────────────┤
│ [IR ARRAY]     [POGO INTERFACE]     [USB-C]  │
│ (Front Edge)   (Flush Underside)    (Bottom) │
└──────────────────────────────────────────────┘
```

* **Microcontroller:** ESP32-C3 System-on-Chip (SoC). Provides low-power RISC-V computing and native Bluetooth Low Energy (BLE) for offline smartphone pairing.
* **Storage Vault:** 8MB NAND Flash Memory. Used to store localized encrypted vector data, firmware, and peripheral reaction scripts.
* **Power Source:** 3.7V 150mAh Lithium-Polymer (LiPo) pouch cell. Deep-sleep optimizations allow for 3–4 weeks of keyring standby time.
* **Primary Handshake Array (Front Edge):** High-intensity Infrared (IR) Transmitter/Receiver LED pair for active, line-of-sight physical "bumps."
* **Charging/Data Tether (Bottom Edge):** Recessed, flush-mount USB-C interface.

---

## 3. The Smart Skin Interface (6-Pin Pogo Map)
The underside of the chassis features six flush, gold-plated copper contact pads. When docked inside a Smart Skin, spring-loaded pogo pins engage these pads to translate compatibility data into physical performance.

```text
[ Pad 1 ] ─── VCC OUT (+3.3V Power Bus to drive Skin peripherals)
[ Pad 2 ] ─── GND (Common System Ground)
[ Pad 3 ] ─── SKIN_ID (ADC line reading an internal resistor to identify the Skin archetype)
[ Pad 4 ] ─── LED_DATA (Single-wire data line for addressable RGB LEDs inside the skin)
[ Pad 5 ] ─── AUDIO_PWM (Pulse-Width Modulation output for piezoelectric buzzers/speakers)
[ Pad 6 ] ─── HAPTIC_DRV (Logic line triggering internal vibration/haptic motors)
```

---

## 4. Firmware & Data Philosophy

* **Zero-Cloud Architecture:** Data is generated via an offline companion app, compiled into a text-based vector matrix, and transferred entirely over local BLE or USB-C.
* **Vector Dot-Product Matching:** Math is computed natively on the ESP32-C3 by comparing preference arrays. No raw data points are ever broadcast during an IR bump—only the final compatibility score is exchanged.
* **AI Manifest Compatibility:** The finalized 200+ point local vector matrix doubles as a standardized "Human Manifest File" capable of onboarding local AI models and consumer robotics via a secure, physical NFC/Bluetooth handshake.
* **[ANIMA Venue Hub System](HUB_SPEC.md):** Learn how Project ANIMA scales into physical third spaces via offline thermal printing hubs, mass-proximity handshakes, and game-theory anti-exploit protocols.

---

## 🚀 How to Join the Tribe
We are actively recruiting hardware engineers (KiCad), embedded firmware developers (ESP-IDF), and industrial designers to build the V1 prototype batch. 

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide before claiming an open ticket on our Issues board!
