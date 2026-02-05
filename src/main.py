import os
import json
import pandas as pd

from agent import generate_answer


def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".log", ".txt"]:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()

    elif ext == ".csv":
        df = pd.read_csv(file_path)
        return df.to_string().split("\n")

    elif ext == ".xlsx":
        df = pd.read_excel(file_path)
        return df.to_string().split("\n")

    elif ext == ".json":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return json.dumps(data, indent=2).split("\n")

    else:
        raise ValueError("Unsupported file format")


def extract_error_lines(lines):
    keywords = ["error", "exception", "traceback", "fatal", "failed"]
    return [line for line in lines if any(k in line.lower() for k in keywords)]


def analyze_file_with_ai(file_path):
    lines = read_file(file_path)
    error_lines = extract_error_lines(lines)

    if not error_lines:
        return "✅ No errors found in the uploaded file."

    error_text = "\n".join(error_lines[:50])
    return generate_answer(error_text)
