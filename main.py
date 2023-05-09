def on_button_pressed_ab():
    global steps, hang
    steps = 0
    hang = 0
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global hang, steps
    hang += 1
    basic.clear_screen()
    steps += 1
    basic.show_number(Math.round(steps / 10))
    music.ring_tone(hang * 110)
    basic.pause(60)
    music.stop_all_sounds()
    if hang >= 10:
        hang = 0
    serial.write_value("steps", steps)
    serial.write_value("hang", hang)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

hang = 0
steps = 0
steps = 0
hang = 0
basic.show_icon(IconNames.HEART)