#!/usr/bin/env python3

import argparse
from mutagen.oggopus import OggOpus
from mutagen.flac import Picture
from base64 import b64encode

def embed_thumbnail(audio_file, thumbnail_file):
    # Read the thumbnail image
    covart = Picture()
    covart.data = open(thumbnail_file, 'rb').read()
    covart.type = 3  # Cover (front)
    covart.mime = "image/jpeg"  # Set the MIME type explicitly
    covart.desc = "Cover (front)"  # Add a description for the cover art

    # Open the audio file and embed the thumbnail
    audio = OggOpus(audio_file)
    audio['metadata_block_picture'] = b64encode(covart.write()).decode('ascii')

    # Save the changes
    audio.save()
    print(f"Thumbnail from '{thumbnail_file}' embedded into '{audio_file}' successfully.")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Embed a thumbnail image into an Ogg Opus audio file.")
    parser.add_argument("audio_file", help="Path to the Ogg Opus audio file.")
    parser.add_argument("thumbnail_file", help="Path to the thumbnail image file (e.g., .jpg).")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to embed the thumbnail
    embed_thumbnail(args.audio_file, args.thumbnail_file)

if __name__ == "__main__":
    main()
