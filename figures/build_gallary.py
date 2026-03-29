import os
from PIL import Image
import pillow_heif

# --- Configuration ---

# List of album folder names (inside the "albums" directory)
albums = ["Yosemite", "Kearsarge Pass-Kings Canyon NP", "Southern Utah (Bryce - Capitol - Cedar Breaks etc etc)"]

# Base directories for the albums and where HTML files will be generated.
albums_dir = os.path.join(os.getcwd(), "albums")
output_dir = os.path.join(os.getcwd(), "galleries")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Supported image extensions
supported_ext = (".jpg", ".jpeg", ".png", ".gif", ".heic")

# --- Functions ---

def convert_heic_to_jpg(album_path, filename):
    """
    Convert a HEIC image to JPEG and return the new filename.
    The new file is stored in the same album folder.
    """
    file_path = os.path.join(album_path, filename)
    try:
        heif_file = pillow_heif.read_heif(file_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )
    except Exception as e:
        print(f"Error reading HEIC {filename}: {e}")
        return None

    new_filename = os.path.splitext(filename)[0] + ".jpg"
    new_path = os.path.join(album_path, new_filename)
    try:
        image.save(new_path, "JPEG")
        print(f"Converted {filename} to {new_filename}")
        return new_filename
    except Exception as e:
        print(f"Error saving {new_filename}: {e}")
        return None

def generate_gallery_html(album_name, image_list):
    """
    Generates an HTML gallery page for the given album.
    Each image is wrapped in a clickable link that opens it full screen.
    """
    # Start gallery snippet with a grid container.
    gallery_html = '<div class="gallery">\n'
    for img in image_list:
        # Wrap each image in an anchor tag pointing to the full image
        gallery_html += f'  <a href="../albums/{album_name}/{img}" target="_blank"><img src="../albums/{album_name}/{img}" alt="{img}"></a>\n'
    gallery_html += '</div>\n'
    return gallery_html

def generate_album_page(album_name, gallery_html):
    """
    Generates a full HTML page (as a string) for a single album.
    """
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{album_name} Gallery</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {{
      font-family: sans-serif;
      margin: 20px;
      background-color: #f5f5f5;
    }}
    h1 {{
      text-align: center;
      margin-bottom: 20px;
    }}
    .gallery {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 10px;
    }}
    .gallery img {{
      width: 100%;
      height: auto;
      display: block;
      cursor: pointer;
      transition: transform 0.2s;
    }}
    .gallery img:hover {{
      transform: scale(1.05);
    }}
    nav {{
      margin-bottom: 20px;
      text-align: center;
    }}
    nav a {{
      margin: 0 10px;
      text-decoration: none;
      color: #007acc;
    }}
  </style>
</head>
<body>
  <nav>
    <a href="../index.html">Home</a>
  </nav>
  <h1>{album_name} Gallery</h1>
  {gallery_html}
</body>
</html>
"""
    return html

# --- Main Build Process ---

# A list to hold the names of all album pages generated
album_pages = []

for album in albums:
    album_path = os.path.join(albums_dir, album)
    if not os.path.isdir(album_path):
        print(f"Album folder '{album}' does not exist in {albums_dir}. Skipping.")
        continue

    # List image files in the album folder
    files = os.listdir(album_path)
    image_files = []
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext not in supported_ext:
            continue

        # If the file is a HEIC image, convert it to JPG.
        if ext == ".heic":
            new_file = convert_heic_to_jpg(album_path, f)
            if new_file:
                image_files.append(new_file)
        else:
            image_files.append(f)

    # Sort the image list (optional)
    image_files.sort()

    # Generate the gallery HTML snippet for this album
    gallery_snippet = generate_gallery_html(album, image_files)
    album_page_html = generate_album_page(album, gallery_snippet)

    # Write the album HTML page to the output directory
    album_filename = f"{album}.html"
    album_pages.append((album, album_filename))
    album_output_path = os.path.join(output_dir, album_filename)
    with open(album_output_path, "w") as f:
        f.write(album_page_html)
    print(f"Generated gallery page for album: {album}")

# --- Generate an Index Page That Links to All Album Pages ---

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Albums Index</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: sans-serif;
      margin: 20px;
      background-color: #f5f5f5;
    }
    h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    ul {
      list-style: none;
      padding: 0;
      text-align: center;
    }
    li {
      margin: 10px 0;
    }
    a {
      text-decoration: none;
      color: #007acc;
      font-size: 1.2em;
    }
  </style>
</head>
<body>
  <h1>Albums</h1>
  <ul>
"""

for album, filename in album_pages:
    index_html += f'    <li><a href="galleries/{filename}">{album} Gallery</a></li>\n'

index_html += """  </ul>
</body>
</html>
"""

# Write the index page in the root folder
with open("index.html", "w") as f:
    f.write(index_html)

print("Index page generated successfully.")

