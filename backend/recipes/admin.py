from django.contrib import admin

from .models import Favorite, Ingredient, Recipe, ShoppingList, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'measurement_unit')
    list_filter = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'in_favorite')
    list_filter = ['name', 'author', 'tags']

    def in_favorite(self, obj):
        return obj.in_favorite.all().count()


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingList, ShoppingListAdmin)
