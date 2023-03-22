import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

class CVX(object):
    """
    verify the correctness of ADMM which is used to obtain 'Z'.
    """
    def __init__(self, givenYtn, givenGt, givenEta, givenGamma, givenNumberOfFeatures):
        self.__diffMat = DiffMatrix(givenNumberOfFeatures=givenNumberOfFeatures).get()
        self.__d = givenNumberOfFeatures
        self.__gt = givenGt
        self.__eta = givenEta
        self.__gamma = givenGamma
        self.__Ytn = givenYtn
        self.__V = np.zeros(self.__d)
        pass

    def execute(self):
        Y = cp.Variable(self.__d)
        problem = cp.Problem(cp.Minimize( cp.norm1(self.__diffMat @ (Y - self.__Ytn)) + (cp.norm2(Y - (self.__Ytn - self.__eta*self.__gt)) ** 2) / (2*self.__eta*self.__gamma) ))
        problem.solve()
        self.__V = Y.value

    def getV(self):
        return self.__V
    pass

class AuxiliaryMatrix(object):
    """
    symetric and positive defined matrix. For example the auxiliary matrix may be 'diffMat^\top * diffMat' or 'diffMat * diffMat^\top'.
    """
    def __init__(self, givenDiffMatrix, givenTransposeOperatorLoc):
        if givenTransposeOperatorLoc == 'left':
            self.__mat = givenDiffMatrix.T @ givenDiffMatrix
        if givenTransposeOperatorLoc == 'right':
            self.__mat = givenDiffMatrix @ givenDiffMatrix.T
        eigValue, eigVec = np.linalg.eig(self.__mat) # mat = P * Sigma * P^{-1}
        self.__sigma = eigValue
        self.__P = eigVec
        pass
    
    def get(self):
        return self.__mat
    
    def getEigenValue(self):
        return self.__sigma
    
    def getEigenVec(self):
        return self.__P
    
    pass

class DiffMatrix(object):
    """
    The difference matrix: 'Q', which is generated by graph G.
    """
    def __init__(self, givenGraph):
        self.__diffMat = self.__initDiffMat()
    
    def __initDiffMat(self):
        dd

    def get(self):
        return self.__diffMat
    pass

class SimilarityInDataSpace(object):
    """
    Compute similarity between nodes in the data space. Here, use the sketch of samples to represent a distribution.
    """
    def __init__(self, givenDataDistributionDict):
        
        pass

    def computeSimilarityMat(self):
        pass

    def getSimilarityMat(self):
        pass
    pass

class SimilarityInFeatureSpace(object):
    def __init__(self, givenDataDistributionDict):
        
        pass

    def computeSimilarityMat(self):
        pass

    def getSimilarityMat(self):
        pass
    pass

class SimilarityInModelSpace(object):
    def __init__(self, givenDataDistributionDict):
        
        pass

    def computeSimilarityMat(self):
        pass

    def getSimilarityMat(self):
        pass
    pass

class GraphGenerater(object):
    def __init__(self, givenNumOfNode):
        pass

    def generateAdjacentMat(self, givenSimilarityObj):
        if isinstance(givenSimilarityObj, SimilarityInDataSpace):
            xxx
        if isinstance(givenSimilarityObj, SimilarityInFeatureSpace):
            xxx
        if isinstance(givenSimilarityObj, SimilarityInModelSpace):
            xxx
        pass

    def getAdjacentMat(self):
        pass
    
    pass

























