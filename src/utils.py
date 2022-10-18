from typing import List
import itertools


def parse_prompt(prompt: str) -> List[str]:
    """Parses a prompt into different variants if specified."""
    prompts = []

    stack = 0
    start_index = None
    results = {}
    for i, c in enumerate(prompt):
        if c == "[":
            if stack == 0:
                start_index = i + 1
            stack += 1
        elif c == "]":
            stack -= 1
            if stack == 0:
                out = prompt[start_index:i].split(", ")
                results[prompt[start_index - 1 : i + 1]] = out

    possibitilies = list(itertools.product(*results.values()))
    for x in possibitilies:
        current_prompt = prompt
        for i, y in enumerate(x):
            placeholder = list(results.keys())[i]
            current_prompt = current_prompt.replace(placeholder, y)

        prompts.append(current_prompt.split("#")[0])

    return prompts


def get_prompts(file_path: str) -> List[str]:
    """Reads a file and parses all prompts"""
    file = open(file_path, mode="r", encoding="utf-8")
    raw_prompts = file.read().split("\n")

    prompts = []
    for l in raw_prompts:
        if l.startswith("* "):
            continue
        elif l.startswith("- "):
            prompts += parse_prompt(l.replace("- ", ""))

    return prompts
