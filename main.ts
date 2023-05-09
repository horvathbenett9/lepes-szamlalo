input.onButtonPressed(Button.AB, function () {
    steps = 0
    hang = 0
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.Shake, function () {
    hang += 1
    basic.clearScreen()
    steps += 1
    basic.showNumber(Math.round(steps / 10))
    music.ringTone(hang * 110)
    basic.pause(60)
    music.stopAllSounds()
    if (hang >= 10) {
        hang = 0
    }
    serial.writeValue("steps", steps)
    serial.writeValue("hang", hang)
})
let hang = 0
let steps = 0
steps = 0
hang = 0
basic.showIcon(IconNames.Heart)
