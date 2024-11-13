import time
import pyautogui
import webbrowser

def switch_subscription(channel_name):

  chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

  # webbrowser.get(chrome_path).open(url4)
  webbrowser.open_new_tab("https://youtube.com")

  #open new tab
  # pyautogui.hotkey("ctrl", "t")

  time.sleep(5)
  x, y = pyautogui.locateCenterOnScreen("yt_search_btn.png", confidence=0.5)
  pyautogui.moveTo(x, y, 1)
  pyautogui.click()

  pyautogui.write(channel_name)
  pyautogui.hotkey("enter")

  time.sleep(3)
  x, y = pyautogui.locateCenterOnScreen("mr_beast_logo.png", confidence=0.5)
  pyautogui.moveTo(x, y, 1)
  pyautogui.click()

  time.sleep(2)
  # Attempt to locate the first image
  try:
    x, y = pyautogui.locateCenterOnScreen("unsuscribe_btn.png", confidence=0.8)
  except pyautogui.ImageNotFoundException:
      # If the first image is not found, try the second image
      try:
          x, y = pyautogui.locateCenterOnScreen("subscribe_btn.png", confidence=0.8)
      except pyautogui.ImageNotFoundException:
          print("Neither image was found on the screen.")
      else:
          # If the second image is found, move to and click it
          pyautogui.moveTo(x, y, 1)
          pyautogui.click()
          time.sleep(2)
          pyautogui.hotkey("ctrl", "w")
  else:
      # If the first image is found, move to and click it
      pyautogui.moveTo(x, y, 1)
      pyautogui.click()
      time.sleep(1)
      unsuscribe_btn_menu = pyautogui.locateCenterOnScreen("unsuscribe_btn_menu.png", confidence=0.8)
      x, y = unsuscribe_btn_menu
      pyautogui.moveTo(x, y, 1)
      pyautogui.click()
      time.sleep(1)
      unsuscribe_btn_menu_dialog = pyautogui.locateCenterOnScreen("unsuscribe_btn_menu_dialog.png", confidence=0.7)
      x, y = unsuscribe_btn_menu_dialog
      pyautogui.moveTo(x, y, 1)
      pyautogui.click()
      time.sleep(2)
      pyautogui.hotkey("ctrl", "w")

# Run the function every minute
while True:
    channel_name=pyautogui.prompt(text="",title="Enter channel name")
    switch_subscription("channel_name")
    time.sleep(60)

