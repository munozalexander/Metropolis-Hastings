# Metropolis-Hastings
Sample from a discrete distribution (only requires proportionality) using Metropolis Hastings MCMC.

For a demo, run `python demo.py`

To use the sampler with custom parameters, define the necessary parameters and run:
```python
from mcmc import MetropolisHastings

sampler = MetropolisHastings(stationary=stationary, P=P)
samples = sampler.sample(num_samples=num_samples, burnin=burnin, thin=thin)
```

Parameters for MetropolisHastings() class initialization:
* stationary : proportional to stationary distribution of interest (required)
* P : proposal distribution (default: use random walk over all states)

Parameters for MetropolisHastings().sample() method:
* num_samples : number of samples to draw before burnin and thinning (default: 100,000)
* burnin : drop percent initial samples to allow chain to reach stationary (default: 20%)
* thin : lessen sample autocorrelation by keeping every nth sample (default: 5)
