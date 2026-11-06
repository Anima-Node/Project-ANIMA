# The Venue Hub Node Architecture & Edge AI Printing Pipeline

This specification codifies the industrial system architecture, anti-exploit protocols, and generative AI execution parameters for the **ANIMA Venue Hub**. Operating entirely offline within volatile RAM, the Venue Hub processes local vector matches and manages the physical receipt-printing pipeline at Third-Space deployments.

---

## 🏗️ Module 1: The Offline Gateway Hardware Topology

The Venue Hub is designed as an isolated, standalone hardware drop node. It operates independently of external cloud networks, preventing remote tracking and ensuring continuous execution in connectivity-degraded environments.

```text
┌───────────────────────┐
│   ESP32-C3 Core Pod   │
└───────────┬───────────┘
            │ (Local BLE Handshake)
            ▼
┌───────────────────────────────────────────────────────────┐
│                    ANIMA VENUE HUB                        │
│                                                           │
│  ┌────────────────────┐          ┌─────────────────────┐  │
│  │ Volatile RAM (eID)  │ ──────►  │  Local LLM Engine   │  │
│  └────────────────────┘          │  (Llama-3 via cpp)  │  │
│                                  └──────────┬──────────┘  │
└─────────────────────────────────────────────┼─────────────┘
                                              │ (ESC/POS Serial)
                                              ▼
                                    ┌─────────────────────┐
                                    │ 58mm Thermal Printer│
                                    └─────────────────────┘
```

### Hardware Component Blueprint
* **Compute Unit:** Raspberry Pi 4 (8GB RAM) or Radxa Rock 4 SE platform running an optimized, read-only Debian Linux kernel.
* **Storage Configuration:** Industrial-grade MicroSD card configured with an immutable boot partition. All operational logs, matchmaking tracking states, and temporary tokens are forced directly into a volatile **RAM disk (`tmpfs`)** that instantly self-wipes upon power loss.
* **Physical Printing Interface:** A 58mm commercial-grade TTL serial ESC/POS thermal receipt print mechanism embedded into a custom-molded enclosure or laser-cut venue housing.

---

## 🛡️ Module 2: The Ephemeral Token Loop & Anti-Exploit Protocols

To mitigate automated "location gaming," rapid repetitive point-grinding, or unauthorized credential spoofing, the Venue Hub applies strict hardware-level rate-limiting and rolling cryptographic validations.

### 1. The 15-Minute Ephemeral Identifier (`eID`)
The Hub continuously broadcasts a rotating, temporary Bluetooth identification beacon (`eID`) generated locally using a secure random number generator:

\[\text{eID} = \text{HMAC-SHA256}(\text{VenueSalt}_{24h}, \text{Timestamp}_{15min})\]

* The `eID` vanishes from the Hub’s memory every 15 minutes.
* The Base Core saves this `eID` to its internal NAND Flash to validate that an interaction occurred organically in the real world at that specific time window.

### 2. Physical Rate-Limiting Constraints
* **Hardware MAC Isolation:** The Hub tracks incoming MAC addresses of interacting Base Cores. It drops communication requests from any device address that has initiated an execution handshake more than once within a **60-minute window**.
* **Daily Rotating Salts:** The system updates its global structural salt (\(\text{VenueSalt}_{24h}\)) at exactly 00:00 UTC daily. This protocol stops bad actors from using pre-calculated validation tokens harvested on previous days.

---

## 🤖 Module 3: The Edge AI Local Inference Pipeline

When a user reaches a verified interaction milestone or checks in with a matching peer, the Hub triggers a local Large Language Model (LLM) execution thread to generate a customized, narrative RPG-style character card.

### Local LLM Operational Framework
* **Inference Engine:** Driven completely offline by `llama.cpp` using a highly optimized, 4-bit quantized version of the **Llama-3-8B-Instruct** model architecture.
* **System Prompt Isolation:** The model is locked to a strict system prompt instruction set to guarantee fast execution speeds and protect against prompt injection.

### Standardized System Prompt Payload
```text
[SYSTEM INSTRUCTION]
You are the Project ANIMA Local Generation Engine. You will ingest a 10-digit integer array representing a human user's personality traits and output a raw text, retro RPG character bio card.
- Do not include conversational preambles, summaries, or metadata.
- Keep the entire character profile limited to a maximum of 4 lines of thematic text.
- Use an abstract, mysterious, and analytical tone.

[INPUT VECTOR MATRIX]
User Profile:

[TARGET EXECUTION STRUCTURE]
CLASS: [Determine a customized class name based on Tier 3 values]
CORE TRAIT: [Synthesize a signature personality characteristic]
VULNERABILITY: [Expose a conceptual vulnerability based on penalty rules]
BIOMASS LOG: [A 2-sentence descriptive, abstract narrative summary]
```

---

## 🖨️ Module 4: 58mm TTL ESC/POS Thermal Printing Pipeline

Once the local inference execution completes, the raw output string is formatted into custom low-level escape sequence commands (ESC/POS) and streamed directly via a serial interface (`/dev/ttyS0`) to the physical thermal receipt printer.

### Raw ESC/POS Layout Formatting Script
```text
[ESC/POS Command: 0x1B, 0x40] // Initialize printer configuration
[ESC/POS Command: 0x1B, 0x61, 0x01] // Align text alignment to Center
----------------------------------------
▲ ▲ ▲   P R O J E C T   A N I M A   ▲ ▲ ▲
----------------------------------------
[ESC/POS Command: 0x1B, 0x61, 0x00] // Reset text alignment to Left
[ESC/POS Command: 0x1B, 0x45, 0x01] // Enable bold text formatting
CLASS: THE SILENT ARCHITECT
[ESC/POS Command: 0x1B, 0x45, 0x00] // Disable bold text formatting

TRAIT: Deep Existential Logic
FRICT: Severe Emotional Blindspot

LOG: Solitary operator optimized for complex
system mapping. Exhibits severe processing friction
when exposed to rapid chaotic group settings.
----------------------------------------
[ESC/POS Command: 0x1B, 0x61, 0x01] // Center text alignment
[ESC/POS Command: 0x1D, 0x6B, 0x04, 0x0A] // Generate local validation Barcode
[VENUE VERIFIED: NODE_04_SYNC]
----------------------------------------
[ESC/POS Command: 0x1B, 0x64, 0x04] // Feed paper out by 4 clean blank lines
```