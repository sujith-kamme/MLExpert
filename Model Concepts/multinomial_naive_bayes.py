from collections import defaultdict
import math

class MultinomialNB:
    def __init__(self, articles_per_tag):
        self.articles_per_tag = articles_per_tag
        self.tags = set(articles_per_tag.keys())
        self.prior_per_tag = {}
        self.likelihood = {}
        self.train()
    
    def train(self):
        # Calculate priors
        doc_count = sum(len(docs) for docs in self.articles_per_tag.values())
        self.prior_per_tag = {
            tag: len(docs)/doc_count 
            for tag, docs in self.articles_per_tag.items()
        }
        
        # Calculate word likelihoods
        self.likelihood = self._get_likelihood()
    
    def _get_likelihood(self):
        # Track word frequencies
        word_counts = defaultdict(lambda: {tag: 0 for tag in self.tags})
        total_words = defaultdict(int)
        
        # Count occurrences
        for tag, articles in self.articles_per_tag.items():
            for article in articles:
                for word in article:
                    word_counts[word][tag] += 1
                    total_words[tag] += 1
        
        # Calculate probabilities with Laplace smoothing
        probabilities = defaultdict(lambda: {tag: 0.5 for tag in self.tags})
        for word, tag_counts in word_counts.items():
            for tag in self.tags:
                count = tag_counts[tag]
                total = total_words[tag]
                probabilities[word][tag] = (count + 1) / (total + 2)
                
        return probabilities
    
    def predict(self, article):
        # Initialize with prior log probabilities
        scores = {
            tag: math.log(prior) 
            for tag, prior in self.prior_per_tag.items()
        }
        # Add word log probabilities
        for word in article:
            for tag in self.tags:
                scores[tag] += math.log(self.likelihood[word][tag])
        
        return scores
