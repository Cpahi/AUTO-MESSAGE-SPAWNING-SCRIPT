import pyautogui
import time 

try:
   print ("--------Welcome to this basic Auto Message Spawning(AMS) script---------\n |||||||||please note that this program messages to any interface wherever your cursor is placed after 60 seconds of running the final step (step2)||||||||||| ")



   message = input("STEP 1: Enter the message you want to send:\n")
   frequency = int(input("STEP 2: Enter the number of times you want to send this message:\n"))
    
   if frequency <= 0:
        raise ValueError("Frequency must be a positive integer.")

   print("Place your cursor at the point of deployment. Messages will start spawning in 60 seconds after running this code.")
   time.sleep(60)

   for i in range(frequency):
        pyautogui.typewrite(message, interval=0)
        pyautogui.press("enter")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Script completed.")