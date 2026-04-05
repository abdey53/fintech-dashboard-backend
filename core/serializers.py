from rest_framework import serializers
from .models import User, FinancialRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active']
        read_only_fields = ['id']


class FinancialRecordSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = FinancialRecord
        fields = '__all__'
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    # 🔥 Validation: amount positive hona chahiye
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

    # 🔥 Validation: date future ka nahi hona chahiye
    def validate_date(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("Date cannot be in the future")
        return value

    # 🔥 Extra validation (optional but strong)
    def validate(self, data):
        if data['type'] == 'expense' and data['amount'] > 1000000:
            raise serializers.ValidationError("Expense amount too large")
        return data