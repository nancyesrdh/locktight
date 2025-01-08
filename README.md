# LockTight

LockTight is a Python utility that enhances security by providing advanced configuration options for lock screen settings on Windows devices. It allows you to set the lock screen timeout, enable or disable the lock screen, and force the lock screen to activate immediately.

## Features

- **Set Lock Screen Timeout**: Customize the inactivity timeout duration before the lock screen is activated.
- **Toggle Lock Screen**: Enable or disable the lock screen functionality.
- **Force Lock Screen Activation**: Instantly activate the lock screen.

## Prerequisites

- Windows Operating System
- Python 3.x
- Administrator privileges are required to change lock screen settings.

## Usage

Run the script with the appropriate command:

### Set Lock Screen Timeout

```bash
python locktight.py set_timeout <seconds>
```

Replace `<seconds>` with the desired timeout duration in seconds.

### Toggle Lock Screen

```bash
python locktight.py toggle <enable|disable>
```

Use `enable` to turn on the lock screen or `disable` to turn it off.

### Force Lock Screen

```bash
python locktight.py lock_now
```

This command will immediately activate the lock screen.

## Note

Make sure to run the script with administrator privileges to apply changes to the lock screen settings.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.