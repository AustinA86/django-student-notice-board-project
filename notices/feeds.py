from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Notice

# MODULE 4: Feed Framework (RSS Feed)
class LatestNoticesFeed(Feed):
    title = "Student Notice Board Updates"
    link = "/feeds/"
    description = "Latest notices from the student portal."

    def items(self):
        return Notice.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    def item_link(self, item):
        return reverse('notice-detail', args=[item.pk])
