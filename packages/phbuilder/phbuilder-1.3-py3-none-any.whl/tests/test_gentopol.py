from os import mkdir
from shutil import rmtree
from subprocess import run
from .testutils import cmd, reqTestFiles


def test_gentopol_pdb():
    mkdir("_tmp")
    reqTestFiles("1cvo.pdb")

    result = run(
        cmd("phbuilder gentopol -f 1cvo.pdb -ph 4.0", input=[1]), shell=True, cwd="_tmp"
    )

    if result.returncode == 0:  # Cleanup if everything was fine.
        rmtree("_tmp")

    assert result.returncode == 0


def test_gentopol_gro():
    mkdir("_tmp")
    reqTestFiles("1cvo.gro")

    result = run(
        cmd("phbuilder gentopol -f 1cvo.gro -ph 4.0", input=[1]), shell=True, cwd="_tmp"
    )

    if result.returncode == 0:  # Cleanup if everything was fine.
        rmtree("_tmp")

    assert result.returncode == 0
