from rest_framework import serializers
from api.models.models_ropa import Ropa

class ropaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ropa  
        exclude = ["id"]