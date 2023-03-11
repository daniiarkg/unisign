from django.db import models
from django.db.utils import IntegrityError

# ТЕСТ МОДЕЛЬ


class Test(models.Model):
    bity = models.CharField(unique=True, max_length=50)

    def save(self):
        if Test.objects.filter(bity=self.bity):
            self.bity = 'NO'
        super(Test, self).save()
