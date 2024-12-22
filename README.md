# Subdomain Takeover Finder

- This Python tool simplifies the process of discovering and validating subdomains for potential takeover vulnerabilities. It integrates with assetfinder and subzy to automate subdomain enumeration, cleaning, validation, and takeover checks.

## Features

1. Automated Subdomain Discovery: Uses assetfinder to collect subdomains.
2. Subdomain Cleaning and Validation: Filters out invalid or wildcard subdomains, ensuring only valid entries are processed.
3. Subdomain Takeover Checks: Uses subzy to check for subdomain takeover vulnerabilities.
4. User-Friendly Execution: Requires minimal input and handles file creation and processing automatically.

## Requirements

- Python 3.6+
- Tools:
    - assetfinder
    - subzy

- Add $GOPATH and $GOBIN to your environment variables:

```
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN
```

Ensure these tools are installed and accessible in your system's PATH.


## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/subdomain-takeover-finder.git
cd subdomain-takeover-finder
```

2. Install the required tools:
    - Follow the installation instructions for assetfinder.
    - Follow the installation instructions for subzy.

3. (Optional) Create a virtual environment and install dependencies if needed:

```
python -m venv env
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

## Usage
Run the tool:

```
python subdomain_takeover_finder.py
Enter the target domain when prompted:
Enter the domain (e.g., example.com): example.com
```

The tool will:
- Use assetfinder to enumerate subdomains and save them to <domain>_raw.txt.
- Clean and validate subdomains, saving results to <domain>_cleaned.txt.
- Use subzy to check for subdomain takeover vulnerabilities.


## Example Run
Example run output for `example.com`:

![alt][./example.PNG]

## Output
- Raw Subdomains: <domain>_raw.txt
- Cleaned Subdomains: <domain>_cleaned.txt
- Subzy Output: Displayed on the terminal.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality.

## Disclaimer
This tool is for educational and ethical purposes only. The author is not responsible for any misuse. Always obtain proper authorization before scanning or testing any domain.
