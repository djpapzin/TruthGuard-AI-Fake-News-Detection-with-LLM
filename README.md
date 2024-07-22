# Fake News Classification with Meta-Llama-3-8B-Instruct

This project uses the `Meta-Llama-3-8B-Instruct` model to classify news articles as real or fake. The model is fine-tuned to specifically handle this task.

## Prerequisites

- Python 3.7 or later
- An API key from Together

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fake-news-classification.git
    cd fake-news-classification
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your Together API key as an environment variable:
    - On Unix-based systems, add this line to your `.bashrc` or `.zshrc` file:
      ```bash
      export TOGETHER_API_KEY='your_api_key_here'
      ```
    - On Windows, set the environment variable through the System Properties.

## Usage

Run the classification script with a sample article:
```bash
python classify_news.py
```

The script will output whether the given news article is classified as real or fake.

## Example

Here's an example of running the script:

```bash
$ python classify_news.py
Classification result: Fake
```

## Files

- `classify_news.py`: The main script for classifying news articles.
- `requirements.txt`: Lists the dependencies needed for the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.