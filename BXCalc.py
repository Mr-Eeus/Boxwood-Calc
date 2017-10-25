# CURRENT STATUS | MAY 15, 2017 |
#
# PROGRAM RUNS CORRECTLY FOR SETINFO FUNCTION, MATH IS CORRECT. NEED TO REPEAT
# FOR PLANTER AND FRAME.

# Currently Still Need :
# Boxwood Set Info ----- COMPLETED -----
# Planter Set Info ----- COMPLETED -----
# Frame Set Info   ----- COMPLETED -----
# Pricing Calculations ----- COMPLETED IN EXCEL -----
# Pricing Total ----- (Jannah currently working on this in excel. If it can be done in program, attempt.)
# Quit Option
# Executable Version ----- COMPLETED -----


import os

PORT = os.getenv("PORT", "8080")
HOST = os.getenv("IP", "0.0.0.0")

print('Welcome to the Boxwood Calculation Beta. Please enter all dimensions in '
      'inches.')

BOXH = 0
BOXW = 0
BOXD = 0

PLANH = 0
PLANW = 0
PLAND = 0

FRAMEH = 0
FRAMEW = 0
FRAMED = 0


def setBXInfo():
    BOXH = float(input('Please enter the Height of your boxwood, from top to'
                       ' bottom of the Boxwood:  '))
    BOXW = float(input('Please enter the Width, or length, of your boxwood:  '))
    BOXD = float(input('Please enter the Depth of your boxwood:  '))

    widep = float(BOXW / 12) * (BOXD / 12)
    hidep = float(BOXH / 12) * (BOXD / 12)
    hiwi = float(BOXH / 12) * (BOXW / 12)
    total = 0.0

    hidep += hidep
    hiwi += hiwi

    total += float(round(widep + hidep + hiwi, 2))
    print('--' * 45 + '\n')
    print('The total square footage of the BOXWOOD is:  {}'.format(total))
    print('--' * 45 + '\n')


def setPLInfo():
    PLANH = float(input('Please enter the Height of your planter, from top to'
                        ' bottom of planter (exterior):  '))
    PLANW = float(input('Please enter the Width, or length, of your planter (exterior):  '))
    PLAND = float(input('Please enter the Depth of your planter (exterior):  '))

    widep = float(PLANW / 12) * (PLAND / 12)
    hidep = float(PLANH / 12) * (PLAND / 12)
    hiwi = float(PLANH / 12) * (PLANW / 12)
    total = 0.0

    hidep += hidep
    hiwi += hiwi

    total += float(round(widep + hidep + hiwi, 2))
    print('--' * 45 + '\n')
    print('The total square footage of the PLANTER is:  {}'.format(total))
    print('--' * 45 + '\n')


def setFRInfo():
    FRAMEH = float(input(
        'Please enter the Height of your boxwood from the TOP of the boxwood, to the bottom of the planter (interior):  '))
    FRAMEW = float(input('Please enter the Width, or length, of your boxwood from side to side (interior):  '))
    FRAMED = float(input('Please enter the Depth of your planter, from front to back (interior):  '))

    widep = float(FRAMEW / 12) * (FRAMED / 12)
    hidep = float(FRAMEH / 12) * (FRAMED / 12)
    hiwi = float(FRAMEH / 12) * (FRAMEW / 12)
    total = 0.0

    hidep += hidep
    hiwi += hiwi

    total += float(round(widep + hidep + hiwi, 2))
    print('--' * 45 + '\n')
    print('The total square footage of the FRAME is:  {}'.format(total))
    print('--' * 45 + '\n')


try:
    setBXInfo()
    setPLInfo()
    setFRInfo()
except ValueError:
    print('\nSorry, not all of your answers were numbers. Please try again.')
    setBXInfo()
    setPLInfo()
    setFRInfo()

GLOBALQUIT = input('Thank you. Press any key to exit.')

if GLOBALQUIT == 'Q'.lower():
    quit

