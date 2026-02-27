import cv2
import numpy as np
import time
import os
import sys
import shutil
import pygame
def get_terminal_dimensions():
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines - 1
def play_braille_video(video_path, audio_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open '{video_path}'.")
        return
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frame_delay = 1.0 / fps
    dot_map = np.array([
        [1, 8], 
        [2, 16], 
        [4, 32], 
        [64, 128]
    ])
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(audio_path)
    except pygame.error:
        print(f"Error: Could not load audio file '{audio_path}'. Make sure it exists!")
        return
    sys.stdout.write("\033[?1049h\033[?25l\033[2J\033[H")
    sys.stdout.flush()
    pygame.mixer.music.play()
    try:
        while True:
            ret, frame = cap.read()
            if not ret: break
            start_time = time.time()
            term_w, term_h = get_terminal_dimensions()
            vid_h, vid_w = frame.shape[:2]
            max_img_w = term_w * 2
            max_img_h = term_h * 4
            scale = min(max_img_w / vid_w, max_img_h / vid_h)
            new_img_w = max(2, int((vid_w * scale) // 2) * 2)
            new_img_h = max(4, int((vid_h * scale) // 4) * 4)
            char_w = new_img_w // 2
            char_h = new_img_h // 4
            pad_x = (term_w - char_w) // 2
            pad_y = (term_h - char_h) // 2
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized_gray = cv2.resize(gray, (new_img_w, new_img_h))
            resized_color = cv2.resize(frame, (char_w, char_h))
            rgb_frame = cv2.cvtColor(resized_color, cv2.COLOR_BGR2RGB)
            edges = cv2.Canny(resized_gray, 50, 150)
            binary = edges > 128
            reshaped = binary.reshape(char_h, 4, char_w, 2).transpose(0, 2, 1, 3)
            braille_values = np.sum(reshaped * dot_map, axis=(2, 3)).astype(int)
            out_str = ""
            empty_line = " " * term_w + "\n"
            out_str += empty_line * pad_y
            for y in range(char_h):
                row_str = " " * pad_x 
                for x in range(char_w):
                    val = braille_values[y, x]
                    if val == 0:
                        row_str += " "
                    else:
                        r, g, b = rgb_frame[y, x]
                        char = chr(0x2800 + val)
                        row_str += f"\033[38;2;{r};{g};{b}m{char}"
                pad_right = term_w - pad_x - char_w
                row_str += "\033[0m" + (" " * pad_right) + "\n"
                out_str += row_str
            pad_bottom = term_h - pad_y - char_h
            out_str += empty_line * pad_bottom
            sys.stdout.write("\033[H" + out_str)
            sys.stdout.flush()
            elapsed = time.time() - start_time
            if frame_delay > elapsed:
                time.sleep(frame_delay - elapsed)
    except KeyboardInterrupt:
        pass
    finally:
        pygame.mixer.music.stop()
        cap.release()
        
        # 1. \033[?1049l = Exit Alternate Screen Buffer (restores previous terminal state)
        # 2. \033[?25h = Restore Cursor
        # 3. \033[0m = Reset terminal colors
        sys.stdout.write("\033[?1049l\033[?25h\033[0m")
        sys.stdout.flush()
        
        # We delete the print statement so it leaves zero trace that it was ever here!
        print("\n  [+] 🌿 Grass touched.\n  Still no bitches, still broken code.\n")
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    video_file = os.path.join(script_dir, "grass.mp4") 
    audio_file = os.path.join(script_dir, "grass.mp3") 
    play_braille_video(video_file, audio_file)