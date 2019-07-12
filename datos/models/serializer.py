from rest_framework import serializers

from subscriptions.models import ModelApiCall

# This class is to serialize the data, directly tied to a django model for the DRF endpoint.
class ModelApiCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelApiCall

        #TODO: add the process_time_ms, and any other fields, once the inference to cloud is complete.
        fields = ('model_subscription',)
