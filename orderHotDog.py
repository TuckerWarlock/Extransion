# Repeat ad nauseam 
# 1000 400 -- Salad button
# 800 275 -- Baja 
# Press down the row, increase Y by 113 each iteration (x6)
# 2400 1300 -- PAY / CLOSE ORDER
# 1600 400 -- Exact Cash Button
# Need to add a delay due to "contacting punch"
# Click anywhere again once (Change Due message)
# AND REPEAT AND REPEAT AND REPEAT AND REPEAT
##########################################################################################

import pyautogui
from time import sleep
# Click salad section,
# order each salad in first column,
# close order
# Function assumes you are at the main menu where the Green salad button is displayed
def order(orderIterations):
    try:
        for i in range(orderIterations):
            pyautogui.click(x=358, y=101) # Click menu button
            # pyautogui.click(x=800, y=275) # Click (Not needed for this layout)
            for i in range(2): # Iterate through all the rest of the salads. Each button is 113 pixels apart. 
                pyautogui.click(646,297) # Order Hot Dog
                pyautogui.click(646,297) # Order Hot Dog
            pyautogui.click(x=242, y=711) # Cash button, bottom of order lane
            pyautogui.click(x=552, y=572) # Done button
            sleep(1) # 1 second sleep while punchh does its thing
            pyautogui.click(x=901, y=378) # touch anywhere to "ok" the Change Due
    except TypeError:
        pyautogui.alert('Invalid operation!')