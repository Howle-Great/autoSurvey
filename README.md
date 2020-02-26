# autoSurvey

This project will help people who need to send a large number of messages to different groups in https://vk.com/

### Installation

1. Replace selenium drivers in the drivers folder with your Google Chrome drivers.You can download all the necessary drivers from https://sites.google.com/a/chromium.org/chromedriver/downloads
2. Package installation
```bash
pip3 install selenium pyyaml
```
3. Add your post, message, and group links to the processing file.yaml file located in the root directory
4. Export your login and password for vk.com this way:
```bash
export LOGIN="<YOUR LOGIN>" PASSWORD="<YOUR PASSWORD>"
```
5. Run it
```bash
python3 run_tests.py
```
6. For the first time, you may need to enter a captcha from Google. You will have 4 minutes to do this.