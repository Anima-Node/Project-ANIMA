# Companion App Architecture & Local BLE Sync Logic

This specification defines the software architecture, data schema, and Bluetooth Low Energy (BLE) sync logic for the offline-first Project ANIMA companion application. The companion app acts as a local bridge to compile user profile matrices and securely push them to the Base Core without external cloud infrastructure.

---

## 📱 Module 1: Local-First Application Architecture

The companion app is strictly a local data compiler. It maintains zero remote server dependencies, requires no user account creation, and stores all cryptographic states within the host device’s secure on-device storage.

```text
┌────────────────────────┐
│  10-Question UI Input  │
└───────────┬────────────┘
            ▼
┌────────────────────────┐
│ Secure Local Database  │ ──► [ Local Validation Engine ]
│ (SQLite / CoreData)    │
└───────────┬────────────┘
            ▼
┌────────────────────────┐
│ BLE Sync Interface     │ ──► [ Local Encrypted Payload ] ──► [ ESP32-C3 Core ]
└────────────────────────┘
```

### Technical Stack Guidelines
* **Cross-Platform Core:** Built using Flutter or React Native to maintain a single codebase for iOS and Android, focusing exclusively on native BLE APIs.
* **Local Storage Engine:** SQLite (via encrypted SQLCipher) or a lightweight on-device key-value store (Hive/MMKV).
* **Privacy Isolation:** The application manifest must explicitly omit internet permissions (`android.permission.INTERNET` is omitted or stripped during compilation) to prove to open-source auditors that data leakages to external servers are architecturally impossible.

---

## 🗃️ Module 2: The Human Manifest Local Schema

The application translates user input into an optimization-ready, 10-byte transaction payload. This schema encapsulates the answers to the 10-Question Trial Schema alongside local administrative parameters.

### 10-Byte Byte-Array Mapping Layout
The final payload pushed to the hardware core over BLE consists of a raw byte array (`uint8_t[10]`) mapped exactly as follows:

| Byte Index | Data Field | Accepted Value Range | Description |
| :--- | :--- | :--- | :--- |
| **0x00** | Tier 1: Q1 (Noise) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x01** | Tier 1: Q2 (Style) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x02** | Tier 1: Q3 (Plans) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x03** | Tier 2: Q4 (Humor) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x04** | Tier 2: Q5 (Stars) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x05** | Tier 2: Q6 (Nostalgia) | 0x01 – 0x03 | Answer integer selection mapping. |
| **0x06** | Tier 2: Q7 (Narrative) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x07** | Tier 3: Q8 (Role) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x08** | Tier 3: Q9 (Boundary) | 0x01 – 0x04 | Answer integer selection mapping. |
| **0x09** | Tier 3: Q10 (Gift) | 0x01 – 0x04 | Answer integer selection mapping. |

---

## ⚡ Module 3: Local BLE Handshake & Sync Logic

To prevent third-party tracking or passive wireless sniffing in public spaces, the Base Core keeps its BLE radio disabled by default. The sync sequence is exclusively user-initiated via a physical interaction loop.

### The Hardware Sync Lifecycle Sequence
1. **User Trigger:** The user holds down the manual sync button on the Base Core for 3 seconds, or plugs it into a device via USB-C.
2. **Advertising Window:** The ESP32-C3 firmware wakes the BLE radio and begins advertising a unique, non-identifiable Service UUID (`4a4e494d-412d-434f-5245-5f53594e4300`) for a strict 60-second operational window.
3. **App Discovery:** The companion app scans locally, matches the explicit Service UUID, and initiates a secure passkey connection handshake.
4. **Payload Write:** The companion app writes the 10-byte Profile Array to the custom write characteristic.
5. **Termination:** The Core acknowledges safe transmission storage within its 8MB NAND Flash chip, terminates the Bluetooth connection, and returns the BLE radio to an unpowered deep-sleep isolation state.

### Companion App Connection Logic Sample (Dart/Flutter Pseudo-Code)

```dart
import 'package:flutter_blue_plus/flutter_blue_plus.dart';

class AnimaSyncEngine {
  static const String ANIMA_SERVICE_UUID = "4a4e494d-412d-434f-5245-5f53594e4300";
  static const String ANIMA_WRITE_CHAR_UUID = "4a4e494d-412d-434f-5245-5f5752495445";

  Future<bool> pushProfileToCore(List<int> profileByteArray) async {
    // Ensure profile matches strict 10-byte constraint
    if (profileByteArray.length != 10) return false;

    // Start scanning for the local device
    FlutterBluePlus.startScan(withServices: [Guid(ANIMA_SERVICE_UUID)], timeout: Duration(seconds: 15));

    // Listen for scan outcomes
    await for (List<ScanResult> results in FlutterBluePlus.scanResults) {
      for (ScanResult result in results) {
        // Device located, halt scan and connect
        await FlutterBluePlus.stopScan();
        BluetoothDevice device = result.device;
        await device.connect();

        // Discover characteristics
        List<BluetoothService> services = await device.discoverServices();
        var animaService = services.firstWhere((s) => s.uuid.toString() == ANIMA_SERVICE_UUID);
        var writeChar = animaService.characteristics.firstWhere((c) => c.uuid.toString() == ANIMA_WRITE_CHAR_UUID);

        // Write the local 10-byte array payload securely
        await writeChar.write(profileByteArray, withoutResponse: false);

        // Disconnect and cleanly close channel
        await device.disconnect();
        return true;
      }
    }
    return false;
  }
}
```

---

## 🛡️ Module 4: Verification & Anti-Sniffing Protocols

Because Project ANIMA broadcasts numbers over the air during peer-to-peer exchanges, the companion app applies an initialization filter to scramble tracking patterns.

* **Dynamic MAC Address Masking:** The companion app randomizes its BLE broadcast identification profiles dynamically on every connection attempt. This makes it impossible for stationary commercial Bluetooth sniffer beacons placed in city infrastructure to trace or map user movements through the companion app.
* **Firmware Verification Loop:** Upon receiving the 10-byte payload, the ESP32-C3 chip runs a quick range verification check. If any single byte contains a value outside its bounded constraint (e.g., a value of `0x09` on an item expecting `0x01` through `0x04`), the core rejects the sync payload entirely, flushes its temporary RAM, and flashes an amber error loop via `LED_DATA`.