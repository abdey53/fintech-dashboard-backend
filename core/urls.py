from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FinancialRecordViewSet,dashboard_summary, category_summary, recent_transactions, monthly_trends

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'records', FinancialRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/summary/', dashboard_summary),
    path('dashboard/categories/', category_summary),
    path('dashboard/recent/', recent_transactions),
    path('dashboard/trends/', monthly_trends),
]