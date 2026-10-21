# Tokyo Night for osxphotos

A [Tokyo Night](https://github.com/rojadesign/iTerm2-Tokyo-Night-Color-Theme) color theme for the [osxphotos](https://github.com/RhetTbull/osxphotos) command-line tool.

## Palette

| Style | Color | Used for |
| --- | --- | --- |
| `color` | `#c0caf5` | Default foreground text |
| `filename` | `#bb9af7` | File names (bold) |
| `filepath` | `#9ece6a` | File paths (bold) |
| `num` / `count` / `time` | `#7dcfff` | Numbers, counts, timestamps |
| `tz` | `#2ac3de` | Time zones (bold) |
| `uuid` | `#ff9e64` | Photo UUIDs |
| `warning` | `#e0af68` | Warnings (bold) |
| `error` | `#db4b4b` | Errors (bold) |
| `change` | `#f7768e` | Changed values (bold) |
| `no_change` | `#9ece6a` | Unchanged values (bold) |
| `highlight` | `#1a1b26` on `#f7768e` | Highlighted matches |
| `bar.*` / `progress.*` | various | Progress bars |

## Installation

osxphotos loads custom themes from `~/.config/osxphotos/themes/`.

1. Download the theme into that directory:

   ```sh
   mkdir -p ~/.config/osxphotos/themes
   curl -fsSL -o ~/.config/osxphotos/themes/tokyonight.theme \
     https://raw.githubusercontent.com/timcheadle/osxphotos-tokyo-night/main/tokyonight.theme
   ```

   Or clone this repo and copy `tokyonight.theme` there yourself.

2. Check that osxphotos sees it:

   ```sh
   osxphotos theme --list
   osxphotos theme --preview tokyonight
   ```

## Making it the default

The `--theme` option on osxphotos commands only accepts the built-in themes (`dark`, `light`, `mono`, `plain`). Instead, osxphotos uses a theme named `default` whenever one exists, so clone Tokyo Night under that name:

```sh
osxphotos theme --clone tokyonight default
```

Confirm with:

```sh
osxphotos theme --default
```

To go back to the automatic dark/light behavior, delete the clone:

```sh
osxphotos theme --delete default
```

## Credits

- **Colors:** adapted from [iTerm2 Tokyo Night Color Theme](https://github.com/rojadesign/iTerm2-Tokyo-Night-Color-Theme) by [rojadesign](https://github.com/rojadesign), itself based on the original [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme) theme by [enkia](https://github.com/enkia).
- **osxphotos:** written and maintained by [Rhet Turnbull](https://github.com/RhetTbull). Thanks for a great tool, and for building in theme support.

## License

[MIT](LICENSE)
