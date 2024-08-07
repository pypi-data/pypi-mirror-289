# CSV Detective

This is a package to **automatically detect column content in CSV files**. As of now, the script reads the first few rows of the CSV and performs various checks to see for each column if it matches with various content types. This is currently done through regex and string comparison.

## How To ?

### Install the package

You need to have python >= 3.7 installed. We recommend using a virtual environement.

```
pip install csv-detective
```

### Detect some columns

Say you have a CSV file located in `file_path`. This is how you could use `csv_detective`:

```
# Import the csv_detective package
from csv_detective.explore_csv import routine
import os # for this example only
import json # for json dump only

# Replace by your file path
file_path = os.path.join('.', 'tests', 'code_postaux_v201410.csv')

# Open your file and run csv_detective
inspection_results = routine(
  file_path,
  num_rows=-1, # Value -1 will analyze all lines of your csv, you can change with the number of lines you wish to analyze
  output_mode="LIMITED", # By default value is LIMITED, if you want result of analysis of all detections made, you can apply an output_mode="ALL"
  save_results=False, # Default False. If True, it will save result output into the same directory than the csv analyzed
  output_profile=True, # Default False. If True, returned dict will contain a property "profile" indicating profile (min, max, mean, tops...) of every column of you csv
  output_schema=True, # Default False. If True, returned dict will contain a property "schema" containing basic [tableschema](https://specs.frictionlessdata.io/table-schema/) of your file. This can be use to validate structure of other csv which should match same structure. 
)


# Write your file as json
with open(file_path.replace('.csv', '.json'), 'w', encoding='utf8') as fp:
    json.dump(inspection_results, fp, indent=4, separators=(',', ': '))

```

## So What Do You Get ?

### Output

The program creates a `Python` dictionnary with the following information :

```
{
    "heading_columns": 0, 					# Number of heading columns
    "encoding": "windows-1252", 			        # Encoding detected
    "ints_as_floats": [],					# Columns where integers may be represented as floats
    "trailing_columns": 0,					# Number of trailing columns
    "headers": ['code commune INSEE', 'nom de la commune', 'code postal', "libell\\u00e9 d'acheminement\n"], # Header row
    "separator": ";",						# Detected CSV separator
    "headers_row": 0,						# Number of heading rows
    "columns": { # Property that conciliate detection from labels and content of a column
        "Code commune": {
            "python_type": "string",
            "format": "code_commune_insee",
            "score": 1.0
        },
    },
    "columns_labels": { # Property that return detection from header columns
        "Code commune": {
            "python_type": "string",
            "format": "code_commune_insee",
            "score": 0.5
        },
    },
    "columns_fields": { # Property that return detection from content columns
        "Code commune": {
            "python_type": "string",
            "format": "code_commune_insee",
            "score": 1.25
        },
    },
    "profile": {
      "column_name" : {
        "min": 1, # only int and float
        "max: 12, # only int and float
        "mean": 5, # only int and float
        "std": 5, # only int and float
        "tops": [  # limited to 10
          "xxx",
          "yyy",
          "..."
        ],
        "nb_distinct": 67,
        "nb_missing_values": 102
      }
    },
    "schema": {
      "$schema": "https://frictionlessdata.io/schemas/table-schema.json",
      "name": "",
      "title": "",
      "description": "",
      "countryCode": "FR",
      "homepage": "",
      "path": "https://github.com/etalab/csv-detective",
      "resources": [],
      "sources": [
        {"title": "Spécification Tableschema", "path": "https://specs.frictionlessdata.io/table-schema"},
        {"title": "schema.data.gouv.fr", "path": "https://schema.data.gouv.fr"}
      ],
      "created": "2023-02-10",
      "lastModified": "2023-02-10",
      "version": "0.0.1",
      "contributors": [
        {"title": "Table schema bot", "email": "schema@data.gouv.fr", "organisation": "data.gouv.fr", "role": "author"}
      ],
      "fields": [
        {
          "name": "Code commune",
          "description": "Le code INSEE de la commune",
          "example": "23150",
          "type": "string",
          "formatFR": "code_commune_insee",
          "constraints": {
            "required": False,
            "pattern": "^([013-9]\\d|2[AB1-9])\\d{3}$",
          }
        }
      ]
    }
}
```

