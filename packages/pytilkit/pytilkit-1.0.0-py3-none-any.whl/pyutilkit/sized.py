from os.path import getsize
from maths import div, mul

def fileSizeMB(filePath) -> float:
    """
    # func > fileSizeMB

    Returns the size of the given file in MB.

    :param filePath: str
    :return: float
    """

    return div(getsize(filePath), mul(1024, 1024))

def fileSizeGB(filePath) -> float:
    """
    # func > fileSizeGB

    Returns the size of the given file in GB.

    :param filePath: str
    :return: float
    """

    return div(fileSizeMB(filePath), 1000)
