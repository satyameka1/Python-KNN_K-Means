from builtins import len
import pandas as pd
import numpy as np
import sys

clusters = {}


def generate_initial_centroids(k, data):
    centroid_list = []
    for i in range(k):
        sample = data.sample()
        sample_list = sample.values.tolist()
        for j in sample_list:
            centroid_list.append(j)
        key = "cluster_" + str(i + 1)
		
        clusters[key] = []
    print("Initial Centroids : ")
    print("-----------------------------------------------------------------------")
    for i in range(len(centroid_list)):
        print("Centroid of Cluster {} is : {}".format(i+1, centroid_list[i]))
    print("-----------------------------------------------------------------------")
    return centroid_list


def standardize_data(data):
    mean = data.mean()
    std_deviation = data.std()
    data = (data - mean) / std_deviation
    return data


def update_centroids(k, centroid_list):
    for i in range(k):
        cluster_name = "cluster_" + str(i+1)
        if sys.argv[2] == "2":
            labels = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PS/G']
        # labels = ['Age', 'G']
        else:
            labels = ['3P%', '2P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK']
        cluster_data = pd.DataFrame.from_records(clusters[cluster_name], columns=labels)
        centroid_list[i] = cluster_data.mean().values.tolist()
    return centroid_list


def clustering(k, data, centroid):
    i_break = True
    j_break = True
    count = 1
    while True:
        print("Iteration : {}".format(count))
        for i in range(k):
            cluster_name = "cluster_"+str(i+1)
            clusters[cluster_name] = []
        for row in data:
            a = np.array(row)
            min_distance = 99
            closest_centroid = "cluster_1"
            for i in range(k):
                distance = np.linalg.norm(a - centroid[i])
                if distance < min_distance:
                    min_distance = distance
                    closest_centroid = "cluster_" + str(i + 1)
            clusters.setdefault(closest_centroid, []).append(row)
        for i in range(k):
            print("Number of Players in Cluster {} is : {}".format(i+1, len(clusters["cluster_"+str(i+1)])))
        print("-----------------------------------------------------------------------")
        recent_centroid = centroid.copy()
        centroid = update_centroids(k, centroid)
        for i in range(k):
            j_break = True
            for j in range(len(centroid[0])):
                if centroid[i][j] != recent_centroid[i][j]:
                    break
            else:
                j_break = False
        else:
            i_break = False
        if i_break is False and j_break is False:
            break
        count += 1
    return centroid


def kmeans(x, k):
    columns = x.columns.values.tolist()
    question_number = int(sys.argv[2])
    if question_number == 2:
        print("### CONSIDERING All ATTRIBUTES ###")
        columns_to_remove = ['Player', 'Pos', 'Tm']
    else:
        print("### CONSIDERING ONLY '3P%', '2P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK' ###")
        columns_to_remove = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '2P', '2PA', 'eFG%', 'FT', 'FTA', 'ORB', 'DRB', 'TOV', 'PF', 'PS/G']

    for column in columns_to_remove:
        columns.remove(column)
    compute_data = x[columns]
    standardized_data = standardize_data(compute_data)
    data_list = standardized_data.values.tolist()
    centroid_list = generate_initial_centroids(k, standardized_data)
    final_centroids = clustering(k, data_list, centroid_list)
    print("#############################")
    print("##THE FINAL CENTROIDS ARE :##")
    print("#############################")
    for i in range(len(final_centroids)):
        print("***Cluster {} Centroid*** : {}".format(i+1, final_centroids[i]))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid Number of arguments. Argument format is Comma Separated K values ex: 3,5 and "
              "question number which is either 2 or 4")
        sys.exit(0)
    if sys.argv[2] != "2" and sys.argv[2] != "4":
        print("Invalid question number. Valid question numbers are 2 and 4.")
        sys.exit(0)
    k_value = sys.argv[1]
    list_of_k = k_value.split(',')
    entire_data = pd.read_csv('NBAstats.csv')
    for i in list_of_k:
        print("********************* Performing {} - MEANS CLUSTERING ******************".format(i))
        kmeans(entire_data, int(i))
        print("********************* END OF {} - MEANS CLUSTERING ******************\n".format(i))



