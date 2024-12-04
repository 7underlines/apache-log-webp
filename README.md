# Apache Log WebP Compatibility Checker

## Description
Analyze your Apache 2 access log to identify browsers that lack full WebP support.

## Installation
```bash
# Clone the repository
git clone https://github.com/7underlines/apache-log-webp.git

# Navigate to the project directory
cd apache-log-webp

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Start the script
python log_analyzer.py
```

### Example output:
```
Browsers without full WebP support:
Firefox 55.0 - 1161
Safari 13.1.2 - 28
Safari 11.1.2 - 23
IE 11.0 - 12
Firefox 15.0 - 8
Firefox 53.0 - 6
Chrome 24.0.1309 - 1
Chrome 26.0.1410 - 1
IE 5.1 - 1
Firefox 28.0 - 1
Firefox 64.0 - 1
Safari 10.1.2 - 1
Firefox 7.0.1 - 1
Safari 7.0.3 - 1
```
User agents are grouped by browser name and version, with the number of occurrences shown next to each entry.

Note that requests from older browsers are often not from legitimate users but from bots. For instance, the 1161 requests with `Firefox 55.0` in this example were all from a bot, making them irrelevant to WebP support considerations. To determine if real users are involved, inspect your `access.log` file.

## License
[AGPL-3.0](LICENSE)
