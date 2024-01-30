from django.shortcuts import render , redirect
from .models import institute
from .models import questions,Comment
from .forms  import QuestionForm, CommentForm
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView, CreateView
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    
    Allcollege = institute.objects.all()
    return render(request, "index.html", {'Allcollege' : Allcollege})


def showinformation(request):
    if request.method== 'POST':
        fm = QuestionForm(request.POST)
        if fm.is_valid():
            title = fm.cleaned_data['TiTLe']
            tag = fm.cleaned_data['Tag']
            cont = fm.cleaned_data['Content']
            user = request.user;
            db =questions( TiTLe=title, Tag =tag, Content =cont,user =user)
            db.save()
            return redirect("home")

    else:
         fm = QuestionForm()
      
    return render(request,'AskaQuestion.html',{'form' : fm})
    
def post_list(request):
     posts= questions.objects.all()
     context={
         'posts' : posts
     
     }
     return render(request, 'home.html',context)
     
def openchatbot(request):
	return render(request,'FAQ.html')

def bot_search(request):
    query = request.GET.get('query')

    
    try:
        client = wolframalpha.Client("<--Your API key-->")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'FAQ.html', {'ans': ans, 'query': query})

            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'FAQ.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'FAQ.html', {'ans': ans, 'query': query})	      	

	
def post_detail(request, id, slug):
       post = get_object_or_404(questions ,id=id, slug=slug)
       comments = Comment.objects.filter(post=post).order_by('-id')
       if request.method=='POST':
          comment_form = CommentForm(request.POST or None)
          if comment_form.is_valid():
              content = request.POST.get('content')
              comment= Comment.objects.create(post=post, user=request.user, content=content)
              comment.save()
              return redirect('home')
       else:
             comment_form= CommentForm()
     
       context={
                   'post' : post,    
                   'comment_form' : comment_form,
                   'comments' : comments,           
           }
       return render(request, 'reply.html', context)
           
       

 


     
    
    
  

    
