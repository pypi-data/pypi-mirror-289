# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=logging-fstring-interpolation
# pylint: disable=line-too-long
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught

import os 
import json

def log_error(message, logger=None , print_out=False, exc_info=False):
    if logger:
        logger.error(message, exc_info=exc_info)
    elif print_out:
        print(message)

def log_warning(message, logger=None, print_out=False):
    if logger:
        logger.warning(message)
    elif print_out:
        print(message)

def log_info(message, logger=None, print_out=False):
    if logger:
        logger.info(message)
    elif print_out:
        print(message)


def save_json_locally_extended(data:dict | list | str, file_name:str, local_path:str, file_exists_if_starts_with_prefix:str=None, overwrite_if_exists:bool=False, increment_if_exists:bool=False,
                      max_deletable_files:int=1, logger=None, print_out=False):
    
    """Saves data to a local JSON file.

    Args:
        data (dict | list | str): The data to save.
        file_name (str): The desired file name.
        local_path (str): The directory where the file should be saved.
        file_exists_if_starts_with_prefix (str, optional):  If provided, used to check for
            existing files with the given prefix. Defaults to None.
        overwrite_if_exists (bool, optional): If True, overwrites existing files. Defaults to False.
        increment_if_exists (bool, optional): If True, increments the file name if it exists.
            Defaults to False.
        max_deletable_files (int, optional): Maximum number of files to delete when overwriting. 
            Defaults to 1.

    Returns:
        dict: Metadata about the save operation, including:
            - local_path (str): The full path to the saved file (or None if not saved).
            - local_file_already_exists (bool): True if a file with the same name or prefix existed.
            - local_file_overwritten (bool): True if an existing file was overwritten.
            - local_deleted_file_names (str): A comma-separated string of deleted file names (or None).
            - local_file_saved_with_increment (bool): True if the file was saved with an incremented name.
            - local_save_error (bool): True if there was an error saving the file.
    """

    local_save_error=None
    # Input validation
    if overwrite_if_exists and increment_if_exists:
        msg = "Both 'overwrite_if_exists' and 'increment_if_exists' cannot be True simultaneously."
        log_error(msg, logger=logger, print_out=print_out)
        return {"local_save_error" : msg} 
    if max_deletable_files > 10:
        msg = "max_deletable_files should be less than 10 for safety. For more, use another method."
        log_error(msg, logger=logger, print_out=print_out)
        return {"local_save_error" : msg}
    

    # Prepare data
    if isinstance(data, (list, dict)):
        data_str = json.dumps(data, indent=2)
    else:
        data_str = data


    # Extract directory from file_name if present
    directory = os.path.dirname(file_name)
    full_local_path = os.path.join(local_path, directory)

    # Create the full directory path if it doesn't exist
    os.makedirs(full_local_path, exist_ok=True)

    # Now use the full file path including the subdirectories
    base_file_name, ext = os.path.splitext(os.path.basename(file_name)) 
    increment = 0
    full_file_path = os.path.join(full_local_path, f"{base_file_name}{ext}")

    # Metadata
    local_path = None
    local_file_already_exists = False
    local_file_overwritten = False
    local_file_saved_with_increment = False
    local_deleted_file_names = None
    local_save_error = None

    try:
        # --- Overwrite Logic ---
        if overwrite_if_exists:
            if file_exists_if_starts_with_prefix:
                files_to_delete = [
                    f for f in os.listdir(full_local_path)
                    if f.startswith(file_exists_if_starts_with_prefix)
                ]
                if len(files_to_delete) > max_deletable_files:
                    raise ValueError(
                        f"Error: Attempt to delete {len(files_to_delete)} matched files, but limit is {max_deletable_files}."
                    )
                if files_to_delete:
                    local_file_already_exists = True
                    for file in files_to_delete:
                        os.remove(os.path.join(full_local_path, file))
                    local_file_overwritten = True
                    local_deleted_file_names = ",,,".join(files_to_delete)
            elif os.path.exists(full_file_path):
                local_file_already_exists = True
                os.remove(full_file_path)
                local_file_overwritten = True

        # --- Increment Logic ---
        elif increment_if_exists:
            while os.path.exists(full_file_path):
                local_file_already_exists = True
                increment += 1
                file_name = f"{base_file_name}_v{increment}{ext}"
                full_file_path = os.path.join(full_local_path, file_name)
                local_file_saved_with_increment = True

        # --- Save the File ---
        with open(full_file_path, "w", encoding="utf-8") as f:
            f.write(data_str)
        local_path = full_file_path

    except Exception as e:
        local_save_error=f"Error saving file to local path: {full_file_path} : {type(e).__name__}-{str(e)}"
        log_error(local_save_error, logger=logger, print_out=print_out)
        return {"local_save_error" : msg}

    return {
        "local_path": local_path,
        "local_file_already_exists": local_file_already_exists,
        "local_file_overwritten": local_file_overwritten,
        "local_deleted_file_names": local_deleted_file_names,
        "local_file_saved_with_increment": local_file_saved_with_increment,
        "local_save_error": local_save_error,
    }