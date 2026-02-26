# COVID-19 Drivers: Business and Data Understanding

Various studies were referenced and confirm the following statements about driving habits in the United States during and after the pandemic:
* Americans believe aggressive driving has increased since the COVID-19 pandemic, and super majorities believe that one or more of the following specific behaviors have increased: distracted driving, driving too fast, and reckless driving including weaving, tailgating, and running red lights. (Leppert, 2024, November 12)
* Fatalities per miles driven in May 2020 increased significantly over the same month in 2019. (NSC, 2020, July 21)
* Americans who admit to engaging in risky driving behaviors increased the amount of time they spent driving while safer drivers reduced the amount of time they spent driving during the first few months of the pandemic. (Tefft et al., 2022) 
* The average number of daily trips taken by car dropped significantly in April 2020 during the COVID-19 lockdown compared to the last six months of 2019. (Tefft et al., 2021) 

While these studies confirm important trends and patterns, none of them show if aggressive driving actually increased during COVID or if it has since declined or stabilized. They also do not show if the rate of accidents caused by at least one aggressive driver has changed or if any type of aggression (speeding, distraction, recklessness) has increased more than others. Data scientists can answer these questions using appropriate data and modeling techniques.
It is important for the public to know if they are correct about an increase in aggressive driving, and it is important to understand which types may have increased. Public awareness brings solutions by moving the public to elect public officials who will enact laws or by moving organizations and individuals to organize and fund advocacy or education efforts. 


The contents of this folder include a utils folder, which contains a functions.py file 
that defines functions used in the project.

It also contains four Jupyter Notebooks:

* covid_drivers_01_init - reads all of the data and evaluates relationships
* covid_drivers_02_desc - reads CRASH and FLAGS data, evaluates 
and selects variables for the project, merges selected variables, and writes 
the merged dataset to file for use in the next two notebooks
* covid_drivers_03_expl - reads the merged dataset and evaluates univariate and
bivariate relationships
* covid_drivers_04_qual - reads the merged file and assesses the quality of the data