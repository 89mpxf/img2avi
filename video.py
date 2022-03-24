# Import dependencies
import easygui
import sys
import os
from PIL import Image
import cv2

# Get path to images
path = easygui.diropenbox(msg="Select your image directory.", title=None)
if path is None:
    sys.exit(0)

# Get desired frame video
frameDelay = None
try:
    frameDelayPrompt = easygui.integerbox("Enter the desired frame rate below.")
    frameDelay = int(frameDelayPrompt)
except:
    pass


# Begin image correction
os.system("mkdir tmp")
print("Beginning image correction...")
print("")
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
        im = Image.open(os.path.join(path, file))
        width, height = im.size
        print(str(file) + " | " + str(width) + "x" + str(height))
        print("Processing " + str(file) + "...")
        imResize = im.resize((1920, 1080), Image.ANTIALIAS)
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            imResize.save("./tmp/" + file, 'JPEG', quality = 95)
            print("Successfully processed " + str(file))
        elif file.endswith(".png"):
            imResize.save("./tmp/" + file, 'PNG', quality = 95)
            print("Successfully processed " + str(file))
        print("")
print("Image processing complete.")
print("")

# Video generation routine
video_path = easygui.filesavebox(msg="Choose where to save the outputted video", default="output.avi", filetypes=["*.avi"])
if video_path is None:
    sys.exit(0)
print("Starting video generation...")
print("Writing to " + video_path)
print("")
images = [img for img in os.listdir("./tmp/") if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png")]
video_output = cv2.VideoWriter(video_path, 0, frameDelay, (1920, 1080))
for image in images:
    video_output.write(cv2.imread(os.path.join("./tmp/", image)))
cv2.destroyAllWindows()
video_output.release()
print("Video generation completed.")