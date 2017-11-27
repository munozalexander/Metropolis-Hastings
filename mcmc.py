from __future__ import division
import numpy as np

class MetropolisHastings():
    def __init__(self, stationary, P=None):
        '''
        sample from discrete distribution with metropolis hastings MCMC

        PARAMETERS
        stationary : proportional to stationary distriubtion of interest
        P : proposal distribution; if not specified, use random walk over all states
        '''
        self.s = stationary
        self.M = len(stationary)
        if P is None:
            self.P = np.zeros((self.M, self.M)) + (1/self.M)
        else:
            self.P = P

    def __generateProposal(self, currstate):
        ''' generate a proposal from the current state using P '''
        rand = np.random.random()
        for nextstate in range(self.M):
            if rand <= sum(self.P[currstate, :(nextstate+1)]):
                return nextstate

    def __acceptProposal(self, currstate, nextstate):
        ''' determine weather to accept a proposal by calculating a_ij '''
        a_ij = (self.s[nextstate]*self.P[nextstate,currstate]) / \
               (self.s[currstate]*self.P[currstate,nextstate])
        a_ij = min([a_ij, 1])
        return np.random.random() <= a_ij

    def __markovStep(self, currstate):
        ''' proposes new state then accepts or rejects to generate next state '''
        proposal = self.__generateProposal(currstate)
        if self.__acceptProposal(currstate, proposal):
            return proposal
        else:
            return currstate

    def sample(self, num_samples=100000, burnin=0.2, thin=5):
        '''
        samples from markov chain, then performs burnin and thinning

        PARAMETERS
        num_samples : number of samples to draw before burnin and thinning
        burnin : drop percent initial samples to allow chain to reach stationary
        thin : lessen sample autocorrelation by keeping every nth sample
        '''
        samples = []
        state = 0
        for i in range(num_samples):
            state = self.__markovStep(state)
            samples.append(state)
        samples = samples[int(burnin*num_samples)::thin]
        return samples
