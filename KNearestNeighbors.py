import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#Step 1: Making the Data
trainingX = np.array([[4], [4.6], [5.3], [5.9], [5.4], [4.3]]) # trainingX contains the features used for training
trainingY = np.array([4, 4, 7, 7, 7, 4]) # trainingY contains the labels/classes for training
testX = np.array([[4.7], [5.7]]) # testX contains the features used for testing/prediction

#Step 2: Creating the Algorithm
model = KNeighborsClassifier() # classification using the KNearestNeighbors Algorithm

#Step 3: Learning/Training
model.fit(trainingX, trainingY)

#Step 4: Prediction/Testing
testPrediction = model.predict(testX)
print(f'The predicted classes are {testPrediction}')

#Step 5: Graphing
trainZero = [0]*len(trainingX) # plot 1D data (single feature data) on a 2D plot by multiplying the number of data points in trainingX by zero  
testZero = [0]*len(testX) # plot 1D data (single feature data) on a 2D plot by multiplying the number of data points in testX by zero  

plt.figure(figsize=(15, 3))
plt.scatter(trainingX, trainZero, c = trainingY, cmap = 'winter', label = 'Training Data') #X is the dataset, zero_count is supposed to make sure that all the data is in one place so it doesnt have random y values and c = y gives each "grade" a different color so the classification is easy to see
plt.scatter(testX, testZero, c = testPrediction, marker = 'x', cmap = 'winter', s = 200, label = 'Testing Data')
plt.yticks([]) # lets you chooose the numbers you would like to see on the y-axis
plt.xlabel('Height')
plt.title('Height (ft) of Children in Grades 4 & 7')

plt.legend()
plt.colorbar()

plt.savefig('HeightsOfStudents(KNN).png')