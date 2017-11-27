# Metropolis-Hastings
Sample from a discrete distribution using Metropolis Hastings MCMC.

For a demo, run `python demo.py`

To use the sampler with custom parameters, define the necessary parameters and run:
```python
from mcmc import MetropolisHastings

sampler = MetropolisHastings(stationary=stationary, P=P)
samples = sampler.sample(num_samples=num_samples, burnin=burnin, thin=thin)
```

Parameters for MetropolisHastings() class initialization:
* stationary : Proportional to stationary distribution of interest (required).
* P : Proposal distribution. If not specified, use random walk over all states by default.

Parameters for MetropolisHastings().sample() method:
* num_samples : Number of samples to draw before burnin and thinning.
* burnin : Drop percent initial samples to allow chain to reach stationary.
* thin : Lessen sample autocorrelation by keeping every nth sample.
