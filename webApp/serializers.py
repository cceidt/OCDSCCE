from apiRest.models import *
from django import forms
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from rest_framework.serializers import ModelSerializer, CharField

class ValueSerializer(EmbeddedDocumentSerializer):
	
	def _include_additional_options(self, *args, **kwargs):
		return self.get_extra_kwargs()

	class Meta:
		model = Value
		fields = ('amount',)
		
class TenderSerializer(EmbeddedDocumentSerializer):
    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    value = ValueSerializer(read_only=True)
    class Meta:
        model = Tenders
        fields = ('description', 'value')	

class ContractSerializer(EmbeddedDocumentSerializer):
    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    value = ValueSerializer(read_only=True)
    class Meta:
        model = Contracts
        fields = ('description', 'value')

class AwardsSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Awards
        fields = ('description','value')

class BuyerSerializer(EmbeddedDocumentSerializer):
    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Organization
        fields = ('identifier', 'name')

class ReleasesSerializer(DocumentSerializer):
    
    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()


    class Meta:
        a =('id','num_constancia', 'date', 'tag', 'tender', 'buyer')
        def get_queryset(self):
            queryset = Releases.objects.all()
            tag = self.request.get('tag')
            if 'contract' in tag or 'contractTermination' in tag:
                a = ('num_constancia', 'date', 'tag', 'contracts', 'buyer')
            if 'award' in tag or 'awardCancellation'in tag :
                a = ('num_constancia', 'date', 'tag', 'awards', 'buyer')
            else:
                pass

        tender = TenderSerializer(read_only=True,)
        contracts = ContractSerializer(read_only=True)
        awards = AwardsSerializer(read_only=True)
        buyer = BuyerSerializer(read_only=True)
        model = Releases
        fields = a


class PackagemetadataSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    releases = ReleasesSerializer(many=True, read_only=True)

    class Meta:
        model =Packagemetadata
        fields = ('num_constancia','uri', 'publishedDate','releases', 'publisher')