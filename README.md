# Eligibility Checker

A reusable Python pattern for checking whether someone meets minimum age and height requirements, shown across three examples.

## Files
- **access_checker.py** — theme park ride access requirements
- **flight_eligibility_checker.py** — unaccompanied minor airline travel requirements
- **learners_permit_checker.py** — learner's permit application requirements

## How it works
- Checks age against a minimum requirement
- Checks height against a minimum requirement
- Both conditions must be met to be granted access/eligibility

## How to run
```bash
python access_checker.py
python flight_eligibility_checker.py
python learners_permit_checker.py
```
You'll be prompted to enter age and height, and the script will tell you if the requirements are met.

## What I learned
- Using `if / elif / else` for sequential condition checks
- Applying the same eligibility-checking pattern across different real-world contexts (entertainment, travel, driving)
