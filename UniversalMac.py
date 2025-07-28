import time
import pyautogui

pyautogui.click(1031, 1547)  # Switch to BlueStacks!
while True:
    pyautogui.click(1031, 1547)  # Attack!
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(2085, 1278)  # Find a Match
    time.sleep(5)  # Wait for 5 second
    for i in range(5):
        pyautogui.keyDown('down') # Zoom out
    pyautogui.keyUp('down')  # Release the down key
    pyautogui.click(1093, 1578)  # Dragon!
    for i in range(17): 
        pyautogui.click(2347, 1207)  # Deploy Dragons at right corner!
    pyautogui.click(1364, 1580)  # Hero 1 Selection!
    pyautogui.click(2347, 1207)  # Deploy Hero 1 at right corner!
    pyautogui.click(1487, 1580)  # Hero 2 Selection!
    pyautogui.click(2347, 1207)  # Deploy Hero 2 at right corner!
    pyautogui.click(1608, 1580)  # Hero 3 Selection!
    pyautogui.click(2347, 1207)  # Deploy Hero 3 at right corner!
    pyautogui.click(1727, 1580)  # Hero 4 Selection!
    pyautogui.click(2347, 1207)  # Deploy Hero 4 at right corner!
    pyautogui.click(1364, 1580)  # Activate Hero 1 ability!
    pyautogui.click(1487, 1580)  # Activate Hero 2 ability!
    pyautogui.click(1608, 1580)  # Activate Hero 3 ability!
    pyautogui.click(1727, 1580)  # Activate Hero 4 ability!
    time.sleep(87)  # Wait for 87 seconds
    pyautogui.click(1043, 1438)  # Surrender
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(1905, 1340)  # Okay
    time.sleep(2)  # Wait for 2 second
    pyautogui.click(1719, 1531)  # Return Home!
    time.sleep(5)  # Wait for 5 seconds
    pyautogui.click(1652, 1152)  # Address Errors!
    time.sleep(9)  # Wait for 9 seconds