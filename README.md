# Raffle
<img width="687" alt="Screen Shot 2023-03-22 at 11 59 37 PM" src="https://user-images.githubusercontent.com/91110018/227107829-61dbe774-c069-4cbd-97fc-dd3eff3b8d84.png">

This project was taught as a Technical Project Workshop for the Association of Computer Scientists at the University of Texas at Austin. This project is complete, though small changes may be added in the future. You can find more information [here](https://github.com/UT-ABCS/tech-workshops).  <br />

The goal of this project is to create a raffle from respondees of a given Google Form by utilizing the Google Sheets API. This workshop will cover:
+ selecting a random item from a list
+ obtaining credentials from the Google Cloud Console
+ using pip to install third party libraries into a Python project
+ retrieving data from Google Sheets using the Google Sheets API

You can find the slides associated with this workshop at [this link](https://google.com).  <br />
  
__Technology Used__
+ Python
+ pip
+ Google Cloud Platform
+ Google Sheets API

## Installation
1. Ensure that you have the latest version of Python and pip installed on your computer 
2. Clone this repository, `cd` into this respository
3. Install the necessary dependencies by calling `pip install -r requirements.txt`
4. Run the program by calling `python raffle.py`

## How to run
Before running this code, make sure that you have a Google Cloud project and a Spotify Web Application made.
1. `cd` into this respository
2. Go to the Google Cloud Console and navigate to your Google Cloud project.
3. Download the OAuth 2.0 Client ID associated with your Google Cloud project.
4. Move the OAuth Client ID into your repository on the top level, and title the file `credentials.json`.
5. Create a new file called `secret.py`
6. In `secret.py`, add the following code:
```
# Spreadsheet of Google Form responses we can raffle from
SPREADSHEET_ID = "ID OF GOOGLE SHEET"

# Range to check within the spreadsheet
SPREADSHEET_RANGE = "A2:F"
```
7. Call `python raffle.py`.

## Find a bug?
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!

## Potential Future Improvements
For those who want to continue this project you can add additional functionality to:
+ Only consider each respondee once by checking the UT EID of responses
+ Raffle multiple times without replacement
+ Pull data from multiple different spreadsheets
