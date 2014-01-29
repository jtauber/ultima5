# Notes

## `.TLK` Files

Ultima V has `.TLK` files but only four of them:

 - `CASTLE.TLK`
 - `DWELLING.TLK`
 - `KEEP.TLK`
 - `TOWNE.TLK`

In Ultima IV, the files were all 4608 bytes made up of 288 bytes for each of
16 characters.

Here in Ultima V, they are variable length and a hexdump of the files reveals
no readable text.

## Castle, Dwelling, Keep, Towne

As well as `.TLK`, each of Castle, Dwelling, Keep, Towne has a `.DAT` file and
a `.NPC` file. There are quite a few additional `.DAT` files but these are the
only four `.NPC` and `.TLK` files.

### `.DAT` Files

Looking at a hexdump of `CASTLE.DAT`, it's clearly a map (likely referring to
tiles either with one byte or two). The Castle, Dwelling, Keep, Towne `.DAT`
files are all 16384 bytes. I suspect `BRIT.DAT` is the surface of Britannia
and `UNDER.DAT` is the Underworld. I'll attempt to tackle Castle, Dwelling,
Keep and Towne first, though.

### `TILES.` Files

There are two `TILES.` files:

 - TILES.4
 - TILES.16

which I presume are the tiles at different bit-depths. There are actually a
lot of files with a `.4` and `.16` pair.

Given the variety of lengths, I suspect these files are compressed.
