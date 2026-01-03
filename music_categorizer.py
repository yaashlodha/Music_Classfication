import os, shutil, time, random
from pathlib import Path
from google import genai
from tinytag import TinyTag
from dotenv import load_dotenv

# CONFIG
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
TARGET_FOLDER = Path(r"D:\Music")
MOOD_CATEGORIES = [
    "High Energy",
    "Chill",
    "Happy",
    "Sad",
    "Romance",
    "Party",
    "Focus",
    "Relax",
    "Uplifting",
    "Angry",
    "Dreamy",
    "Moody"
]

# To this (ensure the argument name is correct):
client = genai.Client(api_key=API_KEY)

def get_mood(file_path):
    # Try only 3 times per song to avoid infinite loops
    for attempt in range(2):
        try:
            tag = TinyTag.get(file_path)
            
            response = client.models.generate_content(
                model="gemma-3-27b-it", 
                contents=f"Analyze the song {tag.title} by {tag.artist}. Based on its known tempo, genre, and emotional tone, categorize it into exactly one of these moods: {MOOD_CATEGORIES}. Return only the category name."
            )
            
            result = response.text.strip()
            
            for m in MOOD_CATEGORIES:
                if m.lower() in result.lower(): return m
            print(result)
            return "Uncategorized"

        except Exception as e:
            err_msg = str(e)
            if "limit: 0" in err_msg:
                print("!!! CRITICAL: Your API key has a 0 limit. Please check Google AI Studio project settings.")
                return "STOP" # Signal the main loop to kill the script
            
            if "429" in err_msg:
                wait = 20 * (attempt + 1)
                print(f"Rate limit for {file_path.name}. Waiting {wait}s...")
                time.sleep(wait)
                continue
            if "404" in err_msg:
                print("Error 404: Model not found. Check if the model name is correct.")
                continue
    return "Uncategorized"

def organize():
    # Move files OUT of Uncategorized first to retry them
    uncat = TARGET_FOLDER / "Uncategorized"
    if uncat.exists():
        for f in uncat.glob("*.mp3"):
            shutil.move(str(f), str(TARGET_FOLDER / f.name))

    files = list(TARGET_FOLDER.glob("*.mp3"))
    print(f"Starting analysis of {len(files)} songs...")

    for f_path in files:
        mood = get_mood(f_path)
        
        if mood == "STOP": 
            print("Script halted due to zero quota.")
            break
            
        dest = TARGET_FOLDER / mood
        dest.mkdir(exist_ok=True)
        shutil.move(str(f_path), str(dest / f_path.name))
        print(f"✓ [{mood}] {f_path.name}")
        time.sleep(7) # Steady 5-second gap to prevent hitting limits

if __name__ == "__main__":
    organize()