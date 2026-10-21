"""Render README images for the osxphotos Tokyo Night theme.

Run with the Python that osxphotos is installed into (it provides rich and
rich_theme_manager), passing the repo root:

    $(brew --prefix osxphotos)/libexec/bin/python scripts/render_images.py .
"""
import re, sys
from pathlib import Path
from rich.console import Console
from rich.progress import BarColumn, Progress, TextColumn
from rich.terminal_theme import TerminalTheme
from rich_theme_manager import Theme, ThemeManager

repo = Path(sys.argv[1])
theme = Theme.read(str(repo / "tokyonight.theme"))
out = repo / "images"
(out / "swatches").mkdir(parents=True, exist_ok=True)

# Terminal colors from the Tokyo Night iTerm2 palette, so the "window" matches.
term = TerminalTheme(
    (0x1a, 0x1b, 0x26), (0xc0, 0xca, 0xf5),
    [(0x15,0x16,0x1e),(0xf7,0x76,0x8e),(0x9e,0xce,0x6a),(0xe0,0xaf,0x68),
     (0x7a,0xa2,0xf7),(0xbb,0x9a,0xf7),(0x7d,0xcf,0xff),(0xa9,0xb1,0xd6)],
    [(0x41,0x48,0x68),(0xf7,0x76,0x8e),(0x9e,0xce,0x6a),(0xe0,0xaf,0x68),
     (0x7a,0xa2,0xf7),(0xbb,0x9a,0xf7),(0x7d,0xcf,0xff),(0xc0,0xca,0xf5)],
)

def console():
    return Console(theme=theme, record=True, width=104, force_terminal=True,
                   color_system="truecolor", highlight=False, file=open("/dev/null", "w"))

# 1. Sample osxphotos session, using the same markup osxphotos emits.
c = console()
c.print("[color]$ osxphotos export ~/Pictures/Export --verbose --update")
c.print("Loaded options from file [filepath]~/.config/osxphotos/export.toml[/]")
c.print("exiftool path: [filepath]/opt/homebrew/bin/exiftool[/]")
c.print("[color]Exporting [num]4[/] photos to [filepath]~/Pictures/Export[/]...")
rows = [
    ("IMG_4821.HEIC", "9A1F3C2E-6B7D-4E21-A0C4-5D8E9F01B2A3", "2026-09-14 08:12:03", "-0700"),
    ("IMG_4822.HEIC", "C47D02B9-1E3A-4F55-9B6C-7A2D3E4F5061", "2026-09-14 08:13:47", "-0700"),
    ("DSC_0193.JPG",  "5E8B7A61-3C2F-4D9E-8A1B-0F6C2D3E4A57", "2026-10-02 17:41:22", "+0900"),
    ("IMG_5030.MOV",  "F2A9C1D4-7B6E-4A38-B5D2-9C0E1F2A3B4C", "2026-10-05 19:05:10", "+0900"),
]
for i, (fn, uuid, t, tz) in enumerate(rows):
    c.print(f"Exporting [filename]{fn}[/] ([uuid]{uuid}[/]) taken [time]{t}[/] [tz]{tz}[/]")
    if i == 2:
        c.print(f"  Skipping [no_change]{fn}[/], already up to date")
    else:
        c.print(f"  Exported [change]{fn}[/] to [filepath]~/Pictures/Export/2026/{fn}[/]")
c.print("[warning]Warning running exiftool: IMG_5030.MOV has no GPS data[/]")
c.print("[error]Error: could not export DSC_0193.xmp: file is locked[/]")
c.print("Processed: [count]4[/] photos, exported: [count]3[/], skipped: [count]1[/], errors: [count]1[/]")
c.print("Elapsed time: [time]0:00:04[/]")
p = Progress(TextColumn("{task.description}"), BarColumn(bar_width=40),
             TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
             TextColumn("[progress.elapsed]{task.fields[elapsed]}"),
             TextColumn("[progress.remaining]{task.fields[remaining]}"), console=c)
p.add_task("Exporting", total=100, completed=100, elapsed="0:00:04", remaining="0:00:00")
p.add_task("Updating ", total=100, completed=62, elapsed="0:00:02", remaining="0:00:01")
c.print(p.get_renderable())
c.save_svg(str(out / "screenshot.svg"), title="osxphotos — Tokyo Night", theme=term)

# 2. The built-in `osxphotos theme --preview` table.
c = console()

ThemeManager.preview_theme(theme, show_path=False, console=c)
c.save_svg(str(out / "preview.svg"), title="osxphotos theme --preview tokyonight", theme=term)

# 3. Color swatches.
for color in sorted(set(re.findall(r"#[0-9a-f]{6}", (repo / "tokyonight.theme").read_text()))):
    (out / "swatches" / f"{color[1:]}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14">'
        f'<rect width="14" height="14" rx="3" fill="{color}" stroke="#565f89"/></svg>\n')
print("done")
