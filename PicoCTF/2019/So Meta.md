# So Meta

---
## Description

Find the flag in this picture.
Hint 1 : What does meta mean in the context of files?
Hint 2 : Ever heard of metadata?

---
## Solution

Metadata is data that describes other data.

from the name or the hint you can notice that the flag is in the metadata of the image , you can use an online tool to examine it but in my case i know two tools imagemagick and exiftool that can get the metadata from the image

```bash
$ identify -verbose pico_img.png | grep picoCTF
    Artist: picoCTF{s0_m3ta_eb36bf44}

$ exiftool pico_img.png | grep picoCTF
Artist                          : picoCTF{s0_m3ta_eb36bf44}
```

---
## Flag

picoCTF{s0_m3ta_eb36bf44}
