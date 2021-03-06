from django.shortcuts import render,redirect
from signin.models import UserProfile                   #neww222
from signin.forms import ExtendedUserCreationForm, UserProfileForm #neww222
from .models import Post,Item,quantity,orders
from django.db.models import Q
# Create your views here.
from django.views.generic import ListView, DetailView, View
from .forms import ser_req
from .forms import buy,number
from django.core.paginator import Paginator

#for email
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def req(request):
    aut=request.user.username
    current_user=request.user
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    if request.method == "POST":
        form = ser_req(request.POST,initial={'aut':aut,'flat_number':flat_number})
        if form.is_valid():
            form.save()
            return redirect('email')    
    else:
        form = ser_req(initial={'aut':aut,'flat_number':flat_number})
    context = {
        'form':form
    }
    return render(request, 'Ask_form.html', context)
    

@login_required
def serv_mail(request):    

    current_user=request.user
    mail=request.user.email
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    x=str(flat_number)
    
    mobile_number=obj.mobile_number
    y=str(mobile_number)
    
    
    obj2=Post.objects.last()
    msg=obj2.body
    p=str(msg)

    mg=obj2.time
    s=str(mg)
    
    z="flat number :"+x+"\n"+"mobile number  :"+y+"\n"+"problem: "+p+"\n"+"Time: "+s

    subject = 'Service request posted'
    message=z
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['aalwinarakkal@gmail.com',mail] 
    send_mail( subject, message, email_from, recipient_list )    
    return redirect('show')

@login_required
def shopmail(request):    
    
    current_user=request.user
    mail=request.user.email
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    x=str(flat_number)
    
    mobile_number=obj.mobile_number
    y=str(mobile_number)
    
    # obj2=Post.objects.filter(aut=current_user).order_by('created')[:1]
    obj2=Item.objects.last()
    if(obj2.bread):

        sel1=str(obj2.bread)
       
        b= sel1+ " PACKET BREAD "+"\n"
    else:
        b=""
    if(obj2.water):
        sel2=str(obj2.water)
       
        w=sel2+ " CAN WATER ,"+"\n"
    else:
        w=""
    
    if(obj2.milk):

        sel3=str(obj2.milk)
        
        m=sel3+  " PACKET MILK "+"\n"
       
    else:
        m=""
    if(obj2.rice):

        sel4=str(obj2.rice)
        
        r=sel4+" kg RICE "+"\n"
       
    else:
        r=""
    
    z="FLAT NUMBER :"+x+"\n"+"MOBILE NUMBER :"+y+"\n"
    
    
    shoppinglist=(z+" ITEM LIST :"+"\n"+b+w+m+r)
    
    context = {
        'details':shoppinglist
    }
    
    
   #email details---

    subject = 'You have orders'
    message=shoppinglist
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['aalwinarakkal@gmail.com',mail] 
    print (obj2.bread or obj2.bread )
    if (obj2.bread or obj2.water or obj2.milk or obj2.rice):
        send_mail( subject, message, email_from, recipient_list )    
    
   
    
    return redirect('list')

