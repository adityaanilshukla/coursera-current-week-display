# Coursera UOL Comp Science Week Checker

## Overview

This Python script fetches and displays the current week of the Coursera UOL Computer Science module from the [world-class/REPL](https://github.com/world-class/REPL) repository.

## Features

- Retrieves the current week information from the GitHub page.
- Displays the week number in a Tkinter window on startup.

## Requirements

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `tkinter`

Install the required packages using the following command:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python week_checker.py
```

The script will display a Tkinter window showing the current week of the Coursera UOL Computer Science module.

## Customization

- Adjust the transparency, font, and colors in the `show_week_window` function to suit your preferences.

## Adding to Windows Startup

To add the script to your Windows startup:

1. Convert the script to an executable using PyInstaller:

    ```bash
    pyinstaller --onefile --noconsole week_checker.py
    ```

2. Copy the generated executable to a safe location.
3. Press `Win + R` to open the Run dialog.
4. Type `shell:startup` and press Enter. This opens the Startup folder.
5. Copy your executable file into this folder.

## Windows Defender Exclusion

If Windows Defender flags the executable as suspicious:

1. Open Windows Security.
2. Go to "Virus & Threat Protection."
3. Under "Virus & Threat Protection Settings," click "Manage Settings."
4. Scroll down to "Exclusions" and click "Add or remove exclusions."
5. Click on "Add an exclusion" and select "File."
6. Browse to the location of your executable and add it to the exclusions.

This should prevent Windows Defender from blocking your executable.

