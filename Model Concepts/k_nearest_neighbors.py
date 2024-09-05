from collections import Counter
def predict_label(examples, features, k, label_key="is_intrusive"):
    nearest_neightbors = find_k_nearest_neighbors(examples, features, k)
    predictions = []
    for nn in nearest_neightbors:
        predictions.append(examples[nn][label_key])

    value_counts = Counter(predictions)
    most_common_value, _ = value_counts.most_common(1)[0]
    return most_common_value


def find_k_nearest_neighbors(examples, features, k):
    eucd_dist={}
    nearest_neightbors = []
    for key,value in examples.items():
        dist = get_euclidean_distance(value["features"],features)
        eucd_dist[key]= dist

    sorted_eucd_dist= sorted(eucd_dist.items(), key=lambda x: x[1])
    
    return [item[0] for item in sorted_eucd_dist[:k]]

def get_euclidean_distance(feat_1,feat_2):
    ssd = 0
    for x,y in zip(feat_1,feat_2):
        ssd += (x-y)**2

    return ssd ** 0.5