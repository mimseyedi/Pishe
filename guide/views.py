from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from guide.models import Paper, PaperCategory, PaperTag


def guide_home_view(request, **kwargs):
    papers = Paper.objects.filter(status=1)
    last_papers = papers[:3]
    categories = PaperCategory.objects.all().annotate(posts_count=Count('paper'))
    tags = PaperTag.objects.all()

    if kwargs.get("cat_name") != None:
        papers = papers.filter(category__name=kwargs["cat_name"])

    if kwargs.get("tag_name") != None:
        papers = papers.filter(tag__name=kwargs["tag_name"])

    papers = Paginator(papers, 4)
    try:
        page_number = request.GET.get('page')
        papers = papers.get_page(page_number)
    except PageNotAnInteger:
        papers = papers.get_page(1)
    except EmptyPage:
        papers = papers.get_page(1)

    context = {"papers": papers, "categories": categories, "last_papers": last_papers, "tags": tags}
    return render(request, 'guide/guide_home_page.html', context)

