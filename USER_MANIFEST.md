# Project ANIMA: The Human Manifest Schema & Local Scoring Engine v1.0

This specification establishes the mathematical data architecture for the 10-Question Trial Schema. It defines the integer vector array layouts, hardcoded philosophical offset penalties, and raw C++ calculation sequences executed by the ESP32-C3 Base Core during offline matchmaking cycles.

---

## 🔢 Module 1: The Vector Array & Mathematical Map

When a user completes the schema inside the sandboxed companion app, their answers are compiled into a 10-element integer vector array ($V$). Each element corresponds to a question index, and the assigned integer value (1 to 4) corresponds directly to their selected multiple-choice option.

$$V = [Q_{1}, Q_{2}, Q_{3}, Q_{4}, Q_{5}, Q_{6}, Q_{7}, Q_{8}, Q_{9}, Q_{10}]$$

### The Tiered Weighting System
Questions are stratified into three distinct conceptual layers, each carrying an assigned point weight used to scale the raw overlapping alignment score:

* **Tier 1: Surface Aesthetics** (Weight $W_1 = 5$) $\rightarrow Q_1, Q_2, Q_3$
* **Tier 2: Mental Quirks & Humor** (Weight $W_2 = 10$) $\rightarrow Q_4, Q_5, Q_6, Q_7$
* **Tier 3: Core Identity & Values** (Weight $W_3 = 20$) $\rightarrow Q_8, Q_9, Q_{10}$

### Maximum Possible Base Score
The maximum possible base score ($S_{\max}$) represents a perfect, item-for-item identical match across all 10 vector spaces:

$$S_{\max} = (3 \times 5) + (4 \times 10) + (3 \times 20) = 15 + 40 + 60 = 115 \text{ points}$$

---

## 🚫 Module 2: Hardcoded Philosophical Offset Penalties

A baseline dot-product matrix calculation cannot inherently identify deep ideological friction. To resolve this, the local calculation engine passes matching profiles through a native Offset Penalty Matrix. If two users select fundamentally incompatible worldviews, a hard penalty is subtracted directly from their cumulative point pool before the final percentage is evaluated.

* **Penalty Rule 1: The Core Value Clash ($Q_{10}$)**
  * *Conditions:* User A selects `1 [Critical Logic]` AND User B selects `2 [Radical Empathy]` (or vice versa).
  * *Logic:* A purely analytical mind paired with a purely emotionally driven empathetic perspective creates severe core operational friction.
  * *Penalty:* -5 points
* **Penalty Rule 2: The Existential Divide ($Q_5$)**
  * *Conditions:* User A selects `1 [Existential Comfort]` AND User B selects `2 [Existential Dread]` (or vice versa).
  * *Logic:* Total peace with cosmic insignificance running parallel to active, paralyzing dread causes immediate existential dissonance.
  * *Penalty:* -5 points
* **Penalty Rule 3: The Social Loop Friction ($Q_3 \times Q_8$)**
  * *Conditions:* User A selects $Q_3=3\text{ [Battery Drained]}$ & $Q_8=4\text{ [Lone Wolf]}$ WHILE User B selects $Q_3=4\text{ [Chaotic Change]}$ & $Q_8=2\text{ [The Catalyst]}$.
  * *Logic:* A highly volatile social instigator will completely shatter the operational comfort zone of an isolated individual seeking quiet privacy.
  * *Penalty:* -10 points

---

## 💻 Module 3: ESP32-C3 Local Compatibility Engine (C++)

This production-ready, clean C++ logic executes purely inside the volatile, temporary cache memory of the local hardware core during an over-the-air exchange loop.

```cpp
#include <Arduino.h>

// Struct to hold local calculation metrics
struct MatchResult {
    int rawScore;
    int penalties;
    float finalPercentage;
};

// Computes compatibility percentage locally on-chip via IR/BLE handshake
MatchResult calculateCompatibility(const int userA[10], const int userB[10]) {
    int score = 0;
    int penaltyPool = 0;

    // 1. Calculate Base Layer Component Scores
    for (int i = 0; i < 10; i++) {
        if (userA[i] == userB[i]) {
            if (i >= 0 && i <= 2)       score += 5;  // Tier 1
            else if (i >= 3 && i <= 6)  score += 10; // Tier 2
            else if (i >= 7 && i <= 9)  score += 20; // Tier 3
        }
    }

    // 2. Evaluate Hardcoded Philosophical Penalties

    // Penalty 1: Logic (1) vs Empathy (2) on Question 10 (Index 9)
    if ((userA[9] == 1 && userB[9] == 2) || (userA[9] == 2 && userB[9] == 1)) {
        penaltyPool += 5;
    }

    // Penalty 2: Cosmic Comfort (1) vs Cosmic Dread (2) on Question 5 (Index 4)
    if ((userA[4] == 1 && userB[4] == 2) || (userA[4] == 2 && userB[4] == 1)) {
        penaltyPool += 5;
    }

    // Penalty 3: Social Exhaustion vs Chaotic Catalysis
    bool A_isolated = (userA[2] == 3 && userA[7] == 4);
    bool B_isolated = (userB[2] == 3 && userB[7] == 4);
    bool A_chaotic  = (userA[2] == 4 && userA[7] == 2);
    bool B_chaotic  = (userB[2] == 4 && userB[7] == 2);

    if ((A_isolated && B_chaotic) || (B_isolated && A_chaotic)) {
        penaltyPool += 10;
    }

    // 3. Compile Final Pool Outcomes
    int rawFinalScore = score - penaltyPool;
    if (rawFinalScore < 0) rawFinalScore = 0; // Safeguard against negative values

    const int maxPossibleBaseScore = 115;
    float finalPct = ((float)rawFinalScore / (float)maxPossibleBaseScore) * 100.0f;

    MatchResult result;
    result.rawScore = rawFinalScore;
    result.penalties = penaltyPool;
    result.finalPercentage = finalPct;

    return result;
}
```

---

## 🎯 Module 4: Output Tier Threshold Profiles

Once the final matching percentage calculation resolves on-chip, the firmware triggers specialized hardware behavior trees mapped directly to the compatibility tier.

### Tier 1: System Isolation (0% – 25%)
* **Hardware Behavior:** Immediate low-compatibility sensory feedback loops. Onboard addressable LED arrays trigger slow, single-pulse dull flashes. Piezoelectric buzzers generate short, clean low-frequency mechanical warning tones.
* **System Action:** No localized transaction payloads are passed over BLE. The device automatically logs an immutable hardware cool-down cycle, dropping active matchmaking requests from that specific MAC address for 1 hour to prevent location tracking or point spam.

### Tier 2: Neutral Alignment (26% – 65%)
* **Hardware Behavior:** Stable, continuous ambient breathing patterns pass across the active LED layouts. Short, isolated high-pitch chiptune audio blips ring out once.
* **System Action:** Handshake interaction markers are logged inside the local companion application storage vault purely as a standard historical contact baseline.

### Tier 3: Resonant Manifestation (66% – 100%)
* **Hardware Behavior:** Smart Skins unlock premium execution loops. High-intensity multi-color strobe cascades loop alongside complex polyphonic chiptune arpeggios, and haptic ERM/LRA motors skitter aggressively.
* **System Action:** Generates an encrypted, ephemeral data handshake payload. When brought near an offline Venue Hub node, this payload triggers the local generative Edge AI prompt queue via `llama.cpp` to print a custom physical character receipt sheet.