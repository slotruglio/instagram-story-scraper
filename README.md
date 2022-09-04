# instagram-story-scraper
Simple Instagram Story Scraper without login and visualization

## Installation
```bash
pip install -r requirements.txt
```
Please write in a file called `path.txt` the path of your chrome driver. This could vary depending on your OS. Check the internet for more information.
For example:
`/Users/user/.wdm/drivers/chromedriver/os/version/chromedriver`

## Usage
To scrape stories from a user, run the following command:
```bash
python scraper.py <username>
```

To scrape stories from a list of users, run the following command:
```bash
python scraper.py -l <username1> <username2> <username3> ...
```

To scrape stories from a file. Put it in this folder and run the following command:
```bash
python scraper.py -f <filename>
```
where filename is a text file containing a list of usernames, one per line.

Running the script without argument will scrape stories from the users in the `users.txt` file.

## Output
The output will be a folder for each user containing the stories in `jpg` or `mp4` format.

### Things to know
- This code works only for public accounts.
- The source of the stories is NOT the Instagram API, so it is possible that some stories are not available or at some iteration the scraper will not work.
- To work, the scraper connects to https://insta-stories.online/. This website is not mine, I just use it to scrape the stories.