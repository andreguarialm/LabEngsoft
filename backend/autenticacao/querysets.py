
from django.db.models import QuerySet


class SocioQuerySet(QuerySet):
    
    def alunos(self):
        return self.filter(breve__isnull=True)