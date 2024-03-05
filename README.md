# Welcome to Merge Madness 24!
![Merge Madness](/helpers/merge-madness.jpg)

Join our NCAA bracket challenge and sharpen your Git skills at the same time! Whether you're a Git newbie or a seasoned veteran, follow these steps to submit your bracket predictions.

## Step 1: Join the fun!
Join by opening a new issue. Click **Issues** and then **new issue**. 

The issue should be titled: **"{your-github-username} joining merge madness"**

It's important to title it like that, as that will create a new branch named after your username.

## Step 2: Fork the Repository
At the top-right corner of the page, click the Fork button. This creates a copy of the repository in your GitHub account.

## Step 3: Clone Your Fork
Open your terminal or Git Bash.
Clone your forked repository to your local machine with the following command:

```git clone https://github.com/<your-github-username>/merge-madness.git```

Change directory to the cloned repository:
```cd merge-madness```

## Step 4: Change to your branch
Change to your branch, the one that has the same name as your username:

```git checkout -b <your-github-username>```

## Step 5: Fill Out Your Bracket

The easiest way to fill out the bracket is by running `fill_bracket.py`.
That will prompt you to provide the winner of each game. 
After picking each game, it will generate a new file called `final_bracket.json` with all of your picks.

(If you don't want to run python, you can open `initial_bracket.json` in a text editor and manually fill in winners, but you must ensure you keep the formatting, spelling, capitalization exactly the same)

## Step 6: Commit Your Changes
After you've filled out your bracket, it's time to commit your changes:

Add the modified bracket.json file:
```git add final_bracket.json```
Commit your changes with a meaningful message:
```git commit -m "Submitting <your-github-username> bracket"```

## Step 7: Push Your Branch to GitHub
Push your new branch to GitHub. Remember that your branch name is the same as your GitHub username.

```git push origin <your-github-username>```

## Step 8: Submit a Pull Request
Go to your forked repository on GitHub.
You'll see a Compare & pull request button for your recently pushed branches. Click it to create a pull request.

Ensure the base repository is set to ewimpey/merge-madness and the base branch is main. The "compare" branch should be your username branch.
Give your pull request a title and description, such as `<your-github-username> bracket submission`
Click Create pull request.

***
Congratulations! You've successfully submitted your bracket for the Merge Madness challenge.

Next Steps:
* Confirm that the pull request gets approved
* Watch the repository for updates, including the leaderboard and game results.
* There will be some more madness to come once we get to the Sweet 16! 
* Feel free to discuss predictions, strategies, and Git tips in the Issues section!

## Thank you for participating, and may the best bracket win!
