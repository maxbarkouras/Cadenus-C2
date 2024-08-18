# Cadenus C2 - C2 Framework Written in Python

Cadenus-C2 is a single connection C2 platform written in Python with a dense feature set that is always growing and changing. Feature list can be shown with HELP command, all commands entered that are not feature commands will be executed on the target system. Beacon is currently windows only, connection will bind and normal bash commands will execute but special commands will not work.

## Features

- Includes keystroke injection, download, upload, screenshot, and more
- Stealth and sleep mode to help evade detection
- Easy to use CLI

## Getting Started

Follow these simple steps to get Cadenus-C2 up and running:

### Prerequisites

1. Python 3.x installed on your system

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/maxbarkouras/cadenus-c2.git
   ```

2. `cd` into the directory:

   ```bash
   cd cadenus-c2
   ```

3. Install library requirements with pip

   ```bash
   pip3 install -r requirements.txt
   ```

4. Change HOST and PORT in cadenus-c2.py and beacon.py:

5. Start C2 and run HELP when connected!

   ```bash
   python3 c2.py
   ```

### Note

Beacon contains multiple non-native libraries, so you must compile into a PE (using pyinstaller) or ship with external modules

---

Happy hacking!!!
