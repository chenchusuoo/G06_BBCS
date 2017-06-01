from microbit import*
while True:
    presses= button_a.get_presses()
    if presses > 5:
        display.show(Image.ANGRY)
    sleep(2000)
