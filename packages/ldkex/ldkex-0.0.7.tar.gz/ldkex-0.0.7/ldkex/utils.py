import decimal
import struct
import re

import webcolors


def read_int(file):
    bytes_data = read_fully(file, 4)
    return struct.unpack('>i', bytes_data)[0]


def read_coordinate(file):
    bytes_data = read_fully(file, 4)
    value = struct.unpack('>i', bytes_data)[0] * 1e-7
    bd = decimal.Decimal(value).quantize(decimal.Decimal('1.0000000'), rounding=decimal.ROUND_HALF_UP)
    return float(bd)


def read_long(file):
    bytes_data = read_fully(file, 8)
    return struct.unpack('>q', bytes_data)[0]


def read_double(file):
    bytes_data = read_fully(file, 8)
    return struct.unpack('>d', bytes_data)[0]


def read_pointer(file):
    bytes_data = read_fully(file, 8)
    return struct.unpack('>Q', bytes_data)[0]


def read_string(file, length):
    buffer = []
    buffer_size = 1024  # Read in chunks of 1 KB

    while length > 0:
        bytes_to_read = min(length, buffer_size)
        chunk = read_fully(file, bytes_to_read)
        if not chunk:
            break
        buffer.append(chunk.decode('utf-8'))
        length -= len(chunk)

    return ''.join(buffer).strip()


def read_boolean(file):
    byte = file.read(1)
    if len(byte) == 0:
        raise EOFError("End of file reached before reading a boolean")
    return byte != b'\x00'


def read_fully(file, size):
    data = bytearray()
    while len(data) < size:
        print(f"Reading {size - len(data)} bytes;")  # Debug
        chunk = file.read(size - len(data))
        if not chunk:
            raise EOFError("End of file reached before reading the required number of bytes")
        data.extend(chunk)
    return bytes(data)


def get_metadata_version(magic_number, file_type):
    if magic_number > 100:
        return 3
    elif file_type == "trk":
        return 2 if magic_number == 3 else 1
    else:
        return 2 if magic_number == 2 else 1


color_names = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque",
    "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue",
    "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan",
    "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey",
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred",
    "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey",
    "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey",
    "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro",
    "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew",
    "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush",
    "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
    "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink",
    "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey",
    "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon",
    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen",
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred",
    "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace",
    "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen",
    "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum",
    "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon",
    "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue",
    "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle",
    "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"
]

hex_color_regex = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$')
rgb_color_regex = re.compile(r'rgb\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
kml_color_regex = re.compile(r'\b[0-9a-fA-F]{8}\b')


def rgb_to_hex(rgb_color):
    r, g, b = map(int, rgb_color)
    return webcolors.rgb_to_hex((r, g, b))


def kml_color_to_hex(kml_color):
    return f"#{kml_color[6:8]}{kml_color[4:6]}{kml_color[2:4]}"


color_name_patterns = {name: re.compile(re.escape(name), re.IGNORECASE) for name in color_names}


def standardize_color(color):   # TODO optimise function execution time
    if isinstance(color, bytes):
        color = color.decode('utf-8')

    color = color.strip().lower()
    if color in color_names:
        return webcolors.name_to_hex(color)

    if hex_color_regex.match(color):
        return color

    rgb_match = rgb_color_regex.match(color)
    if rgb_match:
        return rgb_to_hex(rgb_match.groups())

    if kml_color_regex.match(color):
        return kml_color_to_hex(color)

    return ""
