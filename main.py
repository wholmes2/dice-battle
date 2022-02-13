p1_roll = 0

def on_gesture_shake():
    global p1_roll
    p1_roll = randint(1, 6)
    soundExpression.slide.play()
    if p1_roll == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    if p1_roll == 2:
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . . . .
                        . # . . .
                        . . . . .
        """)
    if p1_roll == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    if p1_roll == 4:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
    if p1_roll == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    if p1_roll == 6:
        basic.show_leds("""
            . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
