from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html
from pytils.translit import slugify


class NameBaseModel(models.Model):
    '''Abstract model for classes with name field.'''

    name = models.CharField(
        'Название',
        max_length=200,
        unique=True,
        db_index=True,
    )
    slug = models.SlugField(
        'slug',
        max_length=200,
        unique=True,
        blank=True,
    )
    image = models.ImageField(
        'Избражение',
        upload_to='category/images/',
        null=True,
        blank=True,
        default=None,
    )

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name

    def clean(self):
        '''Capitalize the name and check its uniqueness.'''

        self.name = self.name.capitalize()

        instance_exists = self.__class__.objects.filter(pk=self.pk).first()

        if (not instance_exists or
                instance_exists.name != self.name):
            if self.__class__.objects.filter(
                name=self.name,
            ).exists():
                raise ValidationError(
                    {'name': 'Данное название уже существует.'}
                )

    def save(self, *args, **kwargs):
        '''Generata a slug value before saving.'''
        self.full_clean()
        if not self.slug:
            max_length = self.__class__._meta.get_field('slug').max_length
            self.slug = slugify(self.name)[:max_length]
        return super().save(*args, **kwargs)


class Category(NameBaseModel):
    '''Product category model.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(NameBaseModel):
    '''Product subcategory model.'''

    categories = models.ManyToManyField(
        Category,
        verbose_name='Категории',
        related_name='subcategories'
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def display_categories(self, delimiter='<br>'):
        category_queryset = self.categories.all()
        categories = f"{delimiter}".join(
            category.name for category in category_queryset
        )

        return format_html(categories)

    display_categories.short_description = 'Категории'
