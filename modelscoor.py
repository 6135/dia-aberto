# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Coordenador(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.
    gabinete = models.CharField(db_column='Gabinete', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unidadeorganicaid = models.ForeignKey('Unidadeorganica', models.DO_NOTHING, db_column='unidadeOrganicaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coordenador'
