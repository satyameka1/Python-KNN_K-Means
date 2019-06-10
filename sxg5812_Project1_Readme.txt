Programming Language/Version: Python 3.6.2
Steps to execute the code:
1. Unzip all the contents of the zipped file into a directory.
2. Open command prompt/terminal and change the directory to the directory where the zip folder was unzipped.

3. For kmeans clustering, 
	General format for running:
	python kmeans.py [comma separated list of k values] [What to execute]
For example to run the code to group the players into k ={3,5} clusters: 
	python kmeans.py 3,5 [what to execute]
	
4. For knn classification,
	General format for running:
	python knn.py [comma separated list of k values] [What to execute]

	
References used : 
1) https://pythonprogramming.net/testing-our-k-nearest-neighbors-machine-learning-tutorial/
2) https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
3) https://www.datascience.com/blog/k-means-clustering



About the dataset: for k-means clustering
 The dataset I took for this problem NBAstats.csv is stats from NBA players. The players are indexed by their names, 
and they are labeled by 5 different positions: {center (C), power forward (PF), small forward (SF), shooting guard (SG), 
point guard (PG)} and there are 27 attributes, e.g., age, team, games, games started, minutes played and 
so on (that makes total of 29 columns in the data matrix). Here the data is standardized before the analysis.


The submitted kmeans.py contains the code for performing kmeans clustering.  
The kmeans clustering algorithm, takes in the data and k – the number of clusters to be formed as the input.  
The first step is to get the columns. Next, a standardize_data(data) function is used to standardize the data set taken. 
Based on the value of K – I selected K number of initial centroids. 

 A clustering(k, data_list, centroid_list) function distributes the data set into separate clusters 
based on the Euclidian distance i.e. a point belongs to a particular cluster if its distance to the 
centroid of that cluster is the least when compared to the centroid of the other clusters. Based on 
these newly created clusters, I calculated the mean of each of points to compute the new centroids 
for that cluster. This process is repeated till the newly computed centroid is the same as the 
centroid computed in the previous iteration. 

This method returns the final centroids list of the clusters. 
 

 The dataset I took for this problem NBAstats.csv is stats from 475 NBA players. The players are labeled 
by 5 different positions: {center (C), power forward (PF), small forward (SF), shooting guard (SG), 
point guard (PG)} and there are 27 attributes, e.g., age, team, games, games started, minutes played 
and so on. I used the first 375 players as training data and remaining 100 players as testing data. I made sure 
that the data is standardized (zero-mean and standard deviation = 1) before I analyzed the data. 


• Initially, the program took 2 inputs from the user, the list of k values to perform knn classification and the number of attributes to be considered. 
• x -> Data set of the attributes that will be used to do the classification 
• y -> Classification label or the label to which each of the player will finally be classified into. 
• I standardized the X dataset and then inserted the labels column at the end of the x dataset. 
• I split this new dataset into 2 i.e. first 375 are the training data and the next 100 are the test data. 
• For each k value in the list of k values provided by the user, I performed the knn classification and compute the accuracy of the algorithm. 
• The knn algorithm takes in 3 arguments i.e. training data, test data and k 
• For each point in the test data, I got the k nearest neighbors based on the Euclidian distance. I fetched the classes of all these k nearest neighbors and then assign the class of test data to be equal to the class that is the most common in the k nearest neighbors. 
• To compute the accuracy, I calculated the percentage based on the number of matches between the predicted class and the actual class. 

Initially I used all the features except team (I got an accuracy of 50.0% for 10 nearest neighbours). 
