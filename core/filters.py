from django_filters import rest_framework as filters

from core import models

# Filtros de pesquisa
LIKE = 'unaccent__icontains'  # Usando unaccent para ignorar acentos e trazer palavras semelhantes
ICONTAINS = 'icontains'  # Usando icontains para trazer palavras semelhantes
UNACCENT_IEXACT = 'unaccent__iexact'  # Usando unaccent para ignorar acentos e trazer palavras exatas
EQUALS = 'exact'  # Usando exact para trazer o campo exatas
STARTS_WITH = 'startswith'  # Usando startswith para trazer palavras que começam com o termo pesquisado
GT = 'gt'  # maior que
LT = 'lt'  # menor que
GTE = 'gte'  # maior ou igual a
LTE = 'lte'  # menor ou igual a
IN = 'in'  # Usando in para trazer palavras que estão na lista


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr=LIKE)
    country = filters.CharFilter(field_name="country", lookup_expr=LIKE)
    email = filters.CharFilter(field_name="email", lookup_expr=LIKE)
    created_at_gte = filters.DateFilter(field_name="created_at", lookup_expr=GTE)
    created_at_lte = filters.DateFilter(field_name="created_at", lookup_expr=LTE)

    class Meta:
        model = models.Author
        fields = ["name", "country", "email", "created_at_gte", "created_at_lte"]


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr=LIKE)
    publication_date_gte = filters.DateFilter(field_name="publication_date", lookup_expr=GTE)
    publication_date_lte = filters.DateFilter(field_name="publication_date", lookup_expr=LTE)
    author = filters.ModelMultipleChoiceFilter(field_name="author", queryset=models.Author.objects.all())
    category = filters.ModelChoiceFilter(field_name="category", queryset=models.Category.objects.all())

    class Meta:
        model = models.Book
        fields = ["title", "publication_date_gte", "publication_date_lte", "author", "category"]


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr=LIKE)
    cpf = filters.CharFilter(field_name="cpf", lookup_expr=STARTS_WITH)
    status = filters.NumberFilter(field_name="status", lookup_expr=LIKE)
    profile = filters.ModelMultipleChoiceFilter(field_name="profile", queryset=models.Profile.objects.all())

    class Meta:
        model = models.User
        fields = ["name", "cpf", "status", "profile"]


class LoanFilter(filters.FilterSet):
    loan_gte = filters.DateFilter(field_name="loan", lookup_expr=GTE)
    loan_lte = filters.DateFilter(field_name="loan", lookup_expr=LTE)
    date_withdraw_gte = filters.DateFilter(field_name="date_withdraw", lookup_expr=GTE)
    date_withdraw_lte = filters.DateFilter(field_name="date_withdraw", lookup_expr=LTE)
    date_return_gte = filters.DateFilter(field_name="date_return", lookup_expr=GTE)
    date_return_lte = filters.DateFilter(field_name="date_return", lookup_expr=LTE)
    delivery_time = filters.TimeFilter(field_name="delivery_time", lookup_expr=LIKE)
    quantity_gt = filters.NumberFilter(field_name="quantity", lookup_expr=GT)
    book = filters.ModelChoiceFilter(field_name="book", queryset=models.Book.objects.all())
    user = filters.ModelChoiceFilter(field_name="user", queryset=models.User.objects.all())

    class Meta:
        model = models.Loan
        fields = ["loan_gte", "loan_lte", "date_withdraw_gte", "date_withdraw_lte",
                  "date_return_gte", "date_return_lte", "delivery_time", "quantity_gt", "book", "user"]


class AddressFilter(filters.FilterSet):
    address = filters.CharFilter(field_name="address", lookup_expr=LIKE)
    cep = filters.CharFilter(field_name="cep", lookup_expr=EQUALS)
    public_place = filters.CharFilter(field_name="public_place", lookup_expr=LIKE)
    reference_point = filters.CharFilter(field_name="reference_point", lookup_expr=LIKE)
    user = filters.ModelChoiceFilter(field_name="user", queryset=models.User.objects.all())

    class Meta:
        model = models.Address
        fields = ["address", "cep", "public_place", "reference_point", "user"]


class PhoneFilter(filters.FilterSet):
    number = filters.NumberFilter(field_name="number", lookup_expr=LIKE)
    user = filters.ModelChoiceFilter(field_name="user", queryset=models.User.objects.all())

    class Meta:
        model = models.Phone
        fields = ["number", "user"]


class ProfileFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr=LIKE)
    limit_delivery = filters.NumberFilter(field_name="limit_delivery", lookup_expr=LIKE)

    class Meta:
        model = models.Profile
        fields = ["name", "limit_delivery"]
