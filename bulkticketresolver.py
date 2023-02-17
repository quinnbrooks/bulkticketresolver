import time
import pyautogui
import pymsgbox

pymsgbox.alert("SolarWinds bulk ticket resolver. Devoloped by: Quinn Brooks")
pymsgbox.alert("This program has been specially designed for a 2560x1600 resolution screen running Google Chrome. After reading this message, you will be prompted to enter your ticket numbers. You will then have two seconds to quickly switch to Google Chrome in full screen mode, which should be pulled up on service desk page of your SolarWinds ticketing system.")


# Get user input
nums = input("Please enter, separated by commas, the ticket number(s) you want to resolve: ")

# Split the comma-separated numbers into a list
num_list = nums.split(',')

# Loop through the list of numbers
for num in num_list:
    # Wait 5 secs
    time.sleep(2)

    # Move mouse to x=1193 y=100 and left click
    pyautogui.moveTo(1193, 100, duration=0.1)
    pyautogui.click()
    time.sleep(.5)
    # Type the user input
    pyautogui.typewrite(num)

    # Press enter
    pyautogui.press('enter')
    time.sleep(1.2)
    # Move mouse to x=416 y=341 and left click
    # Edit durtation according to network speed
    pyautogui.moveTo(230, 321, duration=1)
    pyautogui.click()

    time.sleep(1.2)

    # Edit durtation accorresolveding to network speed
    pyautogui.moveTo(302, 170, duration=0)
    pyautogui.click()
    pyautogui.typewrite("resolve")
    pyautogui.moveTo(403,284, duration=0.4)
    time.sleep(.15)
    pyautogui.click()
    pyautogui.moveTo(1075,762, duration=0.4)
    pyautogui.click()
    pyautogui.moveTo(34,165, duration=0.4)
    pyautogui.click()