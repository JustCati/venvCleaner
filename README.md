# Virtual Environment Cleaner

## Description

This Python script automatically cleans up unused virtual environments from a specified directory. It identifies virtual environments linked to projects that no longer exist and deletes them. 

## Features

- Cleans up virtual environments from a default or user-specified directory.
- Ignores virtual environments listed in an ignore list.
- Periodically checks for unused virtual environments at a user-defined interval.

## Requirements

- Python 3.x
- `shutil` (standard library)
- `argparse` (standard library)

## Usage

```bash
python3 venvCleaner.py --path /path/to/virtualenvs --time 3600 --ignore-list env1 env2
```

### Arguments

- `--path`: (Optional) The directory where virtual environments are located. Defaults to `~/.local/share/virtualenvs`.
- `--time`: (Optional) Time in seconds between cleanup runs. Default is 3600 seconds (1 hour).
- `--ignore-list`: (Optional) Names of virtual environments to ignore during cleanup.

## Example

To run the script with a custom path and interval:

```bash
python3 venvCleaner.py --path /home/user/venvs --time 1800 --ignore-list myenv1 myenv2
```

## Setting up as a systemd Service

To run this script as a background service:

1. **Create a systemd service file**:
   ```bash
   sudo nano /etc/systemd/system/venv-cleaner.service
   ```

2. **Add the following configuration**:
   ```ini
   [Unit]
   Description=Virtual Environment Cleaner
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/venvCleaner.py --path /path/to/virtualenvs --time 3600 --ignore-list env1 env2
   Restart=always
   User=your-username
   WorkingDirectory=/path/to

   [Install]
   WantedBy=multi-user.target
   ```

   Replace `/path/to/venvCleaner.py` and `/path/to/virtualenvs` with the actual paths.

3. **Reload systemd and enable the service**:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable venv-cleaner.service
   sudo systemctl start venv-cleaner.service
   ```

4. **Check the service status**:
   ```bash
   sudo systemctl status venv-cleaner.service
   ```

## License

This script is provided under the MIT License.

--- 

Let me know if you need further customization!
