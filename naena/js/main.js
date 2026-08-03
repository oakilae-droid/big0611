document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Hamburger Menu Toggle
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navLinks = document.querySelectorAll('.navbar-custom .nav-link');

    if (navbarToggler && navbarCollapse) {
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 992) {
                    navbarToggler.click(); // Close collapse on link click on mobile
                }
            });
        });
    }

    // 2. Intersection Observer for Fade-in Scroll Animations
    const fadeSections = document.querySelectorAll('.fade-in-section');
    const sectionObserverOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -100px 0px'
    };

    const sectionObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Animates only once
            }
        });
    }, sectionObserverOptions);

    fadeSections.forEach(section => {
        sectionObserver.observe(section);
    });

    // 3. Active Nav Link Highlighting on Scroll
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.navbar-custom .nav-link');

    const highlightNavLink = () => {
        let scrollY = window.pageYOffset;
        
        sections.forEach(current => {
            const sectionHeight = current.offsetHeight;
            const sectionTop = current.offsetTop - 150; // offset for navbar height
            const sectionId = current.getAttribute('id');
            
            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navItems.forEach(item => {
                    item.classList.remove('active');
                    if (item.getAttribute('href') === `#${sectionId}`) {
                        item.classList.add('active');
                    }
                });
            }
        });
    };

    window.addEventListener('scroll', highlightNavLink);
    highlightNavLink(); // Run once initially

    // 4. Contact Form Web3Forms Submission & Validation
    const contactForm = document.getElementById('contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Basic validation
            const name = document.getElementById('name').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const message = document.getElementById('message').value.trim();
            
            if (!name || !phone || !message) {
                e.preventDefault();
                alert('모든 입력란을 작성해주세요.');
                return;
            }
            
            // Simple Korean Phone regex check
            const phoneRegex = /^01[0-9]-?[0-9]{3,4}-?[0-9]{4}$/;
            if (!phoneRegex.test(phone)) {
                e.preventDefault();
                alert('올바른 전화번호 형식(예: 010-1234-5678)을 입력해 주세요.');
                return;
            }
            
            // Allow default submission to Web3Forms
        });
    }
});
