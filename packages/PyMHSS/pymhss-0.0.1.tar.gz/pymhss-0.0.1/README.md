# Metropolis-Hastings with Scalable Subsampling (MH-SS)

Python package that can be used to reproduce the figures and tables presented in [Prado, E.B., Nemeth, C. & Sherlock, C. Metropolis-Hastings with Scalable Subsampling. arxiv (2024)][mhss_paper].

Some datasets used in the real-world applications can be found in the UCI machine learning repository, and the links are provided in the scripts. The road casualties dataset can be downloaded from the R package "stats19" as shown in the corresponding script. Finally, the US census dataset is provided in this repository.


----

## MH-SS' abstract

The Metropolis--Hastings (MH) algorithm is one of the most widely used Markov Chain Monte Carlo schemes for generating samples from Bayesian posterior distributions. The algorithm is asymptotically exact, flexible and easy to implement. However, in the context of Bayesian inference for large datasets,  evaluating the likelihood on the full data for thousands of iterations until convergence can be prohibitively expensive. This paper introduces a new subsample MH algorithm that satisfies detailed balance with respect to the target posterior and utilises control variates to enable exact, efficient Bayesian inference on datasets with large numbers of observations. Through theoretical results, simulation experiments and real-world applications on certain generalised linear models, we demonstrate that our method requires substantially smaller subsamples and is computationally more efficient than the standard MH algorithm and other exact subsample MH algorithms.

[mhss_paper]: https://arxiv.org/pdf/2407.19602