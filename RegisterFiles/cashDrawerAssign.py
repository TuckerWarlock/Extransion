# Assign cash drawer
# Login > Clock in > Manager Functions > Assign drawer > Go to Menu

import pyautogui
import calculateCDPosition

def cashDrawerAssign():
    _reg = reg # new variable for register number

    pyautogui.click(812, 27) # Click Manager functions
    pyautogui.click(510, 178) # Click Manager drawers
            
    # Call to cash drawer grid
    _x, _y = calculateCoords(_reg) # returns coords for drawer click
    pyautogui.click(_x, _y) #click cash drawer grid

    pyautogui.click(87, 729) # Click Assign button
    pyautogui.click(381, 338) # Click top left available employee
    pyautogui.click(442, 572) # Click OK in Bank Amount
    pyautogui.click(932, 724) # Click Done in cash drawer assignments
    pyautogui.click(358, 101) # Select Menu for ordering