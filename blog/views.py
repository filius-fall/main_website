from django.shortcuts import render


# Create your views here.
def home(request):
    test_data = [
        {
            'title': 'Card One',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.',
            'published_date': '26/11/1997',
            'author': 'Sreeram A'
        },
        {
            'title': 'Card Two',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.',
            'published_date': '13/05/2022',
            'author': 'Sreeram A'
        },
        {
            'title': 'Card Three',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.',
            'published_date': '10/2/2021s',
            'author': 'Sreeram A'
        },
        {
            'title': 'Card Four',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.',
            'published_date': '10/2/2021s',
            'author': 'Sreeram A'
        },
        {
            'title': 'Card Five',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.',
            'published_date': '10/2/2021s',
            'author': 'Sreeram A'
        },
        {
            'title': 'Card Six',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.',
            'published_date': '10/2/2021s',
            'author': 'Sreeram A'
        }
    ]

    context = {
        'test_data':test_data
    }
    return render(request,'blog/blog.html',context)


def about(request):
    return render(request,'blog/about.html')