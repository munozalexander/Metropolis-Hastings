from __future__ import division
from mcmc import MetropolisHastings

sampler = MetropolisHastings([0.3, 0.1, 0.1, 0.5])
samples = sampler.sample()

print [samples.count(i)/len(samples) for i in range(4)] #approx [0.3,0.1,0.1,0.5]
