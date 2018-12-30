# Effects of Randomized Redistricting on Congressional Balance of Power

## Background
The concept of redistricting is a popular topic in discussions about congressional representation in the United States. Parties in power often resort to "[gerrymandering](https://en.wikipedia.org/wiki/Gerrymandering)" - the act of re-drawing district boundaries to gain an advantage in the balance of representation. The purpose of this project is to explore how representation in the U.S. House of Representatives shifts from randomizing the redistricting process.

## Updates & Project Timeline
*Progress will be dictated by how well I balance coursework, research, job-hunting, and taking care of a newborn. :)*
- **November 2018** - project initiation, source data, Exploratory Data Analysis (EDA), pre-processing
- **December 2018** - implement clustering algorithm (still TBD) to partition each state into congressional districts
- **January 2019** - develop map-based UI on an OSM base

### To-Do List (updated 12/30/18)
1. ~~Source precinct-level returns data from Harvard Dataverse~~
2. ~~Source 2010 Redistricting File (PL 94-171) from U.S. Census Bureau~~
3. ~~Split elections data by state~~
4. ~~EDA of elections data:~~
   - ~~Remove unused columns~~
   - ~~Remove write-ins (assume inconsequential)~~
   - ~~Assess prevalence of missing values for political party~~
   - ~~Develop algo and manually process edge cases to impute missing values~~
   - Generate unique identifier for each precinct
   - Others?
5. EDA/pre-processing of Census data:
   - ~~Write Python script to automate FTP download of voting district geographies~~
   - ~~Write Python script to automate FTP download of PL-94-171 data~~
   - Write Python script to extract Census .zip files
   - Convert .txt and .dbf files to database files (SQL or NoSQL?)
   - Convert to graph data structure (.xml or .json output)
   - TBD

## Dependencies
*Coming soon!*
   
## Installation Instructions
*Coming soon!*

## Data
- MIT Election Da a and Science Lab, 2018, "U.S. House of Representatives Precinct-Level Returns 2016", https://doi.org/10.7910/DVN/PSKDUJ, Harvard Dataverse, V10
- U.S. Census Bureau, 2011, "2010 Redistricting File (Public Law 94-171) Dataset", https://www.census.gov/data/datasets/2010/dec/redistricting-file-pl-94-171.html, U.S. Census Bureau

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/sherwinhlee/random-redistricter/blob/master/LICENSE) file for details.
