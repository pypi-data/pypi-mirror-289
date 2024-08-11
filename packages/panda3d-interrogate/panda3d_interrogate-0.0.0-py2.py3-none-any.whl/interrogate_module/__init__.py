import os
import subprocess
import sys
import panda3d

try:
    import panda3d_tools
except:
    panda3d_tools = None


def _get_executable(name):
    if sys.platform == 'win32':
        name += '.exe'

    if panda3d_tools:
        tools_dir = os.path.dirname(panda3d_tools.__file__)
    else:
        tools_dir = os.path.join(os.path.dirname(os.path.dirname(panda3d.__file__)), 'bin')

    path = os.path.join(tools_dir, name)
    if not os.path.isfile(path):
        if sys.version_info >= (3, 3):
            raise FileNotFoundError(name + ' not found')
        else:
            raise IOError(name + ' not found')

    return path


def _run(name):
    executable = _get_executable(name)
    return subprocess.call([executable] + sys.argv[1:])


def main():
    raise SystemExit(_run("interrogate_module"))
