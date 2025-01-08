class TreeNode:
    def __init__(self, examples):
        self.examples = examples
        self.left = None
        self.right = None
        self.split_point = None

    def split(self):
        if len(self.examples) == 1:
            return
            
        optimal = {
            "feat": None,
            "threshold": None,
            "error": float("inf"),
            "partition": None,
        }

        features = [f for f in self.examples[0].keys() if f != "bpd"]
        
        for feat in features:
            sorted_examples = sorted(self.examples, key=lambda x: x[feat])
            
            for idx in range(len(sorted_examples)-1):
                threshold = (sorted_examples[idx][feat] + 
                           sorted_examples[idx+1][feat]) / 2
                           
                error, partition = self._evaluate_partition(feat, threshold)
                
                if error < optimal["error"]:
                    optimal.update({
                        "feat": feat,
                        "threshold": threshold,
                        "error": error,
                        "partition": partition
                    })

        self.split_point = optimal
        sorted_data = sorted(self.examples, 
                           key=lambda x: x[optimal["feat"]])
        
        split_idx = optimal["partition"]
        self.left = TreeNode(sorted_data[:split_idx])
        self.right = TreeNode(sorted_data[split_idx:])
        
        self.left.split()
        self.right.split()

    def _evaluate_partition(self, feat, threshold):
        left = [x["bpd"] for x in self.examples if x[feat] <= threshold]
        right = [x["bpd"] for x in self.examples if x[feat] > threshold]
        
        left_err = self._calc_squared_error(left)
        right_err = self._calc_squared_error(right)
        
        n_total = len(left) + len(right)
        weighted_err = (len(left)*left_err + len(right)*right_err) / n_total
        
        return weighted_err, len(left)
        
    def _calc_squared_error(self, values):
        if not values:
            return 0
        avg = sum(values) / len(values)
        return sum((x - avg)**2 for x in values) / len(values)


class RegressionTree:
    def __init__(self, data):
        self.root = TreeNode(data)
        self.fit()
        
    def fit(self):
        self.root.split()
        
    def predict(self, sample):
        node = self.root
        while node.left and node.right:
            if sample[node.split_point["feat"]] <= node.split_point["threshold"]:
                node = node.left
            else:
                node = node.right
                
        predictions = [x["bpd"] for x in node.examples]
        return sum(predictions) / len(predictions)
