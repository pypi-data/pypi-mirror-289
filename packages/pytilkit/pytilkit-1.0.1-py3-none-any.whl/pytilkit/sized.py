from os.path import getsize

def fileSizeMB(filePath) -> float:
    """
    # func > fileSizeMB

    Returns the size of the given file in MB.

    :param filePath: str
    :return: float
    """

    return getsize(filePath) / (1024 * 1024)

def fileSizeGB(filePath) -> float:
    """
    # func > fileSizeGB

    Returns the size of the given file in GB.

    :param filePath: str
    :return: float
    """

    return fileSizeMB(filePath) / 1000
