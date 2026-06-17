// Initialize FullPage.js
document.addEventListener('DOMContentLoaded', function() {
    new fullpage('#fullpage', {
        // Navigation
        navigation: true,
        navigationPosition: 'right',
        navigationTooltips: ['프로필', '기술스택', '포트폴리오', '연락처'],
        
        // Scrolling
        scrollingSpeed: 700,
        autoScrolling: true,
        fitToSection: true,
        fitToSectionDelay: 1000,
        
        // Design
        sectionsColor: ['#667eea', '#f5f7fa', '#667eea', '#f5f7fa'],
        paddingTop: '80px',
        paddingBottom: '60px',
        
        // Accessibility
        keyboardScrolling: true,
        animateAnchor: true,
        recordHistory: true,
        
        // Responsive
        responsiveWidth: 0,
        responsiveHeight: 0,
        responsiveSlides: false,
        
        // Custom selectors
        sectionSelector: '.section',
        slideSelector: '.slide',
        
        // Events
        afterLoad: function(origin, destination, direction) {
            // Add animation class to section
            destination.item.classList.add('loaded');
            
            // Update active nav link
            updateActiveNavLink(destination.index);
        },
        
        onLeave: function(origin, destination, direction) {
            // Remove animation class from leaving section
            origin.item.classList.remove('loaded');
        }
    });
});

// Update active navigation link
function updateActiveNavLink(sectionIndex) {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = ['profile', 'techstack', 'portfolio', 'contact'];
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + sections[sectionIndex]) {
            link.classList.add('active');
        }
    });
}

// Smooth scroll for navigation links
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const sectionIndex = ['profile', 'techstack', 'portfolio', 'contact'].indexOf(targetId);
        
        if (sectionIndex !== -1) {
            fullpage_api.moveTo(sectionIndex + 1);
        }
    });
});

// Contact form submission
document.querySelector('.contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form data
    const formData = {
        name: this.querySelector('input[type="text"]').value,
        email: this.querySelector('input[type="email"]').value,
        subject: this.querySelector('input[type="text"]:nth-of-type(2)').value,
        message: this.querySelector('textarea').value
    };
    
    // Validate form
    if (!formData.name || !formData.email || !formData.subject || !formData.message) {
        alert('모든 필드를 작성해주세요.');
        return;
    }
    
    // Simulate form submission
    alert('메시지가 성공적으로 전송되었습니다!\n\n' +
          '이름: ' + formData.name + '\n' +
          '이메일: ' + formData.email + '\n' +
          '제목: ' + formData.subject + '\n' +
          '메시지: ' + formData.message);
    
    // Reset form
    this.reset();
});

// Add scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.tech-card, .portfolio-card, .contact-item').forEach(el => {
    observer.observe(el);
});

// Add animation classes dynamically
const style = document.createElement('style');
style.textContent = `
    .tech-card, .portfolio-card, .contact-item {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.6s ease;
    }
    
    .animate-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
    
    .loaded .tech-card,
    .loaded .portfolio-card,
    .loaded .contact-item {
        opacity: 1;
        transform: translateY(0);
    }
    
    .loaded .tech-card:nth-child(1),
    .loaded .portfolio-card:nth-child(1),
    .loaded .contact-item:nth-child(1) {
        transition-delay: 0.1s;
    }
    
    .loaded .tech-card:nth-child(2),
    .loaded .portfolio-card:nth-child(2),
    .loaded .contact-item:nth-child(2) {
        transition-delay: 0.2s;
    }
    
    .loaded .tech-card:nth-child(3),
    .loaded .portfolio-card:nth-child(3),
    .loaded .contact-item:nth-child(3) {
        transition-delay: 0.3s;
    }
    
    .loaded .tech-card:nth-child(4),
    .loaded .portfolio-card:nth-child(4),
    .loaded .contact-item:nth-child(4) {
        transition-delay: 0.4s;
    }
    
    .loaded .tech-card:nth-child(5),
    .loaded .portfolio-card:nth-child(5),
    .loaded .contact-item:nth-child(5) {
        transition-delay: 0.5s;
    }
    
    .loaded .tech-card:nth-child(6),
    .loaded .portfolio-card:nth-child(6),
    .loaded .contact-item:nth-child(6) {
        transition-delay: 0.6s;
    }
`;
document.head.appendChild(style);

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Add navbar scrolled style
const navbarStyle = document.createElement('style');
navbarStyle.textContent = `
    .navbar.scrolled {
        background: rgba(255, 255, 255, 0.98) !important;
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.15) !important;
    }
`;
document.head.appendChild(navbarStyle);

// Typing effect for profile section
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typing effect when profile section loads
const profileSection = document.getElementById('profile');
if (profileSection) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const h2 = entry.target.querySelector('h2');
                if (h2 && !h2.classList.contains('typed')) {
                    h2.classList.add('typed');
                    const originalText = h2.innerHTML;
                    typeWriter(h2, originalText, 50);
                }
            }
        });
    }, { threshold: 0.5 });
    
    observer.observe(profileSection);
}

// Parallax effect for profile image
document.addEventListener('mousemove', function(e) {
    const profileImage = document.querySelector('.profile-image');
    if (profileImage) {
        const x = (window.innerWidth / 2 - e.pageX) / 50;
        const y = (window.innerHeight / 2 - e.pageY) / 50;
        profileImage.style.transform = `translate(${x}px, ${y}px)`;
    }
});

// Add loading screen
window.addEventListener('load', function() {
    const loadingScreen = document.createElement('div');
    loadingScreen.id = 'loading-screen';
    loadingScreen.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner"></div>
            <p>Loading...</p>
        </div>
    `;
    document.body.appendChild(loadingScreen);
    
    // Add loading screen styles
    const loadingStyle = document.createElement('style');
    loadingStyle.textContent = `
        #loading-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            transition: opacity 0.5s ease, visibility 0.5s ease;
        }
        
        .loading-spinner {
            text-align: center;
            color: white;
        }
        
        .spinner {
            width: 50px;
            height: 50px;
            border: 5px solid rgba(255, 255, 255, 0.3);
            border-top-color: white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        #loading-screen.hidden {
            opacity: 0;
            visibility: hidden;
        }
    `;
    document.head.appendChild(loadingStyle);
    
    // Hide loading screen after content loads
    setTimeout(() => {
        loadingScreen.classList.add('hidden');
        setTimeout(() => {
            loadingScreen.remove();
        }, 500);
    }, 1000);
});

// Mobile menu handling
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

if (navbarToggler && navbarCollapse) {
    navbarToggler.addEventListener('click', function() {
        navbarCollapse.classList.toggle('show');
    });
    
    // Close menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function() {
            navbarCollapse.classList.remove('show');
        });
    });
}

// Add smooth reveal animations
const revealElements = document.querySelectorAll('.section-title, .profile-content, .contact-form');
revealElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
});

// Reveal elements when section loads
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(() => {
        revealElements.forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        });
    }, 500);
});
