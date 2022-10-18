from utils import *
from gtts import gTTS
from io import BytesIO
import random

if __name__ == "__main__":
    mp3_fp = BytesIO()
    prompts = get_prompts("prompts//oral_exam1.txt")
    prompt = random.choice(prompts)
    print(prompt)
    tts = gTTS(prompt, lang="ko")
    tts.write_to_fp(mp3_fp)
