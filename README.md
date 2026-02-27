# 🌿 Touch Grass CLI

**The most over-engineered mental health check for your terminal.**

Ever get so lost in the matrix that you forget what the outside world looks like? Did you just type `gut` instead of `git` for the 400th time today?

`Touch Grass CLI` is an asynchronous, hardware-accelerated, high-resolution Braille video engine built entirely in Python. It hijacks your terminal to play an AV rendering of a hand touching grass to remind you to step away from the keyboard.

![Demo](demo.gif) _(Pro Tip: Record your terminal running the script and replace this with a real GIF!)_

## ✨ Features

- **The Typo Trap:** Intercepts common typos (like `gut` instead of `git`) and forces you to touch grass before you can continue.
- **The Post-Deploy Zen:** Wraps your `git push` command. When your code successfully ships, it automatically plays the animation to reward you.
- **Manual Override:** Just type `tg` anywhere, anytime, to trigger a mental reset.
- **HD Braille Matrix Engine:** Uses OpenCV and NumPy to dynamically convert video files into a 60FPS TrueColor terminal hologram.
- **Asynchronous Audio:** Uses Pygame to flawlessly sync the audio track without blocking terminal execution.
- **Responsive Letterboxing:** Automatically scales and centers the video to fit perfectly in your terminal or VS Code panel without stretching.

## 🛠️ Prerequisites

You will need Python 3 installed on your machine (Mac, Linux, or WSL).

Install the required Python libraries:

```bash
pip3 install opencv-python numpy pygame
```

````

_Note: You must have a video file (`grass.mp4`) and an audio file (`grass.mp3`) in the repository folder before installing!_

## 🚀 Installation

This project includes an idempotent, zero-friction install script. It automatically copies the engine to a hidden vault (`~/.touch-grass`) and injects the triggers into your `.bashrc` or `.zshrc`.

1. Clone the repository:

```bash
git clone [https://github.com/YOUR_USERNAME/touch-grass-cli.git](https://github.com/YOUR_USERNAME/touch-grass-cli.git)
cd touch-grass-cli

```

2. Make the installer executable and run it:

```bash
chmod +x install.sh
./install.sh

```

3. Reload your terminal (or just close and reopen it):

```bash
source ~/.bashrc  # Or source ~/.zshrc for Mac/Zsh users

```

## 🎮 Usage

Once installed, it operates globally from any directory.

- `tg` -> Instantly play the touch grass animation.
- `gut commit ...` -> Triggers the typo punishment.
- `git push` -> Triggers the post-deploy reward (only plays on a successful push).

## 🧹 Uninstallation

To remove Touch Grass CLI from your system:

1. Delete the hidden vault: `rm -rf ~/.touch-grass`
2. Open your `~/.bashrc` or `~/.zshrc` and delete the `🌿 TOUCH GRASS TERMINAL TRIGGERS 🌿` block at the bottom.
````
