import time
import pyautogui

while True:
    pyautogui.click(1368, 1349)  # Attack!
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(2175, 1134)  # Find a Match
    time.sleep(5)  # Wait for 5 second
    for i in range(5):
        pyautogui.keyDown('down') # Zoom out
    pyautogui.click(1408, 1359)  # Dragon!
    for i in range(16): 
        pyautogui.click(2403, 1063)  # Deploy Dragons at right corner!
    # pyautogui.click(1619, 1363)  # Queen!
    # pyautogui.click(2403, 1063)  # Deploy Queen at right corner!
    # pyautogui.click(1619, 1363)  # Activate Queen ability!
    time.sleep(95)  # Wait for 95 seconds
    pyautogui.click(1371, 1263)  # Surrender
    time.sleep(1)  # Wait for 1 second
    pyautogui.click(2044, 1190)  # Okay
    time.sleep(2)  # Wait for 2 second
    pyautogui.click(1906, 1336)  # Return Home!
    time.sleep(4)  # Wait for 4 seconds
    try:
        reloadGame = pyautogui.locateOnScreen('RELOADGAME.png', confidence=0.8)  # Check if there is an error.
        pyautogui.click(reloadGame)  # If there is an error, click RELOAD GAME.
        time.sleep(9)  # Wait for 9 seconds
    except pyautogui.ImageNotFoundException:
        continue  # If no errors, proceed with the bot.
    try:
        tryAgain = pyautogui.locateOnScreen('TRYAGAIN.png', confidence=0.8)  # Check if there is an error.
        pyautogui.click(tryAgain)  # If there is an error, click TRY AGAIN.
        time.sleep(9)  # Wait for 9 seconds
    except pyautogui.ImageNotFoundException:
        continue  # If no errors, proceed with the bot.