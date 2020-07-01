# Git Is Good
## About

### General Information

__Challenge__: The flag used to be there. But then I redacted it. Good Luck.

__Challege Category__: FORENSICS

__Challenge Difficulty__: Medium

__Skills__: GIT CUI, and log viewing

Download the repo [here.](https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc)

## Solution

Here, we are given a git repository, with file named ```flag.txt```. Now let's view the contents of it.

![Image1]()

It says ```flag{REDACTED}```. It tried this as the flag in the input field but didn't work. I wonder if the flag is really _REDACTED_ so I tried to view the logs of the file, and found there were these logs.

![Image2]()

Then I try to find the changes from the previous 2 commits using the ```--patch``` or ```-p``` flag.

![Image3]()

__Flag__: flag{protect_your_git}
