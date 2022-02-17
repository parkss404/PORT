from django.shortcuts import render,HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

userlist = [
        ["박성준" , "pkjjs5178", "pkjjs11@naver.com"],
        ["백하준" , "1234", "12112@naver.com"],
        ]   

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
    global userlist
    if request.method == 'GET':
        article = '''
          <form action="/login/" method="post">
                  <p><input type="text" name="name" placeholder="이름"></p>
                  <p><input type="text" name="pw" placeholder="PW"></p>
                  <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(logintemp(article))
    
    elif request.method == 'POST':
        name = request.POST['name']
        pw = request.POST['pw']

        for i in userlist:
            if(name == i[0] and pw == i[1]):

                return HttpResponse(home(name))
    
        else:
            return HttpResponse('''
            <h1>로그인 오류입니다.<h1>
            <h3><a href="/login">다시 시도</a></h3> 
            ''')


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
        <h2><a href ='/inproject'>PROJECTARCHIVE</a></h2>
        <h2><a href ='/idea'>IDEA</a></h2>
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
                <p><input type="text" name="pw" placeholder="PW"></p>
                <p><input type="text" name="email" placeholder="EMAIL"></p>
            <button><a href = '/login'>멤버등록하기</a></button>
            </form>
        '''     
        return HttpResponse(assigntemp(article))

    elif request.method == 'post':

        name = request.POST['name']
        pw = request.POST['pw']
        email = request.POST['email'] 
        
        single = [name,pw,email]

        userlist.append(single)

        return HttpResponse(request.POST['name'])  


def projectarchive(request):
    return HttpResponse(f'''
        <h1><h1>
        <h2><a href ='/DISPLAY'>DISPLAY</a></h2>
        <h2><a href ='/PROJECT PAGE'>PROJECT PAGE</a></h2>
        <h3>팀원일정</h3>
        <h3>팀원정보</h3>
    ''')


def inproject(request):
    return HttpResponse(f'''
        <h1><h1>
        <h2><a href ='/DISPLAY'></a></h2>
        <h2><a href ='/PROJECT PAGE'>PROJECT PAGE</a></h2>
        <h3>팀원일정</h3>
        <h3>팀원정보</h3>
        <h4><a href = '/' >진행 중인 프로젝트</h4>
        <h4><a href = '/' > 프로젝트</h4>
        <h5>+ 더보기</h5>
        <h3><a href = '/'>프로젝트 시작하기<h3>
        <h4>완료 프로젝트</h4>
    ''')

