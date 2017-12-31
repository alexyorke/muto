# muto
Convert Google Slides and PowerPoint presentations into GIFs via the CLI.

[![Updates](https://pyup.io/repos/github/Decagon/muto/shield.svg)](https://pyup.io/repos/github/Decagon/muto/) [![Python 3](https://pyup.io/repos/github/Decagon/muto/python-3-shield.svg)](https://pyup.io/repos/github/Decagon/muto/)

![Alt Text](https://i.imgur.com/ZaN9Xqb.gif)

For example, run `python3 muto.py --url https://docs.google.com/presentation/d/1R72VWZoNsywrLC9_8LdUiiBwi4it2Sl8UHDZq0rjHVc/edit?usp=sharing` to generate a GIF of that Google Slide and save it in the current directory.


```
usage: muto.py [-h] [--url URL] [--width [WIDTH]] [--height [HEIGHT]]
               [--slides [SLIDES]] [--durationPerSlide [DURATIONPERSLIDE]]
               [--output [OUTPUT]]

Creates GIFs from Google Slides

optional arguments:
  -h, --help            show this help message and exit
  --url URL             The Google Slide url
  --width [WIDTH]       The maximum width of the GIF
  --height [HEIGHT]     The maximum height of the GIF
  --slides [SLIDES]     The slides that should be included in the GIF. For
                        example, 1,2,3,5-6,10
  --durationPerSlide [DURATIONPERSLIDE]
                        How long each frame should display in seconds; floats
                        are allowed
  --output [OUTPUT]     The location where the final GIF should be stored
```


Muto only downloads the slides that you need, and only in the resolution that you require. This saves bandwidth and overall processing speed. Support for PowerPoint presentations coming soon!
