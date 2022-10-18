import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from utils import *
from gtts import gTTS
from io import BytesIO
import random
import pygame

if __name__ == "__main__":
    prompts = get_prompts("prompts//oral_exam1.txt")
    prompt = random.choice(prompts)
    print(prompt)
    tts = gTTS(prompt, lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
