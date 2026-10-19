// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Header scroll effect
const header = document.querySelector('.header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    }
    
    lastScroll = currentScroll;
});

// Scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Add fade-in class to elements
document.querySelectorAll('.skill-card, .portfolio-card, .contact-item').forEach(el => {
    el.classList.add('fade-in');
    observer.observe(el);
});

// Skill bar animation
const skillBars = document.querySelectorAll('.skill-progress');
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const width = entry.target.style.width;
            entry.target.style.width = '0';
            setTimeout(() => {
                entry.target.style.width = width;
            }, 100);
        }
    });
}, { threshold: 0.5 });

skillBars.forEach(bar => skillObserver.observe(bar));

// Contact form handling
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(contactForm);
    const submitBtn = contactForm.querySelector('.submit-btn');
    const originalText = submitBtn.textContent;
    
    submitBtn.textContent = '전송 중...';
    submitBtn.disabled = true;
    
    try {
        const response = await fetch(contactForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });
        
        if (response.ok) {
            formMessage.textContent = '메시지가 성공적으로 전송되었습니다!';
            formMessage.className = 'form-message success';
            contactForm.reset();
        } else {
            formMessage.textContent = '전송 중 오류가 발생했습니다. 다시 시도해 주세요.';
            formMessage.className = 'form-message error';
        }
    } catch (error) {
        formMessage.textContent = '전송 중 오류가 발생했습니다. 다시 시도해 주세요.';
        formMessage.className = 'form-message error';
    }
    
    submitBtn.textContent = originalText;
    submitBtn.disabled = false;
    
    setTimeout(() => {
        formMessage.style.display = 'none';
    }, 5000);
});

// Active navigation link highlighting
const sections = document.querySelectorAll('section');
const navItems = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === `#${current}`) {
            item.classList.add('active');
        }
    });
});

// Typing effect for profile subtitle (optional enhancement)
const profileSubtitle = document.querySelector('.profile-subtitle');
if (profileSubtitle) {
    const text = profileSubtitle.textContent;
    profileSubtitle.textContent = '';
    let i = 0;
    
    function typeWriter() {
        if (i < text.length) {
            profileSubtitle.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    }
    
    // Start typing effect after page load
    setTimeout(typeWriter, 500);
}

// Parallax effect for profile section
window.addEventListener('scroll', () => {
    const profileSection = document.querySelector('.profile-section');
    const scrolled = window.pageYOffset;
    
    if (profileSection && scrolled < window.innerHeight) {
        profileSection.style.backgroundPositionY = scrolled * 0.5 + 'px';
    }
});

// Add loading animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});

// Portfolio card hover effect enhancement
document.querySelectorAll('.portfolio-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// Skill card hover effect enhancement
document.querySelectorAll('.skill-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) rotateX(5deg)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) rotateX(0)';
    });
});

// Dynamic year in footer
const footerYear = document.querySelector('.footer-text');
if (footerYear) {
    const currentYear = new Date().getFullYear();
    footerYear.textContent = footerYear.textContent.replace('2024', currentYear);
}
