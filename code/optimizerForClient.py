import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

class CVX(object):
    """
    verify the correctness of ADMM which is used to obtain 'nabla'.
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
    The difference matrix: 'Lambda'
    """
    def __init__(self, givenNumberOfFeatures):
        self.__d = givenNumberOfFeatures
        self.__diffMat = self.__initSuccessiveDiffMat()
    
    def __initSuccessiveDiffMat(self):
        diffMat = np.eye(self.__d)
        for i in range(self.__d-1):
            diffMat[i, i+1] = -1
        return diffMat

    def get(self):
        return self.__diffMat
    pass

class ADMM(object):
    def __init__(self, givenYtn, givenGt, givenEta, givenGamma, givenNumberOfFeatures):
        self.__diffMat = DiffMatrix(givenNumberOfFeatures=givenNumberOfFeatures).get()
        auxiliaryMatObj = AuxiliaryMatrix(givenDiffMatrix=self.__diffMat, givenTransposeOperatorLoc='left')
        self.__P = auxiliaryMatObj.getEigenVec()
        self.__sigma = auxiliaryMatObj.getEigenValue()
        self.__d = givenNumberOfFeatures
        self.__Ytn = givenYtn
        self.__R, self.__Y, self.__Omega = np.zeros(self.__d), np.zeros(self.__d), np.zeros(self.__d)
        self.__gt = givenGt
        self.__eta = givenEta
        self.__gamma = givenGamma
        self.__J = 25
        pass

    def __updateR(self):
        left = np.maximum(self.__diffMat @ (self.__Y - self.__Ytn) - self.__Omega - 1, 0) # set all negative element to be 0
        right = np.maximum(self.__diffMat @ (self.__Ytn - self.__Y) + self.__Omega - 1, 0)
        self.__R = left - right
        pass

    def __updateY(self):
        diagVals = self.__eta*self.__gamma*self.__sigma + 1
        left = self.__P @ np.diag(np.true_divide(1.0, diagVals)) @ self.__P.T
        right = self.__eta*self.__gamma*self.__diffMat.T @ (self.__R + self.__diffMat @ self.__Ytn + self.__Omega) + self.__Ytn - self.__eta*self.__gt
        self.__Y = left @ right
        pass

    def __updateOmega(self):
        self.__Omega = self.__Omega + (self.__R - self.__diffMat @ self.__Y + self.__diffMat @ self.__Ytn)
        pass
    
    def __stopCriterion(self, givenPreviousY,):
        diff = givenPreviousY - self.__Y
        if np.linalg.norm(diff) <= 1e-2:
            return True
        return False
    
    def execute(self):
        for j in range(self.__J):
            # update R
            self.__updateR()
            # update Y
            previousY = self.__Y
            self.__updateY()
            # update Omega
            self.__updateOmega()    
            # stop now?
            if self.__stopCriterion(givenPreviousY=previousY) == True:
                break
        pass

    def getY(self):
        return self.__Y
    pass

class Optimizer(object):
    def __init__(self, givenGt, givenYtn, givenGamma, givenEta):
        self.__gt = givenGt
        self.__Ytn = givenYtn
        self.__gamma = givenGamma
        self.__eta = givenEta
        self.__numberOfFeatures = len(self.__Ytn)
        self.__nabla = self.computeNabla()
        pass
    
    def computeNabla(self):
        admm = ADMM(givenYtn=self.__Ytn, givenGt=self.__gt, givenEta=self.__eta, givenGamma=self.__gamma, givenNumberOfFeatures=self.__numberOfFeatures)
        admm.execute()
        nabla = np.true_divide(self.__Ytn - admm.getY(), self.__eta)
        return nabla 

    def show(self):
        seriesList = [Series(givenValues=self.__nabla, givenHeaderName='Local update with CER(ADMM)'), Series(givenValues=self.__gt, givenHeaderName='Local update without CER')]  
        LinePloter(givenMultipleSeriesList=seriesList, givenLinePloterSetting=LinePloterSetting(givenXLabel='Dimension', givenYLabel='Value'), givenSavedFigPath='/home/yawei/communication-efficient-federated-training/code/xxx.jpg').plot()  
    pass

class Series(object):
    def __init__(self, givenValues, givenHeaderName):
        self.__headerName = givenHeaderName
        self.__valueList = givenValues
    
    def getValues(self):
        return self.__valueList
    
    def getHeaderName(self):
        return self.__headerName
    pass
   
class LinePloterSetting(object):
    def __init__(self, givenXLabel, givenYLabel):
        self.__xLabel = givenXLabel
        self.__yLabel = givenYLabel
        self.__gridOn = False

    def getXLabel(self):
        return self.__xLabel

    def getYLabel(self):
        return self.__yLabel

    def getGridOn(self):
        return self.__gridOn
    pass

class LinePloter(object):
    def __init__(self, givenMultipleSeriesList, givenLinePloterSetting, givenSavedFigPath):
        assert(isinstance(givenLinePloterSetting, LinePloterSetting))
        self.__seriesList = givenMultipleSeriesList
        self.__settingInfo = givenLinePloterSetting
        self.__savedFigPath = givenSavedFigPath
        pass

    def __getLegends(self):
        legendList = []
        for seriesIndex, series in enumerate(self.__seriesList):
            legend = series.getHeaderName()
            legendList.append(legend)
        return legendList

    def plot(self):
        legendList = self.__getLegends()
        fig = plt.figure() 
        ax1 = fig.add_subplot(1, 1, 1)
        for series in self.__seriesList:
            assert(isinstance(series, Series))
            valueList = series.getValues()
            ax1.plot([int(id) for id in range(1,len(valueList)+1)], [float(value) for value in valueList], linewidth = 1) 
        ax1.set_ylabel(self.__settingInfo.getYLabel()) 
        ax1.set_xlabel(self.__settingInfo.getXLabel()) 
        ax1.legend(legendList)
        ax1.grid(self.__settingInfo.getGridOn()) 
        plt.savefig(self.__savedFigPath) 
        plt.show()
    pass

class Test(object):
    def testOptimizer(self):
        givenGt = np.random.randn(500)
        givenYtn = np.random.randn(500)
        opt = Optimizer(givenGt=givenGt,givenYtn=givenYtn,givenGamma=50,givenEta=1e-2)
        opt.show()
    pass

np.random.seed(0)
Test().testOptimizer()

























