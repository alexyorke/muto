from bs4 import BeautifulSoup
import sys
import os
from urllib.request import urlopen
import imageio
import urllib.request
from random import *
import shutil
import argparse

# prepare command line args
parser = argparse.ArgumentParser(description='Creates GIFs from Google Slides')

parser.add_argument('--url',
                    help='The Google Slide url')

parser.add_argument('--width', type=int, nargs='?',
                    help='The maximum width of the GIF')

parser.add_argument('--height', type=int, nargs='?',
                    help='The maximum height of the GIF')

parser.add_argument('--slides', nargs='?',
                    help='The slides that should be included in the GIF. For example, 1,2,3,5-6,10')

parser.add_argument('--durationPerSlide', type=float, nargs='?',
                    help='How long each frame should display in seconds; floats are allowed')

parser.add_argument('--output', nargs='?',
                    help='The location where the final GIF should be stored')

args = parser.parse_args()

# parse args
googleSlideUrl = args.url

width = args.width
if (width is None):
    width = 960

height = args.height
if (height is None):
    height = 540

selectedSlides = args.slides
if (args.slides is None):
    selectedSlides = "all"

if (args.durationPerSlide is not None):
    secondsPerSlide = float(args.durationPerSlide)
else:
    secondsPerSlide = 0.5

# normalize url (it's a bit hacky)
googleSlideId = googleSlideUrl.split("presentation/d/")[1].split("/")[0]

tempDir = "/tmp/" + str(randint(10000, 100000))
os.makedirs(tempDir, exist_ok=True)

# convert slide indencies and ranges into int list
if (selectedSlides != "all"):
    finalPages = []
    for item in selectedSlides.split(","):
        if ("-" not in item):
            finalPages.append(int(item))
        else:
            startEndIndex = item.split("-")
            startIndex = startEndIndex[0]
            endIndex = startEndIndex[1]
            finalPages.extend(list(range(int(startIndex), int(endIndex) + 1)))

# download slide index
print("Fetching slide index...")
r = urlopen("https://docs.google.com/presentation/d/" +
            googleSlideId + "/htmlpresent").read()
soup = BeautifulSoup(r, "lxml")

slides = soup.findAll("section", {"class": "slide-content"})
slideUrls = []
images = []
counter = 0
for slide in slides:
    counter = counter + 1
    slideUrl = (slide.get("style").split("url(")[1][:-2])
    slideUrl = slideUrl.replace("showText=0", "showText=1")

    # poor man's url parsing
    slieUrl = slideUrl.replace("w=960", "w=" + str(width))
    slideUrl = slideUrl.replace("h=540", "h=" + str(height))
    slideUrls.append(slideUrl)

    # download slide
    if (selectedSlides != "all") and (counter not in finalPages):
        print("Skipping slide " + str(counter) + "...")
    else:
        print("Downloading slide " + str(counter) + "...")
        downloadSlideFilePath = tempDir + "/" + str(counter) + ".png"
        urllib.request.urlretrieve(slideUrl, downloadSlideFilePath)
        images.append(imageio.imread(downloadSlideFilePath))

print("Creating GIF...")
# https://stackoverflow.com/questions/753190/

outputFilePath = googleSlideId + "_pres.gif"

if (args.output) is not None:
    outputFilePath = args.output

imageio.mimsave(googleSlideId + "_pres.gif", images, duration=secondsPerSlide)

print("Cleaning up...")
shutil.rmtree(tempDir)
