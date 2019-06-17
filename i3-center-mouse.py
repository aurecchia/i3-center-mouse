#!/usr/bin/env python3

import sys
import i3ipc
from subprocess import DEVNULL, STDOUT, check_call, call, CalledProcessError


TRIGGERS = []


# Used to distinguish 'window::focus' events that follow 'exec' and 'kill'
# commands directly, because we only want to update the mouse position on focus
# change if it follows one of those events
should_refocus = False

def usage():
    print("Usage: center_mouse.py <i3 command>...")

def center(i3, event):
    rect = i3.get_tree().find_focused().rect
    x = rect.x + int(rect.width / 2)
    y = rect.y + int(rect.height / 2)
    call(['xdotool', 'mousemove', str(x), str(y)])

def on_binding(i3, event):
    command = event.binding.command

    for trigger in TRIGGERS:
        if command.startswith(trigger):
            if trigger.startswith('kill') or trigger.startswith('exec'):
                global should_refocus
                should_refocus = True
            else:
                center(i3, event)
            return

def on_focus(i3, event):
    global should_refocus
    if should_refocus:
        should_refocus = False
        center(i3, event)


def usage():
    print("i3-center-mouse")
    print()
    print("Usage: i3-center-mouse.py <event>...")
    print("       i3-center-mouse.py -a | --all")
    print("       i3-center-mouse.py -h | --help")
    print()
    print("Options:")
    print("    -a, --all   Subscribe to all events.")
    print("    -h, --help  Print this help message and exit.")
    print()
    print("Events:")
    print("    focus, move, layout, workspace, floating, kill, exec")


if __name__ == '__main__':

    try:
        check_call(['which', 'xdotool'], stdout=DEVNULL, stderr=STDOUT)
    except CalledProcessError:
        print("Missing dependency 'xdotool'")
        sys.exit(1)

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    option = sys.argv[1]
    if option in ('-h', '--help'):
        usage()
        sys.exit(0)
    elif option in ('-a', '--all'):
        TRIGGERS=['focus', 'move', 'layout', 'workspace', 'floating', 'kill', 'exec']
    else:
        TRIGGERS.extend(sys.argv[1:])

    i3 = i3ipc.Connection()

    i3.on('binding', on_binding)
    i3.on('window::focus', on_focus)

    i3.main()
