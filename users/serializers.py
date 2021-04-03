from rest_framework import serializers

from users.models import User, Adapter


class AdapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adapter
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    serial_number = serializers.CharField()
    code = serializers.CharField()
    # adapters = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['uuid', 'email', 'username', 'is_master', 'is_active', 'serial_number', 'code',]

    def validate(self, attrs):
        try:
            print(attrs['code'])
            print()
            Adapter.objects.get(code=attrs['code'], serial_number=attrs['serial_number'])
        except Adapter.DoesNotExist:
            message = {
                "serial_number": "There is no adapter with given serial number and code"
            }
            raise serializers.ValidationError(message)
        return attrs

