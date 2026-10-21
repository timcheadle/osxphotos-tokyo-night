"""Render README images for the osxphotos Tokyo Night theme.

Run with the Python that osxphotos is installed into (it provides rich and
rich_theme_manager), passing the repo root:

    $(brew --prefix osxphotos)/libexec/bin/python scripts/render_images.py .
"""
import re, sys
from pathlib import Path
from rich._export_format import CONSOLE_SVG_FORMAT
from rich.console import Console
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

# Rich's SVG template pulls Fira Code from a CDN, which GitHub blocks inside
# <img>. Use Input Mono Narrow (the font in the reference terminal) when the
# viewer has it installed, without embedding it, and fall back to system fonts.
FONT_FACES = "".join(
    f'@font-face {{{{ font-family: "Terminal"; src: local("{name}"); font-weight: {weight}; }}}}\n'
    for name, weight in [("InputMonoNarrow-Regular", 400), ("Input-Regular", 400),
                         ("InputMonoNarrow-Bold", 700), ("Input-Bold", 700)]
)
SVG_FORMAT = re.sub(r"@font-face \{\{.*?\}\}\n", "", CONSOLE_SVG_FORMAT, flags=re.S)
SVG_FORMAT = SVG_FORMAT.replace("<style>", "<style>\n" + FONT_FACES, 1).replace(
    "font-family: Fira Code, monospace;",
    "font-family: Terminal, \"Input Mono Narrow\", \"SF Mono\", Menlo, Consolas, monospace;")
assert "Fira" not in SVG_FORMAT


def console():
    return Console(theme=theme, record=True, width=100, force_terminal=True,
                   color_system="truecolor", highlight=False, file=open("/dev/null", "w"))

# 1. Sample `osxphotos export --verbose` session. Messages use the same markup
# osxphotos emits (see osxphotos/cli/export.py); paths and photos are made up.
import random, uuid as uuidlib
from osxphotos.cli.rich_progress import rich_progress

rng = random.Random(1)  # fixed seed so re-renders don't churn the SVG
random_uuid = lambda: str(uuidlib.UUID(int=rng.getrandbits(128), version=4)).upper()
c = console()
c.print("[color]$ osxphotos export /Volumes/Backup/Photos --load-config ~/.osxphotos/backup.toml --verbose")
c.print("Loaded options from file [filepath]/Users/me/.osxphotos/backup.toml")
c.print("osxphotos version: 0.77.2")
c.print("exiftool path: [filepath]/opt/homebrew/bin/exiftool")
c.print("Using last opened Photos library: /Users/me/Pictures/Photos Library.photoslibrary")
c.print("[warning]Warning: export database '/Users/me/.osxphotos/export.db' is in a different "
        "directory than export destination '/Volumes/Backup/Photos'")
c.print("Using osxphotos export database: version [num]11.1[/] located at "
        "[filepath]/Users/me/.osxphotos/export.db")
c.print("Processing database [filepath]/Users/me/Pictures/Photos Library.photoslibrary/database/Photos.sqlite[/]")
c.print("Photos database version: [num]5001[/], [num]11.1[/].")
for what in ("persons in photos", "albums", "keywords", "photo details", "EXIF details"):
    c.print(f"Processing {what}.")
c.print("Done processing details from Photos library.")
c.print("Exporting [num]6[/num] photos to [filepath]/Volumes/Backup/Photos[/]...")
names = ["IMG_0101.HEIC", "IMG_0102.HEIC", "IMG_0103.MOV", "IMG_0104.HEIC", "IMG_0105.MOV", "IMG_0106.JPG"]
for i, name in enumerate(names, 1):
    ext = name.rsplit(".", 1)[1].lower()
    c.print(f"Exporting [filename]{name}[/] ([filename]{random_uuid()}.{ext}[/]) ([count]{i}/{len(names)}[/])")
progress = rich_progress(console=c, auto_refresh=False, get_time=lambda: 0.0)
task = progress.add_task(f"Exporting [num]{len(names)}[/] photos", total=len(names))
progress.update(task, completed=len(names))  # marks the task finished
c.print(progress.get_renderable())
c.print("Processed: [num]6[/] photos, exported: [num]6[/], missing: [num]0[/], error: [num]0[/]")
c.print("Elapsed time: [time]0:00:03")
c.print("Wrote export report to [filepath]/Users/me/.osxphotos/reports/export-report.csv")
c.save_svg(str(out / "screenshot.svg"), title="osxphotos — Tokyo Night", theme=term, code_format=SVG_FORMAT)

# 2. The built-in `osxphotos theme --preview` table.
c = console()

ThemeManager.preview_theme(theme, show_path=False, console=c)
c.save_svg(str(out / "preview.svg"), title="osxphotos theme --preview tokyonight", theme=term, code_format=SVG_FORMAT)

# 3. Color swatches.
for color in sorted(set(re.findall(r"#[0-9a-f]{6}", (repo / "tokyonight.theme").read_text()))):
    (out / "swatches" / f"{color[1:]}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14">'
        f'<rect width="14" height="14" rx="3" fill="{color}" stroke="#565f89"/></svg>\n')
print("done")
