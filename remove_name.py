from pathlib import Path

# Configuration
# 1. Set the folder where your files are located
TARGET_FOLDER = Path("D:\Music") 

# 2. Set the text you want to remove from the filenames
# Example: If file is "image_draft_v1.jpg" and you remove "_draft", it becomes "image_v1.jpg"
TEXT_TO_REMOVE = "_spotdown.org" 

def remove_text_from_filenames(folder_path, text_to_remove):
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Folder not found: {folder}")
        return

    if not text_to_remove:
        print("Please specify text to remove.")
        return

    print(f"Scanning '{folder}' to remove '{text_to_remove}' from filenames...")

    count = 0
    # Iterate over all files in the directory
    for file_path in folder.iterdir():
        if file_path.is_file():
            original_name = file_path.name
            
            # Check if the text exists in the filename
            if text_to_remove in original_name:
                # Create the new name
                new_name = original_name.replace(text_to_remove, "")
                
                # Optional: Clean up double spaces if 'text_to_remove' left some behind
                new_name = new_name.replace("  ", " ").strip()
                
                new_path = file_path.with_name(new_name)
                
                # Prevent overwriting existing files
                if new_path.exists():
                    print(f"Skipping: '{original_name}' -> '{new_name}' (Target file already exists)")
                else:
                    try:
                        file_path.rename(new_path)
                        print(f"Renamed: '{original_name}' -> '{new_name}'")
                        count += 1
                    except Exception as e:
                        print(f"Error renaming '{original_name}': {e}")
    
    print(f"Finished. Renamed {count} files.")

if __name__ == "__main__":
    remove_text_from_filenames(TARGET_FOLDER, TEXT_TO_REMOVE)
