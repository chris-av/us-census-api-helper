# US Census Bureau API

Some code to be able to query the US Census Bureau data in an efficient manner

## Installation

Will need an environment variable, `USCENSUS_KEY` defined somewhere in your global environment. Can be set in your environment or usinng a `.env` file.

To use the project, run :

```python
pip install  -r requirements.txt    # install the dependencies
source env/bin/activate             # load the virtual environment
```


## Example of a successful query


```python
# get data from the ACS/ACS5 Survey
# for the 2021 year dataset
# for variables NAME, B01001_001E
# for zips: ... (string concatenated, delimited by comma)
# must include key query parameter for this query to work
url = "https://api.census.gov/data/2021/acs/acs5?get=NAME,B01001_001E&for=zip%20code%20tabulation%20area:<zips>&key=<key>"
response = requests.get(url)
```


## Further Reading

The list of datasets from the US Census Bureau can be found [here](https://api.census.gov/data.html).

