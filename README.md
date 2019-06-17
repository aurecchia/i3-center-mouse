# i3-center-mouse

This is a small script that listens for i3 events and centers the mouse in the
currently focused window when they occur. It can be used to keep track of which
window is focused without having to rely on decorations.

Since a GIF is worth 1000^2 words, this is how it works when changing focus
between windows:


## Dependencies

The is written in Python 3, therefore you'd need that to run it. Moreover you
need:

- [`i3ipc-python`](https://github.com/acrisci/i3ipc-python)
- [`xdotool`](https://www.semicomplete.com/projects/xdotool/)

## Usage

The script is supposed to be run in background, by adding something like this to
your config:

```
exec --no-startup-id ~/.scripts/i3-center-mouse.py --all
```

See `i3-center-mouse.py --help` for more info.
