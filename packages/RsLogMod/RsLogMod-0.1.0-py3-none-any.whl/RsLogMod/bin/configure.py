from RsLogMod.bin.utilities import locate
import os.path
import json


class RsConfigure:
    def __init__(self):
        # Determine the absolute path to the configs.json file
        self.conf_file_path = locate('configs.json')

    def display(self):
        try:
            with open(self.conf_file_path, 'r') as file:
                content = json.load(file)
                print(json.dumps(content, indent=4))  # Pretty print the JSON content
        except FileNotFoundError:
            print(f"Configuration file not found at {self.conf_file_path}.")
        except json.JSONDecodeError:
            print("Error decoding the JSON configuration file.")

    def log_folder_path(self, path: str):
        try:
            if not os.path.exists(path):
                os.makedirs(path)

            with open(self.conf_file_path, 'r+') as file:
                content = json.load(file)
                content['out_dir'] = path

                # Move the file pointer to the beginning of the file
                file.seek(0)

                # Write the updated content and truncate the file to remove any leftover data
                json.dump(content, file, indent=4)
                file.truncate()

        except FileNotFoundError:
            print(f"Configuration file not found at {self.conf_file_path}.")
        except json.JSONDecodeError:
            print("Error decoding the JSON configuration file.")
        except IOError as e:
            print(f"Failed to write to the configuration file: {e}")

    def log_max_size(self, mega_bytes: int):
        try:
            if not mega_bytes.is_integer():
                mega_bytes = int(mega_bytes)

            with open(self.conf_file_path, 'r+') as file:
                content = json.load(file)
                content['max_size_in_mega_bytes'] = mega_bytes

                # Move the file pointer to the beginning of the file
                file.seek(0)

                # Write the updated content and truncate the file to remove any leftover data
                json.dump(content, file, indent=4)
                file.truncate()

        except FileNotFoundError:
            print(f"Configuration file not found at {self.conf_file_path}.")
        except json.JSONDecodeError:
            print("Error decoding the JSON configuration file.")
        except IOError as e:
            print(f"Failed to write to the configuration file: {e}")

    def log_rotation(self, value: bool):
        try:
            with open(self.conf_file_path, 'r+') as file:
                content = json.load(file)
                content['log_rotation'] = value

                # Move the file pointer to the beginning of the file
                file.seek(0)

                # Write the updated content and truncate the file to remove any leftover data
                json.dump(content, file, indent=4)
                file.truncate()

        except FileNotFoundError:
            print(f"Configuration file not found at {self.conf_file_path}.")
        except json.JSONDecodeError:
            print("Error decoding the JSON configuration file.")
        except IOError as e:
            print(f"Failed to write to the configuration file: {e}")
