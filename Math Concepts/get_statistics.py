from collections import Counter

def get_statistics(input_list):
    statistics_dict = {}
    list_count = len(input_list)
    list_sum = sum(input_list)
    
    # Mean
    statistics_dict["mean"] = list_sum / list_count

    # Median
    sorted_list = sorted(input_list)
    mid_value = list_count // 2
    if list_count % 2 == 0:
        statistics_dict["median"] = (sorted_list[mid_value - 1] + sorted_list[mid_value]) / 2
    else:
        statistics_dict["median"] = sorted_list[mid_value]

    # Mode
    value_counts = Counter(input_list)
    most_common_value, _ = value_counts.most_common(1)[0]
    statistics_dict["mode"] = most_common_value

    # Sample Variance
    mean = statistics_dict["mean"]
    statistics_dict["sample_variance"] = sum((x - mean) ** 2 for x in input_list) / (list_count - 1)
    
    # Sample Standard Deviation
    statistics_dict["sample_standard_deviation"] = statistics_dict["sample_variance"] ** 0.5

    # Mean Confidence Interval
    standard_error = statistics_dict["sample_standard_deviation"] / (list_count ** 0.5)
    confidence_margin = 1.96 * standard_error
    statistics_dict["mean_confidence_interval"] = [mean - confidence_margin, mean + confidence_margin]

    return statistics_dict