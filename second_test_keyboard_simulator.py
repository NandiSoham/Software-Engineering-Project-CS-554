import unittest
import time
from keyboard_input_simulator import press_key, release_key, KEY_W, KEY_A, KEY_D

def setUp():
    pass

def tearDown():
    pass

def test_press_and_release_key():
    press_key(KEY_W)
    time.sleep(1)
    release_key(KEY_W)

def test_press_and_release_different_keys():
    press_key(KEY_A)
    time.sleep(0.5)
    release_key(KEY_A)
    
    press_key(KEY_D)
    time.sleep(0.5)
    release_key(KEY_D)

if __name__ == '__main__':
    setUp()
    
    try:
        test_press_and_release_key()
        test_press_and_release_different_keys()
    finally:
        tearDown()
