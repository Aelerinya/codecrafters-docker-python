import ctypes

libc = ctypes.CDLL(None)
syscall = libc.syscall


CLONE_NEWPID = 0x20000000
__NR_unshare = 272


def unshare_pid():
    syscall(__NR_unshare, CLONE_NEWPID)
