#!/usr/bin/env python3
"""Screenshot Tool - Capture screenshots from command line."""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

def take_screenshot(save_path=None, fullscreen=True):
    if save_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = Path.home() / f"screenshot_{timestamp}.png"
    else:
        save_path = Path(save_path)
    
    system = sys.platform
    
    try:
        if system == 'darwin':  # macOS
            cmd = ['screencapture', '-x', str(save_path)]
        elif system == 'linux':
            if subprocess.run(['which', 'gnome-screenshot'], capture_output=True).returncode == 0:
                cmd = ['gnome-screenshot', '-f', str(save_path)]
            elif subprocess.run(['which', 'scrot'], capture_output=True).returncode == 0:
                cmd = ['scrot', str(save_path)]
            else:
                # Try import (macOS/Linux with GUI)
                raise ImportError
        else:  # Windows
            import win32gui, win32ui, win32con
            hwnd = win32gui.GetDesktopWindow()
            dc = win32gui.GetWindowDC(hwnd)
            mi = win32ui.CreateBITMAPINFO()
            mi['bmiHeader']['biWidth'] = win32gui.GetSystemMetrics(win32con.SM_CXSCREEN)
            mi['bmiHeader']['biHeight'] = -win32gui.GetSystemMetrics(win32con.SM_CYSCREEN)
            mi['bmiHeader']['biPlanes'] = 1
            mi['bmiHeader']['biBitCount'] = 32
            bmp = win32ui.CreateBitmap()
            bmp.CreateCompatibleBitmap(dc, mi['bmiHeader']['biWidth'], abs(mi['bmiHeader']['biHeight']))
            bmp.BitBlt((0, 0), (mi['bmiHeader']['biWidth'], abs(mi['bmiHeader']['biHeight'])), dc, (0, 0), win32con.SRCCOPY)
            bmp.SaveBitmapFile(dc, str(save_path))
            win32gui.ReleaseDC(hwnd, dc)
            print(f"✓ Saved: {save_path}")
            return
        
        subprocess.run(cmd, check=True)
        print(f"✓ Saved: {save_path}")
    except ImportError:
        # Fallback: PIL screenshot (requires pyautogui)
        try:
            import pyautogui
            pyautogui.screenshot(save_path).save(save_path)
            print(f"✓ Saved: {save_path}")
        except ImportError:
            print("Error: Install pyautogui or use native screenshot tool")
            sys.exit(1)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Take a screenshot')
    parser.add_argument('--output', '-o', help='Output file path')
    args = parser.parse_args()
    take_screenshot(args.output)