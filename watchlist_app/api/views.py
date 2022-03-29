from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

class MoviesList(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        ## serializer just process single objet
        serializer = MovieSerializer(movies, many=True)
        #print(dir(serializer))
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetail(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            content = {'please move along': 'no movie to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        content = {'msg': 'iz to remove sth huh?'}
        return Response(content, status=204)

