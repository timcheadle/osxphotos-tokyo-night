# Tokyo Night for osxphotos

A [Tokyo Night](https://github.com/rojadesign/iTerm2-Tokyo-Night-Color-Theme) color theme for the [osxphotos](https://github.com/RhetTbull/osxphotos) command-line tool.

![osxphotos export output using the Tokyo Night theme](images/screenshot.svg)

## Palette

| | Style | Color | Used for |
| --- | --- | --- | --- |
| <img src="images/swatches/c0caf5.svg" width="14" height="14"> | `color` | `#c0caf5` | Default foreground text |
| <img src="images/swatches/bb9af7.svg" width="14" height="14"> | `filename` | `#bb9af7` | File names (bold) |
| <img src="images/swatches/9ece6a.svg" width="14" height="14"> | `filepath` | `#9ece6a` | File paths (bold) |
| <img src="images/swatches/7dcfff.svg" width="14" height="14"> | `num` / `count` / `time` | `#7dcfff` | Numbers, counts, timestamps |
| <img src="images/swatches/2ac3de.svg" width="14" height="14"> | `tz` | `#2ac3de` | Time zones (bold) |
| <img src="images/swatches/ff9e64.svg" width="14" height="14"> | `uuid` | `#ff9e64` | Photo UUIDs |
| <img src="images/swatches/e0af68.svg" width="14" height="14"> | `warning` | `#e0af68` | Warnings (bold) |
| <img src="images/swatches/db4b4b.svg" width="14" height="14"> | `error` | `#db4b4b` | Errors (bold) |
| <img src="images/swatches/f7768e.svg" width="14" height="14"> | `change` | `#f7768e` | Changed values (bold) |
| <img src="images/swatches/9ece6a.svg" width="14" height="14"> | `no_change` | `#9ece6a` | Unchanged values (bold) |
| <img src="images/swatches/1a1b26.svg" width="14" height="14"> <img src="images/swatches/f7768e.svg" width="14" height="14"> | `highlight` | `#1a1b26` on `#f7768e` | Highlighted matches (bold) |
| <img src="images/swatches/f7768e.svg" width="14" height="14"> | `bar.complete` / `progress.percentage` | `#f7768e` | Progress bar in progress, percentage |
| <img src="images/swatches/9ece6a.svg" width="14" height="14"> | `bar.finished` | `#9ece6a` | Completed progress bar |
| <img src="images/swatches/3b4261.svg" width="14" height="14"> | `bar.back` | `#3b4261` | Progress bar track |
| <img src="images/swatches/737aa2.svg" width="14" height="14"> | `bar.pulse` | `#737aa2` | Indeterminate progress pulse |
| <img src="images/swatches/7dcfff.svg" width="14" height="14"> | `progress.elapsed` / `progress.remaining` | `#7dcfff` | Progress timers |

<details>
<summary>Full <code>osxphotos theme --preview tokyonight</code> output</summary>

![osxphotos theme --preview output for Tokyo Night](images/preview.svg)

</details>

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
