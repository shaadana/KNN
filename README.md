# KNN
Simple KNearestNeighbors Algorithm for Classification using SciKit-learn

## Description of Algorithm:
I used data to train a KNearestNeighbors Classifier to classify people in grades based on how tall they are.
After training it, I gave it data to try classifying people and it worked.

We call this algorithm NearestNeighbors because it classifies data based on the data-point's nearest neighbors.

## How KNN Works:
The algorithm will take data and classify it based on its proximity to other data-points. 

### Example (1 Neighbor):
If a data-point is closer to the blue data-points than the red data-points, it will be classified as a blue data-point.

### Example (Multiple Nearest Neighbors):
If a data-point is closer to more of the blue data-points than the red data-points, it will be classified as a blue data-point.
This means the data-point could be near 9 blue data-points and near 2 red data-points. The data-point would be classified as blue because it is near more of them.

## More Details Here:

[Read this article for more information on KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)

## Here is the data:
![Graph of Data](HeightsOfStudents(KNN).png "data")
