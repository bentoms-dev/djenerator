# Djenerator

Generate djent-style MIDI patterns for your music compositions.

## Installation

You can install `djenerator` using `pip`. Open your terminal or command prompt and run:

```bash
pip install djenerator

### Usage

After installing the package, you can use it to generate djent-style MIDI patterns.

```bash
generate_djent

By default, this command will generate a MIDI pattern with a tempo of 160 BPM and save it as DjentPattern.mid in your current directory.

You can also specify optional arguments:

--file-name or -f: Specify the base name for the generated MIDI file (default is 'DjentPattern').
--num-measures or -n: Specify the number of measures in the pattern (default is 4).
--tempo-bpm or -t: Specify the tempo in BPM (default is 160).
--note-range or -r: Specify the range of MIDI notes as a tuple (e.g., --note-range 40 52 for notes from 40 to 52).
Example with optional arguments:

```bash
djenerator --file-name DjentPattern --num-measures 8 --tempo-bpm 140 --note-range 36 48


#### License

This package is distributed under the MIT License. See the LICENSE file for details.

##### Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request on the GitHub repository.

###### Credits

Created by Ben Toms
