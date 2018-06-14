## Least significant bit encoding
- Extract smallest bit from each byte in file
- Convert to hex and then to ascii
- Check all 8 alignments when converting binary number to hex

`python2 lsb.py | strings | grep 'flag'`
