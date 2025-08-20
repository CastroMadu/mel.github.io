# EcoConecta - Descarte Eletrônico Consciente

## Overview

EcoConecta is a web application focused on promoting conscious electronic waste disposal practices. The application serves as an educational platform that connects users with sustainable practices for electronic waste management, supporting UN Sustainable Development Goals, particularly SDG 17 (Partnerships and Means of Implementation).

The application is built as a simple, informative website with three main pages: Home (INÍCIO), SDGs (ODS), and Practices (PRÁTICAS). It emphasizes environmental awareness and provides practical guidance for sustainable technology consumption.

## System Architecture

### Frontend Architecture
- **Framework**: Flask web application serving static HTML templates
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **Styling**: Custom CSS with modern design principles
- **JavaScript**: Vanilla JavaScript for interactive elements
- **Responsive Design**: Mobile-first approach with CSS Grid and Flexbox

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Structure**: Simple MVC pattern with routes defined in `app.py`
- **Session Management**: Flask session handling with secret key configuration
- **Deployment**: Gunicorn WSGI server for production deployment

### Key Design Principles
- **Color Scheme**: Green, white, and light gray palette reflecting environmental themes
- **Visual Elements**: Soft shadows, rounded corners, entrance animations
- **External Images**: Unsplash integration for high-quality environmental imagery
- **Accessibility**: Semantic HTML structure with proper navigation

## Key Components

### Application Structure
```
├── app.py              # Main Flask application with route definitions
├── main.py             # Entry point for deployment
├── templates/          # Jinja2 HTML templates
│   ├── base.html       # Base template with shared layout
│   ├── index.html      # Homepage template
│   ├── ods.html        # SDG information page
│   └── praticas.html   # Sustainable practices page
├── static/             # Static assets
│   ├── css/style.css   # Main stylesheet
│   └── js/script.js    # JavaScript functionality
└── pyproject.toml      # Python dependencies and project configuration
```

### Route Definitions
- **Home Route** (`/`): Landing page with environmental impact information
- **ODS Route** (`/ods`): Educational content about UN Sustainable Development Goals
- **Practices Route** (`/praticas`): Practical guidance for sustainable technology use

### Frontend Components
- **Navigation Bar**: Fixed header with responsive mobile menu
- **Hero Sections**: Full-width banners with background images and call-to-action content
- **Card Layouts**: Information cards with images, icons, and descriptive text
- **Interactive Elements**: Animated entrance effects using AOS (Animate On Scroll) library

## Data Flow

### Static Content Delivery
1. User requests page through browser
2. Flask application processes route and renders appropriate template
3. Template engine combines base layout with page-specific content
4. Static assets (CSS, JS, images) are served alongside HTML
5. Client-side JavaScript initializes animations and interactive features

### Content Structure
- **Educational Content**: Static information about electronic waste impact
- **Practice Guidelines**: Actionable steps for sustainable technology consumption
- **Resource Lists**: Fictional local electronic waste collection points
- **External Media**: Images sourced from Unsplash for visual impact

## External Dependencies

### Python Dependencies
- **Flask**: Web framework for application structure and routing
- **Flask-SQLAlchemy**: ORM for potential future database integration
- **Gunicorn**: Production WSGI server for deployment
- **psycopg2-binary**: PostgreSQL adapter for potential database features
- **email-validator**: Input validation utilities

### Frontend Libraries
- **Feather Icons**: Icon library for consistent visual elements
- **AOS (Animate On Scroll)**: Animation library for entrance effects
- **Google Fonts**: Poppins font family for typography
- **Unsplash**: External image hosting for environmental photography

### Infrastructure Dependencies
- **OpenSSL**: Security library for encrypted connections
- **PostgreSQL**: Database server (configured but not actively used)
- **Nix Package Manager**: Development environment management

## Deployment Strategy

### Development Environment
- **Python Version**: 3.11 with Nix environment management
- **Local Server**: Flask development server with debug mode enabled
- **Hot Reload**: Automatic application restart on code changes

### Production Deployment
- **Server**: Gunicorn with multi-worker configuration
- **Binding**: All interfaces (0.0.0.0) on port 5000
- **Scaling**: Autoscale deployment target for traffic management
- **Process Management**: Gunicorn handles worker processes and load balancing

### Configuration Management
- **Environment Variables**: Session secret key and other sensitive configuration
- **Static Assets**: Served directly through Flask in development
- **Template Caching**: Jinja2 template compilation for performance

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- June 23, 2025. Initial setup