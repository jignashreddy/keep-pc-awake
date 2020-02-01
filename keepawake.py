import pyautogui as pd
try:
    while(True):
        pd.moveTo(100,100)
        pd.press('shift')
        pd.moveTo(1000,100)
        # if(KeyboardInterrupt):
        #     break
except (KeyboardInterrupt, SystemExit):
        raise
