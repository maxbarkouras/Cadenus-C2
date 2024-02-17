def keystroke():
    from pynput.keyboard import Key, Controller
    stroke = raw.replace('<keys> ', '')
    if 'GUI' in stroke:
        keyboard.press(Key.cmd)
        keyboard.type((stroke.replace('GUI ', '')))
        keyboard.release(Key.cmd)
    elif 'CTRL' in stroke:
        keyboard.press(Key.ctrl)
        keyboard.type((stroke.replace('CTRL ', '')))
        keyboard.release(Key.ctrl)
    elif 'ALT' in stroke:
        keyboard.press(Key.alt)
        key = (stroke.replace('ALT ', ''))
        if key == 'F4' or 'f4':
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
            keyboard.release(Key.alt)
        else:
            keyboard.type((stroke.replace('ALT ', '')))
            keyboard.release(Key.alt)
    elif 'SHIFT' in stroke:
        keyboard.press(Key.shift)
        keyboard.type((stroke.replace('SHIFT ', '')))
        keyboard.release(Key.shift)
    elif 'ENTER' in stroke:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif 'DEL' in stroke:
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    else:
        keyboard.type(stroke)