### What Formats Can Be Detected

Includes :

- Communes, Départements, Régions, Pays
- Codes Communes, Codes Postaux, Codes Departement, ISO Pays
- Codes CSP, Description CSP, SIREN
- E-Mails, URLs, Téléphones FR
- Years, Dates, Jours de la Semaine FR
- UUIDs, Mongo ObjectIds

### Format detection and scoring
For each column, 3 scores are computed for each format, the higher the score, the more likely the format:
- the field score based on the values contained in the column (0.0 to 1.0).
- the label score based on the header of the column (0.0 to 1.0).
- the overall score, computed as `field_score * (1 + label_score/2)` (0.0 to 1.5).

The overall score computation aims to give more weight to the column contents while
still leveraging the column header.

#### `output_mode` - Select the output mode you want for json report

This option allows you to select the output mode you want to pass. To do so, you have to pass a `output_mode` argument to the `routine` function. This variable has two possible values:

- `output_mode` defaults to `'LIMITED'` which means report will contain only detected column formats based on a pre-selected threshold proportion in data. Report result is the standard output (an example can be found above in 'Output' section).
Only the format with highest score is present in the output.
- `output_mode='ALL'` which means report will contain a full list of all column format possibilities for each input data columns with a value associated which match to the proportion of found column type in data. With this report, user can adjust its rules of detection based on a specific threshold and has a better vision of quality detection for each columns. Results could also be easily transformed into dataframe (columns types in column / column names in rows) for analysis and test.

## TODO (this list is too long)

- Clean up
- Make more robust
- Batch analyse
- Command line interface
- Improve output format
- Improve testing structure to make modular searches (search only for cities for example)
- Get rid of `pandas` dependency
- Improve pre-processing and pre-processing tracing (removing heading rows for example)
- Make differentiated pre-processing (no lower case for country codes for example)
- Give a sense of probability in the prediction
- Add more and more detection modules...

Related ideas:

- store column names to make a learning model based on column names for (possible pre-screen)
- normalising data based on column prediction
- entity resolution (good luck...)

## Why Could This Be of Any Use ?

Organisations such as [data.gouv](http://data.gouv.fr) aggregate huge amounts of un-normalised data. Performing cross-examination across datasets can be difficult. This tool could help enrich the datasets metadata and facilitate linking them together.

[Here](https://github.com/Leobouloc/data.gouv-exploration) is project (just started) that has code to download all csv files from the data.gouv website and analyse them using csv_detective.

## Release

The release process uses `bumpr`.

```shell
pip install -r requirements-build.txt
```

### Process

1. `bumpr` will handle bumping the version according to your command (patch, minor, major)
2. It will update the CHANGELOG according to the new version being published
3. It will push a tag with the given version to github
4. CircleCI will pickup this tag, build the package and publish it to pypi
5. `bumpr` will have everything ready for the next version (version, changelog...)

### Dry run

```shell
bumpr -d -v
```

### Release

This will release a patch version:

```shell
bumpr -v
```

See bumpr options for minor and major:

```
$ bumpr -h
usage: bumpr [-h] [--version] [-v] [-c CONFIG] [-d] [-st] [-b | -pr] [-M] [-m] [-p]
             [-s SUFFIX] [-u] [-pM] [-pm] [-pp] [-ps PREPARE_SUFFIX] [-pu]
             [--vcs {git,hg}] [-nc] [-P] [-nP]
             [file] [files ...]

[...]

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         Verbose output
  -c CONFIG, --config CONFIG
                        Specify a configuration file
  -d, --dryrun          Do not write anything and display a diff
  -st, --skip-tests     Skip tests
  -b, --bump            Only perform the bump
  -pr, --prepare        Only perform the prepare

bump:
  -M, --major           Bump major version
  -m, --minor           Bump minor version
  -p, --patch           Bump patch version
  -s SUFFIX, --suffix SUFFIX
                        Set suffix
  -u, --unsuffix        Unset suffix

[...]
```
