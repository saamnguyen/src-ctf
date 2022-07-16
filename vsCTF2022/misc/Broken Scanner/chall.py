from PIL import Image
from itertools import product
from random import shuffle
from math import ceil


FLAG_FILE = 'flag.png'
TEMPLATE_FILE = 'scan_base.png'
OUTPUT_FILE = 'scan.apng'
OVERLAY_CANVAS_COORDS = (20, 60)  # canvas area starts at this coord
OVERLAY_KEY_COORDS = (563, 63)  # key area starts at this coord
FRAME_DURATION = 100  # in milliseconds


original_img = Image.open(FLAG_FILE)
original_pix = original_img.load()
original_width, original_height = original_img.size
assert original_img.size == (500, 270)
total_pixels = original_width * original_height
original_coords = [coord for coord in product(range(original_width), range(original_height))]
shuffle(original_coords)

total_frames = ceil(total_pixels / 256)

overlay_img = Image.open(TEMPLATE_FILE)
key_id_coords = [(OVERLAY_KEY_COORDS[0] + ((key_index // 64) * 10), OVERLAY_KEY_COORDS[1] + ((key_index % 64) * 4)) for key_index in range(256)]
key_value_coords = [(coord[0] + 4, coord[1]) for coord in key_id_coords]

overlay_pix = overlay_img.load()
for i, coord in enumerate(key_id_coords):
    overlay_pix[coord[0], coord[1]] = (0, i, 0)


images = []
while original_coords:
    scan_quantity = min(len(original_coords), 256)
    scanning_coords = [original_coords.pop() for _ in range(scan_quantity)]

    this_frame = overlay_img.copy()
    this_pix = this_frame.load()

    for color_val, coord in enumerate(scanning_coords):
        orig_x, orig_y = coord

        # place pixel on canvas
        canvas_x, canvas_y = orig_x + OVERLAY_CANVAS_COORDS[0], orig_y + OVERLAY_CANVAS_COORDS[1]
        this_pix[canvas_x, canvas_y] = (0, color_val, 0)

        # place pixel on key
        key_x, key_y = key_value_coords[color_val]
        this_pix[key_x, key_y] = original_pix[orig_x, orig_y]

    images.append(this_frame)

images[0].save(OUTPUT_FILE, save_all=True, append_images=images[1:], duration=FRAME_DURATION, loop=0)
