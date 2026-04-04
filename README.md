# COVID-19 Drivers

## Introduction

PA Data Discourse (PDD) is a new digital news publication focused on investigative public interest reporting.  PDD collects and analyzes open data from state, county, and municipal portals to provide data-driven insights on topics of interest to Pennsylvania residents.

A current topic of interest that has open questions involves PA drivers and driving behaviors that may have changed during and after the COVID-19 pandemic. A majority of Americans believe drivers have been more aggressive since the lockdown. Various studies were referenced, which confirm the following statements about driving habits in the United States during and after the pandemic:

* Americans believe aggressive driving has increased since the COVID-19 pandemic, and super majorities believe that one or more of the following specific behaviors have increased: distracted driving, driving too fast, and reckless driving including weaving, tailgating, and running red lights. (Leppert, 2024, November 12)
* Fatalities per miles driven in May 2020 increased significantly over the same month in 2019. (NSC, 2020, July 21)
* Americans who admit to engaging in risky driving behaviors increased the amount of time they spent driving while safer drivers reduced the amount of time they spent driving during the first few months of the pandemic. (Tefft et al., 2022) 
* The average number of daily trips taken by car dropped significantly in April 2020 during the COVID-19 lockdown compared to the last six months of 2019. (Tefft et al., 2021) 

While these studies confirm important trends and patterns, none of them show if aggressive driving actually increased during COVID or if it has since declined or stabilized. They also do not show if the rate of accidents caused by at least one aggressive driver has changed or if any type of aggression (speeding, distraction, recklessness) has increased more than others. Data scientists can answer these questions using appropriate data and modeling techniques.
It is important for the public to know if they are correct about an increase in aggressive driving, and it is important to understand which types may have increased. Public awareness brings solutions by moving the public to elect public officials who will enact laws or by moving organizations and individuals to organize and fund advocacy or education efforts. 

## Jupyter Notebooks

The contents of this folder include a utils folder, which contains a functions.py file that defines functions used in the project. The functions.py file is only used by covid_drivers_01_INIT, 02_DESC, 03_EXPL, 04_QUAL notebook files.

This folder also contains the Jupyter Notebooks created for this analysis:

* covid_drivers_01_init - reads all of the data and evaluates relationships.
* covid_drivers_02_desc - reads all of the data, evaluates and selects variables for the project, merges selected variables, and writes the merged dataset to file for use in the next two notebooks.
* covid_drivers_03_expl - reads the merged dataset from covid_drivers_02_DESC and evaluates univariate and bivariate relationships including time series plots.
* covid_drivers_04_qual - reads the merged dataset from covid_drivers_02_DESC and assesses the quality of the data - missingness, consistency, etc.
* covid_drivers_05_PREP - reads CRASH, FLAGS, and VEHICLE datasets, merges CRASH and FLAGS, filters records to include only crashes that involve a vehicle in motion or a hit and run using the VEHICLE dataset, decodes variables, selects columns and writes 'ready_data_final.csv' dataset to file for analysis.
* covid_drivers_06_PRIM_MODL_LGR -  primary objective model POST_COVID ~ AGGRESSIVE_DRIVING with logistic regression
* covid_drivers_06_PRIM_MODL_RF - primary objective model POST_COVID ~ AGGRESSIVE_DRIVING with random forest
* covid_drivers_06_PRIM_MODL_XGB - primary objective model POST_COVID ~ AGGRESSIVE_DRIVING with gradient boosting
* covid_drivers_07_PRIM_MODL_LGR - primary objective model POST_COVID ~ NHTSA_AGG_DRIVING with logistic regression
* covid_drivers_07_PRIM_MODL_RF - primary objective model POST_COVID ~ NHTSA_AGG_DRIVING with random forest
* covid_drivers_07_PRIM_MODL_XGB - primary objective model POST_COVID ~ NHTSA_AGG_DRIVING with gradient boosting
* covid_drivers_08_SEC_MODL_LOF - secondary objective models POST_COVID ~ NO_CLEARANCE and other specific behaviors separately, with local outlier factor one-class classifier
* covid_drivers_08_SEC_MODL_SVM - secondary objective models POST_COVID ~ NO_CLEARANCE and other specific behaviors, separately, with support vector machine one-class classifier
* covid_drivers_09_SEC_MODL_COFAC_AGGDRV - secondary objective model POST_COVID plus demographic flags ~ AGGRESSIVE_DRIVING with logistic regression, random forest, and gradient boosting
* covid_drivers__09_SEC_MODL_COFAC_NHTSA - secondary objective model POST_COVID plus demographic flags ~ NHTSA_AGG_DRIVING with logistic regression, random forest, and gradient boosting
* covid_drivers_10_TIME_SERIES_1 - Time series lag and autocorrelation plots
* covid_drivers_10_TIME_SERIES_2 - Time series decomposition and changes in seasonal behavior over time

## Notebook Updates and Additions for Final Report

#### The following notebooks were updated to support the final report

* covid_drivers_06_PRIM_MODL_RF - an ROC AUC plot was created for use in the final report

#### The following notebooks are additions to the project to support the final report

* covid_drivers_10_TIME_SERIES_1
* covid_drivers_10_TIME_SERIES_1

## Instructions for Replicating this analysis

1. Create a project folder on your computer.

2. Copy the contents of this folder to your project folder to preserve the current Jupyter Notebooks if analysts wish to modify the notebooks to conduct additional exploration, quality checks, preparation, or modeling.

3. Run the notebooks with the numbers 01, 02, 03, 04, and 05 in the filenames in order based on the number in the filename. The notebook covid_drivers_05_PREP creates the files ready_data.csv and read_data_final.csv in the folder 'data/ready/', which are read by the remaining notebooks.

4. Setup a Google account if you don't already have one.

5.  Create the following folder hierarchy on your Google Drive:
'MyDrive/Colab Notebooks/Case Studies in Data Science/data/ready/'

6. Copy the Jupyter Notebooks with the numbers 06, 07, 08, 09, and 10 in the filenames to the 'Case Studies in Data Science' folder.

7. Copy ready_data.csv and ready_data_final.csv to the 'ready' folder.

8. Using Google Colaboratory, open and run (see Note below) the notebooks with the numbers 06, 07, 08, 09, and 10 in the filenames in order based on the number in the filename. Notebooks with the same number can be run in any order within the group.

Note: Some of these notebooks were setup to write images to files. This functionality was either commented out or revised to work with Colaboratory. However, the ones setup to write to the Google Drive using Colaboratory still do not work, but they do not produce errors that stop the execution of the notebook.
 
