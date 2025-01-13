from webbrowser import open_new_tab
import subprocess
import pygetwindow as gw

def browser(name="Opera"):
    windows = [w for w in gw.getAllWindows() if name in w.title]
    if windows:
        windows[0].activate()
    else:
        subprocess.run(["start", "opera"], shell=True)