@login_required
def Myreqview(request):              #display service requests

   
    req=Post.objects.all().order_by('-created')
    aut=request.user.username
    info=[]
    for x in req:
        y={'flnum':x.created,'aut':x.aut,'aut2':aut}
        info.append(y)
    
   
    paginator=Paginator(info,5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        info = paginator.page(page)
    except(EmptyPage, InvalidPage):
        info=paginator.page(paginator.num_pages)

    context={
            'info':info,
            
        }   
    return render(request,'show.html',context)

class ServiceListView(ListView):
    model = Post
    template_name = 'show2.html'

    def get_queryset(self):

        category5= self.kwargs.get('category')
    
        return Post.objects.filter(created=category5)
@login_required
def MyView(request):                #display ordered items

    query_results = Item.objects.all().order_by('-created')
    q = quantity.objects.all()
    aut=request.user.username

   
    # paginator=Paginator(query_results,5)
    # try:
    #     page = int(request.GET.get('page','1'))
    # except:
    #     page = 1
    # try:
    #     query_results = paginator.page(page)
    # except(EmptyPage, InvalidPage):
    #     query_results=paginator.page(paginator.num_pages)
    #                                                     #/pagination
    context = {
        'details':query_results,
        'aut':aut,
        'quantity':q
    }
    print (q)
    # return render(request, 'display.html',context)
    return render(request, 'neworders.html',context)


@login_required
def residents(request): 
    tenants=UserProfile.objects.all()
    info=[]
    for x in tenants:
        y={'flnum':x.flat_number}
        info.append(y)
    
    context={
            'info':info
        }    
    return render(request,'residents.html',context)



class CategoryListView(ListView):
    model = UserProfile
    template_name = 'residents_info.html'

    def get_queryset(self):

        category = self.kwargs.get('category')
    
        return UserProfile.objects.filter(flat_number=category)




@login_required
def shop(request):                                             
    # aut=request.user.username
    # current_user=request.user
    # obj=UserProfile.objects.get(user=current_user)
    # flat_number=obj.flat_number
    # items = orders.objects.all()
    # if request.method == "POST":
    #     form = buy(request.POST,initial={'aut':aut,'flat_number':flat_number})     #neww for admin login
    #     form2= number(request.POST)
    #     print (form2)
    #     print("--------------------------------------------------------------------------")
    #     print(form)
       
    #     if form.is_valid() and form2.is_valid():
            
    #         form.save()

    #         print(form)
    #         form2.save()
    #         print(form2)
    #         # return redirect('gmail')
    #         return redirect('index')
    # else:
    #     form = buy(initial={'aut':aut,'flat_number':flat_number})
    #     form2= number(request.POST)
    # context = {
        # 'form':form,'form2':form2,
    #     'items':items
    # }
    # return render(request, 'buy2.html', context)
    # return render(request, 'buynew.html', context)
    

    item=orders.objects.all()
    aut=request.user.username
    info=[]
    for x in item:
        y={'item':x.item1}
        info.append(y)
    print (info)

    context={
            'info':info,
            
        }   
    print (info)
    return render(request,'buynew.html',context)


   
    # paginator=Paginator(info,5)
    # try:
    #     page = int(request.GET.get('page','1'))
    # except:
    #     page = 1
    # try:
    #     info = paginator.page(page)
    # except(EmptyPage, InvalidPage):
    #     info=paginator.page(paginator.num_pages)

    

@login_required
def buynow(request):                                             
    aut=request.user.username
    current_user=request.user
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    items = orders.objects.all()
    if request.method == "POST":
        form = buy(request.POST,initial={'aut':aut,'flat_number':flat_number})     #neww for admin login
        form2= number(request.POST)
        print (form2)
        print("--------------------------------------------------------------------------")
        print(form)
       
        if form.is_valid() and form2.is_valid():
            
            form.save()
            form2.save()
            # return redirect('gmail')
            return redirect('index')
    else:
        form = buy(initial={'aut':aut,'flat_number':flat_number})
        form2= number(request.POST)
    context = {
        'form':form,'form2':form2,
        'items':items
    }
    return render(request, 'buydeatiled.html', context)


# class BuyListView(ListView):
#     model = quantity
#     template_name = 'buydeatiled.html'

#     # def get_queryset(self):

#     #     category5 = self.kwargs.get('category')
#     #     return quantity.objects.filter( t=category5 )


#     def get_context_data(self, **kwargs) :
#         context = super(BuyListView, self).get_context_data(**kwargs)
#         context['form'] = number()
#         # context['form2'] =buy() 
#         return context



def exp(request,category):
    aut=request.user.username
    current_user=request.user
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    context = {
        'form1':number(request.POST),
        'form2':buy(request.POST),
        'cat':category,
        'aut':aut,
        'flat':flat_number
    }
    print(category)
    return render (request,'buydeatiled.html',context)

