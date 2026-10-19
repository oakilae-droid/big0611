# 홍길동 - Big Data Developer Portfolio

모던하고 세련된 개인 포트폴리오 웹사이트입니다. 빅데이터 1000시간 과정을 수료한 데이터 개발자의 프로필, 스킬, 포트폴리오, 연락처 정보를 담고 있습니다.

## 🚀 기술 스택

- **HTML5**: 시맨틱 마크업 및 구조
- **CSS3**: 모던 스타일링, 반응형 디자인, 애니메이션
- **JavaScript**: 인터랙티브 기능, 폼 처리, 스크롤 효과

## 📁 프로젝트 구조

```
my/
├── index.html          # 메인 HTML 파일
├── css/
│   └── style.css      # 외부 CSS 스타일시트
├── js/
│   └── script.js      # 외부 JavaScript 파일
├── images/
│   ├── subway.svg     # Subway 프로젝트 이미지
│   ├── movieflow.svg  # MovieFlow 프로젝트 이미지
│   └── recipe.svg     # Recipe 플랫폼 프로젝트 이미지
├── favicon.svg        # 파비콘
└── README.md          # 프로젝트 설명 파일
```

## 🎨 주요 기능

### 1. 반응형 디자인
- 모바일, 태블릿, 데스크톱 등 모든 디바이스에 최적화
- 모바일 메뉴 (햄버거 메뉴) 지원

### 2. 섹션 구성
- **Header**: 고정 네비게이션 바
- **Profile**: 개인 프로필 및 소개
- **Skills**: 기술 스킬 및 진척도
- **Portfolio**: 3개의 프로젝트 포트폴리오
- **Contact**: 연락처 폼
- **Footer**: 저작권 및 소셜 링크

### 3. 인터랙티브 기능
- 스무스 스크롤 네비게이션
- 스크롤 애니메이션 효과
- 스킬 바 애니메이션
- 호버 효과
- 모바일 메뉴 토글

### 4. 포트폴리오 프로젝트
- **Subway Data Analysis**: https://subwaykr.onrender.com
- **MovieFlow**: https://movieflowkr.onrender.com
- **Recipe Platform**: https://recipekr.onrender.com

## 📧 연락처 폼 설정 (Formspree)

연락처 폼은 Formspree 서비스를 사용하여 실제 이메일 전송 기능을 제공합니다.

### Formspree 설정 방법

1. **Formspree 계정 생성**
   - https://formspree.io/ 에서 무료 계정 생성
   - GitHub 계정으로 로그인 가능

2. **새 폼 생성**
   - 대시보드에서 "New Form" 클릭
   - 폼 이름 입력 (예: "Portfolio Contact")
   - 수신 이메일 주소 입력

3. **Form ID 복사**
   - 생성된 폼의 Form ID 복사
   - 형식: `https://formspree.io/f/YOUR_FORM_ID`

4. **HTML 파일 업데이트**
   - `index.html` 파일의 183번 라인에서 `YOUR_FORM_ID`를 실제 Form ID로 교체
   ```html
   <form action="https://formspree.io/f/YOUR_ACTUAL_FORM_ID" method="POST" class="contact-form" id="contactForm">
   ```

5. **테스트**
   - 로컬에서 웹사이트 실행 후 연락처 폼 테스트
   - Formspree 대시보드에서 전송된 메시지 확인

## 🚀 배포 가이드

### GitHub에 업로드

1. **Git 초기화**
   ```bash
   git init
   ```

2. **파일 스테이징**
   ```bash
   git add .
   ```

3. **커밋 생성**
   ```bash
   git commit -m "Initial portfolio website"
   ```

4. **GitHub 리포지토리 생성**
   - GitHub에서 새 리포지토리 생성
   - 리포지토리 이름: `portfolio` (또는 원하는 이름)

5. **GitHub에 푸시**
   ```bash
   git remote add origin https://github.com/USERNAME/REPOSITORY.git
   git branch -M main
   git push -u origin main
   ```

### Netlify에 배포

1. **Netlify 계정 생성**
   - https://www.netlify.com/ 에서 무료 계정 생성
   - GitHub 계정으로 연동

2. **새 사이트 생성**
   - Netlify 대시보드에서 "Add new site" > "Import an existing project"
   - GitHub 리포지토리 선택

3. **빌드 설정**
   - Build command: (비워둠 - 정적 사이트이므로 빌드 불필요)
   - Publish directory: `.` (루트 디렉토리)

4. **배포**
   - "Deploy site" 클릭
   - 자동으로 배포 완료

5. **도메인 설정** (선택사항)
   - Netlify에서 무료 도메인 제공
   - 또는 개인 도메인 연결 가능

## 🎨 커스터마이징

### 개인 정보 수정
- `index.html` 파일에서 이름, 이메일, 전화번호 등 개인 정보 수정
- 프로필 설명과 스킬 내용을 본인에 맞게 변경

### 색상 변경
- `css/style.css` 파일의 `:root` 변수에서 색상 수정
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f093fb;
    /* ... */
}
```

### 포트폴리오 추가/수정
- `index.html`의 Portfolio 섹션에서 프로젝트 추가/수정
- `images/` 폴더에 새로운 프로젝트 이미지 추가

## 📱 브라우저 호환성

- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저 (iOS Safari, Chrome Mobile)

## 🌐 라이브 데모

배포 후 다음 주소에서 웹사이트 확인:
- Netlify 제공 도메인: `https://YOUR-SITE.netlify.app`

## 📄 라이선스

이 프로젝트는 개인 포트폴리오 용도로 제작되었습니다.

## 👤 연락처

- **이름**: 홍길동
- **이메일**: honggildong@email.com
- **전화번호**: 010-1234-5678
- **GitHub**: https://github.com/honggildong
- **LinkedIn**: https://linkedin.com/in/honggildong

---

**제작일**: 2026년  
**버전**: 1.0.0
