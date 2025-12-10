import time
import board
import digitalio
import displayio
import terminalio
from adafruit_display_text import label
import i2cdisplaybus
import adafruit_displayio_ssd1306
import adafruit_adxl34x
import neopixel
import random
import microcontroller
from rotary_encoder import RotaryEncoder

displayio.release_displays()

# --- Init hardware ---
i2c = board.I2C()
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
pixels = neopixel.NeoPixel(board.D0, 1, brightness=0.1, auto_write=True)
acc = adafruit_adxl34x.ADXL345(i2c)
btn = digitalio.DigitalInOut(board.D9)
btn.switch_to_input(pull=digitalio.Pull.UP)
encoder = RotaryEncoder(board.D7, board.D6, debounce_ms=3, pulses_per_detent=3)

# --- Move symbols (NEW FORMAT) ---
MOVE_SYMBOLS = {
    "LEFT": "<- LEFT",
    "RIGHT": "RIGHT ->",
    "UP": "^ UP",
    "DOWN": "v DOWN",
    "SHAKE": "~ SHAKE"
}

# --- Splash screen ---
first_boot = True

if first_boot:
    splash = displayio.Group()
    
    text1 = label.Label(terminalio.FONT, text=" O", color=0xFFFFFF)
    text1.anchor_point = (0.5, 0.5)
    text1.anchored_position = (50, 20)
    splash.append(text1)
    
    text2 = label.Label(terminalio.FONT, text="/|\\", color=0xFFFFFF)
    text2.anchor_point = (0.5, 0.5)
    text2.anchored_position = (50, 28)
    splash.append(text2)
    
    text3 = label.Label(terminalio.FONT, text="/ \\", color=0xFFFFFF)
    text3.anchor_point = (0.5, 0.5)
    text3.anchored_position = (50, 36)
    splash.append(text3)
    
    title = label.Label(terminalio.FONT, text="MOTION GAME", color=0xFFFFFF)
    title.anchor_point = (0.5, 0.5)
    title.anchored_position = (64, 50)
    splash.append(title)
    
    display.root_group = splash
    pixels[0] = (255, 0, 0)
    time.sleep(0.3)
    
    splash = displayio.Group()
    
    text1 = label.Label(terminalio.FONT, text="O", color=0xFFFFFF)
    text1.anchor_point = (0.5, 0.5)
    text1.anchored_position = (64, 20)
    splash.append(text1)
    
    text2 = label.Label(terminalio.FONT, text="/|\\", color=0xFFFFFF)
    text2.anchor_point = (0.5, 0.5)
    text2.anchored_position = (64, 28)
    splash.append(text2)
    
    text3 = label.Label(terminalio.FONT, text="/ \\", color=0xFFFFFF)
    text3.anchor_point = (0.5, 0.5)
    text3.anchored_position = (64, 36)
    splash.append(text3)
    
    title = label.Label(terminalio.FONT, text="MOTION GAME", color=0xFFFFFF)
    title.anchor_point = (0.5, 0.5)
    title.anchored_position = (64, 50)
    splash.append(title)
    
    display.root_group = splash
    pixels[0] = (0, 255, 0)
    time.sleep(0.3)
    
    splash = displayio.Group()
    
    text1 = label.Label(terminalio.FONT, text="O ", color=0xFFFFFF)
    text1.anchor_point = (0.5, 0.5)
    text1.anchored_position = (78, 20)
    splash.append(text1)
    
    text2 = label.Label(terminalio.FONT, text="/|\\", color=0xFFFFFF)
    text2.anchor_point = (0.5, 0.5)
    text2.anchored_position = (78, 28)
    splash.append(text2)
    
    text3 = label.Label(terminalio.FONT, text="/ \\", color=0xFFFFFF)
    text3.anchor_point = (0.5, 0.5)
    text3.anchored_position = (78, 36)
    splash.append(text3)
    
    title = label.Label(terminalio.FONT, text="MOTION GAME", color=0xFFFFFF)
    title.anchor_point = (0.5, 0.5)
    title.anchored_position = (64, 50)
    splash.append(title)
    
    display.root_group = splash
    pixels[0] = (0, 0, 255)
    time.sleep(0.3)
    
    splash = displayio.Group()
    
    text1 = label.Label(terminalio.FONT, text="O", color=0xFFFFFF)
    text1.anchor_point = (0.5, 0.5)
    text1.anchored_position = (64, 20)
    splash.append(text1)
    
    text2 = label.Label(terminalio.FONT, text="/|\\", color=0xFFFFFF)
    text2.anchor_point = (0.5, 0.5)
    text2.anchored_position = (64, 28)
    splash.append(text2)
    
    text3 = label.Label(terminalio.FONT, text="/ \\", color=0xFFFFFF)
    text3.anchor_point = (0.5, 0.5)
    text3.anchored_position = (64, 36)
    splash.append(text3)
    
    title = label.Label(terminalio.FONT, text="MOTION GAME", color=0xFFFFFF)
    title.anchor_point = (0.5, 0.5)
    title.anchored_position = (64, 50)
    splash.append(title)
    
    display.root_group = splash
    pixels[0] = (255, 255, 0)
    time.sleep(0.3)
    
    first_boot = False

