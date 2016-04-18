from apiRest.models import *
from django import forms
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from  rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class TendersSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Tenders
        fields = ('id_tender','title','description','status','items','minValue','value','procurementMethod','procurementMethodRationale','awardCriteria','awardCriteriaDetails','submissionMethod','submissionMethodDetails', 'tenderPeriod', 'enquiryPeriod', 'hasEnquiries', 'eligibilityCriteria', 'awardPeriod', 'numberOfTenderers', 'tenderers', 'procuringEntity', 'documents', 'milestones', 'amendment')

class AwardsSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Awards
        fields = ('id_award','title','description','status', 'date', 'value','suppliers', 'items', 'contractPeriod','documents','amendment','deliveryAddressh','id_release')

class ContractsSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Contracts
        fields = ('id','id_contract','awardID','title','description','status','period','value','items','dateSigned','documents','amendment','implementation', 'id_release')

class ReleasesSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Releases
        fields = ('id_release', 'num_constancia', 'date', 'tag', 'initiationType', 'planning','tender', 'buyer', 'awards', 'language')

class PlanningSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Releases
        fields = ('planning','documents',)

class AmendmentSerializer(EmbeddedDocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Amendment
        fields = ('date', 'changes','rationale')

class MilestoneSerializer(EmbeddedDocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Milestone
        fields = ('id','title','description','dueDate','dateModified','status','documents')

class ImplementationSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Implementation
        fields = ('id', 'transactions','documents', 'milestones')

class BudgetSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model = Budget
        fields = ('source', 'id_budget','description', 'amount','uri')

class PackagemetadataSerializer(DocumentSerializer):

    def _include_additional_options(self, *args, **kwargs):
        return self.get_extra_kwargs()

    class Meta:
        model =Packagemetadata
        fields = ('num_constancia','uri', 'publishedDate','releases', 'publisher', 'procurement_type')