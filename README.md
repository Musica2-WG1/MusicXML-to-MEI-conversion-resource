# MusicXML-to-MEI-conversion-resource

This repository contains a set of MusicXML, MEI files and scripts used in the article The Music Encoding Initiative and its Generation Workflows. These files serve as a basis for illustrating and comparing the results of different workflows for converting standard music notation into MEI format, especially using Verovio or MEI Garage. The goal of this repository is to provide reproducible examples of MusicXML to MEI conversion and highlight subtle differences in metadata encoding between conversion tools.

## Reproduction Instructions

If you wish to replicate the command lines with Verovio introduced in the article, use the `verovio` command to convert MusicXML files to MEI:

`verovio -f musicxml -t mei -o output.mei input.xml`

```bash
for file in *.xml; do
  verovio -f musicxml -t mei -o "${file%.xml}.mei" "$file"
done
```
## License

The files in this repository are shared under a CC BY 4.0 license. You are free to use, share, and adapt the materials with proper attribution.


