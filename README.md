# Automatic Short Form Content Video Creator (asFCVC 🔥)

This project automates the creation of short-form content by scraping subreddits, synthesizing audio using Google Text-to-Speech (gTTS), and rendering videos with template background videos and subtitles.

## Setup

1. Clone the repository to your local machine.
2. Create a custom `.env` file in the root cloned file path with the following template:

```
SECRET={}
PERSONAL_USE={}
```

## Usage

1. Ensure you have the necessary Python packages installed.

```
pip install praw gtts python-dotenv
```

Alternatively, you can use the the following command to install all the required Python packages
```
pip install -r requirements.txt
```

2. Run the Python script!

```
python main.py
```

## Requirements

- [praw](https://pypi.org/project/praw/): A Python wrapper for the Reddit API.
- [gtts](https://pypi.org/project/gTTS/): A Python library and CLI tool to interface with Google Text-to-Speech API.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.

## Contributing

Contributions are welcome! If you have any ideas or suggestions for improvements, feel free to open an issue or submit a pull request.

---

**Disclaimer:** This project is for educational and personal use only. Please ensure compliance with Reddit's API usage policy and respect subreddit rules and guidelines when scraping content.
