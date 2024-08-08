#pragma once
#include "PA.h"

namespace tomoto
{
    template<TermWeight _tw>
	struct DocumentHPA : public DocumentPA<_tw>
	{
		using BaseDocument = DocumentPA<_tw>;
		using DocumentPA<_tw>::DocumentPA;
		using WeightType = typename DocumentPA<_tw>::WeightType;

		template<typename _TopicModel> void update(WeightType* ptr, const _TopicModel& mdl);

		DECLARE_SERIALIZER_WITH_VERSION(0);
		DECLARE_SERIALIZER_WITH_VERSION(1);
	};

	struct HPAArgs : public PAArgs
	{
	};

	class IHPAModel : public IPAModel
	{
	public:
		using DefaultDocType = DocumentHPA<TermWeight::one>;
		static IHPAModel* create(TermWeight _weight, bool _exclusive, const HPAArgs& args,
			bool scalarRng = false);
	};
}
