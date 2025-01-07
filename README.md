# Project Setup and Usage Guide
This guide will help you set up the virtual environment, install dependencies, and execute the project to fetch titles using Selenium and a headless Chrome browser.

---
## Directory Structure
```
Lambda/
├── tmp/                # Directory for Chrome headless binary
├── venv/               # Python virtual environment   (After creation)
├── calling.py          # Script to call the Lambda function
├── lambda_function.py  # Lambda function implementation
├── requirements.txt    # Python dependencies
```

---
## Steps to Set Up and Execute

### 1. Create a Virtual Environment
To isolate dependencies, create a Python virtual environment in the `Lambda` directory.
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 2. Install Dependencies
Install required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Download Chrome Headless Binary
1. Visit the [Chrome for Testing Availability](https://googlechromelabs.github.io/chrome-for-testing/) page
2. Find the latest stable version of `chrome-headless-shell`
3. Download the appropriate version for your operating system:
   - Windows: chrome-headless-shell-win64.zip
   - macOS: chrome-headless-shell-mac-x64.zip
   - Linux: chrome-headless-shell-linux-x64.zip
4. Extract the downloaded zip file
5. Place the chrome-headless-shell binary in the following path:
```
tmp/bin/chrome-headless-shell-win64/chrome-headless-shell.exe  # Windows
tmp/bin/chrome-headless-shell-mac-x64/chrome-headless-shell    # macOS
tmp/bin/chrome-headless-shell-linux-x64/chrome-headless-shell  # Linux
```

### 4. Verify the Headless Chrome Binary Path
Ensure the Chrome headless binary path is correctly set in `lambda_function.py`:
```python
CHROME_BINARY_PATH = os.path.join(
    os.path.dirname(__file__), "tmp", "bin", "chrome-headless-shell-win64", "chrome-headless-shell.exe"
)
```
Adjust the path according to your operating system.

### 5. Run the `calling.py` Script
The `calling.py` script invokes the Lambda function defined in `lambda_function.py`. It simulates a Lambda environment by passing an event and context.
Execute the script as follows:
```bash
python calling.py
```

### 6. Output
The script will:
- Fetch titles from Google search results.
- Print the titles to the console.
- Return a response object with the titles.

Sample console output:
```
Lambda invoked with event: {'requestContext': {'http': {'method': 'POST'}}, 'path': '/lambda_googlescholar', 'body': '{"keywords": ["AI"], "num_papers": 20}'}
Fetched Titles:
1. What is Artificial Intelligence?
2. Latest Trends in AI Research
...
```

---
## Notes
- The Chrome for Testing service provides versioned Chrome binaries specifically designed for automated testing
- Binary versions are guaranteed to work with corresponding ChromeDriver versions
- For debugging Chrome binary path issues:
  ```python
  print("Constructed Chrome Binary Path:", CHROME_BINARY_PATH)
  ```
- If running on AWS Lambda, package all dependencies and binaries as a deployment package
- Chrome headless shell is a lightweight version of Chrome designed specifically for automation and headless operation

---
## Requirements
- Python 3.10
- Selenium
- BeautifulSoup4
- Chrome headless shell binary (downloaded from Chrome for Testing service)