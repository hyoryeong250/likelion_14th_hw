from django.shortcuts import render

# Create your views here.


def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {                           
            'HTML': 'templates/앱이름/ 경로에 HTML 파일을 생성한다',
            'View': 'views.py에서 함수를 정의하고 render을 통해 HTML을 반환한다',
            'URL': 'urls.py에서 특정 경로와 View 함수를 연결하고 name으로 별명을 지정한다'
        },
        'shortcuts': [
            '변수/반복문: {{변수}}로 데이터를 출력하고, {% for %}문으로 리스트 데이터를 반복 출력한다',
            '템플릿 상속: 중복되는 HTML구조를 base.html에 작성하고, {% extends %}와 {% block % }을 사용하여 효율적으로 관리한다',
            '파일 분리: {% include %}를 사용해 navbar 같은 공통 요소를 별도 파일로 분리할 수 있다'
        ]
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')
