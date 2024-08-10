from typing import List
from shutil import copy, copytree


def cmd(command: str, input: List[str] = []) -> List[str]:
    """Pre-process command line input for subprocess.run().

    Args:
        command (str): command line input.
        input (List[str], optional): values to use when prompted for input. Defaults to [].

    Returns:
        List[str]: List of arguments for subprocess.
    """

    if input:
        xstr = " << EOF\n"
        for val in input:
            xstr += "{}\n".format(val)
        command += xstr + "EOF"

    return command


def reqTestFiles(
    fileNames: str, ff: bool = False, source: str = "test_files", target: str = "_tmp"
) -> None:
    """Copy test files from source to target directory.

    Args:
        fileNames (str): names of the files to copy.
        ff (bool, optional): get the force field (from phbuilder/ffield). Defaults to False.
        source (str, optional): source directory. Defaults to "test_files".
        target (str, optional): target directory. Defaults to "_tmp".
    """

    for fileName in fileNames.split():
        try:
            copy(f"{source}/{fileName}", target)
        except IsADirectoryError:
            copytree(f"{source}/{fileName}", f"{target}/{fileName}")

    # If required we copy the force field from phbuilder/ffield, as this is the
    # version that is actually shipped with phbuilder. We want to avoid having a
    # separate copy of the ffield in test_files.
    if ff:
        copytree("../phbuilder/ffield/charmm36-mar2019-cphmd.ff", f"{target}/charmm36-mar2019-cphmd.ff")
