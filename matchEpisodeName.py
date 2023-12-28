import os

def rename_subtitles_to_match_videos(video_ext, srt_ext, directory):
    video_files = []
    srt_files = []

    for file in sorted(os.listdir(directory)):
        if file.endswith(video_ext):
            video_files.append(file)
        elif file.endswith(srt_ext):
            srt_files.append(file)

    if len(video_files) != len(srt_files):
        print("Error: The number of video files does not match the number of SRT files.")
        return

    for video, srt in zip(video_files, srt_files):
        video_name, _ = os.path.splitext(video)
        srt_name, _ = os.path.splitext(srt)

        if video_name != srt_name:
            new_srt_name = f"{video_name}{srt_ext}"
            old_srt_path = os.path.join(directory, srt)
            new_srt_path = os.path.join(directory, new_srt_name)
            os.rename(old_srt_path, new_srt_path)
            print(f"Renamed '{srt}' to '{new_srt_name}'")

if __name__ == "__main__":
    # Ask for directory path
    directory = input("Enter the directory path: ")
    
    # Ask for video file extension
    video_ext = input("Enter the video file extension (e.g., .mp4, .mkv, .avi): ")

    # Ask for subtitle file extension
    srt_ext = input("Enter the subtitle file extension (e.g., .srt): ")

    rename_subtitles_to_match_videos(video_ext, srt_ext, directory)
