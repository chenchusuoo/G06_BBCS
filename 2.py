from microbit import*
boat = Image("90009:"
             "90009:"
             "90909:"
             "99099:"
             "90990:")
boat2= Image("00000:"
             "00000:"
             "99999:"
             "09990:"
             "09900:")
allboat = [boat, boat2]             
             
while True:
    display.show(allboat, delay =300)
