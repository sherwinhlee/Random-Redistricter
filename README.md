# Effects of Randomized Redistricting on Congressional Balance of Power

## Background
The concept of redistricting is a popular topic in discussions about congressional representation in the United States. Parties in power often resort to "[gerrymandering](https://en.wikipedia.org/wiki/Gerrymandering)" - the act of re-drawing district boundaries to gain an advantage in the balance of representation. The purpose of this project is to explore how representation in the U.S. House of Representatives shifts from randomizing the redistricting process.

This repo serves to house all code written across the lifecycle of the data and development process. Therefore, it should not be treated as an installable package or library. The ultimate objective is to construct the underlying algorithm to model results from a random redistricting cycle. Time and resources permitting, I also intend to look at developing a web-based map UI using an OpenStreetMap base, where the randomized redistricting can be visualized as partitions are drawn and congressional seats are tallied.

This project uses precinct-level returns from the 2016 U.S. congressional elections and the 2010 U.S. Census Redistricting Data Program.

## Updates & Project Timeline
- **November 2018** - ~~project initiation, source data, Exploratory Data Analysis (EDA), pre-processing~~
- **December 2018** - ~~complete EDA/pre-processing of precinct returns, automate download of Census source data~~
- **January 2019 - May 2019** - ~~develop ETL pipeline framework, port Census database platform from MS Access environment to Python/pandas and PostgreSQL~~
- **June 2019** - implement fuzzy matching algorithm on voting district (Census) and precinct (returns) names to create a unique identifier key
- **July 2019 - ?** - Set up PostgreSQL data tables, convert voting district (VTD) geographies to graph data structures, research randomized partitioning algorithm 

### To-Do List (updated 12/30/18)
1. ~~Source precinct-level returns data from Harvard Dataverse~~
2. ~~Source 2010 Redistricting File (PL 94-171) from U.S. Census Bureau~~
3. ~~Split elections data by state~~
4. ~~Pre-process elections data:~~
   - ~~Remove unused columns~~
   - ~~Remove write-ins (assume inconsequential)~~
   - ~~Assess prevalence of missing values for political party~~
   - ~~Develop algo and manually process edge cases to impute missing values~~
5. Preprocess Census data:
   - ~~Write Python script to automate FTP download of voting district geographies~~
   - ~~Write Python script to automate FTP download of PL-94-171 data~~
   - ~~Write Python script to extract Census .zip files~~
   - Parse Census .pl files and load into pandas using .xsd schema
   - Additional transform operations (subsetting, drop columns, etc.) in pandas
   - Load dataframe into PostgreSQL for each table
   - Convert VTD geographies to graph data structure (.xml or .json output)
6. Apply fuzzy matching to generate unique identifier for relating Census and returns tables
7. Research and implement randomized partitioning algorithm for redistricting<sup>[1]</sup>

## Dependencies
*In-progress!*

## Data
- MIT Election Data and Science Lab, 2018, "U.S. House of Representatives Precinct-Level Returns 2016", https://doi.org/10.7910/DVN/PSKDUJ, Harvard Dataverse, V10
- U.S. Census Bureau, 2011, "2010 Redistricting File (Public Law 94-171) Dataset", https://www.census.gov/data/datasets/2010/dec/redistricting-file-pl-94-171.html, U.S. Census Bureau

## Notes
[1] This task is the core part of the project and will be the most challenging. Further research is needed but I understand that the computational nature of this algorithm puts it in NP-hard territory. Assuming that is the case, some type of approximate algorithm (i.e., not truly random) is needed. If there are any math academics aware of this dilemma, please let me know!

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/sherwinhlee/random-redistricter/blob/master/LICENSE) file for details.
