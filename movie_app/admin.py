from django.contrib import admin
from movie_app.models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'director',)
    list_display_links = ('id', 'title',)
    search_fields = 'title descriptions'.split(),
    # inlines = [CommentInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Review)