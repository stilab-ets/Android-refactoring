
# An Empirical Study on the Impact of Refactoring on Quality Metrics in Android Applications

This repository contains all the material required to replicate our analysis, including (1) the data (2) the statistical analysis scripts, and (3) the analysis 
results.

## How to cite?

Please, use the following bibtex entry:

```
@inproceedings{Hamdi2021empirical,
  title={An Empirical Study on the Impact of Refactoring on Quality Metrics in Android Applications},
  author=Hamdi, Oumayma and Ouni, Ali and AlOmar, Eman Abdullah and {\'O} Cinn{\'e}ide, Mel and Mkaouer, Mohamed Wiem},
  booktitle={8th IEEE/ACM International Conference on Mobile Software Engineering and Systems 2021},
  pages={1--12},
  year={2021}
}
```
## Data collection :

The data used for this study can be obtained by executing the scripts available in dataCollection folder: 

* githubCrawler.py: Mines Github repository for open-source, published apps.
* androidManifestChecker.py: Filters apps that do not have a corresponding Manifest file. 
* googlePlayPageChecker.py: Identifies the existence of Google Play Store page reported in links in repositories
* csvDuplicatesRemover.py: Removes duplicate entries from the csv.  
* Repodriller : RepoDriller is a Java framework that helps developers on mining software repositories. With it, we extracted Commits ([Availaible here](https://github.com/mauricioaniche/repodriller)).
* RefactoringMiner: RefactoringMiner is a library/API written in Java that can detect refactorings applied in the history of a Java project ([Availaible here](https://github.com/tsantalis/RefactoringMiner)).
* CkeckoutCommit.py: checkouts commits before and after each applied refactoring.
* Detect-metrics-ck: Detects quality metrics using Ck-metrics
* Detect-metrics-understand: Detects quality metrics using Understands.
* Merge.py: Merges CSV files. 


## Analysis : 

The totality of the statistical analysis scripts utilized for the study are available in Analysis folder: 

* Analysis_plots.py: Performs plots results related to RQ.
* Analysis.R: Performs all analysis related to RQ.

## Data :

The data used for the analysis is available in Data folder where we found the list of apps and the detected quality metrics.