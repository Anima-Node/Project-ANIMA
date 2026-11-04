
Project ANIMA: Contributor Guidelines

Welcome to the Project ANIMA development sandbox! We are building an open-source, zero-cloud Tangible Social Interface (TSI) designed to reclaim physical spaces from algorithmic, surveillance-heavy tech platforms.
Whether you are a seasoned electronic design automation (EDA) engineer, an embedded firmware wrangler, an industrial designer, or a technical writer, we need your skills to bring this physical proxy loop to life.

🧭 Our Architectural Core Values

Before opening a text channel or writing code, every contributor must align with our primary non-negotiable pillars:
1. Absolute Data Autonomy: Zero-cloud, zero telemetry, zero persistent tracking. All matching computations happen entirely at the physical edge via local vector math over line-of-sight hardware handshakes.
2. Modular Form Factor Separation: The Base Core acts strictly as the hardware "Brain" (universal, minimalist, cheap). The Smart Skin acts as the physical "Soul" (expressive, customizable, community-fabricated).
3. Radical Access: Hardware layouts remain anchored under the CERN-OHL-W license, and firmware is bound under the MIT license. We support open manufacturing, local repairability, and decentralized physical hubs.

🛠️ Active Development Tracks

To prevent redundant or conflicting engineering efforts, our workflow is rigidly divided into specific technical tracks. Please review our [GitHub Issues Board] to claim an unassigned task before starting.

🔌 Track 1: Hardware Engineering (PCB & Electrical)

• Primary EDA Tool: KiCad v8.x (All schematic layouts and board footprints must use open-source native tooling).
• Current Goals:
	• Routing an ultra-slim, dual-layer or four-layer PCB constrained tightly to the 30mm x 40mm x 6mm internal cavity footprint.
	• Implementing a highly efficient miniature Battery Management System (BMS) for the 3.7V 150mAh LiPo over a recessed flush-mount USB-C rail.
	• Fusing the 6-pin gold-plated copper Pogo interface pad lines into safe, ESD-protected analog/digital pathways on the underside plane.

💻 Track 2: Embedded Firmware (ESP32-C3 Architecture)

• Development Framework: ESP-IDF (Preferred for production power management) or Arduino Core for rapid prototyping blocks.
• Current Goals:
	• Writing ultra-aggressive deep-sleep routines and wake-on-interrupt logic triggered by the active IR receiver array.
	• Optimizing localized 256-dimensional vector dot-product calculations within a sandboxed, encrypted memory partition on the 8MB NAND Flash vault.
	• Structuring the local Bluetooth Low Energy (BLE) pairing profile for secure, offline profile flashing from the mobile companion app companion.

📐 Track 3: Industrial Design & Smart Skins

• Aesthetic Files: STEP, STL, or 3MF formats preferred.
• Current Goals:
	• Validating physical snap tolerances and dual-sided guide rails to safely lock the core into diverse mediums (3D-printed filaments, machined metal enclosures, or textile plush rigs).

🚦 Git & Pull Request (PR) Workflow Rules

To keep our master repository stable, we maintain a strict information filtering loop:
1. The Single Source of Truth Rule: Never share raw code files, schematics, or firmware patches inside Discord or messaging chats. All technical design modifications must pass through a GitHub Pull Request.
2. Branching Strategy: Fork the repo and create your feature branches off the main development line:
	• feature/hardware-pads
	• bugfix/deep-sleep-loop
3. Commit Messages: Use descriptive, imperative commit notation (e.g., feat: add ESD protection diodes to pogo data lines or fix: optimize vector matrix array initialization memory allocation).
4. The Review Loop: Every PR targeting core hardware traces or encryption logic requires peer verification from at least one repository maintainer before merging.

💬 Where the Tribe Gathers

• Public Announcements & Milestones: Check out our project log timeline on [Hackaday.io Project Link].
• Real-Time Engineering Debates: Join the #hardware-ee and #firmware-code workbenches on our [Discord Server Link].
• Vocabulary Sync: If you hit unfamiliar technical jargon or architecture references, check out or add to our global definitions inside GLOSSARY.md.
Thank you for helping us seed a healthier, tactile digital counter-movement. Let's build something real!
