"""
Image processing utilities
"""

import os
import logging
from pathlib import Path
from datetime import datetime, timedelta
from PIL import Image
import mimetypes

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Helper class for image processing operations"""
    
    def __init__(self, upload_folder):
        self.upload_folder = upload_folder
        self.allowed_extensions = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'}
    
    def allowed_file(self, filename):
        """Check if file extension is allowed"""
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.allowed_extensions
    
    def get_file_size_mb(self, filepath):
        """Get file size in MB"""
        size_bytes = os.path.getsize(filepath)
        return round(size_bytes / (1024 * 1024), 2)
    
    def cleanup_old_files(self, hours=24):
        """Remove files older than specified hours"""
        try:
            cutoff_time = datetime.now() - timedelta(hours=hours)
            for filename in os.listdir(self.upload_folder):
                filepath = os.path.join(self.upload_folder, filename)
                if os.path.isfile(filepath):
                    file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                    if file_time < cutoff_time:
                        os.remove(filepath)
                        logger.info(f"Cleaned up old file: {filename}")
        except Exception as e:
            logger.error(f"Error cleaning up files: {e}")
    
    def get_image_info(self, filepath):
        """Get image information"""
        try:
            img = Image.open(filepath)
            return {
                'size': img.size,
                'format': img.format,
                'mode': img.mode,
                'file_size_mb': self.get_file_size_mb(filepath)
            }
        except Exception as e:
            logger.error(f"Error getting image info: {e}")
            return None
