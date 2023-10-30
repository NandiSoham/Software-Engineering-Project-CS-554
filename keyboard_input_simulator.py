import ctypes
import time


KEY_W = 0x11
KEY_A = 0x1E
KEY_S = 0x1F
KEY_D = 0x20
KEY_SPACE = 0x39

PTR_UL = ctypes.POINTER(ctypes.c_ulong)

class KeyboardEvent(ctypes.Structure):
    _fields_ = [
        ("virtual_key", ctypes.c_ushort),
        ("scan_code", ctypes.c_ushort),
        ("flags", ctypes.c_ulong),
        ("timestamp", ctypes.c_ulong),
        ("extra_info", PTR_UL)
    ]

class HardwareEvent(ctypes.Structure):
    _fields_ = [
        ("message", ctypes.c_ulong),
        ("param_low", ctypes.c_short),
        ("param_high", ctypes.c_ushort)
    ]

class MouseEvent(ctypes.Structure):
    _fields_ = [
        ("x_movement", ctypes.c_long),
        ("y_movement", ctypes.c_long),
        ("mouse_data", ctypes.c_ulong),
        ("flags", ctypes.c_ulong),
        ("timestamp", ctypes.c_ulong),
        ("extra_info", PTR_UL)
    ]

def press_key(key_code):
    input_event = create_input_event(key_code, 0x0008)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_event), ctypes.sizeof(input_event))

def release_key(key_code):
    input_event = create_input_event(key_code, 0x0008 | 0x0002)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_event), ctypes.sizeof(input_event))


if __name__ == '__main__':
    press_key(KEY_W)
    time.sleep(1)
    release_key(KEY_W)
    time.sleep(1)