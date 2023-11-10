import unittest
import time
from keyboard_input_simulator import press_key, release_key, KEY_W, KEY_A, KEY_D

class TestKeyboardFunctions(unittest.TestCase):
    
    def test_press_and_release_key(self):
        press_key(KEY_W)
        time.sleep(1)
        release_key(KEY_W)

    def test_press_and_release_different_keys(self):
        press_key(KEY_A)
        time.sleep(0.5)
        release_key(KEY_A)
        
        press_key(KEY_D)
        time.sleep(0.5)
        release_key(KEY_D)

if __name__ == '__main__':
    unittest.main()
