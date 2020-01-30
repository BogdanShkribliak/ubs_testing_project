### UBS testing project
Technologies used:
* python 2.7 as a programming language
* behave as BDD tool and test runner

Created feature file for testing tabs from main page
Project could be run on different instances


### Environment Setup

1. Setup
    * Clone the repo
	* Install the dependencies `pip install -r requirements.txt`


### Running Tests

* To run a single test, run `paver run single`
* To run parallel tests, run `paver run parallel`



*  To be able to run only one feature file: `behave -i file_name.feature`

*  To be able to run only one test: `behave -n 'This is a scenario name'`

*  To be able to run on different browsers: `behave --junit -D browser=Chrome`. Please note. If  -D browser=Browser_name is not specified - it will run on defaul one (Edge)

*  paremeter --junit - will save test results into a file