# --- Display setup ---
root = displayio.Group()
display.root_group = root

line1 = label.Label(terminalio.FONT, text="")
line1.anchor_point = (0.5, 0.5)
line1.anchored_position = (64, 20)
root.append(line1)

line2 = label.Label(terminalio.FONT, text="")
line2.anchor_point = (0.5, 0.5)
line2.anchored_position = (64, 35)
root.append(line2)

line3 = label.Label(terminalio.FONT, text="")
line3.anchor_point = (0.5, 0.5)
line3.anchored_position = (64, 50)
root.append(line3)

# --- Button helper ---
def wait_button_press():
    while btn.value:
        time.sleep(0.01)
    time.sleep(0.05)
    while not btn.value:
        time.sleep(0.01)
    time.sleep(0.05)

# --- High score functions ---
def load_highscores():
    try:
        data = microcontroller.nvm[0:18]
        scores = []
        for i in range(3):
            score = (data[i*6] << 8) | data[i*6 + 1]
            name = ""
            for j in range(3):
                char_val = data[i*6 + 2 + j]
                if char_val >= 65 and char_val <= 90:
                    name += chr(char_val)
                else:
                    name += "A"
            if score != 0xFFFF and score != 0:
                scores.append((score, name))
        if len(scores) == 0:
            return [(0, "AAA"), (0, "AAA"), (0, "AAA")]
        while len(scores) < 3:
            scores.append((0, "AAA"))
        return scores
    except:
        return [(0, "AAA"), (0, "AAA"), (0, "AAA")]

def save_highscores(scores):
    data = bytearray(18)
    for i in range(3):
        score, name = scores[i]
        data[i*6] = (score >> 8) & 0xFF
        data[i*6 + 1] = score & 0xFF
        for j in range(3):
            data[i*6 + 2 + j] = ord(name[j])
    microcontroller.nvm[0:18] = data

def enter_initials():
    initials = ["A", "A", "A"]
    current_letter = 0
    
    line1.text = "Enter Initials"
    pixels[0] = (255, 255, 0)
    
    last_pos = encoder.position
    
    while current_letter < 3:
        display_name = ""
        for i in range(3):
            if i == current_letter:
                display_name += "[" + initials[i] + "]"
            else:
                display_name += " " + initials[i] + " "
        
        line2.text = display_name
        line3.text = "Press to confirm"
        
        if encoder.update():
            pos = encoder.position
            if pos != last_pos:
                last_pos = pos
                letter_idx = pos % 26
                initials[current_letter] = chr(ord("A") + letter_idx)
        
        if not btn.value:
            wait_button_press()
            current_letter += 1
            pixels[0] = (0, 255, 0)
            time.sleep(0.2)
            pixels[0] = (255, 255, 0)
        
        time.sleep(0.001)
    
    return "".join(initials)

