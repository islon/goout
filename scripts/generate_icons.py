import struct
import zlib

def create_png(width, height, r, g, b, a=255):
    signature = b'\x89PNG\r\n\x1a\n'
    
    def crc32(data):
        crc = 0xffffffff
        for byte in data:
            crc ^= byte
            for _ in range(8):
                crc = (crc >> 1) ^ (0xedb88320 if crc & 1 else 0)
        return (crc ^ 0xffffffff) & 0xffffffff
    
    def chunk(chunk_type, data):
        length = struct.pack('>I', len(data))
        chunk_data = chunk_type + data
        crc = struct.pack('>I', crc32(chunk_data))
        return length + chunk_data + crc
    
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'
        for x in range(width):
            cx, cy = width // 2, height // 2
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist < min(width, height) * 0.35:
                raw_data += bytes([r, g, b, a])
            elif dist < min(width, height) * 0.45:
                raw_data += bytes([r, g, b, int(a * 0.6)])
            else:
                raw_data += bytes([r, g, b, int(a * 0.2)])
    
    idat = zlib.compress(raw_data)
    iend = b''
    
    return signature + chunk(b'IHDR', ihdr) + chunk(b'IDAT', idat) + chunk(b'IEND', iend)

for size in [16, 32, 48, 128]:
    png_data = create_png(size, size, 102, 126, 234)
    with open(f'favicon-{size}.png', 'wb') as f:
        f.write(png_data)

apple_icon = create_png(180, 180, 102, 126, 234)
with open('apple-touch-icon.png', 'wb') as f:
    f.write(apple_icon)

print('图标创建成功：')
print('  - favicon-16.png')
print('  - favicon-32.png')
print('  - favicon-48.png')
print('  - favicon-128.png')
print('  - apple-touch-icon.png')