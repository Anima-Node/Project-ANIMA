# Project ANIMA: Core Hardware Specifications v1.0
### Open-Source Tangible Social Interface (TSI) & Local AI Handshake Proxy

Project ANIMA is a privacy-first, zero-cloud physical "StreetPass" system designed to reclaim real-world human connection using open hardware and edge computing. By moving identity profiles away from remote server infrastructure and into localized hardware arrays, ANIMA creates tangible, peer-to-peer interactive encounters safely shielded from data farming and telemetry tracking.

This repository serves as the central authority for the physical dimensions, electrical schematics, firmware logic, and modular skin interface requirements of the ANIMA Base Core.

* **Hardware License:** CERN Open Hardware Licence (CERN-OHL-W)
* **Firmware/Software License:** MIT
* **Project GitHub Coordinate:** `Anima_Node/Project-ANIMA`
* **Official Discord Hub:** https://discord.gg/WgPyJf3bv
* **Development Repository Blog:** `https://ko-fi.com/AnimaNode`

---

## 1. Physical Form Factor & Dimensions

The Base Core is an ultra-rugged, pocket-sized electronic pod engineered to slide cleanly into modular, expressive "Smart Skins".

* **Width:** 30 mm
* **Length:** 40 mm (including integrated keyring loop anchor)
* **Thickness:** 6 mm
* **Chassis Material:** Translucent smoke-grey injection-moulded Recycled Polycarbonate (PC)
* **Mounting System:** Dual-sided parallel guide rails featuring mechanical snap-detents for secure, tactile locking into external skin peripherals.

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

* **Microcontroller:** ESP32-C3 System-on-Chip (SoC) featuring an energy-efficient low-power RISC-V computing core and native Bluetooth Low Energy (BLE 5.0) for offline smartphone companion sync.
* **Storage Vault:** 8MB NAND Flash Memory chip configured for local firmware storage, custom skin profile indexes, and encrypted local personal vector arrays.
* **Power Array:** 3.7V 150mAh Lithium-Polymer (LiPo) pouch cell. Advanced deep-sleep firmware configurations yield 3 to 4 weeks of keyring standby time, drawing operational current almost exclusively during 1-second physical handshakes.
* **Primary Handshake Array (Front Edge):** High-intensity Infrared (IR) Transmitter/Receiver LED pair driving direct, line-of-sight physical point-and-click discovery loops.
* **Charging/Data Tether (Bottom Edge):** Flush-mount, recessed USB-C interface for offline synchronization cycles and direct power charging.

---

## 3. The Smart Skin Interface (6-Pin Pogo Map)

The underside of the core features six flush, gold-plated copper contact pads. When docked inside a Smart Skin, spring-loaded pogo pins engage these boundaries to translate mathematical alignment scores into specialized physical performances driven by the target skin.

```text
[ Pad 1 ] ─── VCC OUT (+3.3V Power Bus to drive Skin peripherals)
[ Pad 2 ] ─── GND (Common System Ground)
[ Pad 3 ] ─── SKIN_ID (ADC line reading internal resistor profiles to identify Skin index)
[ Pad 4 ] ─── LED_DATA (Single-wire data line for addressable RGB LEDs/NeoPixels inside the skin)
[ Pad 5 ] ─── AUDIO_PWM (Pulse-Width Modulation output for piezoelectric buzzers/speakers)
[ Pad 6 ] ─── HAPTIC_DRV (Logic line triggering internal ERM/LRA vibration motors)
```

---

## 4. Firmware, Data Scoring, & Privacy Architecture

* **Zero-Cloud Architecture:** Individual interaction data profiles remain entirely sandboxed. Identity criteria are compiled locally via an offline, internet-permissionless mobile companion app and pushed over local BLE/USB-C tethers. No data streams are ever sent to remote external servers.
* **Offline Vector Matching Engine:** Peer compatibility discovery utilizes local vector dot-product matrix calculations directly on the ESP32-C3 chip ($\text{Score} = \sum A_i \cdot B_i$). Devices securely cross-reference integer arrays derived from the 10-Question Trial Schema via direct IR blasts or passive NFC taps. They exchange only the raw calculation outputs; text strings or answers are never transmitted.
* **Human Manifest Integration:** The compiled preference tree operates as a standardized, secure personal schema. This schema can configure new local AI models or consumer robotics instantly through physical handshakes, matching operational settings and behavioral tones to your personality out of the box.
* **ANIMA Venue Hub Platform:** The ecosystem scales into physical third spaces via offline single-board gateway nodes running inside volatile RAM disk storage. When high-compatibility milestones are reached, local quantized AI models (Llama-3-8B via `llama.cpp`) parse traits anonymously and print custom RPG-style character receipt cards using integrated 58mm TTL ESC/POS thermal printers.
* **Anti-Exploit Framework:** To prevent automated point-grinding or "location gaming," hardware rate-limiting restrictions are built into the firmware alongside rolling 15-minute ephemeral BLE tokens (`eID`) and daily rotating cryptographic salts ($\text{VenueSalt}_{24h}$).

---

## 🚀 How to Join the Tribe

We are actively recruiting hardware engineers (KiCad), embedded firmware developers (C++/ESP-IDF), and industrial designers to build our V1 prototype test batch.

Please read our `CONTRIBUTING.md` guide before claiming an open ticket on our active Issues board!

