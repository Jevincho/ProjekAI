"""
Rembg-Fuse Web Application
A complete web application combining background removal and color setting

Author: Your Team
License: MIT License
Version: 1.0
"""

from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import sys
import logging
from datetime import datetime
from pathlib import Path
import io
from PIL import Image
import threading

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Rembg.bg_remover import FuseBackgroundRemover
from BGSetter.bg_setter import BackgroundColorSetter
from web_app.utils.config import Config
from web_app.utils.image_processor import ImageProcessor

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global objects for background processing
bg_remover = None
color_setter = None
processor = None
tools_initialized = False

def initialize_tools():
    """Initialize background removal and color setting tools"""
    global bg_remover, color_setter, processor, tools_initialized
    if tools_initialized:
        return
    
    try:
        logger.info("Initializing tools...")
        color_setter = BackgroundColorSetter()
        processor = ImageProcessor(app.config['UPLOAD_FOLDER'])
        
        # Try to load the defult model for bg_remover
        try:
            bg_remover = FuseBackgroundRemover('u2netp')
            logger.info("Rembg initialized successfully")
        except Exception as e:
            logger.warning(f"Could not initialize rembg immediately: {e}")
            bg_remover = None
        
        tools_initialized = True
            
    except Exception as e:
        logger.error(f"Error initializing tools: {e}")
        tools_initialized = False

@app.before_request
def before_request():
    """Initialize tools before first request"""
    initialize_tools()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'tools': {
            'rembg': 'ready' if bg_remover is not None else 'not initialized',
            'color_setter': 'ready' if color_setter is not None else 'not initialized'
        }
    })

