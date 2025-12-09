from django.shortcuts import render
from .forms import feedbackform
from .models import Feedback

def feedbackview(request):
    print("➡ Entered feedbackview")
    f = feedbackform()

    if request.method == 'POST':
        print("➡ POST detected", request.POST)

        if 'submit' in request.POST:
            print("➡ Submit clicked")
            f = feedbackform(request.POST)
            if f.is_valid():
                feedback_instance = f.save()
                print("✅ Feedback saved successfully")

                d = {
                    'name': feedback_instance.name,
                    'age': feedback_instance.age,
                    'movie': feedback_instance.movie,
                    'email': feedback_instance.email,
                    'feed': feedback_instance.feed
                }
                return render(request, 'myapp/response.html', d)

        elif 'view' in request.POST:
            print("➡ View clicked")
            d = {
                'name': request.POST.get('name', ''),
                'age': request.POST.get('age', ''),
                'movie': request.POST.get('movie', ''),
                'email': request.POST.get('email', ''),
                'feed': request.POST.get('feed', '')
            }
            print("➡ Data passed to template:", d)
            return render(request, 'myapp/output.html', d)

    print("➡ Rendering input.html (initial load or invalid form)")
    return render(request, 'myapp/input.html', {'form': f})
