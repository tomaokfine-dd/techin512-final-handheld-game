# Motion Game Master

A 90s-style handheld motion-controlled game built with ESP32 and CircuitPython.

## Overview

Motion Game Master is an interactive handheld game that challenges players to perform physical movements in response to on-screen prompts within a time limit. The game features three difficulty levels, a scoring system, animated splash screen, and a persistent high score board.

---

## How to Play

### Game Rules
1. **Power on the device** - Watch the animated splash screen with a dancing stick figure
2. **Select difficulty** - Use the rotary encoder to choose between `<Easy>`, `Medium`, or `Hard`
   - Easy: 2000ms initial time, decreases by 100ms per level
   - Medium: 1500ms initial time, decreases by 150ms per level
   - Hard: 1200ms initial time, decreases by 200ms per level
3. **Calibration** - Keep the device still on a flat surface during calibration
4. **Play 10 levels** - Perform the prompted movements before time runs out:
   - `<- LEFT` - Tilt device to the left
   - `RIGHT ->` - Tilt device to the right
   - `^ UP` - Tilt device upward
   - `v DOWN` - Tilt device downward
   - `~ SHAKE` - Shake the device vigorously
5. **Score points** - Each correct move earns 10 points
6. **Enter initials** - If you achieve a high score (top 3), enter your 3-letter name using the rotary encoder
7. **View high scores** - Top 3 scores with player initials are displayed after each game
8. **Restart** - Press the button to play again without power cycling

### Controls
- **Rotary Encoder**: Navigate menus, select difficulty, and enter initials (turn left to cycle through options)
- **Button**: Confirm selections with a single press
- **Accelerometer**: Tilt and shake the device to perform moves

---

## Hardware Components

### Provided Components
- **Xiao ESP32C3** - Microcontroller running CircuitPython
- **SSD1306 OLED Display (128x64)** - Shows game interface, menus, and scores
- **ADXL345 Accelerometer** - Detects tilt and shake movements via I2C
- **Rotary Encoder** - Menu navigation and input
- **NeoPixel LED (1 LED)** - Visual feedback with color indicators
- **LiPo Battery** - Portable power source
- **On/Off Switch** - Power control

### Additional Hardware
- **Perfboard** - Used instead of breadboard for permanent connections
- **Female Headers** - All components are removable for easy maintenance
- **Pull-up Resistors** - 4.7kΩ resistors on I2C lines (SCL and SDA) for stable communication

### Pin Configuration
```
Xiao ESP32C3:
- D0: NeoPixel LED
- D6: Rotary Encoder CLK
- D7: Rotary Encoder DT  
- D9: Button (with internal pull-up)
- SCL: I2C Clock (shared by OLED and Accelerometer)
- SDA: I2C Data (shared by OLED and Accelerometer)
```

---

## Software Features

### Core Requirements
- Three difficulty settings selectable via rotary encoder
- Five possible moves (LEFT, RIGHT, UP, DOWN, SHAKE)
- Countdown timer displayed in milliseconds
- Ten levels with progressively shorter time limits
- Game Over screen when player fails
- Game Win screen when all 10 levels are completed
- Accelerometer calibration on startup (60-sample averaging)
- NeoPixel LED with multiple colors for different game states
- Restart capability without power cycling

### Extra Credit Features
- **Scoring System** (+2 pts): 10 points per level, displayed during gameplay and on results screen
- **Animated Splash Screen** (+2 pts): ASCII stick figure animation on boot (only plays once per power-on)
- **High Score Board** (+8 pts): Saves top 3 scores with 3-letter initials to microcontroller's non-volatile memory (NVM), persists across restarts

**Total Extra Credit: +12 points**

### NeoPixel Color Indicators
- **Orange**: Difficulty selection menu
- **Yellow**: Calibrating or entering high score initials
- **Blue**: Game starting
- **Purple**: Waiting for player move
- **Green**: Correct move detected
- **Red**: Wrong move or timeout
- **Cyan**: Displaying high scores
- **Flashing Yellow**: Victory celebration

---

## Game Logic

### Difficulty System
Each difficulty level affects the initial time limit and how quickly it decreases:
- **Easy**: Starts at 2 seconds, reduces by 100ms each level (minimum 800ms)
- **Medium**: Starts at 1.5 seconds, reduces by 150ms each level (minimum 800ms)
- **Hard**: Starts at 1.2 seconds, reduces by 200ms each level (minimum 800ms)

### Movement Detection
The ADXL345 accelerometer measures acceleration on X, Y, and Z axes. After calibration, movements are detected using these thresholds:
- **LEFT**: X-axis < -4.5 m/s²
- **RIGHT**: X-axis > 4.5 m/s²
- **UP**: Z-axis > 5.0 m/s²
- **DOWN**: Z-axis < -5.0 m/s²
- **SHAKE**: Any axis exceeds ±7 m/s² or ±12 m/s²

### High Score Storage
High scores are stored in the ESP32's non-volatile memory (NVM) in the first 18 bytes:
- Each entry uses 6 bytes: 2 bytes for score (big-endian) + 3 bytes for initials (ASCII)
- Data persists through power cycles and code updates
- Scores are sorted in descending order, keeping only the top 3

---

## Enclosure Design

### Design Philosophy
The enclosure was designed to be simple, functional, and easy to manufacture while meeting all project requirements. The goal was to create a clean, minimalist box that houses all components securely while providing easy access for maintenance.

### Design Features

**Top Surface (Interactive Panel)**
- Rectangular cutout for the OLED display, positioned for clear viewing
- Hole for the rotary encoder shaft with enough clearance for smooth rotation
- Hole for the push button, easily accessible with the thumb
- Small opening for the NeoPixel LED to shine through

**Side Panel**
- Cutout for the on/off toggle switch, positioned for easy access with the index finger
- Rectangular slot for the USB-C port on the Xiao ESP32C3, allowing programming and charging without opening the case

**All Other Surfaces**
- Completely smooth with no additional features
- Clean, minimalist aesthetic

**Internal Structure**
- Mounting posts or standoffs to secure the perfboard in place
- Adequate spacing to accommodate the LiPo battery below the perfboard
- Cable routing space to keep wires organized
- Removable lid (snap-fit or screw-secured) for easy access to electronics

### Manufacturing Approach
The enclosure is 3D printed using PLA, spray paint in grey. Theå design prioritizes:
- **Simplicity**: Basic box shape that's easy to print without complex supports
- **Functionality**: All necessary openings precisely positioned for components
- **Accessibility**: Removable lid allows quick access for troubleshooting or battery replacement
- **Durability**: Adequate wall thickness to protect internal components

### Design Constraints Met
- USB-C connector accessible without disassembly
- On/off switch easily reachable
- Enclosure can be opened to access electronics
- All components securely housed

---

## Author
[Davi Dai]  
[TECHIN 512 B Au 25: Introduction To Sensors And Circuits]
[Dec 9 2025]