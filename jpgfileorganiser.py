import os
import shutil

# ==========================================
#       JPG FILE ORGANIZER
# ==========================================

# Folder containing the files
source_folder = "source file"

# Folder where JPG files will be moved
destination_folder = "JPG Files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Count moved files
moved_files = 0

print("=" * 50)
print("        JPG FILE ORGANIZER")
print("=" * 50)

# Check whether source folder exists
if not os.path.exists(source_folder):
    print("\n❌ Source folder does not exist.")
    print("Please create a folder named 'source file'.")
else:

    # Check all files in source folder
    for filename in os.listdir(source_folder):

        # Check for JPG files
        if filename.lower().endswith(".jpg"):

            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Make sure it is a file
            if os.path.isfile(source_path):

                shutil.move(source_path, destination_path)

                print(f"✅ Moved: {filename}")

                moved_files += 1

    print("\n" + "=" * 50)
    print(f"Total JPG files moved: {moved_files}")
    print("=" * 50)

    if moved_files == 0:
        print("ℹ️ No JPG files were found.")
    else:
        print("🎉 JPG files organized successfully!")