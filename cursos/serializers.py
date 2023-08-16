from rest_framework import serializers
from .models import Curso, Avaliacao

# serializers serve para transformar e destransformar obj JSON

# serializer do model avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    # curso = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="curso-detail"
    # )

    # configuracao do serializer
    class Meta:
        # informando de qual model se trata
        model = Avaliacao

        # campos que irao ser mostrados ao consultar este model
        fields = (
            'id',
            'nome',
            'avaliacao',
            'comentario',
            # ao consultar este model, nao e legal mostrar o campo email (privacidade)
            'email',
            'criacao',
            'ativo',
            'curso'
        )

        # apenas permitido escrever o email (cadastro) na hora da consulta ele nao ira retornar
        extra_kwargs = {
            'email': {'write_only': True}
        }

# serializer de curso


class CursoSerializer(serializers.ModelSerializer):
    # # nested relationship (retornar as avaliacoes dos cursos)

    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #  Hyper linked Related Field retorna o LINK das avaliacoes dos cursos (recomendado API-REST)

    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="avaliacao-detail"
    # )

    # Primary Key Related Field (retorna a pk das avaliacoes)

    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso

        # tds os campos podem ser mostrados
        fields = '__all__'
