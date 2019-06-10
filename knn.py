import pandas as pd
import math
import sys


def standardize_data(data_frame):
    mean = data_frame.mean()
    std_deviation = data_frame.std()
    data_frame = (data_frame - mean) / std_deviation
    return data_frame


def calculate_distance(training, test, length):
    distance = 0
    for i in range(length):
        distance += ((training[1][i] - test[1][i]) ** 2)
		
    return math.sqrt(distance)


def get_neighbours(training, test, k_val):
    distances = []
    nearest_neighbours = []
    length = len(test[1]) - 1
    for row in training.iterrows():
        distance = calculate_distance(row, test, length)
        distances.append((row, distance))
    distances.sort(key=lambda value: value[1])
    for i in range(k_val):
        nearest_neighbours.append(distances[i][0])
    return nearest_neighbours


def predict_class(nearest_neighbours):
    classes = {}
    for i in nearest_neighbours:
        class_key = i[1]['Pos']
        if class_key in classes:
            classes[class_key] = classes[class_key] + 1
        else:
            classes[class_key] = 1
    return max(classes.items(), key=lambda value: value[1])[0]


def knn(training_set, test_set, k_val):
    predicted_class = []
    for row in test_set.iterrows():
        nearest_neighbours = get_neighbours(training_set, row, k_val)
        predicted_class.append(predict_class(nearest_neighbours))
    return predicted_class


def calculate_accuracy(test, predicted_classes, k_val):
    match_count = 0
    actual_labels = test[['Pos']]
    count = 0
    for row in actual_labels.iterrows():
        if row[1]['Pos'] == predicted_classes[count]:
            match_count += 1
        count += 1
    print("The Accuracy for {} nearest neighbours is : {}%".format(k_val, (match_count/len(test)) * 100))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid Number of arguments. Argument format is Comma Separated K values ex: 3,5 and "
              "question number which is either 2 or 4")
        sys.exit(0)
    if sys.argv[2] != "2" and sys.argv[2] != "3":
        print("Invalid question number. Valid question numbers are 2 and 4.")
        sys.exit(0)
    k_value = sys.argv[1]
    list_of_k = k_value.split(',')
    data = pd.read_csv('NBAstats.csv')
    if sys.argv[2] == "2":
        print("### CONSIDERING All ATTRIBUTES ###")
        x = data[
            ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%',
             'ORB',
             'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PS/G']]
    else:
        print("### CONSIDERING ONLY '3P%', '2P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK' ###")
        x = data[['3P%', '2P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK']]
    y = data[['Pos']]
    x = standardize_data(x)
    x.insert(len(x.columns), 'Pos', y.values)
    training_data = x[0:375]
    test_data = x[375:475]
    for i in list_of_k:
        classification_result = knn(training_data, test_data, int(i))
        calculate_accuracy(test_data, classification_result, int(i))
