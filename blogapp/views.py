
# Create your views here.
from django.shortcuts import render,redirect
from .models import Category, Blog, Author
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
from django.core.paginator import Paginator




# Create your views here.
@login_required(login_url='/login')
def index(request):
    categories = Category.objects.all()
    blog = Blog.objects.all()
    #paginator =Paginator(blog,3)
    #page_number = request.GET.get('page')
    #blog_final_data = paginator.get_page(page_number)
    context = {
        'cats' : categories,
        'blogs':blog,   #(it is used for without paginator)     #'blog_final_data' :blog_final_data,
       
    }
    return render(request, 'index.html', context)



@login_required(login_url='/login')
def single(request, id):
    blog = Blog.objects.get(id=id)
    categories = Category.objects.all()
    allblog = Blog.objects.all()
    context = {
        'cats' : categories,
        'blogkey' : blog,
        'blog':allblog,
    }
    return render(request, 'blog-single.html',context)


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        uname = request.POST['uname']
        pswd1 = request.POST['password1']
        pswd2 = request.POST['password2']
        
        if pswd1 == pswd2:
            if User.objects.filter(username=uname).exists():
                messages.error(request,"Username allready exists")
                return redirect("/signup")  
            
            elif User.objects.filter(email=email).exists():
                 messages.error(request,"Email allready exists")
                 return redirect("/signup")  
            else:
                User.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=pswd1)    
                
                messages.error(request,"Your account created successfully")
                return redirect("/login")  
        else:
            messages.error(request,"passwords do not match")
            return redirect("/signup")  
        
    return render(request, 'signup.html')





def login(request):
    if request.method == 'POST':
        #DATA COLLECT FROM FORM
        uname = request.POST['uname']
        pswd = request.POST['password']
        
        #AUTHENTICATE THE USER WHETHER IT EXIST OR NOT
        user = auth.authenticate(request, username=uname, password=pswd)
        
        #if user authencticate hai mtlb kutch na kutch user mila h.
        if user is not None:
            auth.login(request, user=user)
            messages.success(request,"login successfully")
            return redirect("/") 
        else:
            messages.error(request,"Invalid crendential and try again")
            return redirect("/login")
    else:
        return render(request, 'login.html')
    
def logout(request):
    messages.success(request,"Logged out successfully!")
    auth.logout(request)
    return redirect('/login')


def author_reg(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        #fetch the category from form
       user_cat = request.POST['category']
       categori = Category.objects.get(name=user_cat)
       # fetch user from form that is (request.user) it is actrive user
       #crate auther objects ! category(from form) | user(request.user)
       new_author = Author(category=categori, user=request.user)# auther table has two fields category and user.
       new_author.save()
     
       messages.success(request,"You have successfully registered as auther. go to Dashboard for further details")
       return redirect("/")
   
    return render(request,'author_reg.html', {'categories':categories})


def author_dashboard(request):
    user = request.user
    authors = Author.objects.get(user=user)
    blog = Blog.objects.filter(author=authors)
    
    return render(request,'author_dashboard.html', {'blogs':blog})
    
    
def author_add_blog(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        
        #VALUE FETCHING
        title = request.POST['title'] 
        description = request.POST['description']
        cat = request.POST['category'] 
        categori = Category.objects.get(name=cat)
        image = request.FILES['image']
         
        
      #CREATE A BLOG OBJECT
        new_blog = Blog(title=title, description=description, category=categori, author=request.user.author,image=image)
        
        #SAVE THE OBJECT
        new_blog.save() 
        messages.success(request,"your blog has been  uploaded successfully")
        
        return redirect("/author_dashboard")
    return render(request,'author_add_blog.html',{'categories':categories})
    
    
    
def author_update_blog(request,pk):
    
    #FETCH THE OBJECTS THATS NEEDS TO BE EDITED
    blog = Blog.objects.get(id=pk)
    #categories = Category.objects.all()
    
    if request.method == 'POST':
        #VALUES FETCH FROM AUTHOR_UPDATE_BLOG OR USER
        title = request.POST['title'] 
        desc = request.POST['description']
       # categori = request.POST['category']
       # image = request.POST['image']
        
        #VALUES OVERWRITE
        blog.title = title
        blog.description = desc
        #blog.category = categori
        #blog.image = image
        
        #SAVES THE OBJECT
        blog.save()
        messages.success(request,"You have updated successfully")
        
        #REDIRECT TO DASHBOARD
        return redirect("/author_dashboard")
    context = {
        #'cats' : categories,
        'blogs' : blog
    }

    return render(request,'author_update_blog.html', context)
    
    
    
def author_delete_blog(request,pk):
    #FETCH THE BLOG
    blog = Blog.objects.get(id=pk)
    
    #DELETE THE BLOG
    blog.delete()
    messages.success(request,"your blog has been deleted successfully")
    
    #REDIRECT TO DASHBIARD
    return redirect("/author_dashboard")
    

    
def category_wise(request, name):
    
    #FETCH BLOGS WHERE CATEGORY MATCHES

    categori = Category.objects.get(name=name)
    
    blog = Blog.objects.filter(category =categori)
    #FILL THE CONTEXT WITH THESE blog

    #RENDER THE PAGE WITH THIS CONTEXT

    return render(request,'category_wise.html',{'blogs':blog, 'category':categori})
    
    
def search(request):
    if request.method=='POST':
        fetch = request.POST['searchapi']
        
    return render(request,'search.html')
   
   
def comments(request):
    

       return render(request,'comments.html')