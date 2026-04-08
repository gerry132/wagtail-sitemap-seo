from django.core.files.base import ContentFile

from .storage import SitemapS3Storage


def save_xml(name: str, content: bytes) -> str:
    """
    Save an XML file using Django's default storage.

    - In dev (SITEMAP_WRITE_S3): saves to MEDIA_ROOT

    Returns the final storage path.
    """
    storage = SitemapS3Storage()
    if storage.exists(name):
        storage.delete(name)
    return storage.save(name, ContentFile(content))