from os import mkdir
from shutil import rmtree
from subprocess import run
from .testutils import cmd, reqTestFiles


def test_gentopol():
    mkdir("_tmp")
    reqTestFiles("phneutral.pdb phrecord.dat")

    result = run(
        cmd("phbuilder genparams -f phneutral.pdb -ph 4.0"), shell=True, cwd="_tmp"
    )

    if result.returncode == 0:  # Cleanup if everything was fine.
        rmtree("_tmp")

    assert result.returncode == 0


def test_gentopol_verbose():
    mkdir("_tmp")
    reqTestFiles("phneutral.pdb phrecord.dat")

    result = run(
        cmd("phbuilder genparams -f phneutral.pdb -ph 4.0 -v"), shell=True, cwd="_tmp"
    )

    if result.returncode == 0:  # Cleanup if everything was fine.
        rmtree("_tmp")

    assert result.returncode == 0


def test_gentopol_cal():
    mkdir("_tmp")
    reqTestFiles("phneutral.pdb phrecord.dat")

    result = run(
        cmd("phbuilder genparams -f phneutral.pdb -ph 4.0 -cal"), shell=True, cwd="_tmp"
    )

    if result.returncode == 0:  # Cleanup if everything was fine.
        rmtree("_tmp")

    assert result.returncode == 0
