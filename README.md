# 90s-Style Handheld Game (TECHIN 512 Final Project)

## Overview
**Goal.** Build an ESP32C3 + CircuitPython handheld game (Bop-It style).  
**Core parts.** Seeed XIAO ESP32C3, SSD1306 OLED, ADXL345, Rotary Encoder, NeoPixels, LiPo, Switch.

## Repo Structure
```
.
├── Documentation/          # Circuit diagram (.kicad_sch) and system block diagram (.svg/.drawio)
├── src/                    # CircuitPython code and libraries
│   └── .gitkeep
├── .gitignore
└── README.md
```

## Quick Start
- Put your CircuitPython `.py` files in `src/`.
- Place your KiCad schematic in `Documentation/` (e.g., `handheld_game.kicad_sch`).
- Export your system block diagram to `Documentation/system_block_diagram.svg` (starter included).

## Assignment 4 Checklist
- [ ] Create GitHub repo and push this structure.
- [ ] Add `Documentation/handheld_game.kicad_sch` from KiCad.
- [ ] Add `Documentation/system_block_diagram.svg` (update the starter to match your design).
- [ ] Keep `src/` for code that will be added in later assignments.

## Notes for KiCad Schematic
- Libraries: ADXL345 (I²C), SSD1306 (I²C), Rotary Encoder (A/B + switch), NeoPixel (DIN), XIAO ESP32C3.
- Power: LiPo → charger/boost (per course hardware), on/off switch, decoupling caps near VDD pins.
- Nets:
  - I²C: SDA, SCL with pull-ups (if board doesn’t provide). Label nets; avoid spaghetti wires.
  - NeoPixel DIN uses a GPIO with a **series ~300–470Ω** resistor; add a large cap (≥ 1000 µF) on 5V rail if many LEDs.
  - Rotary encoder: A/B to GPIOs + pull-ups, SW to GPIO with pull-up.
  - OLED/ADXL345: share I²C; set unique addresses if needed.
- Annotation & ERC: `Tools → Annotate Schematic`, then `Inspect → Electrical Rules Checker`.

## System Block Diagram Hints
Include: Sensors/Inputs (ADXL345, Rotary, Buttons), Microcontroller (ESP32C3), Power (LiPo, charger/switch), Outputs (OLED, NeoPixels), and Human inputs. Keep arrows left→right (signal), bottom→top (power).

## License
MIT (optional for class). Update if needed.