from .serializers import AvaliacaoSerializer, CursoSerializer
from .models import Curso, Avaliacao
from rest_framework import generics
from rest_framework.generics import get_object_or_404

# retorna toda a lista e cria uma nova colecao


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # essa classe foi modificada na "urls.py", pois na url nao esta sendo utilizado "pk" como padrao
    # por isso, deve mudar o comportamento da classe

    def get_queryset(self):
        # verificar se o curso esta sendo passado na url
        if (self.kwargs.get("curso_pk")):
            #  se tiver, retorna somente este curso
            return self.queryset.filter(curso_id=self.kwargs.get("curso_pk"))

        # se nao retorna todos
        return self.queryset.all()


# retorna toda a lista e cria uma nova colecao


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# acha um obj pelo id e deleta tambem pelo id


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# acha um obj pelo id e deleta tambem pelo id


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # essa classe foi modificada na "urls.py", pois na url nao esta sendo utilizado "pk" como padrao
    # por isso, deve mudar o comportamento da classe

    def get_object(self):
        # pegando a pk da URL
        curso_pk = self.kwargs.get("curso_pk")
        avaliacao_pk = self.kwargs.get("avaliacao_pk")

        # se existe, fazer o JOIN com ela
        if curso_pk:
            # pegando toda a colecao e fazendo o JOIN entre curso_id e pk
            return get_object_or_404(self.queryset.all(), curso_id=curso_pk, pk=avaliacao_pk)

        # se nao exite, nao tem JOIN para fazer
        return get_object_or_404(self.queryset.all(), pk=avaliacao_pk)
