
from rest_framework.routers import DefaultRouter

from core.viewsets import AuthorViewSet, BookViewSet, UserViewSet, LoanViewSet, AddressViewSet, PhoneViewSet, \
    ProfileViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books',  BookViewSet)
router.register('users', UserViewSet)
router.register('loans', LoanViewSet)
router.register('addresses', AddressViewSet)
router.register('phones', PhoneViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns  = router.urls
