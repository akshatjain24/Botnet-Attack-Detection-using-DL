import os

def list_files_in_directory(directory_path):
    """
    Takes a directory path as input and returns a list of all files inside it.
    
    Parameters:
        directory_path (str): Path to the directory.
    
    Returns:
        list: A list of file names (not including directories).
    """
    try:
        # List all entries in the directory
        all_entries = os.listdir(directory_path)
        
        # Filter only files
        files = [f for f in all_entries if os.path.isfile(os.path.join(directory_path, f))]
        
        return files
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
        return []
    except PermissionError:
        print(f"Error: Permission denied for accessing '{directory_path}'.")
        return []
