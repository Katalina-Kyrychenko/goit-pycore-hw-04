from pathlib import Path
from constants import FileStatus

def check_file_status(path):
    """
    Check if a file exists, is readable, and not empty.
    Returns one of: 'OK', 'NOT_FOUND', 'NOT_A_FILE', 'EMPTY', 'CORRUPTED', 'ERROR'.
    """
    file_path = Path(path)

    # 1 Check existence
    if not file_path.exists():
        return  FileStatus.NOT_FOUND.value

    # 2 Ensure it's a file
    if not file_path.is_file():
        return FileStatus.NOT_A_FILE.value

    # 3 Check for empty file
    if file_path.stat().st_size == 0:
        return FileStatus.EMPTY.value

    # 4 Try reading first few bytes (robust for any file type)
    try:
        with open(file_path, "rb") as f:
            f.read(100)
        return FileStatus.OK.value
    except UnicodeDecodeError:
        # File might contain unreadable characters (e.g. wrong encoding)
        return FileStatus.CORRUPTED.value
    except Exception:
        # Any other error (permissions, locks, etc.)
        return FileStatus.ERROR.value