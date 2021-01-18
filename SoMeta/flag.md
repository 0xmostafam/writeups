Find the flag in this picture.

from the name or the hint you can notice that the flag is in the metadata of the image , you can use an online tool to examine it but in my case i know two tools imagemagick and exiftool

```bash
$ identify -verbose pico_img.png | grep picoCTF
    Artist: picoCTF{s0_m3ta_eb36bf44}

$ exiftool pico_img.png | grep picoCTF
Artist                          : picoCTF{s0_m3ta_eb36bf44}
```
