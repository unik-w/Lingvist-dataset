import re
# import matplotlib.pyplot as plt 

def word_frequency(text):
    # Create a dictionary to store word counts
    word_counts = {}

    # Split the text into individual words
    words = re.split(r"\W+", text)

    # Iterate over the words and update the dictionary
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the dictionary by the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the frequency chart
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

from ebooklib import epub
from bs4 import BeautifulSoup

def extract_text_from_epub(epub_path):
    # Read the EPUB file
    book = epub.read_epub(epub_path)

    # Extract text content from the EPUB book
    text_content = []
    for item in book.get_items_of_type(epub.EpubItem.TEXT):
        soup = BeautifulSoup(item.content, 'html.parser')
        text_content.append(soup.get_text())

    return text_content

def save_text_to_file(text_content, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for text_chunk in text_content:
            file.write(text_chunk + '\n\n')

if __name__ == "__main__":
    # Provide the path to your EPUB file
    epub_path = 'HP1.epub'

    # Extract text content
    text_content = extract_text_from_epub(epub_path)

    # Save text content to a text file
    output_file = 'output.txt'
    save_text_to_file(text_content, output_file)

    print(f'Text extracted from EPUB file and saved to {output_file}')


# new=word_frequency(text)
# print(new)