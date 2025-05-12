import numpy as np
from PIL import Image
from noise import pnoise2

width, height = 512, 512
scale = 100.0  # Higher scale = more zoomed out
octaves = 6
persistence = 0.5
lacunarity = 2.0

def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity):
    noise = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            noise[y][x] = pnoise2(x / scale,
                                  y / scale,
                                  octaves=octaves,
                                  persistence=persistence,
                                  lacunarity=lacunarity,
                                  repeatx=width,
                                  repeaty=height,
                                  base=0)
    return noise

# Generate noise
noise = generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity)

# Normalize noise to 0–255
noise_normalized = ((noise - noise.min()) / (noise.max() - noise.min()) * 255).astype(np.uint8)

# Optional: apply color palette (grayscale or color map)
img = Image.fromarray(noise_normalized, mode='L')  # 'L' for grayscale
img = img.convert("RGB")  # Convert to RGB for future color mapping

# Show the image
img.show()
