# ETL mini project

Group memebers: Stefan Lilja, Sebastian Ström, Annika Davies

About the file structure: In the main directory there are some code files used for plotting. The code that airflow uses is in the weather subdirectory. In its subdirectories there are code files that handle the specific tasks in the process. In weather/\_\_init\_\_.py there is code that connects these parts, it is the functions in this file that are called by the DAG (a copy of which can also be found in the weather directory). The data used can be found in weather/data/weather, the subdirectory weather/data/testing contains some data used in a previous task and is not really related to this project.