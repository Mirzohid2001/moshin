// Основной JavaScript файл для Isomer Oil

document.addEventListener('DOMContentLoaded', function() {
    
    // Плавная прокрутка для навигации
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Анимация появления элементов при прокрутке
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Наблюдение за элементами для анимации
    const animateElements = document.querySelectorAll('.card, .capability-item, .product-card');
    animateElements.forEach(el => {
        observer.observe(el);
    });

    // Изменение навигации при прокрутке
    let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
        
        lastScrollTop = scrollTop;
    });

    // Анимация счетчиков
function animateCounters() {
    const counters = document.querySelectorAll('.counter, .stat-number');
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000; // 2 секунды
        const increment = target / (duration / 16); // 60 FPS
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                // Простое отображение числа без форматирования
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                // Финальное значение
                counter.textContent = target;
            }
        };
        
        updateCounter();
    });
}

    // Запуск анимации счетчиков при появлении
    const counterSection = document.querySelector('.counters-section');
    if (counterSection) {
        const counterObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounters();
                    counterObserver.unobserve(entry.target);
                }
            });
        });
        counterObserver.observe(counterSection);
    }

    // Плавная прокрутка для кнопок "Наверх"
    const scrollToTopBtn = document.querySelector('.scroll-to-top');
    if (scrollToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                scrollToTopBtn.classList.add('show');
            } else {
                scrollToTopBtn.classList.remove('show');
            }
        });

        scrollToTopBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Валидация форм
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('Пожалуйста, заполните все обязательные поля', 'error');
            }
        });
    });

    // Уведомления
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} alert-dismissible fade show notification`;
        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Автоматическое удаление через 5 секунд
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    // Анимация загрузки страницы
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
    });

    // Интерактивная карта (если есть)
    const mapContainer = document.querySelector('.map-container');
    if (mapContainer) {
        // Здесь можно добавить код для интерактивной карты
        console.log('Map container found');
    }

    // Фильтрация продуктов
    const filterButtons = document.querySelectorAll('.filter-btn');
    const productItems = document.querySelectorAll('.product-item');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            
            // Удаляем активный класс со всех кнопок
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Добавляем активный класс к текущей кнопке
            this.classList.add('active');
            
            // Фильтруем продукты
            productItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                    item.classList.add('fade-in-up');
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // Модальные окна
    const modalTriggers = document.querySelectorAll('[data-bs-toggle="modal"]');
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', function() {
            const targetModal = document.querySelector(this.getAttribute('data-bs-target'));
            if (targetModal) {
                const modal = new bootstrap.Modal(targetModal);
                modal.show();
            }
        });
    });

    // Параллакс эффект для фона
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.parallax');
        
        parallaxElements.forEach(element => {
            const speed = element.getAttribute('data-speed') || 0.5;
            element.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });

    // Анимация текста
    function animateText(element) {
        const text = element.textContent;
        element.textContent = '';
        
        let i = 0;
        const typeWriter = () => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        typeWriter();
    }

    // Запуск анимации текста для заголовков
    const animatedTexts = document.querySelectorAll('.animate-text');
    animatedTexts.forEach(text => {
        const textObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateText(entry.target);
                    textObserver.unobserve(entry.target);
                }
            });
        });
        textObserver.observe(text);
    });

    // Консольное сообщение
    console.log('🚀 Isomer Oil website loaded successfully!');
    console.log('💡 For support, contact: info@isomeroil.uz');
});

// Дополнительные стили для анимаций
const additionalStyles = `
    .navbar-scrolled {
        background: rgba(26, 26, 26, 0.95) !important;
        backdrop-filter: blur(15px);
    }
    
    .notification {
        position: fixed;
        top: 100px;
        right: 20px;
        z-index: 1060;
        max-width: 400px;
    }
    
    .scroll-to-top {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: var(--gradient-secondary);
        border: none;
        border-radius: 50%;
        color: var(--primary-color);
        font-size: 1.2rem;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .scroll-to-top.show {
        opacity: 1;
        visibility: visible;
    }
    
    .scroll-to-top:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-lg);
    }
    
    .filter-btn.active {
        background: var(--gradient-secondary);
        color: var(--primary-color);
    }
    
    .loaded {
        opacity: 1;
    }
    
    body {
        opacity: 0;
        transition: opacity 0.5s ease;
    }
`;

// Добавляем стили в head
const styleSheet = document.createElement('style');
styleSheet.textContent = additionalStyles;
document.head.appendChild(styleSheet); 