# --- Main game loop ---
while True:
    # --- Select difficulty ---
    difficulties = ["Easy", "Medium", "Hard"]
    difficulty_times = [2000, 1500, 1200]
    time_decrease = [100, 150, 200]
    
    pixels[0] = (255, 165, 0)
    
    last_pos = encoder.position
    idx = 0
    
    while True:
        display_text = ""
        for i in range(len(difficulties)):
            if i == idx:
                display_text += "<" + difficulties[i] + ">"
            else:
                display_text += " " + difficulties[i] + " "
        
        line1.text = "Select"
        line2.text = "Difficulty"
        line3.text = display_text
        
        if encoder.update():
            pos = encoder.position
            if pos != last_pos:
                last_pos = pos
                idx = pos % len(difficulties)
        
        if not btn.value:
            wait_button_press()
            break
        
        time.sleep(0.001)
    
    base_time = difficulty_times[idx]
    time_dec = time_decrease[idx]
    
    # --- Calibration ---
    line1.text = ""
    line2.text = "Calibrating..."
    line3.text = ""
    pixels[0] = (255, 255, 0)
    
    bx = by = bz = 0.0
    for _ in range(60):
        x, y, z = acc.acceleration
        bx += x
        by += y
        bz += z
        time.sleep(0.005)
    bx /= 60
    by /= 60
    bz /= 60
    
    # --- Detect move ---
    def detect_move():
        x, y, z = acc.acceleration
        x -= bx
        y -= by
        z -= bz
        
        if abs(x) > 7 or abs(y) > 7 or abs(z) > 12:
            return "SHAKE"
        if x > 4.5:
            return "RIGHT"
        if x < -4.5:
            return "LEFT"
        if z > 5.0:
            return "UP"
        if z < -5.0:
            return "DOWN"
        return None
    
    # --- Get Ready ---
    line1.text = "Get Ready!"
    line2.text = ""
    line3.text = ""
    pixels[0] = (0, 100, 255)
    time.sleep(1.5)
    
    # --- Play 10 levels ---
    moves = ["LEFT", "RIGHT", "UP", "DOWN", "SHAKE"]
    level = 1
    max_level = 10
    score = 0
    game_won = False
    
    while level <= max_level:
        target = random.choice(moves)
        time_limit = max(800, base_time - (level - 1) * time_dec)
        t_end = time.monotonic() + time_limit / 1000.0
        
        pixels[0] = (100, 0, 255)
        
        success = False
        while True:
            time_left = max(0, int((t_end - time.monotonic()) * 1000))
            line1.text = "Lv" + str(level) + " Score:" + str(score)
            line2.text = MOVE_SYMBOLS[target]
            line3.text = str(time_left) + " ms"
            
            move = detect_move()
            if move == target:
                pixels[0] = (0, 255, 0)
                score += 10
                line1.text = ""
                line2.text = "Correct!"
                line3.text = "+10 points"
                success = True
                time.sleep(0.8)
                break
            
            if time_left <= 0:
                pixels[0] = (255, 0, 0)
                line1.text = ""
                line2.text = "Time's Up!"
                line3.text = ""
                time.sleep(1.5)
                break
            
            time.sleep(0.02)
        
        if not success:
            break
        
        level += 1
    
    # --- Game result ---
    if level > max_level:
        game_won = True
    
    if game_won:
        line1.text = "YOU WIN!"
        line2.text = "Final Score"
        line3.text = str(score) + " points"
        pixels[0] = (255, 255, 0)
        for _ in range(3):
            pixels[0] = (255, 255, 0)
            time.sleep(0.3)
            pixels[0] = (0, 0, 0)
            time.sleep(0.3)
        pixels[0] = (255, 255, 0)
    else:
        line1.text = "GAME OVER"
        line2.text = "Score: " + str(score)
        line3.text = ""
        pixels[0] = (255, 50, 0)
    
    time.sleep(2)
    
    # --- Check for high score ---
    highscores = load_highscores()
    is_highscore = score > highscores[2][0]
    
    if is_highscore and score > 0:
        line1.text = "NEW"
        line2.text = "HIGH SCORE!"
        line3.text = str(score) + " pts"
        pixels[0] = (255, 0, 255)
        time.sleep(2)
        
        player_name = enter_initials()
        
        highscores.append((score, player_name))
        highscores.sort(reverse=True, key=lambda x: x[0])
        highscores = highscores[:3]
        save_highscores(highscores)
    
    # --- Show high score board ---
    line1.text = "HIGH SCORES"
    line2.text = ""
    line3.text = ""
    pixels[0] = (0, 255, 255)
    time.sleep(1.5)
    
    highscores = load_highscores()
    for i in range(3):
        line1.text = str(i+1) + ". " + highscores[i][1]
        line2.text = str(highscores[i][0]) + " points"
        line3.text = ""
        time.sleep(1.5)
    
    line1.text = "Press to"
    line2.text = "play again"
    line3.text = ""
    pixels[0] = (255, 165, 0)
    
    # --- Wait for restart ---
    wait_button_press()