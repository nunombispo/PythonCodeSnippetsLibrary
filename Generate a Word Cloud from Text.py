# pip install matplotlib wordcloud

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_word_cloud(text, output_image="wordcloud.png"):
    # Create a WordCloud object with custom configurations
    wordcloud = WordCloud(width=800, height=400, background_color="white", collocations=False).generate(text)

    # Save the word cloud image to a file
    wordcloud.to_file(output_image)
    print(f"Word cloud saved as '{output_image}'")

    # Display the generated word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# Example usage:
if __name__ == "__main__":
    # Load text from a file (replace 'sample.txt' with your file)
    with open("sample.txt", "r", encoding="utf-8") as file:
        text = file.read()
    generate_word_cloud(text)


# Why? This snippet creates a visually appealing word cloud from any given text using the wordcloud and matplotlib
# libraries. It's great for visualizing textual data, summarizing documents, or simply exploring word frequency
# patterns in an engaging way.
