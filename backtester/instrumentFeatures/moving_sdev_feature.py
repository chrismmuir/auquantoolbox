from instrument_feature import InstrumentFeature
from backtester.financial_fn import msdev

class MovingSDevInstrumentFeature(InstrumentFeature):

    @classmethod
    def validateInputs(cls, featureParams, featureKey, currentFeatures, instrument):
        return True

    @classmethod
    def compute(cls, featureParams, featureKey, currentFeatures, instrument):
    	data = instrument.getLookbackFeatures().getData()[featureParams['featureName']]
        sdev = msdev(data, featureParams['period'])
        if len(sdev.index) > 0 :
        	return sdev[-1]
        else:
        	return 0
