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

## License
[MIT](https://choosealicense.com/licenses/mit/)