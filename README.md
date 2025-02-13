# image_to_opus

`image_to_opus` is a Python tool that allows users to embed an image (JPEG or PNG) into an OGG container with an Opus audio stream **without re-encoding** the audio. This ensures that the original audio quality is preserved while adding visual metadata, such as cover art.

---

## Features

- **No Re-encoding**: The audio remains untouched, preserving its original quality.
- **Image Embedding**: Supports embedding JPEG or PNG images into the OGG container.
- **Simple Command-Line Usage**: Easy-to-use interface for quick processing.

---

## Prerequisites

Before using `image_to_opus`, ensure the following:

1. **Python 3** is installed on your system.
2. The following Python libraries are required:
   - `argparse`
   - `mutagen`
   - `base64`
3. Install the required dependencies using pip if they are not already installed:
   ```bash
   pip install mutagen
   ```

---

## Installation

Clone the repository or download the script to your local machine:

```bash
git clone https://github.com/your-repo/image_to_opus.git
cd image_to_opus
```

---

## Usage

Run the script using the following command:

```bash
python3 embed_thumbnail_in_opus.py 'input.opus' 'image.jpg'
```

### Arguments:
- **`input.opus`**: The Opus audio file you want to embed the image into.
- **`image.jpg`**: The image file to embed. This can also be a PNG file.

### Example:

If you have an Opus file named `song.opus` and a cover image named `cover.png`, you can embed the image into the audio file by running:

```bash
python3 embed_thumbnail_in_opus.py 'song.opus' 'cover.png'
```

## Notes

- Ensure the input files exist in the specified paths before running the command.
- The output file will overwrite the original `input.opus` file. Make a backup if needed.

---

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).
