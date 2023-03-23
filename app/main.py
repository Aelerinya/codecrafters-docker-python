import os
import subprocess
import sys


root_folder = os.environ.get("MY_DOCKER_ROOT")


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    # Uncomment this block to pass the first stage
    command = sys.argv[3]
    args = sys.argv[4:]

    path = root_folder + command if root_folder is not None else command

    _completed_process = subprocess.run([path, *args])


if __name__ == "__main__":
    main()
