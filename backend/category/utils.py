def images_directory_path(instance, filename):
    """
    Define structure for storing models' images.
    """
    if hasattr(instance, 'slug'):
        instance = instance.slug
    return "{0}/{1}".format(instance, filename)
