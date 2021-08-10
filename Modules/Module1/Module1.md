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

#### Git allows you to track changes in a file system, refered to as a repository. Some examples would be adding and removing files, adding and removing lines in a file, renaming files.

<br>

## Repository
*"A receptacle or place where things are deposited, stored, or offered"*
<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \- My google search.

<br>

#### In class, we will refer to repositories as the copies of the course file-system that each one of us holds. Repositories are both local and remote, meaning that repositories are available both offline on your machine, and online on a remote webserver. In our class we will use `GitHub` as our remote host.

<br>

## Pull
#### When you pull a repository you are updating your local copy with any changes that have been made on the remote version. 

<br>

## Commit
#### A commit saves any changes made to files on your local machine, to the local repository. Before committing, you will select which files and/or lines you would like to include. You don't have to include all of them, but you should make sure that what you are committing is correct. A commit requires a message. This message must be descriptive of what is being changed. This helps you keep track of every version change. Commits may be deleted or reverted locally before a Push.

<br>

## Push
#### Pushing to your remote repository will upload all pending commits. You should make sure that all commits are stable and correct before pushing. Oncce a commit has been pushed it will be available to anyone working on the repository. It is easier to delete or revert commits that are local and unpushed, as another user may pull bad code before you fix it. 

<br>

<br>

## A Diagram
<img    src="https://www.pngitem.com/pimgs/m/608-6085261_git-push-and-pull-hd-png-download.png" 
        title="Git diagram" 
        width="60%" 
        height="60%" />

<br>

## Install [Git](https://git-scm.com/downloads) **Correctly** (Windows). `(1pts)`
### In this class we'll use Visual Studio's integrated implementation of Git. MAC users may use XCode's integration. Visual Studio requires Git installed on your machine. XCode includes it.

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

Any users that chose to use Visual Studio Code on Mac should download and install [GitHub Desktop](https://desktop.github.com/) as it is the easiest solution to the git dependency.

<br>

# What is GitHub?
Think of GitHub as an Instagram of Code. A whole bunch of programmers from all around the world share their code so that others may view, comment and like it. They all use the technology of Git and share it on this Hub. GitHub is free, but you may pay to keep your repositories private.

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
*If it already exists, include your second lastname.*

<br>

# What is a branch?     
Branches are diferent versions of  a repository. A central branch(`main`) represents a repository, while many others represent pending changes that are incomplete, in developement, or just diferent. 

<br>

# Set up your development environment

<br>

## Install [Visual Studio Code](https://code.visualstudio.com/download) or [XCode](https://developer.apple.com/xcode/) `(1pts)`

### Visual Studio works for both MAC and PC. Xcode runs only on MAC. Use default settings. I personally prefer the Dark theme.

<br>

## Fork the class repository. `(2pts)`
Forking a repository will create a copy on your GitHub account. You own it now. You may freely alter this copy to take class notes and answer questions. These changes will only be reflected on **your copy**(fork) of the repository. 

<br>

### Visit the class repo and click on `fork`. (top right)
https://github.com/CSI-Carlos-Cobian/CSI-Python-2021

<br>

### Create a folder on your machine. 
You may name it whatever you please but i will use "Courses" as it is simple and descriptive.
This will be your root folder. This means it is the top-level containing folder. You may place it anywhere but i suggest using your Documents or Desktop folder. 
In here you will clone the repositories for any courses that use GitHub. Currently Java, Python and hopefully NovaTech.

<br>

### Clone the project into the 'Classes' folder on your machine.
1. Go to your `Source Control` tab in Visual Studio(3rd).
2. Initialize Repository (if you have not done so).
3. Click on the 3 dots (your git menu).
4. `Clone` the forked repository.
   - Select `Clone from GitHub`
   - Alternatively, enter the fork URL with format: github.com/CSI-Name-Lastname/CSI-Python-2021
5. When prompted by VS, select to open your new repo.

You may clone a repository without forking it, but only `contributors` may push changes to it. When you fork a copy it becomes your own. 

<br>

*You may also update your copy(fork) of the repository to reflect any changes i have made to the course without overwriting your individual changes.*

<br>

## Using Git

<br>

### Update your fork:
You may update your fork on GitHub. When your fork is out of date, a banner will show up. Click on it to update your branch.

<br>

To download fork updates to your **local** repository(PC).
1. Go to your `Source Control` tab in Visual Studio(3rd).
2. Click on the 3 dots (your git menu)
3. Pull

<br>

Alternatively, you may update both simultaneously from Visual Studio by selecting.
1. `Source Control` > Branch > Merge Branch
2. Select `upstream/main`

`upstream/main` represents the main branch of the repository you've forked. 'Merging' it into you branch means that you're applying it's updates into your branch.

<br>

### [Source Tree Git](/../../tree/main/Modules/SourceTree/Setup.md) **(Optional)** 

* #### Provides easier visualization of branches and history. 
* #### Requires many 3rd party authorizations.

<br>

# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module1`</u> directory (Module1.md). `(3pts)`

<!-- This is a comment. It is not processed by the code -->
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What is the difference between Git and GitHub?

 - Answer:

What is the difference between a git commit and a git push?

 - Answer:

What is the difference between a pull, and an upstream pull?

 - Answer:

Lackluster responses may result in point deductions.
-->

* ### Save the file. Commit your changes and push them to your remote repository by the next class. `(1pts)`*(Free for first class. Consult me if you struggle too hard with Git.)*
* ### You may complete the answers by issuing aditional commits and pushing them before the next class.