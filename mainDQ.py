import pyautogui
import time
from orderHotDog import order
# Adds a pause between all actions
pyautogui.PAUSE = .03
# Moving mouse to upper-left will abort program when true
pyautogui.FAILSAFE = True

# Function continually prints out the current mouse X,Y coords for quick prototyping
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionString, end='')
#         print('\b' * len(positionString), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

#######################################
# Coords Based on 1024 x 768 Register monitor #
#######################################

# Only needs to be done once a day.
## Login (x4) 8888
## 503, 256
## Set drawer if needed
## 595, 393 -- "ok" button on login screen
## 812, 27 -- Manager Functions
## 510, 178 -- Manage Drawers
## 145, 80 -- CD1 - Counter Left
## 87, 729 -- Assign Drawer
## 381, 338 -- Name of person to assign to (employee "***"
## 419, 234 (1) - 508 447 (00) - 508 447 (00) -- Set bank amount, Bank = $100
## 442, 572 Ok on bank amount
## 932, 724 -- Close drawer management
## 358, 101 -- Select Menu


def main():
    # add functions here
    order(3000) # orders Hot Dogs X times

if __name__ == '__main__':
    pyautogui.alert('Ensure Brink is at the main menu where the salad button is visible!')
    start_time = time.time() #getting what the current time is, and saving variable
    main()
    print("--- %s seconds to execute 3000 orders in main --- " % (time.time() - start_time)) 
    #current time -prev time
    # to show what the total time was when the program finishes


