import math

def binomial_probability(n, k, p):
    """
    Calculates the binomial probability.

    Args:
        n: Number of trials.
        k: Number of successes.
        p: Probability of success on a single trial.

    Returns:
        The binomial probability.
    """
    return math.comb(n, k) * (p**k) * ((1 - p)**(n - k))

if __name__ == '__main__':
    n = 75
    k = 3
    p = 0.08
    probability = binomial_probability(n, k, p)
    print(f"P(X = {k}) = {probability:.4f}")
