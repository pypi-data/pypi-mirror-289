#pragma once
#include "LDA.h"

namespace tomoto
{
    template<TermWeight _tw>
	struct DocumentCTM : public DocumentLDA<_tw>
	{
		using BaseDocument = DocumentLDA<_tw>;
		using DocumentLDA<_tw>::DocumentLDA;
		Matrix beta; // Dim: (K, betaSample)
		Vector smBeta; // Dim: K
		
		DECLARE_SERIALIZER_WITH_VERSION(0);
		DECLARE_SERIALIZER_WITH_VERSION(1);
	};

	struct CTArgs : public LDAArgs
	{

	};

	class ICTModel : public ILDAModel
	{
	public:
		using DefaultDocType = DocumentCTM<TermWeight::one>;
		static ICTModel* create(TermWeight _weight, const CTArgs& args,
			bool scalarRng = false);

		virtual void setNumBetaSample(size_t numSample) = 0;
		virtual size_t getNumBetaSample() const = 0;
		virtual void setNumTMNSample(size_t numSample) = 0;
		virtual size_t getNumTMNSample() const = 0;
		virtual void setNumDocBetaSample(size_t numSample) = 0;
		virtual size_t getNumDocBetaSample() const = 0;
		virtual std::vector<Float> getPriorMean() const = 0;
		virtual std::vector<Float> getPriorCov() const = 0;
		virtual std::vector<Float> getCorrelationTopic(Tid k) const = 0;
	};
}
