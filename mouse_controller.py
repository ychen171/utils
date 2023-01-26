import pyautogui
import time
import sys

def move_click_return(t_x=0, t_y=0):
    target_x = t_x
    target_y = t_y

    print('Screen Resolution: {0}'.format(pyautogui.size()))
    
    (original_x, original_y) = pyautogui.position()
    print('Original Cursor Position: ({0}, {1})').format(original_x, original_y)

    print('Cursor Clicking at: ({0}, {1})'.format(target_x, target_y))
    pyautogui.click(target_x, target_y)
    print('Current Cursor Position: {0}'.format(pyautogui.position()))

    print('Moving back to Position: ({0}, {1})'.format(original_x, original_y))
    pyautogui.moveTo(original_x, original_y)
    print('Current Cursor Position: {0}'.format(pyautogui.position()))

def move_return(t_x=0, t_y=0):
    target_x = t_x
    target_y = t_y
    print('Screen Resolution: {0}'.format(pyautogui.size()))

    (original_x, original_y) = pyautogui.position()
    print('Original Cursor Position: ({0}, {1})'.format(original_x, original_y))

    print('Moving to ({0}, {1})'.format(target_x, target_y))
    pyautogui.moveTo(target_x, target_y)
    print('Current Cursor Position: {0}'.format(pyautogui.position()))

    print('Moving back to ({0}, {1})'.format(original_x, original_x))
    pyautogui.moveTo(original_x, original_y)
    print('Current Cursor Position: {0}'.format(pyautogui.position()))

def main(time_interval=5, target_x=0, target_y=0):
    while True:
        print('--------------------------------------------')
        (before_x, before_y) = pyautogui.position()
        time.sleep(time_interval)
        (after_x, after_y) = pyautogui.position()
        if ((before_x, before_y) == (after_x, after_y)):
            print('Auto Clicking...')
            move_click_return(target_x, target_y)
        else:
            print('Cursor moved. Skip auto clicking...')

if (__name__ == '__main__'):
    time_interval = 120
    target_x = 0
    target_y = 640
    if (len(sys.argv) >= 4):
        time_interval = int(sys.argv[1])
        target_x = int(sys.argv[2])
        target_y = int(sys.argv[3])
    pyautogui.FAILSAFE = False
    main(time_interval, target_x, target_y)
