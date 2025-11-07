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

    // Анимации по data-атрибутам
    const animatedNodes = document.querySelectorAll('[data-animate]');
    if (animatedNodes.length) {
        const animationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    animationObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -80px 0px'
        });

        animatedNodes.forEach(node => {
            const animation = node.getAttribute('data-animate') || 'fade-up';
            node.classList.add('animate-item', `animate-${animation}`);

            const delay = node.getAttribute('data-delay');
            if (delay) {
                node.style.setProperty('--animation-delay', delay);
            }

            animationObserver.observe(node);
        });
    }

    // Изменение навигации при прокрутке
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

            if (scrollTop > 100) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        }, { passive: true });
    }

    // Интерактивное свечение карточек
    const interactiveCards = document.querySelectorAll('.interactive-card');
    if (interactiveCards.length) {
        const setGlow = (card, x, y, intensity = 0.8) => {
            card.style.setProperty('--mouse-x', `${x}%`);
            card.style.setProperty('--mouse-y', `${y}%`);
            card.style.setProperty('--glow-opacity', intensity);
        };

        const resetGlow = (card) => {
            card.style.setProperty('--glow-opacity', '0');
        };

        interactiveCards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.setProperty('--glow-opacity', '0.4');
            });

            card.addEventListener('mousemove', (event) => {
                const bounds = card.getBoundingClientRect();
                const x = ((event.clientX - bounds.left) / bounds.width) * 100;
                const y = ((event.clientY - bounds.top) / bounds.height) * 100;
                setGlow(card, x, y);
            });

            card.addEventListener('mouseleave', () => {
                resetGlow(card);
            });

            card.addEventListener('touchmove', (event) => {
                const touch = event.touches[0];
                if (!touch) {
                    return;
                }
                const bounds = card.getBoundingClientRect();
                const x = ((touch.clientX - bounds.left) / bounds.width) * 100;
                const y = ((touch.clientY - bounds.top) / bounds.height) * 100;
                setGlow(card, x, y, 0.7);
            }, { passive: true });

            card.addEventListener('touchend', () => {
                resetGlow(card);
            });
        });
    }

    // Анимация счетчиков
    const animateCounters = () => {
        const counters = document.querySelectorAll('.counter, .stat-number');
        counters.forEach(counter => {
            const target = parseInt(counter.getAttribute('data-target'), 10);
            if (Number.isNaN(target)) {
                return;
            }

            const duration = 2000; // 2 секунды
            const increment = target / (duration / 16); // ~60 FPS
            let current = 0;

            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    counter.textContent = Math.floor(current).toLocaleString('ru-RU');
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.textContent = target.toLocaleString('ru-RU');
                }
            };

            updateCounter();
        });
    };

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
    }, { passive: true });

    // Интерактивный параллакс в hero
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        const parallaxLayers = heroSection.querySelectorAll('[data-parallax]');

        const handleParallax = (event) => {
            const bounds = heroSection.getBoundingClientRect();
            const relativeX = (event.clientX - bounds.left) / bounds.width - 0.5;
            const relativeY = (event.clientY - bounds.top) / bounds.height - 0.5;

            parallaxLayers.forEach(layer => {
                const depth = parseFloat(layer.getAttribute('data-parallax')) || 10;
                const translateX = relativeX * depth;
                const translateY = relativeY * depth;
                layer.style.transform = `translate3d(${translateX}px, ${translateY}px, 0)`;
            });
        };

        heroSection.addEventListener('mousemove', handleParallax);
        heroSection.addEventListener('mouseleave', () => {
            parallaxLayers.forEach(layer => {
                layer.style.transform = 'translate3d(0, 0, 0)';
            });
        });
    }

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