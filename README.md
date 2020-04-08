# Information Redactor

Sharing any informaion publicly may cause to misuse some personal or sensitive information. It is necessary to hide the such information from being exposed to the public. For instance, a notice related to some transactions, some legal information etc,. In such cases, information redacting helps in blocking only required information. I am going to walk you through the implement this idea in the coming sections. 

In this project I tried to implent an idea of hiding the confidential information.

## Getting Started

Before getting started please make sure to have python installed on your terminal. After that you need to create a local environment by pipenv. please refer the commands below:
```
pyenv install python 3.7.2
pipenv --3.7.2
```

### Prerequisites

Also, clone your git repository to push into git for future references by using the following command

```
$git clone "link of your repository"
```

### Structure of the tree

Below is the tree structure of required folders and files for the project. 
~~~ .
├── COLLABORATORS
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── docs
├── project1
│   ├── __init__.py
│   ├── files
│   │   ├── first.redacted
│   │   ├── firstmd.redacted
│   │   ├── second.redacted
│   │   └── secondmd.redacted
│   ├── first.txt
│   ├── main.py
│   ├── otherfiles
│   │   ├── firstmd.md
│   │   └── secondmd.md
│   ├── redactor.py
│   ├── second.txt
│   └── stats
├── setup.cfg
├── setup.py
└── tests
    ├── test_dates.py
    ├── test_gender.py
    └── test_names.py
~~~
Import all the essential packages like nltk, spacy, commonRegex, re, etc., into the local environment using:
```pipenv install "package" ```

## Command line
The command at the command line argument looks something like 
```
pipenv run python redactor.py --input '*.txt' \
                    --input 'otherfiles/*.md' \
                    --names --dates \
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr
 ```
 
The command line can take multiple flags at a time. The flags here are "input, output, names, gender, concept, stats'. Each flag serves its own purpose.

```input``` 
This flag is basically meant for input file. In this project, I have taken all .txt and .md extended files and read it using "glob" package. Actually we are giving input through this argument to our functions.

```names```

This is the redacted flag. Which means, we are intended to hide the names which are available in the collected files list from "input" flag.

```gender```
This flag is specifically to hide the genders. The detailed descripition will be discussed below while explaining the functions.

```dates``'
This flag indicates to hide the dates appear in the file.

## Functions & Description:

### Names: 
```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

pipenv 

```
Give an example
```

## Storing in git

Once done with writing code, running test cases, and all, you will have to push the files to github. The commamnds below will help you to push or pull the files to or from github
```
git add file-name
git commit -m "Message to be displayed in git"
git push origin master
git pull origin master
```
## Issues faced & Useful links to solve tthem 
https://github.com/madisonmay/CommonRegex to installation and usage commoRegex
https://spacy.io/usage - helped in solving installation issue with spaCy
You may requred to separate source environment and then deactivated it to install spacy into your local environment

## Limitations
The flags in the command should be given in sequential order
The file redundancy may happen
You may not find all the features explained above

## Authors

* **Prasuna Mitikiri** - *Initial work* - [PurpleBooth](https://github.com/Prasuna-mit/cs5293p19-project)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
