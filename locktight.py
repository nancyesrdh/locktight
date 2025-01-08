import ctypes
import winreg
import sys

class LockTight:
    def __init__(self):
        self.user32 = ctypes.windll.User32
        self.registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"

    def set_lock_screen_timeout(self, timeout_seconds: int) -> None:
        """
        Set the lock screen timeout.

        :param timeout_seconds: Timeout in seconds before the lock screen is activated.
        """
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.registry_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "InactivityTimeoutSecs", 0, winreg.REG_DWORD, timeout_seconds)
                print(f"Lock screen timeout set to {timeout_seconds} seconds.")
        except PermissionError:
            print("Administrator privileges are required to change lock screen settings.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def toggle_lock_screen(self, enable: bool) -> None:
        """
        Enable or disable the lock screen.

        :param enable: True to enable, False to disable.
        """
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.registry_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "DisableLockWorkstation", 0, winreg.REG_DWORD, 0 if enable else 1)
                state = "enabled" if enable else "disabled"
                print(f"Lock screen has been {state}.")
        except PermissionError:
            print("Administrator privileges are required to change lock screen settings.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def force_lock_screen(self) -> None:
        """
        Force the lock screen to activate immediately.
        """
        try:
            self.user32.LockWorkStation()
            print("Lock screen activated.")
        except Exception as e:
            print(f"An error occurred while locking the screen: {e}")

if __name__ == "__main__":
    locktight = LockTight()
    if len(sys.argv) < 2:
        print("Usage: locktight.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "set_timeout":
        if len(sys.argv) != 3:
            print("Usage: locktight.py set_timeout <seconds>")
        else:
            locktight.set_lock_screen_timeout(int(sys.argv[2]))
    elif command == "toggle":
        if len(sys.argv) != 3:
            print("Usage: locktight.py toggle <enable|disable>")
        else:
            locktight.toggle_lock_screen(sys.argv[2].lower() == "enable")
    elif command == "lock_now":
        locktight.force_lock_screen()
    else:
        print(f"Unknown command: {command}")