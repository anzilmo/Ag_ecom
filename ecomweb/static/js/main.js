// Add scroll animations
        document.addEventListener('DOMContentLoaded', function() {
            const featureCards = document.querySelectorAll('.feature-card');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = 1;
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, { threshold: 0.1 });
            
            featureCards.forEach((card, index) => {
                card.style.opacity = 0;
                card.style.transform = 'translateY(50px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                card.style.transitionDelay = `${index * 0.1}s`;
                observer.observe(card);
            });
        });



        // cart javascripet

        // ===== JavaScript =====
document.addEventListener('DOMContentLoaded', function() {
    // Filtering functionality
    const filterButtons = document.querySelectorAll('.filter-btn');
    const carCards = document.querySelectorAll('.car-card');
    
    // Initialize Isotope if filter buttons exist
    if (filterButtons.length > 0) {
        // Create filter buttons container (dynamically added in JS)
        const filterContainer = document.createElement('div');
        filterContainer.className = 'filter-container';
        
        // Add filter buttons
        const filters = ['all', 'sports', 'luxury', 'convertible', 'coupe'];
        filters.forEach(filter => {
            const button = document.createElement('button');
            button.className = 'filter-btn';
            button.dataset.filter = filter;
            button.textContent = filter.charAt(0).toUpperCase() + filter.slice(1);
            filterContainer.appendChild(button);
        });
        
        // Insert filter container before car container
        document.querySelector('h1').insertAdjacentElement('afterend', filterContainer);
        
        // Set default active filter
        document.querySelector('.filter-btn[data-filter="all"]').classList.add('active');
        
        // Add event listeners to filter buttons
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                // Update active button
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                
                const filterValue = this.dataset.filter;
                
                // Filter cars
                carCards.forEach(card => {
                    if (filterValue === 'all' || card.dataset.category.includes(filterValue)) {
                        card.style.display = 'block';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, 10);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300);
                    }
                });
            });
        });
    }
    
    // Add hover effect with delay
    carCards.forEach(card => {
        let hoverTimer;
        
        card.addEventListener('mouseenter', () => {
            clearTimeout(hoverTimer);
            hoverTimer = setTimeout(() => {
                card.style.transform = 'translateY(-10px)';
            }, 100);
        });
        
        card.addEventListener('mouseleave', () => {
            clearTimeout(hoverTimer);
            card.style.transform = 'translateY(0)';
        });
    });
    
    // Add data-category attributes to cards (for filtering demo)
    // In a real implementation, these would come from your backend
    document.querySelectorAll('.car-card').forEach((card, index) => {
        const categories = [
            'sports luxury',
            'sports convertible',
            'luxury coupe',
            'sports',
            'luxury convertible'
        ];
        card.dataset.category = categories[index % categories.length];
    });
});