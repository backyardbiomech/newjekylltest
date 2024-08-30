import re

fname = "Labs/ADInstrumentsLabs/Electromyography/Electromyography.md"
# Read the original file
with open(fname, 'r') as file:
    data = file.read()

# Find all image tags
image_tags = re.findall(r'!\[.*?\]\(.*?\)\{[^}]*?\}', data, re.DOTALL)

for tag in image_tags:
    # Extract the width and height in inches
    width_in_inches = re.search(r'width="(\d+(\.\d+)?)in"', tag, re.DOTALL)
    height_in_inches = re.search(r'height="(\d+(\.\d+)?)in"', tag, re.DOTALL)

    new_tag = tag

    if width_in_inches:
        width_in_inches = float(width_in_inches.group(1))

        # Convert width from inches to pixels (1 inch = 96 pixels)
        width_in_pixels = int(width_in_inches * 96)

        # Replace the width in the original tag
        new_tag = re.sub(r'width=".*?in"', f'width="{width_in_pixels}"', new_tag, flags=re.DOTALL)

    if height_in_inches:
        height_in_inches = float(height_in_inches.group(1))

        # Convert height from inches to pixels (1 inch = 96 pixels)
        height_in_pixels = int(height_in_inches * 96)

        # Replace the height in the original tag
        new_tag = re.sub(r'height=".*?in"', f'height="{height_in_pixels}"', new_tag, flags=re.DOTALL)

        # Format the tag for kramdown
        new_tag = new_tag.replace("{", "{:").replace("in", "")

        # Replace the original tag in the data
        data = data.replace(tag, new_tag)

# Write the modified data to a new file
with open(fname, 'w') as file:
    file.write(data)