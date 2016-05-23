from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    # 表示フィールド
    list_display = ['title', 'updated', 'timestamp']
    # リングフィールド
    list_display_links = ['updated']
    # 表示フィールドで一覧から変更可能なフィールド
    list_editable = ['title']
    # 時刻関係でフィルター
    list_filter = ['updated', 'timestamp']
    # 文字関係でフィルター
    search_fields = ['content']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