@app.route('/api/remove-background', methods=['POST'])
def remove_background():
    """Remove background from image"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        model_name = request.form.get('model', 'u2netp')
        
        # Validate file
        if not processor.allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed. Use: JPG, PNG, GIF, BMP'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"input_{filename}")
        file.save(input_path)
        
        logger.info(f"Processing background removal: {filename}")
        
        # Initialize rembg if needed
        global bg_remover
        if bg_remover is None:
            try:
                bg_remover = FuseBackgroundRemover(model_name)
            except Exception as e:
                logger.error(f"Could not initialize rembg: {e}")
                return jsonify({'error': 'Background removal service not available'}), 503
        else:
            # Reload if different model requested
            if hasattr(bg_remover, 'current_model') and bg_remover.current_model != model_name:
                bg_remover = FuseBackgroundRemover(model_name)
        
        # Process image
        output_filename = f"removed_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename.rsplit('.', 1)[0]}.png"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        
        success = bg_remover.process_image(input_path, output_path)
        
        if not success:
            return jsonify({'error': 'Failed to remove background'}), 500
        
        # Read output file
        with open(output_path, 'rb') as f:
            img_data = f.read()
        
        # Clean up input file
        try:
            os.remove(input_path)
        except:
            pass
        
        return jsonify({
            'success': True,
            'message': 'Background removed successfully',
            'download_filename': output_filename,
            'display_name': f"Removed - {filename}"
        }), 200
        
    except Exception as e:
        logger.error(f"Error in remove_background: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/set-background-color', methods=['POST'])
def set_background_color_api():
    """Set background color on transparent image"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Get RGB color
        try:
            r = int(request.form.get('r', 255))
            g = int(request.form.get('g', 255))
            b = int(request.form.get('b', 255))
            rgb_color = (r, g, b)
        except:
            rgb_color = (255, 255, 255)
        
        # Validate file
        if not processor.allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed. Use: JPG, PNG, GIF, BMP'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"color_input_{filename}")
        file.save(input_path)
        
        logger.info(f"Processing color setting: {filename} with RGB{rgb_color}")
        
        # Process image
        output_filename = f"colored_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename.rsplit('.', 1)[0]}.jpg"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        
        success = color_setter.set_background_color(input_path, output_path, rgb_color)
        
        if not success:
            return jsonify({'error': 'Failed to set background color'}), 500
        
        # Clean up input file
        try:
            os.remove(input_path)
        except:
            pass
        
        return jsonify({
            'success': True,
            'message': 'Background color set successfully',
            'download_filename': output_filename,
            'display_name': f"Colored - {filename}",
            'color': f"rgb({r}, {g}, {b})"
        }), 200
        
    except Exception as e:
        logger.error(f"Error in set_background_color: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/preview-color', methods=['POST'])
def preview_color():
    """Generate a quick preview with background color"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        # Get RGB color
        try:
            r = int(request.form.get('r', 255))
            g = int(request.form.get('g', 255))
            b = int(request.form.get('b', 255))
            rgb_color = (r, g, b)
        except:
            rgb_color = (255, 255, 255)
        
        # Load image
        img = Image.open(file.stream)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create background and composite
        background = Image.new('RGB', img.size, rgb_color)
        background.paste(img, mask=img.split()[3] if img.mode == 'RGBA' else None)
        
        # Save to bytes
        img_io = io.BytesIO()
        background.save(img_io, 'PNG', quality=85)
        img_io.seek(0)
        
        return send_file(
            img_io,
            mimetype='image/png',
            as_attachment=False
        )
        
    except Exception as e:
        logger.error(f"Error in preview_color: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    """Download processed image"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if not os.path.exists(filepath):
            return jsonify({'error': 'File not found'}), 404
        
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        logger.error(f"Error in download: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available background removal models"""
    models = [
        {'name': 'u2netp', 'display': 'U2Net-P (Fast)', 'size': '4 MB'},
        {'name': 'u2net', 'display': 'U2Net (Standard)', 'size': '168 MB'},
        {'name': 'isnet-general-use', 'display': 'ISNet (High Quality)', 'size': '170 MB'},
        {'name': 'silueta', 'display': 'Silueta (Lightweight)', 'size': '43 MB'},
    ]
    return jsonify(models)

@app.route('/api/rotate-image', methods=['POST'])
def rotate_image():
    """Rotate image by specified angle"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        angle = int(request.form.get('angle', 90))
        
        img = Image.open(file.stream)
        img_rotated = img.rotate(angle, expand=True)
        
        img_io = io.BytesIO()
        img_rotated.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error rotating image: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/flip-image', methods=['POST'])
def flip_image():
    """Flip image horizontally or vertically"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        direction = request.form.get('direction', 'horizontal')
        
        img = Image.open(file.stream)
        if direction == 'horizontal':
            img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            img_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
        
        img_io = io.BytesIO()
        img_flipped.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error flipping image: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/adjust-brightness', methods=['POST'])
def adjust_brightness():
    """Adjust image brightness"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        factor = float(request.form.get('factor', 1.0))
        
        from PIL import ImageEnhance
        img = Image.open(file.stream)
        enhancer = ImageEnhance.Brightness(img)
        img_adjusted = enhancer.enhance(factor)
        
        img_io = io.BytesIO()
        img_adjusted.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error adjusting brightness: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/adjust-contrast', methods=['POST'])
def adjust_contrast():
    """Adjust image contrast"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        factor = float(request.form.get('factor', 1.0))
        
        from PIL import ImageEnhance
        img = Image.open(file.stream)
        enhancer = ImageEnhance.Contrast(img)
        img_adjusted = enhancer.enhance(factor)
        
        img_io = io.BytesIO()
        img_adjusted.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error adjusting contrast: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/adjust-saturation', methods=['POST'])
def adjust_saturation():
    """Adjust image saturation"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        factor = float(request.form.get('factor', 1.0))
        
        from PIL import ImageEnhance
        img = Image.open(file.stream)
        enhancer = ImageEnhance.Color(img)
        img_adjusted = enhancer.enhance(factor)
        
        img_io = io.BytesIO()
        img_adjusted.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error adjusting saturation: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/resize-image', methods=['POST'])
def resize_image():
    """Resize image to specified dimensions"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        width = int(request.form.get('width', 800))
        height = int(request.form.get('height', 600))
        
        img = Image.open(file.stream)
        img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
        
        img_io = io.BytesIO()
        img_resized.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error resizing image: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/blur-background', methods=['POST'])
def blur_background():
    """Apply blur effect to image"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        blur_radius = int(request.form.get('radius', 5))
        
        from PIL import ImageFilter
        img = Image.open(file.stream)
        img_blurred = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        
        img_io = io.BytesIO()
        img_blurred.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error blurring image: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/grayscale-image', methods=['POST'])
def grayscale_image():
    """Convert image to grayscale"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        img = Image.open(file.stream)
        img_gray = img.convert('L')
        
        img_io = io.BytesIO()
        img_gray.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error converting to grayscale: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/sharpen-image', methods=['POST'])
def sharpen_image():
    """Sharpen image"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        from PIL import ImageFilter, ImageEnhance
        img = Image.open(file.stream)
        img_sharpened = img.filter(ImageFilter.SHARPEN)
        
        img_io = io.BytesIO()
        img_sharpened.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error sharpening image: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/edge-detect', methods=['POST'])
def edge_detect():
    """Detect edges in image"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        from PIL import ImageFilter
        img = Image.open(file.stream)
        img_edges = img.filter(ImageFilter.FIND_EDGES)
        
        img_io = io.BytesIO()
        img_edges.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error detecting edges: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/invert-colors', methods=['POST'])
def invert_colors():
    """Invert image colors"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        from PIL import ImageOps
        img = Image.open(file.stream)
        img_inverted = ImageOps.invert(img.convert('RGB'))
        
        img_io = io.BytesIO()
        img_inverted.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png', as_attachment=False)
    except Exception as e:
        logger.error(f"Error inverting colors: {e}")
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Initialize tools
    initialize_tools()
    
    # Run app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False
    )
