# GitHub Follower List Bot

This is a Python script that utilizes Selenium and the Firefox web driver to retrieve the list of followers for a given GitHub user.

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Mozilla Firefox browser

## Usage

1. Clone the repository or download the files to your local machine.

2. Install the required dependencies by running the following command:
```
pip install selenium
```

3. Make sure you have Mozilla Firefox installed on your machine.

4. Open the `main.py` file in a text editor and modify the following line to provide the GitHub username of the user you want to retrieve the follower list for:
```python
username = input("Enter the Username of the user you want to receive the tracking list: ")
````

5. Make sure you have Mozilla Firefox installed on your machine.

6. Open a terminal or command prompt and navigate to the directory where the files are located.

7. Run the script using the following command:

```
python main.py
```
8. The script will launch a Firefox browser window, navigate to the user's GitHub profile, retrieve the follower list, and display the names of the followers.

## Explanation

The script follows these steps to retrieve the follower list:

1. It initializes the `GitHubBot` class, which takes the GitHub username and the Selenium web driver as inputs.

2. The `controller` method is responsible for the main functionality of the bot.

3. The `controller` method opens the user's GitHub profile page, maximizes the browser window, and navigates to the "Following" page.

4. It locates the section on the page that contains the follower elements using CSS selectors.

5. It retrieves a list of follower elements using the CSS selector `.f4.Link--primary`.

6. It iterates over the follower elements, extracts the text of each element (the follower's name), and appends it to the `self.followers` list.

7. Finally, it prints the list of followers.
