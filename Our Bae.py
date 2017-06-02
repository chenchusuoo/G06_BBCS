from microbit import *
tank1 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000:")
tank2 = Image("00000:"
              "00000:"
              "90000:"
              "00000:"
              "00000:")
tank3 = Image("00000:"
              "00000:"
              "99000:"
              "00000:"
              "00000:")
tank4 = Image("00000:"
              "90000:"
              "99900:"
              "90000:"
              "90000:")
tank5 = Image("00000:"
              "99000:"
              "99990:"
              "99000:"
              "99000:")
tank6 = Image("00000:"
              "08800:"
              "99999:"
              "99900:"
              "99900:")
tank7 = Image("00000:"
              "00880:"
              "09999:"
              "09990:"
              "09990:")
tank8 = Image("00000:"
              "00088:"
              "00999:"
              "00999:"
              "00999:")
tank9 = Image("00000:"
              "00008:"
              "00099:"
              "00099:"
              "00099:")
tank10 = Image("00000:"
              "00000:"
              "00009:"
              "00009:"
              "00009:")
tank11 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000:")            

alltanks = [tank1, tank2, tank3, tank4, tank5, tank6, tank7, tank8, tank9, tank10, tank11]
while True:       
    if button_a.is_pressed():
        display.scroll("1818")
        display.scroll("Stamford Raffles")
        display.show(Image.STICKFIGURE)
    elif button_b.is_pressed():
        display.scroll("1942-1945")
        display.show(alltanks, delay=500)
        sleep(500)
        display.scroll('WWII')
    elif accelerometer.was_gesture('shake'):
        display.scroll("SG")
        display.show(Image.HEART)
