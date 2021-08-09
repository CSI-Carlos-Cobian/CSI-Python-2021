<div style="text-align:center">
        <img    src="../../images/csi.png" 
                title="Colegio San Ignacio" 
                width="20%" 
                height="20%" />
</div>
<br>

# Module 1: Git and GitHub
### Welcome to Python-2021! In this class we will be using GitHub as our code repository. This is an industry standard that should be understood by all students looking to pursue a carreer path related to software.
<br>

# What is Git?
*"Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency"*
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \- [The Git Website](https://git-scm.com/)

<br>

#### Git allows you to track changes in a file system, refered to as repository. Some examples would be adding and removing files, adding and removing lines to a file, renaming files.

<br>

## Repository
*"A receptacle or place where things are deposited, stored, or offered"*
<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \- My google search.

<br>

#### In class we will refer to repositories as the copies of the course file system that each one of us holds. Repositories are both local and remote, meaning that repositories are available both offline on your machine, and online on a remote webserver. In our class we will use GitHub as our remote host.

<br>

## Pull
#### When you pull a repository you are updating your local copy with any changes that have been made on the remote version. 

<br>

## Commit
#### A commit saves any changes made to files on your local machine to the local repository. Before committing you will select which files and/or lines you would like to include. You don't have to include all of them but you should make sure that what you are committing is correct. A commit requires a message. This message must be descriptive of what is being changes. This helps you keep track of every version change. Commits may be deleted or reverted locally.

<br>

## Push
#### Pushing to your remote repository will upload all pending commits. You should make sure that all commits are stable and correct before pushing. Oncce a commit has been pushed it will be available to anyone working on the repository. It is easier to delete or revert commits that are local and unpushed as another user may have pulled them already. 

<br>

### A Diagram

<br>

<img    src="https://www.pngitem.com/pimgs/m/608-6085261_git-push-and-pull-hd-png-download.png" 
        title="Colegio San Ignacio" 
        width="60%" 
        height="60%" />



<br>

## Install [Git](https://git-scm.com/downloads) **Correctly** (Windows). `(1pts)`
### In this class we'll use Visual Studio's integrated implementation of Git. MAC users may use XCode's integration. We'll install Git on our machines and select Visual Studio Code as our default editor.

<br>

### When installing, use default settings with these exceptions.
- Select Visual Studio Code as your default editor.<br>
<img    src="GitSelect.png" 
        title="Select Visual Studio Code as your default editor" 
        width="50%" 
        height="50%" />

- Use the default windows console.<br>
<img    src="DefaultConsole.png" 
        title="Select Windows Console." 
        width="50%" 
        height="50%" />

<br>

# What is GitHub?
Think of GitHub as an Instagram of Code. A whole bunch of programmers from all around the world share their code so that others may view and like it. They all use the technology of Git and share it on this Hub. GitHub is free, but you may pay to keep your repositories private.

<br>

## Set up a GitHub Account.

### Go to [GitHub.com](https://github.com) and Sign Up **Correctly**. `(1pts)`
* Use your student Email.
* Use the following format for your <u>**username**</u>: CSI-Name-Lastname. 
* Pay attention to Capitalization
* Use my github name as an example: `CSI-Carlos-Cobian`
<br>
<img    src="GitHubSetup.png" 
        title="Create Account" 
        width="70%" 
        height="70%" />

<br>

# What is a branch?
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

<br>

# What is Markdown?
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

<br>


# Set up your development environment

## Install [Python3](https://www.python.org/downloads/) Correctly`(1pts)`
### Run Python Installer
   - [X] Add Python to PATH

<br>

## Install [Visual Studio Code](https://code.visualstudio.com/download) or [XCode](https://developer.apple.com/xcode/) `(1pts)`

### Visual Studio works for both MAC and PC. Xcode runs on MAC. Use default settings. I personally prefer the Dark theme.

<br>

## Fork the class repository `(2pts)`
### Visit the class repo and click on `fork` (top right)
https://github.com/CSI-Carlos-Cobian/CSI-Python-2021

<br>

Create a folder. You may name it whatever you please but i will use "Courses" as it is simple and descriptive.
This will be your root folder. This means it is the top-level containing folder. You may place it anywhere but i suggest using your Documents or Desktop folder. 
In here you will clone the repositories for any classes that use GitHub. Currently Java, Python and hopefully NovaTech.
* In Visual Studio
* Go to File > Open Folder
* Select your newly created directory

<br>

### Create a fork in your GitHub.
Forking a repository will create a copy on your GitHub account. You may freely alter this copy to take class notes and answer questions. These changes will only be reflected on **your** copy of the repository. You may also update your copy of the repository to reflect any changes i have made to the course without overwriting your individual changes.

<br>



### Clone the project into the Classes folder on your machine
1. Go to your `Source Control` tab
2. Initialize Repository if you have not done so.
3. Click on the 3 dots (your git menu)
4. Clone the forked repository.
   - Select `Clone from GitHub`
   - Alternatively, enter the fork URL with format: github.com/CSI-Name-Lastname/CSI-Python-2021
5. When prompted, select to open your new repo.

You may clone a repository without forking it, but only the owner may push changes to it. When you fork a copy it becomes your own. 

<br>

### Update your fork:
You may update your fork on GitHub. When your fork is out of date, a banner will show up.

<br>

To download these changes to your local repository
1. Go to your `Source Control` tab
2. Click on the 3 dots (your git menu)
3. Pull

<br>

Alternatively, you may update both simultaneously from Visual Studio by selecting.
1. `Source Control` > Branch > Merge Branch
2. Select `upstream/main`

<br>

### [Source Tree Git](/../../tree/main/Modules/SourceTree/Setup.md) **(Optional)** 

* #### Provides easier visualization of branches and history. 
* #### Requires many 3rd party authorizations

<br>

# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module1`</u> directory (Module1.md). `(3pts)`

<!-- This is a comment. It is not processed by the code -->
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What is a benefit of using Markdown?
https://www.markdownguide.org/getting-started/

 - Answer:

What is the difference between Git and GitHub?

 - Answer:

What is the difference between a git commit and a git push?

 - Answer:

Lackluster responses may result in point deductions.
-->

* ### Save the file. Commit your changes and push them to your remote repository by the end of the class. `(1pts)`
* ### You may complete the answers by issuing aditional commits and pushing them before the next class.