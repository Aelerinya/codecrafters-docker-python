from multiprocessing import Process
import os
from pathlib import Path
from shutil import copy
import sys
from tempfile import TemporaryDirectory

from app.unshare import unshare_pid


def start_in_chroot(chroot_directory: Path, command: str, args: list[str]):
    os.chroot(chroot_directory)
    os.execv(command, [command, *args])


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    with TemporaryDirectory() as dir:
        dir = Path(dir)
        new_command_path = (dir / ("./" + command)).resolve()
        new_command_path.parent.mkdir(parents=True)
        copy(command, new_command_path)
        unshare_pid()
        subprocess = Process(target=start_in_chroot, args=[dir, command, args])
        subprocess.start()
        subprocess.join()
    exit(subprocess.exitcode)


if __name__ == "__main__":
    main()
