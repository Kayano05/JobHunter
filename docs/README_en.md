# BOSS Direct Job Information Crawler and PDF Generator

[简体中文](../README.md) | [English](README_en.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Deutsch](README_de.md)

This is a Python program that automatically crawls job information from the BOSS Direct website and generates formatted PDF reports.

## Features

- Automatically crawl job information from BOSS Direct
- Support custom search conditions (position, city, pages)
- Save raw data in JSON format
- Generate beautiful PDF format reports
- Support Chinese display
- Automatic pagination
- Include job title, company, salary, location, and other information

## System Requirements

- Python 3.7+
- Chrome browser (for web crawling)
- macOS/Linux/Windows
- Network environment that can access Google services (VPN required in mainland China as the program depends on ChromeDriver download)

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

4. Chinese font settings (if PDF Chinese display is garbled):

For macOS users:
- The system usually includes the required Chinese fonts
- If garbled characters appear, you can download and install Source Han Sans:
```bash
curl -O https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SimplifiedChinese/SourceHanSansSC-Regular.otf
```

For Windows users:
- Make sure Chinese fonts are installed (such as Microsoft YaHei or SimSun)
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

2. Enter search conditions according to prompts:
```
Please enter the job title to search: Python Engineer
Please enter city code (e.g., Beijing 101010100, default is Beijing): [Press Enter to use default]
Please enter maximum pages to crawl (default is 5): [Press Enter to use default]
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
   - Filename format: `job_title_city_code_jobs_timestamp.json`
   - Example: `Python Engineer_101010100_jobs_20240223_172956.json`

2. PDF report: formatted job information report
   - Filename format: `job_title_city_code_jobs_timestamp.pdf`
   - Example: `Python Engineer_101010100_jobs_20240223_172956.pdf`

## PDF Report Content

The generated PDF report includes:
- Title page: displays "Job Information Report"
- Statistics: shows total number of jobs found
- Job details:
  - Job title (highlighted in blue)
  - Company name
  - Salary range
  - Work location

## Important Notes

1. Network Environment Notes:
   - The program needs to download ChromeDriver at startup, which requires access to Google servers
   - If you are using it in mainland China, make sure you can access Google services (e.g., using a VPN)
   - The program will not start and run properly without access to Google services

2. Crawler Usage Notes:
   - Recommended to have intervals between each crawl
   - Avoid frequent mass crawling
   - Recommended to use the default 5-page limit

3. PDF Generation Notes:
   - Ensure Chinese fonts are installed in the system
   - PDF files will automatically paginate
   - Supports Chinese and special characters

4. Possible Issues:
   - If CAPTCHA appears, please try again later
   - If Chinese characters are garbled in PDF, please follow the font installation instructions above
   - If network connection fails, please check network settings
   - If ChromeDriver download fails, please check if you can access Google services

## Development Plan

- [ ] Add more search condition support
- [ ] Optimize PDF report style
- [ ] Add data analysis functionality
- [ ] Support export to more formats

## Contribution Guide

Welcome to submit Issues and Pull Requests to help improve this project.

## License

MIT License 