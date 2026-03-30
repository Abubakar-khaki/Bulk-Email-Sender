# 📧 Bulk Email Sender Pro - Modern PWA Edition

> Advanced bulk email sending platform with PWA support, real-time analytics, and enterprise features

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![React](https://img.shields.io/badge/React-18.2-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi)
![PWA](https://img.shields.io/badge/PWA-Ready-blueviolet)

## ✨ Features

### 🎯 Core Features
- **Campaign Management** - Create, schedule, and send email campaigns
- **Contact Groups** - Organize and manage recipient lists
- **Email Templates** - Pre-built templates with variables
- **Real-time Analytics** - Track opens, clicks, and engagement
- **Bulk Import** - CSV/JSON contact uploads

### 📱 PWA Capabilities
- ✅ **Offline Support** - Works without internet connection
- ✅ **Installable** - Add to home screen on mobile & desktop
- ✅ **Push Notifications** - Real-time campaign updates
- ✅ **Background Sync** - Emails queue offline, send when online
- ✅ **Service Workers** - Fast loading & caching strategies
- ✅ **Web App Manifest** - Native app-like experience

### 🚀 Enterprise Features
- **Authentication & Authorization** - Secure user accounts
- **Email Scheduling** - Schedule campaigns for future delivery
- **Retry Logic** - Automatic retries for failed emails
- **Rate Limiting** - Protect your sending reputation
- **Webhooks** - Integrate with external systems
- **Audit Logs** - Track all activities
- **A/B Testing** - Test subject lines and content
- **WebSocket Updates** - Real-time progress tracking

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Zustand** - State management
- **Workbox** - Service worker tooling
- **Axios** - HTTP client

### Backend
- **FastAPI** - Python web framework
- **SQLAlchemy** - ORM
- **PostgreSQL** - Database
- **Redis** - Caching & queues
- **Celery** - Async tasks
- **WebSocket** - Real-time updates

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose (optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Abubakar-khaki/Bulk-Email-Sender.git
cd Bulk-Email-Sender
git checkout modern-pwa-redesign
```

2. **Setup Backend**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations (if using Alembic)
alembic upgrade head

# Start the server
python -m uvicorn backend.main:app --reload
```

3. **Setup Frontend**
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

### Using Docker

```bash
# Copy environment file
cp .env.example .env

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:5173
# Backend: http://localhost:8000
# Docs: http://localhost:8000/docs
```

## 📖 Usage

### Creating a Campaign

1. Log in to your account
2. Click "New Campaign"
3. Fill in campaign details:
   - Campaign name
   - Email subject
   - Email content
4. Select recipients or contact group
5. Preview email
6. Schedule or send immediately

### Managing Templates

1. Go to "Templates" section
2. Create new template with variables
3. Use in campaigns for quick sending

### Viewing Analytics

- Track email delivery status
- Monitor open rates
- View click-through rates
- Export reports

## 🌐 PWA Installation

### On Mobile (iOS/Android)
1. Open the app in a browser
2. Tap Share → Add to Home Screen
3. The app is now installed

### On Desktop (Windows/Mac/Linux)
1. Open the app in Chrome, Edge, or similar
2. Click Install button in address bar
3. The app is now installed

### Offline Usage
- All previously loaded data is cached
- View campaign history offline
- Queue emails to send when online
- Receive notifications of completion

## 🔐 Security

- **JWT Authentication** - Secure token-based auth
- **Password Hashing** - Bcrypt with salt
- **HTTPS** - TLS encryption
- **CORS** - Cross-origin protection
- **Rate Limiting** - Prevent abuse
- **SQL Injection Prevention** - Parameterized queries
- **XSS Protection** - Content sanitization

## 📊 API Documentation

Interactive API docs available at: `http://localhost:8000/docs`

### Key Endpoints

```
POST   /api/auth/register          - Register new user
POST   /api/auth/login             - Login user
GET    /api/campaigns              - List campaigns
POST   /api/campaigns              - Create campaign
PUT    /api/campaigns/{id}         - Update campaign
DELETE /api/campaigns/{id}         - Delete campaign
POST   /api/campaigns/{id}/send    - Send campaign
GET    /api/campaigns/{id}/analytics - Get analytics
```

## 🧪 Testing

```bash
# Run backend tests
pytest

# Run frontend tests
npm run test

# Run e2e tests
npm run test:e2e
```

## 📦 Deployment

### Heroku
```bash
git push heroku modern-pwa-redesign:main
```

### AWS/DigitalOcean
See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions

### Docker
```bash
docker build -t bulk-email-sender .
docker run -p 8000:8000 bulk-email-sender
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📖 [Documentation](./docs)
- 💬 [GitHub Issues](https://github.com/Abubakar-khaki/Bulk-Email-Sender/issues)
- 📧 [Email Support](mailto:support@example.com)

## 🗺️ Roadmap

- [ ] AI-powered email content suggestions
- [ ] Multi-language support
- [ ] Advanced segmentation
- [ ] Deliverability optimization
- [ ] Mobile app (React Native)
- [ ] GraphQL API
- [ ] Real-time collaboration

## 🎉 Acknowledgments

Built with ❤️ using modern web technologies. Special thanks to the open-source community!