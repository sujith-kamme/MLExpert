def probability_of_disease(accuracy, prevalence):

    prob_healthy = 1 - prevalence
    prob_sick = prevalence

    inaccuracy = 1 - accuracy

    prob_sick_given_positive = prob_sick * accuracy / (prob_sick * accuracy + prob_healthy * inaccuracy)

    prob_healthy_given_negative = prob_healthy * accuracy / (prob_sick * inaccuracy + prob_healthy * accuracy)

    return [prob_sick_given_positive * 100, prob_healthy_given_negative * 100]