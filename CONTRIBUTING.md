# Project ANIMA: Contributor Guidelines

Welcome to the Project ANIMA development sandbox! We are building an open-source, zero-cloud Tangible Social Interface (TSI) designed to reclaim physical spaces from algorithmic, surveillance-heavy tech platforms. 

Whether you are a seasoned electronic design automation (EDA) engineer, an embedded firmware wrangler, an industrial designer, or a technical writer, we need your skills to bring this physical proxy loop to life.

---

## 🧭 Our Architectural Core Values

Before opening a text channel or writing code, every contributor must align with our primary, non-negotiable pillars:

* **Absolute Data Autonomy:** Zero-cloud, zero telemetry, zero persistent tracking. All matching computations happen entirely at the physical edge via local vector math over line-of-sight hardware handshakes.
* **Modular Form Factor Separation:** The Base Core acts strictly as the hardware "Brain" (universal, minimalist, cheap). The Smart Skin acts as the physical "Soul" (expressive, customizable, community-fabricated).
* **Radical Access:** Hardware layouts remain anchored under the CERN-OHL-W license, and firmware/software is bound under the MIT license. We support open manufacturing, local repairability, and decentralized physical hubs.

---

## 🛠️ Active Development Tracks

To prevent redundant or conflicting engineering efforts, our workflow is divided into specific technical tracks. Please review our GitHub Issues Board to claim an unassigned task before starting development.

### 🔌 Track 1: Hardware Engineering (PCB & Electrical)
* **Primary EDA Tool:** KiCad v8.x (All schematic layouts and board footprints must use open-source native tooling).
* **Core Cavity Constraints:** Routing an ultra-slim, dual-layer or four-layer PCB constrained tightly to the **30 mm x 40 mm x 6 mm** internal cavity footprint.
* **Power Management:** Implementing a highly efficient miniature Battery Management System (BMS) for the 3.7V 150mAh LiPo over a recessed flush-mount USB-C rail.
* **Interface Protection:** Fusing the 6-pin gold-plated copper Pogo interface pad lines into safe, ESD-protected analog/digital pathways on the underside plane.

### 💻 Track 2: Embedded Firmware & App Logic (ESP32-C3 Architecture)
* **Development Framework:** ESP-IDF (Preferred for production power management) or Arduino Core for rapid prototyping blocks.
* **Power Optimization:** Writing ultra-aggressive deep-sleep routines and wake-on-interrupt logic triggered by the active front-edge IR receiver array.
* **Vector Execution:** Optimizing localized 256-dimensional vector dot-product calculations within a sandboxed, encrypted memory partition on the 8MB NAND Flash vault.
* **BLE Sync Pipeline:** Structuring the local Bluetooth Low Energy (BLE) pairing profile for secure, offline profile flashing from the mobile companion app using our strict 60-second user-initiated pairing window.

### 📐 Track 3: Industrial Design & Smart Skins
* **Aesthetic Formats:** STEP, STL, or 3MF formats preferred.
* **Mechanical Validation:** Checking physical snap tolerances and dual-sided guide rails to safely lock the core into diverse mediums (3D-printed filaments, machined metal enclosures, or textile plush rigs).
* **Resistor Profile Mapping:** Ensuring all custom skins integrate the exact resistor values matching their designated physical profile index (e.g., 4.7 kΩ for the *Grave-Digga* profile) on Pad 3 (`SKIN_ID`).

---

## 🚦 Git & Pull Request (PR) Workflow Rules

To keep our master repository stable, we maintain a strict information filtering loop:

1. **The Single Source of Truth Rule:** Never share raw code files, schematics, or firmware patches inside Discord or messaging chats. All technical design modifications must pass through a GitHub Pull Request.
2. **Branching Strategy:** Fork the repo and create your feature branches off the main development line. Use descriptive namespace prefixes:
   * `feature/hardware-pads`
   * `bugfix/deep-sleep-loop`
3. **Commit Messages:** Use clean, imperative commit notation to match our GitHub integration logs:
   * `feat: add ESD protection diodes to pogo data lines`
   * `fix: optimize vector matrix array initialization memory allocation`
4. **The Review Loop:** Every PR targeting core hardware traces, encryption logic, or scoring penalties requires peer verification from at least one repository Core Dev or Maintainer before merging.

---

## 💬 Where the Tribe Gathers

* **Public Announcements & Milestones:** Check out our public log and development timeline on our Hackaday.io Project Page.
* **Real-Time Engineering Debates:** Join the `#hardware-dev` and `#firmware-flash` workbenches on our Discord Server.
* **Vocabulary Sync:** If you hit unfamiliar technical jargon or architecture references, check out or add to our global definitions inside `GLOSSARY.md`.

Thank you for helping us seed a healthier, tactile digital counter-movement. Let's build something real!
