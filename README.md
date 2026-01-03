
# 🎵 Music Classification & Automation

**An AI-powered music library organizer that uses Gemini to categorize your songs by mood.**

##  Overview

Manually sorting thousands of songs into playlists is time-consuming. This project automates the process by using the **Gemini 2.5 Flash-Lite** model to analyze your MP3 metadata (Artist and Title) and automatically move files into mood-based folders like **Chill**, **High Energy**, **Romance**, or **Bollywood**.

### Key Features

* **AI Mood Analysis:** Leverages LLMs to understand the "vibe" of a song without needing audio analysis.
* **Automated File Management:** Automatically creates folders and moves your `.mp3` files into them.
* **Rate-Limit Friendly:** Built-in **Exponential Backoff** and cooldown timers to stay within Google's Free Tier quotas.
* **Metadata Extraction:** Uses `tinytag` to read ID3 tags efficiently.

---

##  Installation & Setup

### 1. Prerequisites

* Python 3.10 or higher.
* A Google AI Studio API Key ([Get it here](https://aistudio.google.com/)).

### 2. Clone the Repository

```
git clone https://github.com/yaashlodha/Music_Classfication.git
cd Music_Classfication

```

### 3. Set Up Virtual Environment

It is highly recommended to use a virtual environment to keep your dependencies isolated:

```
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

```

### 4. Install Dependencies

```
pip install google-genai tinytag python-dotenv

pip install -r requirements.txt

```

---

## ⚙️ Configuration

1. **API Key:** Create a `.env` file in the root directory and add your key:
```
GEMINI_API_KEY=your_actual_api_key_here

```


2. **Target Folder:** Open `music_categorizer.py` and update the `TARGET_FOLDER` variable to point to your music directory.

---

##  Usage

Simply run the main script to start organizing your music:

```
python music_categorizer.py

```

---

##  Project Structure

* `music_categorizer.py`: The core automation script.
* `remove_name.py`: A utility script for cleaning up file names before processing.
* `.env`: (Ignored by Git) Stores your sensitive API keys.

---

##  Contributing

Contributions are welcome! If you have ideas for new mood categories or feature improvements, feel free to fork the repo and open a Pull Request.



---

**Would you like me to help you generate a `LICENSE` file or a `.gitignore` file to complete your repository setup?**
