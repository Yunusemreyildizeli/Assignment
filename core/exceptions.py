# exceptions.py

class InvalidTransactionError(Exception):
    """
    Custom exception raised when a transaction contains invalid data.
    Typically used for validation errors such as incorrect types,
    negative values, or missing required fields.
    """
    pass

class FileOperationError(Exception):
    """
    Custom exception raised when file read/write operations fail.
    Common causes include missing files, permission issues,
    or incorrect file formats during CSV processing.
    """
    pass