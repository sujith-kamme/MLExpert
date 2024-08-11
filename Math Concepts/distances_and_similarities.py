class Metrics:
    def euclidean_distance(self, X, Y):
        '''
        X = [x1, x2]
        Y = [y1, y2]
        eucd_dist = sqrt((x1 - y1)**2 + (x2 - y2)**2)
        '''
        eucd_dist = (sum([(x - y) ** 2 for x, y in zip(X, Y)])) ** 0.5
        return round(eucd_dist, 4)

    def manhattan_distance(self, X, Y):
        '''
        X = [x1, x2]
        Y = [y1, y2]
        manhattan_dist = |x1 - y1| + |x2 - y2|
        '''
        manh_dist = sum([abs(x - y) for x, y in zip(X, Y)])
        return round(manh_dist, 4)

    def cosine_similarity(self, X, Y):
        '''
        X = [x1, x2]
        Y = [y1, y2]
        cosine_similarity = X . Y / ||X|| ||Y||
        '''
        X_dotproduct_Y = sum([x * y for x, y in zip(X, Y)])
        det_X = (sum([x ** 2 for x in X])) ** 0.5
        det_Y = (sum([y ** 2 for y in Y])) ** 0.5

        cosine_similarity = X_dotproduct_Y / (det_X * det_Y)

        return round(cosine_similarity, 4)

    def jaccard_similarity(self, X, Y):
        '''
        X = [x1, x2]
        Y = [y1, y2]
        jaccard_similarity = len(X intersection Y) / len(X union Y)
        '''
        jaccard_similarity = len(set(X).intersection(Y)) / len(set(X).union(Y))
        return round(jaccard_similarity, 4)



def distances_and_similarities(X, Y):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]