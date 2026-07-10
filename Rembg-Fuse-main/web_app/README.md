# Rembg-Fuse Web Application

- Combined AI-powered background removal and color setting tool
- Modern, responsive web interface
- Production-ready deployment

## 🎯 Features

### Remove Background
- AI-powered background removal using multiple models
- Support for U2Net, ISNet, Silueta, and more
- Real-time processing
- Output as transparent PNG

### Set Background Color
- Apply custom colors to transparent images
- Color picker with presets
- Live preview
- Output as JPG with solid background

### User Interface
- Modern dark theme with gradient accents
- Drag & drop file upload
- Real-time preview
- Responsive design (mobile/tablet/desktop)
- Intuitive tab-based interface

## 📁 Project Structure

```
web_app/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css      # Styling
│   └── js/
│       └── main.js        # Frontend JavaScript
├── utils/
│   ├── config.py          # Configuration
│   ├── image_processor.py # Image utilities
│   └── __init__.py
└── uploads/               # Temporary file storage
```

## 🚀 Quick Start

### Development

```bash
# 1. Install dependencies
pip install -r web_app/requirements.txt

# 2. Run development server
python -m flask --app web_app.app run --debug

# 3. Open http://localhost:5000
```

### Production

```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# With environment variables
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

## 📦 Deployment Options

See [DEPLOYMENT.md](../DEPLOYMENT.md) for detailed deployment guides:

- Heroku
- Docker
- AWS EC2
- DigitalOcean
- Local Server with Nginx/Supervisor

## 🔧 Configuration

### Environment Variables
Copy `.env.example` to `.env` and update:

```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key
UPLOAD_FOLDER=./uploads
MAX_CONTENT_LENGTH=52428800  # 50MB
```

### Available Models
- `u2netp` - Fast, lightweight
- `u2net` - Standard, accurate
- `isnet-general-use` - High quality
- `silueta` - Lightweight

## 🌐 API Reference

### Remove Background
```bash
POST /api/remove-background
Content-Type: multipart/form-data

Parameters:
- file: image file (required)
- model: model name (optional, default: u2netp)

Response:
{
  "success": true,
  "message": "Background removed successfully",
  "download_filename": "removed_20250101_120000_image.png"
}
```

### Set Background Color
```bash
POST /api/set-background-color
Content-Type: multipart/form-data

Parameters:
- file: image file with transparency
- r: red value (0-255)
- g: green value (0-255)
- b: blue value (0-255)

Response:
{
  "success": true,
  "message": "Background color set successfully",
  "download_filename": "colored_20250101_120000_image.jpg",
  "color": "rgb(255, 255, 255)"
}
```

### Preview Color
```bash
POST /api/preview-color
Content-Type: multipart/form-data

Parameters:
- file: image file
- r, g, b: color values

Response:
PNG image (preview only, not saved)
```

### Available Models
```bash
GET /api/models

Response:
[
  {
    "name": "u2netp",
    "display": "U2Net-P (Fast)",
    "size": "4 MB"
  },
  ...
]
```

### Health Check
```bash
GET /api/health

Response:
{
  "status": "healthy",
  "timestamp": "2025-01-01T12:00:00",
  "tools": {
    "rembg": "ready",
    "color_setter": "ready"
  }
}
```

## 🎨 Customization

### Styling
Edit `static/css/style.css` to customize:
- Color scheme (CSS variables in :root)
- Fonts
- Layout
- Responsive breakpoints

### Frontend Logic
Modify `static/js/main.js` for:
- Form validation
- API calls
- UI interactions
- File handling

### Backend Processing
Update `app.py` to:
- Add new endpoints
- Modify processing logic
- Implement caching
- Add authentication

## 🔒 Security Features

- File upload validation
- Size limits (50MB max)
- Secure filename handling
- Automatic cleanup of old files (24 hours)
- CSRF protection ready
- Environment-based configuration

## ⚡ Performance Tips

1. **Use Nginx/Apache as reverse proxy**
2. **Enable gzip compression**
3. **Cache static files with CDN**
4. **Use multiple Gunicorn workers**
5. **Optimize image processing**
6. **Monitor disk usage** (cleanup old uploads)

## 📊 Monitoring

Check health:
```bash
curl http://localhost:5000/api/health
```

View logs:
```bash
# Development
tail -f flask.log

# Production
tail -f /var/log/rembg-fuse.log
```

## 🐛 Troubleshooting

### Issue: "Module not found"
```bash
pip install -r web_app/requirements.txt
```

### Issue: "Port already in use"
```bash
# Find and kill process
lsof -i :5000
kill -9 <PID>
```

### Issue: "Out of memory"
- Reduce worker count
- Implement image size limits
- Add swap space

### Issue: "Slow processing"
- Switch to faster model (u2netp)
- Check GPU availability
- Monitor system resources

## 📚 Advanced Configuration

### Docker Deployment
```bash
docker build -t rembg-fuse .
docker run -p 5000:5000 rembg-fuse
```

### Kubernetes Deployment
See deployment manifests in `k8s/` directory

### Multi-region Deployment
Use load balancer + multiple instances

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📝 License

MIT License - See LICENSE file

## 📞 Contact

- GitHub: [rembg-fuse](https://github.com/akascape/rembg-fuse)
- Issues: Report bugs and features
- Discussions: Ask questions and share ideas

---

**Version:** 1.0.0  
**Last Updated:** 2025-01-01  
**Python:** 3.8+  
**Status:** Production Ready ✅
