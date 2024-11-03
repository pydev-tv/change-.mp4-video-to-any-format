from moviepy.editor import VideoFileClip

def convert_video_format(input_file, output_file):
    try:
        # Load the video file
        video = VideoFileClip(input_file)

        # Determine the output format from the file extension
        if output_file.endswith('.wav'):
            # Convert to WAV
            audio = video.audio
            audio.write_audiofile(output_file)
            print(f"Converted '{input_file}' to '{output_file}'")
        else:
            # Write the video file in the specified format
            video.write_videofile(output_file)
            print(f"Converted '{input_file}' to '{output_file}'")

        # Close the video clip
        video.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_video_path = "input_video.mp4"  # Change to your input file
    output_audio_path = "output_audio.wav"  # Change to your output file
    output_video_path = "output_video.avi"  # Example for outputting video in a different format

    # Convert to WAV
    convert_video_format(input_video_path, output_audio_path)

    # Convert to another video format (e.g., AVI)
    convert_video_format(input_video_path, output_video_path)
