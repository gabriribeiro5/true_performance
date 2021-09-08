# TRUE PERFORMANCE
**An accurate performance calculator for operational services**

> SUMMARY:
- Intro
- Installation
- Usage
- Contributing
- Dev overview: Archtecture, Build & CI/CD
- License

## Intro

This application supports a wide range of adjustments. Allowing you, not only to reset your input parameters,
but also to rethink the output structure by adjusting it's granularity levels. Upcomming versions will allow
us to compare the app results using different configfile extentions (such as Json, Parquet or CSV), making it
usefull for Data Transfer, ETL and Analytics.

#### >> business definitions
>TRANSACTION:

In this context, we call a ***transaction***, every billable activity recorded at any system (and, probably, used for performance stats).

>WEIGHT / WEIGHTED:

The application's Key Performance Indicator (*KPI*) is here called ***Weighted Transaction*** and is based on two variables:
- The ammount of sub-tasks a given agent must perfom to conclude a transaction;
- The difficulty level for each of those sub-tasks.

**For instance**: a Travel Management Company (TMC) is likely to have it's transactions recorded as follows:
- Air Tickets
- Hotel Books
- Car Rents
- Additional Services (for non regular but billable services sold by the agent)

>SUB-TASK:

At this exemple, a simple set of ***sub-tasks*** for each transaction should be something like:
- pricing,
- reservation,
- booking confirmation (or ticket issuing),
- cancellation
- change of seats, passenger data or departure date,
- e-mailing ticket informations to the passenger

>SETBACK:

Between thoses sub-tasks, there might be some undesirable sub-tasks comming from issues that must be handled in order to complete a transaction. We are calling those issues as '***setbacks***'. The setbacks are likely to cause delay on the transaction conclusion and thus affect the operators performance.

**Exemples:**
Using the same TMC exemple, our setbacks might come from several sources:
- TOOLS AND TECHNOLOGIES
    - expired login (demands new login and delays the sub-task)
    - system error (demands retry)
    - system delay (may reduce the operator's focus)
    - etc

- REQUESTERS
    - Takes too long to decide (resulting on dropped reservations and rework for the operator)
    - Incomplete data (dalays the task)
    - High complexity routes (demands more time and experience to conclude the tasks)
    - etc

- WORKFLOW: All the following setbacks may break the expected workflow to conclude a transaction
    - Service provider needs to be contated via phonecall
    - Interruption from phonecall (retain focus)
    - Operator had to use the Cia's web portal
    - Many passengers handling the same request (causes misscommunication)
    - Not registered passengers
    - Too many undecisive e-mails exchanged with the traveller
    - etc

- SERVICES: These setbacks are likely to increase the risks regarding any transaction 
    - Multiple services into one transaction
    - Multiple payment options to be registered
    - Multiple tickets, one destination
    - etc

>PERFORMANCE RATE:

In order to calculate a more accurate **performance rate**, we must take those setbacks into account. Each of those setbacks must have a wheight, that is a difficulty level that affects the conclusion of a billable activity. Once this weight is defined, we can use the following formula to accurate the performance rate:


```
weighted transaction = mean weight * mean recurrence
--
*mean weight: avarege wheight of all aplicable setbacks
*mean recurrence: avarege setbacks recurrence
```

```
performance rate = weighted transaction * number of transactions
```



## Installation

There are no installation instructions yet.

> installation text exemple:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install exemple
```

## Usage

Adjustable parameters may be found at configfiles directory.
For further understanding of the application, start by checking out the input and output files at configfiles.

> usage text exemple:
```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

#### >> Setup your workspace

>CLONE AND ACTIVATE A VIRTUAL ENVIRONMENT:

1. Create a copy of .venv_global and remane it as **.env_local**
2. Activate the local environment:
On your working terminal, run the following command **from the applications root directory**

Mac OS / Linux:
```bash
source .\.venv_local\Scripts\activate
```

Windows
```bash
.\.venv_local\Scripts\activate
```

Possible error: 
```
the file C:\path\to\true_performance\.venv_local\Scripts\Activate.ps1 can not be
loaded because script execution has been disabled on this system
```
Solution:
Reset the execution policy to run scripts
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. Use the local environment during your development or debbuging process.
Whenever you're **ready to push** your commits into the repository, switch to global environment and rerun the application in order to verify any missing packages that might be used in your new version; install only those missing packages on global.

4. Deactivating virtual environment
On your working terminal, just run the following command **from the applications root directory**

```bash
deactivate
```

Warning:
-> DO NOT use .venv_global for development purpose
-> REMEMBER to update .venv_global by runing your 'push version' and installing the missing packages

#### >> Commiting it right

All commits must comply with [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). See how:

>USE COMMITZEN

DON'T use ```git commit```!

Instead, use **commitizen** to help you create usefull messages and **prevent git commit hook to run and reject your commit**.

With your **local environment setup and activated**, run the following command:
```
cz commit
```

Select the type of change you are committing (Use arrow keys), Then answer the given questions regarding your change (press enter after each answer).

[note]: You can check your commits by running ```git log``` on your terminal.


>WHY COMMITZEN

Our commits contain the following structural elements, to communicate intent to the consumers of this library:

- fix: a commit of the type fix patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).
- feat: a commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).
- BREAKING CHANGE: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with MAJOR in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type.
- types other than 'fix:' and 'feat:' are allowed, for example 'build:', 'chore:', 'ci:', 'docs:', 'style:', 'refactor:', 'perf:', 'test:', and others.


See [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for more information.

## Dev's overview:

#### >> Archtecture: application's design

>ENTITIES:

Brief info about the app's entities.

#### >> Engineering: build & CI/CD

>MAIN TOOLS:

**Virtual environments**:

- .venv_global: an optimized environment containing all (and only) necessary libs for the package. 

**When testing** new features or debugging existing ones, this environment **must be cloned into a local folder**, so you can freely install (or uninstall) source packages.

**Before commiting and pushing**, make sure to **rerun the application using the global environment** (.venv_global) so the missing packages for your new features are required and you can propperly install them.

- .venv_local: this one is meant to be used only in your local machine and must not be pushed into master nor release-candidates.

>VERSION CONTROL:

Our versions are setup as MAJOR.MINOR.PATCH (1.0.0):

1. MAJOR: when changes are incompatible with the previous version;
2. MINOR: when added new functionalities keeping compatibility;
3. PATCH: adjusting flaws and keeping compatibility.

See [Versioning] (https://semver.org/lang/pt-BR/) for more information.

[Commits] (https://www.conventionalcommits.org/en/v1.0.0/)

## License
[MIT](https://choosealicense.com/licenses/mit/)