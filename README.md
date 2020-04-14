# public-services-data
For my internship I had to gather a dataset with informaton about NYC governmental services and their online pages visits in order to rank the most visited services and speculate on the usage of these services.

Here is a failed approach I was exploring involving the website analytics available through the Open Data. 
Intended Procedure:

1. Gather info about services provided and respective urls, i went for web scraping approach rather than manual approach given the huge amount of services offered.  /html_reader.py
2. Read the open data NYC Website analytics associated with each url.   /analytics_reader.py
3. Compare urls from open data to the services urls.
4. Rank.

I got no match between the urls in step (2) and the services urls in step (1). 
The analytics open data was too broad, not speficied on a section on the website (eg. public services, I wish), only the top viewed urls were availbale. Apparently NYC governmental services pages aren't the top viewed pages so this strategy was abandoned. 

