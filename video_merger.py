from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, concatenate_videoclips
from moviepy.video.VideoClip import ColorClip


# Function to freeze the last frame of a video clip
def freeze_last_frame(clip, new_duration):
    # Load the PNG image (to be displayed above the winning video)
    # overlay_image = ImageClip("assets/winner.png")  # Resize to match video width
    last_frame = clip.to_ImageClip(t=clip.duration-0.1)
    frozen_clip = concatenate_videoclips([clip, last_frame.set_duration(new_duration)])
    return frozen_clip


# Load the two video clips
video1 = VideoFileClip("animations/BubleSort_random_shuffle_animation.mp4")
video2 = VideoFileClip("animations/InsertionSort_random_shuffle_animation.mp4")

# Load the VS symbol image
vs_symbol = ImageClip("assets/VS.png").set_duration(max(video1.duration, video2.duration))

# Determine the maximum duration of the two videos
max_duration = max(video1.duration, video2.duration)

# print(video1.duration, video2.duration, max_duration)
# print(max_duration - video1.duration)
# print(max_duration - video2.duration)


# Freeze the last frame of the shorter video if needed
if video1.duration < max_duration:
    video1 = freeze_last_frame(video1, max_duration - video1.duration)

if video2.duration < max_duration:
    video2 = freeze_last_frame(video2, max_duration - video2.duration)

# Determine the height of the final video
total_height = video1.h + video2.h + vs_symbol.h//2

# Create a white background clip
background = ColorClip(size=(video1.w, total_height), color=(255, 255, 255),
                       duration=max(video1.duration, video2.duration))

# Create the final video with the two videos stacked vertically
final_clip = CompositeVideoClip([
    background,
    video1.set_position(("center", 0)),
    video2.set_position(("center", video1.h + vs_symbol.h//2)),
    vs_symbol.set_position(("center", video1.h))
], size=(video1.w, total_height))

# Set the duration to the maximum duration of the two videos
final_clip = final_clip.set_duration(max(video1.duration, video2.duration))

# Write the final video to a file
final_clip.write_videofile("assets/output.mp4", codec="libx264")
