# Rutgers Korean Oral Exam Simulator [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
An oral exam simulator created for Rutgers University - New Brunswick's Elementary Korean
2022 Fall Semester course (01:574:101:01) utilizing [Google's Text-to-Speech](https://gtts.readthedocs.io/en/latest/) API.

**Disclaimer:** This does not calculate the quality of your Korean speech.
This program just fetches a random question prompt and just speaks the prompt, while
also considering any variants that it might have.

If you're going to use this, it might not be good because i literally wrote this in 1h42min
(at the time of writing).

## Run From Source
1. Download the latest version of [Python](https://www.python.org/downloads/)
2. Download this repository and navigate to the directory's root.
3. Run these commands
```
python -m pip install -r requirements.txt
python src/main.py
```

If you want to keep outputting random voices, just do `python src/main.py`.
Do not execute from the inside of `src`.

## Syntax

For prompts,
 - `-` means the program will give the question
 - `*` means the program will skip the question
 - Anything after `#` will be considered as a comment

## Credits

Maintained & created by Andrew Hong | Class of 2026
