# Welcome to Merge Madness 24!
![Merge Madness](/helpers/merge-madness.jpg)

Join our NCAA bracket challenge and sharpen your Git skills at the same time! Whether you're a Git newbie or a seasoned veteran, follow these steps to submit your bracket predictions.

## Step 1: Fork the Repository
At the top-right corner of the page, click the Fork button. This creates a copy of the repository in your GitHub account.

## Step 2: Clone Your Fork
Open your terminal or Git Bash.
Clone your forked repository to your local machine with the following command:

```git clone https://github.com/<your-github-username>/merge-madness-24.git```

Change directory to the cloned repository:
```cd merge-madness-24```

## Step 3: Create a New Branch
Create a new branch using your GitHub username for easy identification:

```git checkout -b <your-github-username>```

## Step 4: Fill Out Your Bracket

Open the `bracket.json` file in your preferred text editor.
Fill out your bracket predictions in the file.
Ensure you follow the format provided to maintain consistency, keeping team names exactly the same spelling and capitalization.

## Step 5: Commit Your Changes
After you've filled out your bracket, it's time to commit your changes:

Add the modified bracket.json file:
```git add bracket.json```
Commit your changes with a meaningful message:
```git commit -m "Submit <your-github-username>'s bracket"```

## Step 6: Push Your Branch to GitHub
Push your new branch to GitHub:

```git push origin <your-github-username>```

## Step 7: Submit a Pull Request
Go to your forked repository on GitHub.
You'll see a Compare & pull request button for your recently pushed branches. Click it to create a pull request.

Ensure the base repository is set to ewimpey/merge-madness-24 and the base branch is main. The "compare" branch should be your username branch.
Give your pull request a title and description, such as `<your-github-username> bracket submission`
Click Create pull request.

***
Congratulations! You've successfully submitted your bracket for the Merge Madness 24 challenge.

Next Steps
Watch the repository for updates, including the leaderboard and game results.
Feel free to discuss predictions, strategies, and Git tips in the Issues section!
Thank you for participating, and may the best bracket win!
