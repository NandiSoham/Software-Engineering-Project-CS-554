import unittest
import time
from keyboard_input_simulator import press_key, release_key, KEY_W

class TestKeyboardFunctions(unittest.TestCase):

    def test_press_and_release_key(self):
        # Test pressing and releasing the 'W' key
        press_key(KEY_W)
        time.sleep(1)  
        release_key(KEY_W)

    def test_press_and_release_key_multiple_times(self):
        # Test pressing and releasing the 'W' key multiple times
        for _ in range(3):  
            press_key(KEY_W)
            time.sleep(0.5)  
            release_key(KEY_W)
            time.sleep(0.5)  

    

if __name__ == '__main__':
    unittest.main()
