import random


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


def get_manhattan_distance(feature_1, feature_2):
    return sum([abs(x - y) for x, y in zip(feature_1, feature_2)])


def get_average_new_centroids(centroid, user_feature_map, num_features_per_user):
    closest_uid_features = []
    
    for uid in centroid.closest_users:
        closest_uid_features.append(user_feature_map[uid])
    
    new_centroid_features = []
    for i in range(num_features_per_user):
        average = sum([x[i] for x in closest_uid_features])/len(closest_uid_features)
        new_centroid_features.append(average)
    
    return new_centroid_features
    
def get_k_means(user_feature_map, num_features_per_user, k):
    random.seed(42)
    initial_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

    centroids = []
    for centroid_coordinates in initial_centroid_users:
        centroids.append(Centroid(user_feature_map[centroid_coordinates]))

    for iter in range(10):
        for uid, features in user_feature_map.items():
            closest_dist = float("inf")
            closest_centroid = None
            for centroid in centroids:
                manh_dist = get_manhattan_distance(features, centroid.location)
                if manh_dist < closest_dist:
                    closest_dist = manh_dist
                    closest_centroid = centroid
            
            closest_centroid.closest_users.add(uid)

        for centroid in centroids:
            centroid.location = get_average_new_centroids(centroid, user_feature_map, num_features_per_user)
            centroid.closest_users.clear()

    return [centroid.location for centroid in centroids]