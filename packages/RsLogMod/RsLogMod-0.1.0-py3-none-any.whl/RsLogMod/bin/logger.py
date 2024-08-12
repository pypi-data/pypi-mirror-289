from .utilities import format_out_path, get_current_date, get_current_time, log_rotation
from .dictionaries import log_prefixes, log_headers
import os


class RsLogger:
    def __init__(self, log_name: str, log_level: int, log_entry: str):
        self.prefix = log_prefixes.get(log_level, '[INFO]')
        self.date_time = f"{get_current_date()} {get_current_time()}"
        self.path = format_out_path(log_name)
        self.entry = log_entry

        # Create a default log file if it doesn't exist
        if not os.path.exists(self.path):
            self.create_default_log()

        # Ensure log rotation if necessary
        if log_rotation(self.path):
            print(f"Log file {self.path} rotated.")

    def log(self):
        try:
            with open(self.path, 'a') as file:
                file.write(f'{self.prefix} {self.date_time}: {self.entry}\n')
        except IOError as e:
            print(f"Failed to write to log file: {e}")

    def create_default_log(self):
        try:
            with open(self.path, 'w') as file:
                file.write(log_headers.get('default', "# Log File #\n"))
        except IOError as e:
            print(f"Failed to create log file: {e}")
