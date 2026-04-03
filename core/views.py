from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.db.models import Sum
from django.db.models.functions import TruncMonth

from .models import User, FinancialRecord
from .serializers import UserSerializer, FinancialRecordSerializer
from .permissions import IsAdmin, IsAnalystOrAdmin


# 👤 USER VIEWSET (Only Admin)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


# 💰 FINANCIAL RECORD VIEWSET
class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all() 
    serializer_class = FinancialRecordSerializer

    def get_queryset(self):
        queryset = FinancialRecord.objects.all() 

        # 🔐 User-based data isolation
        if self.request.user.role != 'admin':
            queryset = queryset.filter(created_by=self.request.user)

        # 🔎 Filtering
        type_param = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if type_param:
            queryset = queryset.filter(type=type_param)

        if category:
            queryset = queryset.filter(category=category)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated(), IsAnalystOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# 📊 DASHBOARD SUMMARY
@api_view(['GET'])
@permission_classes([IsAnalystOrAdmin])
def dashboard_summary(request):
    records = FinancialRecord.objects.all()

    if request.user.role != 'admin':
        records = records.filter(created_by=request.user)

    income = records.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
    expense = records.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0

    return Response({
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    })


# 📊 CATEGORY SUMMARY
@api_view(['GET'])
@permission_classes([IsAnalystOrAdmin])
def category_summary(request):
    records = FinancialRecord.objects.all()

    if request.user.role != 'admin':
        records = records.filter(created_by=request.user)

    data = records.values('category').annotate(total=Sum('amount'))

    return Response(data)


# 🕒 RECENT TRANSACTIONS
@api_view(['GET'])
@permission_classes([IsAnalystOrAdmin])
def recent_transactions(request):
    records = FinancialRecord.objects.all()

    if request.user.role != 'admin':
        records = records.filter(created_by=request.user)

    records = records.order_by('-date')[:5]
    serializer = FinancialRecordSerializer(records, many=True)

    return Response(serializer.data)


# 📈 MONTHLY TRENDS
@api_view(['GET'])
@permission_classes([IsAnalystOrAdmin])
def monthly_trends(request):
    records = FinancialRecord.objects.all()

    if request.user.role != 'admin':
        records = records.filter(created_by=request.user)

    data = records.annotate(month=TruncMonth('date')) \
        .values('month', 'type') \
        .annotate(total=Sum('amount')) \
        .order_by('month')

    return Response(data)