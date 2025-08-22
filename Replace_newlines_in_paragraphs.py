import re

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

# Path to the Markdown file
file_path = '/Users/jacksonbe3/Library/CloudStorage/Box-Box/A&P lab materials/ADInstrumentsLabs/ECG & Heart Sounds Mac/Student Protocol/ECG.md'
remove_newlines_from_paragraphs_and_lists(file_path)