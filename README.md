# BTTZ  

## A sleek yet chill social app powered by Django  

---  
.
├── core/                    # Django 프로젝트의 메인 설정 앱 (settings.py, urls.py 등)
│
├── post/                    # 게시글(Post) 기능을 담당하는 앱
│
├── user/                    # 사용자(User) 인증 및 회원가입 기능을 담당하는 앱
│
├── templates/              # 전역 HTML 템플릿 폴더 (base.html, navbar.html 등 공통 요소)
│
├── static/                 # 정적 파일(css, js, image 등) 저장 폴더
│
├── manage.py               # Django 프로젝트 명령어 실행용 엔트리포인트
│
├── requirements.txt        # 프로젝트 의존 패키지 목록
│
├── .gitignore              # Git에서 제외할 파일/폴더 목록
│
└── README.md               # 프로젝트 설명 문서
  
#### 주요 기능  
- 사용자 관리 : 회원가입, 로그인/로그아웃 기능 제공  
- 게시글 작성 및 관리 : 게시글 작성, 수정, 삭제 기능  
- 정적 파일 관리 : CSS, JS 등 정적 파일 포함  
- 템플릿 사용 : HTML 템플릿 기반 동적 웹 페이지 제공