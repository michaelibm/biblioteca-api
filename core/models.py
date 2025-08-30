from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=False,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
    )

    class Meta:
        abstract = True
        managed = True


class Author(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )

    country = models.CharField(
        db_column='tx_country',
        max_length=40,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        db_column='tx_email',
        null=False,
        blank=False,
    )

    birth_date = models.DateField(
        db_column='tx_birth_date',
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        # colocar o nome da class sempre no plural


class Book(ModelBase):
    title = models.CharField(
        db_column='tx_title',
        max_length=120,
        null=False,
        blank=False,
    )

    publication_date = models.DateField(
        db_column='tx_publication_date',
        null=False,
        blank=False,
    )

    quantity = models.IntegerField(
        db_column='tx_quantity',
        null=False,

    )

    author = models.ManyToManyField(  # Relation Author and book
        Author,
        db_table='book_author',
    )

    category = models.ForeignKey(  # Relation one to many between category and book
        to='Category',
        db_column='id_category',
        on_delete=models.PROTECT,
        null=False,
    )

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Category(ModelBase):
    category = models.CharField(
        db_column='tx_category',
        max_length=40,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Loan(ModelBase):
    loan = models.DateField(
        db_column='tx_loan',
        null=False,
        blank=False,
    )

    date_withdraw = models.DateField(
        db_column='tx_date_withdraw',
        null=False,
        blank=False,
    )

    date_return = models.DateField(
        db_column='tx_date_return',
        null=False,
        blank=False,
    )

    delivery_time = models.TimeField(
        db_column='tx_delivery_time',
        null=False,
        blank=False,
    )

    quantity = models.IntegerField(
        db_column='tx_quantity',
        null=False,
        blank=False,
    )

    book = models.ForeignKey(  # Relation one to many between loan and book #
        to='Book',
        db_column='id_book',
        on_delete=models.PROTECT,
        null=False,
    )

    user = models.ForeignKey(  # Relation one to many between loan and book #
        to='User',
        db_column='id_user',
        on_delete=models.PROTECT,
        null=False,
    )

    employee = models.ForeignKey(  # Relation one to many between loan and book #
        to='Employee',
        db_column='id_employee',
        on_delete=models.PROTECT,
        null=True,
    )

    class Meta:
        db_table = 'loan'
        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'


class Address(ModelBase):
    address = models.CharField(
        db_column='tx_address',
        max_length=60,
        null=False,
        blank=False,
    )

    cep = models.CharField(
        db_column='tx_cep',
        max_length=120,
        null=False,
        blank=False,
    )

    public_place = models.CharField(
        db_column='tx_public_place',
        max_length=40,
        null=False,
        blank=False,
    )

    reference_point = models.CharField(
        db_column='tx_reference_point',
        max_length=40,
        null=False,
        blank=False,
    )

    user = models.ForeignKey(  # Relation one to many between loan and book
        to='User',
        db_column='id_user',
        on_delete=models.PROTECT,
        null=False,
    )

    class Meta:
        db_table = 'address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class User(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )

    cpf = models.CharField(
        db_column='tx_cpf',
        null=False,
        blank=False,
        validators=[MinLengthValidator(11),MaxLengthValidator(11)]
    )

    date_birth = models.DateField(
        db_column='tx_birth_date',
        null=False,
        blank=False,
    )

    status = models.IntegerField(
        db_column='tx_status',
        null=False,
        blank=False,
    )

    profile = models.ManyToManyField(
        'Profile',
        db_table='user_profile',
    )

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Phone(ModelBase):
    number = models.CharField(
        db_column='tx_number',
        null=False,
        blank=False,
        validators=[MinLengthValidator(11), MaxLengthValidator(12)]
    )

    user = models.ForeignKey(  # Relation one to many between loan and book
        to='User',
        db_column='id_user',
        on_delete=models.PROTECT,
        null=False,
    )

    class Meta:
        db_table = 'phone'
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'


class Profile(ModelBase):
    profile = models.TextField(
        db_column='tx_profile',
        null=False,
        blank=False,
    )
    limit_delivery = models.IntegerField(
        db_column='tx_limit_delivery',
        null=True,
        blank=False,
    )

    name = models.CharField(
        db_column='tx_name',
        max_length=240,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Function(ModelBase):
    funcao = models.TextField(
        db_column='tx_funcao',
        null=False,
        blank=False,
    )


    name = models.CharField(
        db_column='tx_name',
        max_length=240,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'employee'
        verbose_name = 'employee'
        verbose_name_plural = 'employee'


class Employee(ModelBase):
    nome = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )

    cpf = models.CharField(
        db_column='tx_cpf',
        null=False,
        blank=False,
        validators=[MinLengthValidator(11),MaxLengthValidator(11)]
    )

    date_birth = models.DateField(
        db_column='tx_birth_date',
        null=False,
        blank=False,
    )

    status = models.IntegerField(
        db_column='tx_status',
        null=False,
        blank=False,
    )

    funcao = models.ManyToManyField(
        'Function',
        db_table='user_funcao',
    )

    class Meta:
        db_table = 'Employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
