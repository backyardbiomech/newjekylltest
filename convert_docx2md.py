"""
Add path to a docx at the bottom, then run (NOTE that doc files need to be opened in word and converted to docx first!!!)
Will convert to markdown with python, forcing tables to be either 
pipe table or html. images saved to ./media, and image size tags
converted to kramdown compatable inline attributes, 
for publication on jekyll sites
Will also add yaml header automatically for jekyll, though may need some edits
"""
import re
import subprocess
from pathlib import Path

def convert_docx_to_md(docx_path, md_path, media_path):
    # Run the pandoc command to convert the .docx file to .md file
    pandoc_command = [
        'pandoc', str(docx_path),
        '--from=docx',
        '--to=markdown-grid_tables-simple_tables-multiline_tables',
        '-o', str(md_path),
        f'--extract-media={media_path}'
    ]
    subprocess.run(pandoc_command, check=True)

def adjust_image_paths(md_path, media_path):
    # Read the original file
    with open(md_path, 'r') as file:
        data = file.read()

    # Adjust image paths to be relative
    def replace_path(match):
        full_path = match.group(1)
        # Ensure the path is relative to the media directory
        relative_path = Path(full_path).relative_to(media_path)
        return f'![]({relative_path})'

    data = re.sub(r'!\[\]\((.*?)\)', replace_path, data)

    # Write the modified data to the same file
    with open(md_path, 'w') as file:
        file.write(data)

def process_image_tags(md_path):
    # Read the original file
    with open(md_path, 'r') as file:
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

        # Format the tag for kramdown and add a newline after the closing brace
        new_tag = new_tag.replace("{", "{:").replace("in", "").replace("\n", " ") + "\n\n"

        # Replace the original tag in the data
        data = data.replace(tag, new_tag)

    # Write the modified data to the same file
    with open(md_path, 'w') as file:
        file.write(data)

def add_yaml_header(md_path, first_word):
    # Create the YAML header
    yaml_header = f"""---
layout: page
permalink: /{first_word.lower()}/
title: Physiology Lab – {first_word.title()}
math: katex
---
"""

    # Read the original file
    with open(md_path, 'r') as file:
        data = file.read()

    # Add the YAML header to the top of the file
    data = yaml_header + data

    # Write the modified data to the same file
    with open(md_path, 'w') as file:
        file.write(data)

def remove_newlines_from_paragraphs_and_lists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
        
    # Split the text into lines
    lines = markdown_text.splitlines()
    
    # This will hold the processed lines
    processed_lines = []
    
    # Flag to track if we are inside a paragraph
    in_paragraph = False
    paragraph_buffer = []
    
    # Check for YAML header
    in_yaml = False

    for line in lines:
        # Check if we are entering or exiting a YAML header
        if line.strip() == '---':
            in_yaml = not in_yaml
            processed_lines.append(line)
            continue
        
        # If we are in a YAML header, just add the line
        if in_yaml:
            processed_lines.append(line)
            continue
        
        # Check for empty lines
        if line.strip() == '':
            # If we are processing a list or paragraph, we should skip empty lines
            if in_paragraph or processed_lines and (re.match(r'^\d+\.', processed_lines[-1]) or re.match(r'^\s*-\s', processed_lines[-1])):
                continue
            else:
                # If not in paragraph or list, just skip the empty line
                continue
        
        # Check if the line is an image
        if re.match(r'!\[.*\]\(.*\)', line):
            # If we were building a paragraph, flush it before adding the new line
            if in_paragraph:
                processed_lines.append(' '.join(paragraph_buffer))
                paragraph_buffer = []
                in_paragraph = False
            
            # Add the image line as is
            processed_lines.append(line)
            continue
        
        # Check if the line is a markdown structure (headers, tables, etc.)
        if line.startswith('#') or line.startswith('|'):
            # If we were building a paragraph, flush it before adding the new line
            if in_paragraph:
                processed_lines.append(' '.join(paragraph_buffer))
                paragraph_buffer = []
                in_paragraph = False
            
            # Add the current line (tables, etc.)
            processed_lines.append(line)
        elif re.match(r'^\d+\.', line) or re.match(r'^\s*-\s', line):
            # If it's a list item, check if the last processed line was an empty line
            if processed_lines and processed_lines[-1].strip() == '':
                # Skip adding another newline
                continue
            
            # If we were building a paragraph, flush it before adding the new line
            if in_paragraph:
                processed_lines.append(' '.join(paragraph_buffer))
                paragraph_buffer = []
                in_paragraph = False
            
            # Add the current list item
            processed_lines.append(line)
        else:
            # If it's a regular paragraph line, add it to the buffer
            paragraph_buffer.append(line.strip())
            in_paragraph = True

    # If there is any remaining paragraph content, add it to the processed lines
    if in_paragraph:
        processed_lines.append(' '.join(paragraph_buffer))

    # Join the processed lines back into a single string
    cleaned_markdown = '\n'.join(processed_lines)

    # Write the cleaned content to a new file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_markdown)
        
def main(docx_path_str):
    # Convert the input path string to a Path object
    docx_path = Path(docx_path_str)

    # Extract the first word from the file name (without extension)
    first_word = docx_path.stem.split()[0]

    # Define the output markdown path in the same directory as the docx file
    md_path = docx_path.parent / f"{first_word}.md"

    # Define the media extraction path in the same directory as the docx file
    media_path = docx_path.parent / (docx_path.stem + '_media')

    # Convert the .docx file to .md file using pandoc
    convert_docx_to_md(docx_path, md_path, media_path)

    # Adjust the image paths in the markdown file to be relative
    adjust_image_paths(md_path, media_path)

    # Process the image tags in the markdown file
    process_image_tags(md_path)

    # Add the YAML header to the markdown file
    add_yaml_header(md_path, first_word)
    
    #clean up the markdown (remove newlines mid paragraph)
    remove_newlines_from_paragraphs_and_lists(md_path)
    

if __name__ == "__main__":
    # Path to the input .docx file
    docx_path = "/Users/jacksonbe3/Library/CloudStorage/Box-Box/A&P lab materials/ADInstrumentsLabs/Reflexes & Reaction Times Mac/Student Protocol/Reflexes and Reaction Times Student Protocol MAC.docx"
    main(docx_path)
    
    