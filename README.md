This repository tries to explore how to run tests in between Snakemake steps. The rationale being that something has been computed and you need to make sure things have gone right. You _could_ do that inside the Snakemake step itself. The disadvantage though is, that the result files are going to be deleted whenever the step fails. Also, it would be better to integrate the tests into `py.test` so that they can be run as often as wanted.
