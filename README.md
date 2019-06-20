# i3-center-mouse

Listens for i3 events (e.g. focus change, new container, ...) and centers the
mouse in the currently focused window when they occur. It can be used to keep
track of which window is focused without having to rely on decorations.

Since a GIF is worth 1000^2 words, this is how it works when changing focus
between windows:

![Demo](demo.gif)

## Dependencies

- [Python 3](https://www.python.org)
- [`i3ipc-python`](https://github.com/acrisci/i3ipc-python)
- [`xdotool`](https://www.semicomplete.com/projects/xdotool/)

## Usage

The script is supposed to be run in background, by adding something like this to
your i3 config:

```
exec --no-startup-id ~/.scripts/i3-center-mouse.py --all
```

See `i3-center-mouse.py --help` for more info.
