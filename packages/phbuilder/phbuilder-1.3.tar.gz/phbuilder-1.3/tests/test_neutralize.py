from os import mkdir
from shutil import rmtree
from subprocess import run
from .testutils import cmd, reqTestFiles


def test_neutralize():
    mkdir("_tmp")
    reqTestFiles("1cvo.pdb phrecord.dat solvated.pdb topol.top", ff=True)

    result = run(
        cmd("phbuilder neutralize -f solvated.pdb -conc 0.15"), shell=True, cwd="_tmp"
    )

    if result.returncode == 0:  # Cleanup if everything was fine.
        rmtree("_tmp")

    assert result.returncode == 0
