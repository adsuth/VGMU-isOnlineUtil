# isOnlineUtil
## Intro
This is a utility for checking if youtube URLs in a given TSV (or CSV) are available in [VGMVersus](https://github.com/adsuth/VGMVersus) or [VGMB](https://github.com/adsuth/VGMB). It does this by checking the video's metadata via the Youtube API.

Currently, the utility can only flag **deleted** videos, **not copyrighted ones**.

Upon completion, the program will output an HTML file to `./index.html`, that can then be opened on a web browser like Chrome.

## Arguments
| Argument | Shorthand | Use | Notes |
| --- | --- | --- | --- |
| `--help` | `-h` | Displays help regarding arguments |  | 
| `source` |  | the source directory or directories, one after another. | eg: `file1 file2 file3` | 
| `--verbose` | `-v` | If present, verbose messaging will be enabled | Verbose messaging includes printing each song as they are being checked. | 

## Important Note
**Using the Youtube API requires proper credentials. In order to use this utility, you will need to be approved by me, [adsuth](https://github.com/adsuth).**

Note that the token (token.pickle) will be placed **outside the isOnlineUtil directory**, so make sure you keep it safe.
