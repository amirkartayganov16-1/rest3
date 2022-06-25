from movie_app.models import *
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'director',)
    list_display_links = ('id', 'title',)
    search_fields = 'title'.split(),

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'movie', 'stars')
    list_display_links = ('id', 'text')
    search_fields = ('text',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Review, ReviewAdmin)