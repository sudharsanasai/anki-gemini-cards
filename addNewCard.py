import sys
from pathlib import Path

# Make sure 'pylib' is in your Python path
sys.path.insert(0, str(Path(__file__).parent / "pylib"))
from anki import Collection

# Path to your collection
col_path = "/Users/sudharsanasaithambi/Library/Application Support/Anki2/User 1/collection.anki2"
col = Collection(col_path)

# Get the default notetype (e.g., Basic)
model = col.models.by_name("Basic")
if not model:
    print("No 'Basic' note type found!")
    exit(1)

# Create a new note
note = col.newNote()
note.model()['name'] = "Basic"
note.fields[0] = "Front text"
note.fields[1] = "Back text"

# Add the note to the collection (this creates the card)
if col.addNote(note):
    print("Note and card created successfully!")

# Save changes and close
col.save()
col.close()