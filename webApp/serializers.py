from apiRest.models import *
from django import forms
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

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
    buyer = BuyerSerializer(read_only=True)
    tender = TenderSerializer(read_only=True)

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()
        

    class Meta:
        model = Releases
        fields = ('num_constancia', 'date', 'tag', 'tender', 'buyer')

class ReleasesContractsSerializer(DocumentSerializer):
    buyer = BuyerSerializer(read_only=True)
    contracts = ContractSerializer(read_only=True)

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()
        

    class Meta:
        model = Releases
        fields = ('num_constancia', 'date', 'tag', 'contracts', 'buyer')

class ReleasesAwardsSerializer(DocumentSerializer):
    buyer = BuyerSerializer(read_only=True)
    awards = AwardsSerializer(read_only=True)

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()
        

    class Meta:
        model = Releases
        fields = ('num_constancia', 'date', 'tag', 'awards', 'buyer')


class PackagemetadataSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    releases = ReleasesSerializer(many=True, read_only=True)

    class Meta:
        model =Packagemetadata
        fields = ('num_constancia','uri', 'publishedDate','releases', 'publisher')

class PackagemetadataContractSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    releases = ReleasesContractsSerializer(many=True, read_only=True)

    class Meta:
        model =Packagemetadata
        fields = ('num_constancia','uri', 'publishedDate','releases', 'publisher')

class PackagemetadataAwardSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    releases = ReleasesAwardsSerializer(many=True, read_only=True)

    class Meta:
        model =Packagemetadata
        fields = ('num_constancia','uri', 'publishedDate','releases', 'publisher')