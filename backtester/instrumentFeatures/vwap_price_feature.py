from instrument_feature import InstrumentFeature


class VwapPriceInstrumentFeature(InstrumentFeature):

    @classmethod
    def validateInputs(cls, featureParams, featureKey, currentFeatures, instrument):
        return True

    @classmethod
    def compute(cls, featureParams, featureKey, currentFeatures, instrument):
        bookData = instrument.getCurrentBookData()
        instrumentType = instrument.getInstrumentType()
        totalVolume = (bookData['askVolume'] + bookData['bidVolume'])
        if totalVolume > 0:
            vwap = ((bookData['askPrice'] * bookData['askVolume']) + (bookData['bidPrice'] *
                                                                      bookData['bidVolume'])) / totalVolume
            return vwap
        else:
            return 0