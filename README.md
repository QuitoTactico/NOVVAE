# NOVVAE Controller

A personal automation script for managing a video/songs-watching and development workflow, primarily centered around YouTube and Visual Studio Code. This script automates actions like liking videos/songs, navigating playlists, managing browser and editor windows, and saving video links for persistence.

## Features

* 📺 **YouTube Video Control**

  * Automatically open and load a saved YouTube video
  * Like videos with visual confirmation or image recognition
  * Control playback (play, pause, skip, rewind, jump to certain timestamps)
  * Save current video URL to a local file

* 🌐 **Browser Automation**

  * Automatically open Opera browser or any specified browser
  * Navigate between tabs and simulate user interaction
  * Perform YouTube or general web searches via command-line

* 💻 **Visual Studio Code Automation**

  * Opens VS Code if not already opened
  * Brings focus to terminal inside the editor
  * Minimizes or closes VS Code if needed

* 🖱️ **Mouse Control**

  * Uses fixed mouse positions to interact with UI elements
  * Recognizes screen elements via screenshots for certain actions

* 💾 **State Persistence**

  * Saves the current video link in a text file for later retrieval

* 🧪 **Command-Line Menu**

  * Interactive command loop allows users to input short commands to automate workflow steps

## Requirements

* Python 3.x
* Modules:

  * `pyautogui`
  * `pyperclip`
  * `pywinauto`

## Setup

1. Install dependencies:

   ```bash
   pip install pyautogui pyperclip pywinauto
   ```

2. Place reference images in a `media/` folder (used for image recognition like `like-icon.png`).

3. (Optional) Adjust screen coordinates if your UI layout differs.

## Usage

Run the script with:

```bash
python NOVVAE.py
```

Once running, you can input commands such as:

| Command          | Action                           |
| ---------------- | -------------------------------- |
| `n`              | Next video                       |
| `b`              | Previous video                   |
| `l`              | Like video                       |
| `p`              | Pause video                      |
| `v`              | See current video tab            |
| `-`              | Print current saved video URL    |
| `00`             | Rewind video to start            |
| `2`              | Jump to quarter mark             |
| `5`              | Jump to halfway point            |
| `s`              | Save video to persistence file   |
| `k`              | Open YouTube "Liked Videos" list |
| `no`             | Open main playlist (NOVVAE)      |
| `git`            | Open GitHub repo                 |
| `search <query>` | Search on default browser        |
| `yt <query>`     | Search on YouTube                |
| `0`              | Exit and save last video state   |
| `09`             | Close browser                    |
| `0'`             | Close VS Code                    |

## File Structure

* `media/`: Directory containing image assets for recognition
* `NOVVAE_PERSISTENCE.txt`: Text file storing the last saved video URL

## Notes

* Coordinates and window titles are hardcoded and may need adaptation for different resolutions or systems.
* This script uses a combination of GUI automation and browser interactions; unintended behavior can occur if the window layout changes.
* Includes ASCII art and versioning (`v2.0.0`) for personal flair.

## Author

Made by [QuitoTactico](https://github.com/QuitoTactico) as part of the NOVVAE project.

Aquí tienes un `README.md` completo y específico para el downloader:

---

# Downloader

This is a simple YouTube to MP3 downloader using `yt-dlp`, with optional support for trimming specific time ranges. It automatically embeds metadata and thumbnails into the resulting audio file. Useful as a utility tool for extracting music, podcast segments, or specific video audio.

## Requirements

* **Python 3.x**

* **FFmpeg**
  Required for audio extraction and conversion.
  Download and install from:

  * [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
  * [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

    > Via `winget install ffmpeg` on Windows cmd if you have [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/) installed.
    > Or install it using `choco install ffmpeg` on cmd using admin privileges if you have [Chocolatey](https://chocolatey.org/) installed.

  Ensure that the `ffmpeg` command is available in your system's PATH. You can check this by running:

  ```bash
  ffmpeg -version
  ```

  If it returns the version information, you're good to go!

* **Python packages**
  Install the required modules with:

  ```bash
  pip install yt-dlp
  ```

  Also ensure the `utils` module (and `utils.UI.folder_selector`) is available in the project directory.

## Features

* Downloads the **best audio** stream from a YouTube video.
* Converts the audio to **MP3 (320kbps)** using FFmpeg.
* Automatically embeds **thumbnails** and **metadata**.
* Allows specifying **start and end times** to trim the audio.
* Prompts the user to select an output folder interactively.

## Usage

Run the script with:

```bash
python downloader.py
```

It will:

1. Prompt you for a YouTube URL.
2. Ask (optionally) for a start time and end time (`hh:mm:ss` format).
3. Open a folder picker to select the destination directory.
4. Download, trim, convert, and save the MP3 file to the selected folder.

Example usage:

```
Introduce el link del video de YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ  
Hora de inicio (formato hh:mm:ss, opcional): 00:01:00  
Hora de fin (formato hh:mm:ss, opcional): 00:02:30  
```

## Output

The downloaded `.mp3` file will be saved to the selected folder with the original video title as filename. It will include:

* High-quality audio (320kbps)
* Embedded thumbnail (if available)
* Metadata (title, etc.)

## Project Structure

```
downloader.py        # Main downloader script  
utils/
  ├── __init__.py    
  └── UI.py          # Includes folder_selector for output directory  
media/               # Optional: used in other NOVVAE components  
```

## Credits/docs

* [yt-dlp](https://github.com/yt-dlp/yt-dlp)


## Why the F

I did all of this because of this song that wasn't anywhere:
27. 01:34:00 - 01:40:00 Bandoukan no gozen 2-ji
https://www.youtube.com/watch?v=87Y3FvH6Oxw&t=5640s