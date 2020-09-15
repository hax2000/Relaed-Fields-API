from django.db import models


class RelatedField3_2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RelatedField3(models.Model):
    name = models.CharField(max_length=100)
    relfield3_2 = models.ForeignKey(RelatedField3_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RelatedField2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RelatedField1(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MainTable(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    field1 = models.IntegerField()
    field2 = models.IntegerField()
    field3 = models.IntegerField()
    field4 = models.DecimalField(max_digits=10, decimal_places=1)
    field5 = models.IntegerField(null=True)
    field6 = models.IntegerField()
    relfield1 = models.ForeignKey(RelatedField1, on_delete=models.CASCADE)
    relfield2 = models.ForeignKey(RelatedField2, on_delete=models.CASCADE)
    relfield3 = models.ForeignKey(RelatedField3, on_delete=models.CASCADE)
