# BOSS Direct Recruitment Job Information Crawler and PDF Generator

[简体中文](../README.md) | [English](README_en.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Deutsch](README_de.md)

A Python program that automatically crawls job information from BOSS Direct Recruitment website and generates formatted PDF reports.

## Features

- Automatic crawling of BOSS Direct job information
- Support for custom search conditions (position, city, pages)
- Save raw data in JSON format
- Generate beautiful PDF format reports
- Support Chinese character display
- Automatic pagination
- Include job title, company, salary, location, and other information

## System Requirements

- Python 3.7+
- Chrome browser (for web crawling)
- macOS/Linux/Windows

## Installation Steps

1. Clone or download this project locally

2. Create and activate virtual environment (recommended):
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Chinese font settings (if PDF shows garbled characters):

For macOS users:
- System usually includes required Chinese fonts
- If garbled, download and install Source Han Sans:
```bash
curl -O https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SimplifiedChinese/SourceHanSansSC-Regular.otf
```

For Windows users:
- Ensure Chinese fonts are installed (like Microsoft YaHei or SimSun)
- Or download and install Source Han Sans

For Linux users:
```bash
# Ubuntu/Debian:
sudo apt-get install fonts-wqy-microhei

# CentOS/RHEL:
sudo yum install wqy-microhei-fonts
```

## Usage

1. Run the crawler program:
```bash
python main.py
```

2. Enter search conditions as prompted:
```
Please enter job title to search: Python Engineer
Please enter city code (e.g., Beijing 101010100, default is Beijing): [Press Enter for default]
Please enter maximum pages to crawl (default is 5): [Press Enter for default]
```

3. Common city codes reference:
- Beijing: 101010100
- Shanghai: 101020100
- Guangzhou: 101280100
- Shenzhen: 101280600
- Hangzhou: 101210100
- Chengdu: 101270100

## Output Files

The program generates two files:

1. JSON file: contains raw data
   - Filename format: `jobTitle_cityCode_jobs_timestamp.json`
   - Example: `PythonEngineer_101010100_jobs_20240223_172956.json`

2. PDF report: formatted job information report
   - Filename format: `jobTitle_cityCode_jobs_timestamp.pdf`
   - Example: `PythonEngineer_101010100_jobs_20240223_172956.pdf`

## PDF Report Content

Generated PDF report includes:
- Title page: displays "Job Information Report"
- Statistics: shows total number of jobs found
- Job details:
  - Job title (highlighted in blue)
  - Company name
  - Salary range
  - Work location

## Notes

1. Crawler usage notes:
   - Recommended to have intervals between each crawl
   - Avoid frequent mass crawling
   - Recommended to use default 5-page limit

2. PDF generation notes:
   - Ensure Chinese fonts are installed
   - PDF files are automatically paginated
   - Supports Chinese and special characters

3. Possible issues:
   - If CAPTCHA appears, please try again later
   - If PDF shows garbled characters, follow the font installation instructions above
   - If network connection fails, check network settings

## Development Plans

- [ ] Add more search condition support
- [ ] Optimize PDF report style
- [ ] Add data analysis functionality
- [ ] Support export to more formats

## Contribution Guidelines

Welcome to submit Issues and Pull Requests to help improve this project.

## License

MIT License 