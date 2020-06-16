# Executive Dashboard
This program provides monthly sales data and visualizations from .csv files.
## Getting Started
---
This program requires Python  version 3.7.  Required third party packages are provided below and are also listed in the *requirements.txt* document included in this repository.
### Prerequisites
* Required third party packages include:
    * *pandas*
    * *numpy*
    * *matplotlib*
### Installing
* The user will be required to clone the repository located at the following hyperlink: https://github.com/laf518/executive_dashboard. 
* Once the user has finished setting up their local repository, they must run the following code within their virtual Python environment to install the required third party packages:
>`pip install -r requirements.txt`
## Deployment
---
The program requires the user to save sales data files in the *data* folder using the following format: "*sales-YYYYMM.csv*".  The user will then be provided a menu of files within the data folder.  They will then input the file number for the data they require.  A bargraph of the sales revenue by item will be displayed in a separate window along with the total montly revenue within the CLI. 

### Errors:
* User will receive the following error message if the input provided is not in the menu list of files: "*Invalid file number!*". *User will be prompted to input a valid file number.*

## Author
---
* **Luke Fellin** - *Programming in Python and Fundamentals of Software Development: **NYU Stern School of Business**, Summer 2020*