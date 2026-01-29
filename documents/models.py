import os
from django.db import models
from django.forms.fields import CharField

#NOTE
def document_upload_path(instance, filename):
    # files will be uploaded to: MEDIA_ROOT/documents/<user_id>/<filename>
    return os.path.join("documents", str(instance.owner.id), filename)

class Document(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    size = models.IntegerField(editable=False)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="documents")
    file = models.FileField(upload_to=document_upload_path, default='documents/default.pdf')

    def save(self, *args, **kwargs):
        # Call the parent save first so the file exists in storage
        super().save(*args, **kwargs)

        # Now update file size if the file exists
        if self.file and hasattr(self.file, 'path') and os.path.exists(self.file.path):
            self.size = self.file.size  # in bytes
            super().save(update_fields=['size'])

    #settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "documents" for loosely coupling
