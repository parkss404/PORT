from django.shortcuts import render,HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def main(request):
    return HttpResponse('''
    <html>
    <body>
        <h2>AlWAYS<br> ROOTING FOR <br> YOUR START - </h2>
        <img src = /img/triport.png>
        <h4><a href="/login">로그인을 해주세요.</a></h4>
        <h3><a href="/login">로그인을 해주세요.</a></h3>
    </body>
    ''')


@csrf_exempt
def login(request):
    global CERTIID
    if request.method == 'GET':
        article = '''
          <form action="/login/" method="post">
                  <p><input type="text" name="name" placeholder="이름"></p>
                  <p><input type="text" name="PW "placeholder="PW"></p>
                  <p><input type="submit"></p>
           </form>
        '''
        return HttpResponse(logintemp(article))
    
    elif request.method == 'POST':
        name = request.POST['name']
        return HttpResponse(home(name))
        


def logintemp(articler):

    return HttpResponse(f'''
    <body>    
            <h1>환영합니다<br>어서오세요.</h1>
                {articler}
            <h3><a href="/assign">멤버가입하기</a></h3>
        </body>
    ''')


def home(name):
    return HttpResponse(f'''
    <html>
    <body>    
        <a href ='/userpage'>{name}님 환영합니다.</a>
        <h2><a href ='/portfolio'>PORTFOLIO</a></h2>
        <h2><a href ='/projectarchive'>PROJECTARCHIVE</a></h2>
        <h2><a href ='/projectarchive'>IDEA</a></h2>
    </body>
    ''')


def assigntemp(card):
    return HttpResponse(f'''
    <html>
    <body>
        <h2>PORT 가입하기</h2><br>
        {card}
        <h3><a href ='/'>main으로</a></h3>
        <h3><a href ='/login'>로그인페이지로</a></h3>
        
    </body>
    ''')

def assign(request):

    if request.method == 'GET':
    article = '''
         <form action="/assign/" method="post">
            <p><input type="text" name="name" placeholder="이름"></p>
            <p><input type="text" pw="pw" placeholder="PW"></p>
            <p><input type="text" email="email" placeholder="EMAIL"></p>
            <button><a href = '/login'>멤버등록하기</a></button>
        </form>
        '''     
        return HttpResponse(assigntemp(article))

    elif request.method == 'post':
        name = request.POST['name']
        pw = request.POST['pw']
        email = request.POST['email'] 
     return HttpResponse(request.POST['name'])  
