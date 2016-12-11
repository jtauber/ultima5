#!/usr/bin/env python3

print("""
<style>
    body {
        width: 4096px;
        margin: 0;
        padding: 0;
    }
    .cell {
        background-image: url('http://wiki.ultimacodex.com/images/5/55/Ultima_5_-_Tiles-pc.png');
        background-repeat: no-repeat;
        height: 16px;
        width: 16px;
        display: inline-block;
    }
""")

for i in range(256):
    y, x = divmod(i, 32)
    y = -16 * y
    x = -16 * x
    print(".cell-{:02X} {{ background-position: {}px {}px; }}".format(i, x, y))

print("""
    .chunk {
        display: inline-block;
    }
</style>
""")

OMIT = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
    (1, 15),
    (2, 15),
    (6, 11),
    (7, 7),
    (7, 8),
    (7, 9),
    (7, 12),
    (8, 0),
    (8, 7),
    (8, 8),
    (8, 9),
    (8, 12),
    (9, 7),
    (9, 9),
    (9, 10),
    (9, 11),
    (9, 12),
    (9, 15),
    (10, 7),
    (10, 9),
    (10, 10),
    (10, 13),
    (10, 14),
    (10, 15),
    (11, 0),
    (11, 1),
    (11, 8),
    (11, 9),
    (11, 10),
    (11, 11),
    (11, 12),
    (11, 13),
    (12, 0),
    (12, 3),
    (12, 8),
    (12, 9),
    (12, 12),
    (13, 0),
    (13, 3),
    (13, 8),
    (13, 9),
    (13, 12),
    (14, 0),
    (15, 0),
    (15, 1),
    (15, 2),
    (15, 5),
]

with open("ULT/BRIT.DAT", "rb") as f:
    castle_dat = f.read()
    offset = 0
    for chunk_y in range(16):
        print("<div>")
        for chunk_x in range(16):
            if (chunk_y, chunk_x) in OMIT:
                print("<div class=\"chunk\">")
                for tile_y in range(16):
                    print("<div>")
                    for tile_x in range(16):
                        print("<div class=\"cell cell-01\"></div>", end="")
                    print("</div>")
                print("</div>", end="")
                continue
            print("<div class=\"chunk\">")
            for tile_y in range(16):
                print("<div>")
                for tile_x in range(16):
                    i = offset + tile_x + tile_y * 16
                    print("<div class=\"cell cell-{:02X}\"></div>".format(castle_dat[i]), end="")
                print("</div>")
            print("</div>", end="")
            offset += 256
        print()
        print("</div>", end="")
    print()
