# Project ANIMA: Venue Hub & Thermal Printer Specifications v1.0

This specification outlines the technical architecture, hardware configurations, and cryptographic execution rules for the ANIMA Venue Hub—a zero-cloud, localized desktop terminal designed for third-space deployments.

---

## 1. System Topology & Hardware Stack

The Venue Hub acts as a localized passive proximity tracker, an edge-computing vector node, and a physical interaction terminal. It operates entirely without an internet connection or corporate cloud routing.

```text
┌────────────────────────────────────────────────────────┐
│                     ANIMA VENUE HUB                    │
│   (Raspberry Pi 4 / 5 or Radxa Zero Single-Board PC)   │
├────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐   ┌──────────────────────┐  │
│  │   OMNIDIRECTIONAL IR  │   │  BLE PASSIVE MATRIX  │  │
│  │   DIFFUSER ARRAY      │   │  (Proximity Tracker) │  │
│  └───────────────────────┘   └──────────────────────┘  │
├────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐   ┌──────────────────────┐  │
│  │ LOCAL LLM EDGE ENGINE │   │ TTL SERIAL THERMAL   │  │
│  │ (Llama-3-8B-Instruct) │   │ PRINTER (58mm Paper) │  │
│  └───────────────────────┘   └──────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

### Component Specifications
* **Host Compute Node:** Raspberry Pi 4 (4GB+ RAM) or equivalent ARM-based Single Board Computer (SBC) running a hardened, read-only Linux distribution.
* **Peripherals:** 
  * 58mm TTL Serial Thermal Receipt Printer (Embedded mini-chassis, e.g., QR701 or CSN-A2).
  * High-intensity 360-degree Infrared (IR) emitter/receiver breakout board.
  * Class 1 USB Bluetooth 5.0 Adapter (High-gain antenna for stable passive multi-device tracking).

---

## 2. Mass Proximity Handling (Multi-Bumping)

To enable passive matching within physical spaces without relying on individual line-of-sight alignments, the Hub runs a secure local radio loop:

* **Passive BLE Beaconing:** Cores within a 2-to-5 meter range of the Hub broadcast a randomized, rolling ephemeral token (`eID`) that changes every 15 minutes.
* **Matrix Buffer:** The Hub logs these tokens into a volatile RAM-only buffer. It never stores historical location logs.
* **Local Evaluation:** When a user physically docks their core to the Hub, the Hub checks the local buffer to calculate compatibility matches with active tokens currently present in the room, keeping users completely anonymous until they choose to connect.

---

## 3. Local AI Character Generation & Thermal Printing

When a user docks their Base Core into the Hub’s magnetic cradle via USB-C or a specialized pogo terminal, the Hub securely parses the Human Manifest File to generate a tangible profile artifact.

### 3.1 Edge AI Architecture
* **Model State:** A fully quantized, offline Large Language Model (e.g., Llama-3-8B-Instruct running via `llama.cpp` using INT4 weight quantization) executed entirely on the local SBC processor.
* **Data Sanitization:** The raw vector file never enters the LLM training space. The host parsing script translates vector tiers into simple, flat semantic tags (e.g., Preference: High-Gardening, Low-MainstreamPop, High-Cyberpunk).

### 3.2 Print Manifest Output Structure
The printer module outputs a standardized 58mm receipt layout formatted via raw ESC/POS commands:

```text
----------------------------------------
             PROJECT ANIMA              
        [ LOCAL SYNC COMPLETE ]         
----------------------------------------

ARCHETYPE: Cyber-Botanist
VIBE LEVEL: 87 / 100

----------------------------------------
[!] SPATIAL MATRIX RADAR:
There is currently a 94% Compatibility Match 
active within this establishment.

----------------------------------------
[!] LOCALIZED GENERATED SPECTRUM:
"You balance an aggressive affinity for 
decentralized command lines with a quiet 
need to watch heirloom tomatoes sprout. 
Your digital footprint is nonexistent, 
which makes you highly dangerous to ad 
networks and highly interesting to the 
person sitting in the corner."
----------------------------------------
```

---

## 4. Game-Theory Protections (Anti-Exploit System)

To prevent users from "gaming" the local matchmaking loops to exploit venue promotions (e.g., faking vector files to secure a 90%+ match score for a free coffee reward), the Hub runs a strict Cryptographic Cooling Protocol.

### 4.1 Daily Venue Salting
Every 24 hours at 04:00 AM, the Venue Hub generates an internal cryptographic salt string. Because this salt alters the mathematical output curve required to trigger a high-tier reward receipt, users cannot reverse-engineer or pre-compile a fake "perfect match" file at home without access to that day's unique localized hash keys.