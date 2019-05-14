from django.shortcuts import render
from home.models      import UserProfile, Confessions
from django.db.models import Q


def search_view(request):
    raw_search_query = request.GET.get('q')

    raw_search_type = 'people'
    raw_search_type = request.GET.get('q_type', 'people')

    formatted_query = raw_search_query.replace(' ', ', ')
    formatted_query = formatted_query.split(', ')

    full_content_list = []

    st_formatted = 'People'

    if raw_search_type == 'confessions':
        st_formatted = 'Confessions'
        for quer in formatted_query:
            if quer:
                full_content_list += Confessions.objects.filter(
                    Q(confession_title__icontains=quer) |
                    Q(confession_body__icontains=quer)
                ).distinct().order_by('-date_created_at')
    else:

        for quer in formatted_query:
            if quer:
                full_content_list += UserProfile.objects.filter(
                    Q(profile_nickname__icontains=quer) |
                    Q(username__icontains=quer)
                ).distinct().exclude(username='admin')

    rendered_full_list = list(set(full_content_list))


    context = {
        'raw_search_query': raw_search_query,
        'raw_search_type': raw_search_type,
        'query_content': rendered_full_list,
        'st_formatted': st_formatted,
    }

    return render(request, 'usearch/search_view.html', context)
