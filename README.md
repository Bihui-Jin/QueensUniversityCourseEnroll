# QueensUniversityCourseEnroll

Automatically get enrolled into all classes in the shopping car -- capable for Queen's University at Kingston only

***The user requires to add classes to the shopping car first

The user might require to increase the time response allowance from 20 (wait = WebDriverWait(driver,20)) to a higher value

This project uses selenium getting from https://www.selenium.dev/downloads/ and browser related driver driverchromedriver.exe from https://chromedriver.chromium.org/home

For the browser's driver, the user may need to replace the executable path from executable_path="/home/user/Documents/chromedriver_linux64/chromedriver" to your local path

1. enter your NetId
2. enter your Password
3. change the term to what you want to enroll with
4. change 2 enroll time pause.until((datetime.datetime(YYYY,M,DD,HH,MM,SS)). One is before 15 mins of your enrollment begin time i.e. 7.45 am and set another at your enrollment begin time i.e. 8.00 am
