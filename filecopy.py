import os
import shutil

def copyfiles(srcdir, destdir, table):
  for root, _, files in os.walk(srcdir):
    for file in files:

      # Construct full source and destination paths
      src_file_path = os.path.join(root, file)
      relative_path = os.path.relpath(root, srcdir)
      dest_folder_path = os.path.join(destdir, relative_path)
      dest_file_path = os.path.join(dest_folder_path, file)

      if (os.path.join("/", relative_path, file) not in table): 
        continue

      # Ensure the destination folder exists
      os.makedirs(dest_folder_path, exist_ok=True)

      # Copy the file
      shutil.copy2(src_file_path, dest_file_path)
      print(f"Copied: {src_file_path} -> {dest_file_path}")

def main():
  if os.path.isdir("./in"):
    
    table = {}
    with open("./list.txt", "r") as file:
      for line in file:
        # Strip whitespace and newline characters
        path = line.strip()
        # Add to dictionary with a default value (e.g., True)
        table[path] = True

    copyfiles("./in", "./out", table)


if __name__ == "__main__":
  main()