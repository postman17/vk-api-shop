=====
vkapi
=====

Vk-api-shop is a simple Django app to module.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "vk-api-shop" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'vk-api-shop',
    ]

2. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/

5, In admin panel visit `Params` model and add all parameters.

6. Add `Product` model::

    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=500)
    image = models.ImageField(upload_to='uploads')
    price = models.FloatField('Price')
    post_it = models.BooleanField('Post it!')

7. In your `product` model add save method::

        def save(self, *args, **kwargs):
            super(ShopModel, self).save(*args, **kwargs)
            if self.post_it:
                PostIn.vk(self)

