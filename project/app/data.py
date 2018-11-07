class TestData(object):
    user = {'username': 'Jatin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # list of feature request, later will be added in database..
    fr = [
     {
         'title': 'hidden links',
         'description': 'The links should be automatically hidden after 5 sec'
     }
    ]