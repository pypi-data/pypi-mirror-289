from datetime import datetime
import shutil
import json
import os


def get_project_root(root_dir_name='RsLogMod', fallback_root=None):
    """
    Determines the root directory of the RsLogMod module by searching for a specific directory name.
    """
    cwd = os.getcwd()
    split_cwd = cwd.split(os.sep)
    path_parts = []

    for segment in split_cwd:
        path_parts.append(segment)
        if segment == root_dir_name:
            return os.path.join(os.sep, *path_parts)

    if fallback_root:
        return fallback_root

    raise RuntimeError(f"Root directory '{root_dir_name}' not found in the current path hierarchy.")


def locate(target):
    """
    Locate a file or folder within the RsLogMod project.
    """
    root = get_project_root()
    if root is None:
        raise FileNotFoundError("Root directory not found")

    for path, folders, files in os.walk(root):
        if target in folders:
            return os.path.join(path, target)
        elif target in files:
            return os.path.join(path, target)

    raise FileNotFoundError(f"'{target}' not found in '{root}'.")


def load_config_from_file(target_config):
    """
    Loads the specified configuration value from configs.json.
    """
    path = locate('configs.json')

    if path:
        with open(path, 'r') as file:
            content = json.load(file)
            return content.get(target_config, None)

    raise FileNotFoundError('configs.json is missing.')


def format_out_path(log_name):
    """
    Returns the output directory from the configuration or a default path.
    """
    out_dir = load_config_from_file('out_dir')
    if not out_dir:
        out_dir = os.getcwd()  # Default to current working directory

    out_dir = os.path.abspath(out_dir)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    return os.path.join(out_dir, f"{log_name}.log")


def get_current_date():
    """
    Returns the current date in the format YYYY-MM-DD.
    """
    return datetime.now().strftime("%Y-%m-%d")


def get_current_time():
    """
    Returns the current time in the format HH:MM:SS.
    """
    return datetime.now().strftime("%H:%M:%S")


def log_rotation(file_path):
    """
    Handles log rotation by checking the file size against the maximum size defined in the configuration.
    """
    def rotate(src_path):
        archive_dir = locate('archived')  # Ensure an 'archived' folder exists
        if not archive_dir:
            archive_dir = os.path.join(get_project_root(), 'archived')
            os.makedirs(archive_dir, exist_ok=True)

        timestamp = f"{get_current_date()}_{get_current_time().replace(':', '-')}"
        archived_path = os.path.join(archive_dir, f"{os.path.basename(src_path)}.{timestamp}")

        shutil.move(src_path, archived_path)
        with open(src_path, 'w') as new_log_file:
            new_log_file.write("# Log rotated on " + get_current_date() + "\n")

    max_size = (load_config_from_file('max_size_in_mega_bytes') * 1024 * 1014)
    log_size = os.path.getsize(file_path)

    if log_size >= int(max_size):
        rotate(file_path)
        return True
    return False
