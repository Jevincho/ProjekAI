/* ===================================
   Rembg-Fuse Web App - JavaScript
   =================================== */

// State Management
const state = {
  removeTab: {
    file: null,
    model: "u2netp",
    downloadFileName: null,
  },
  colorTab: {
    file: null,
    color: "#ffffff",
    previewLink: null,
    downloadFileName: null,
  },
  editor: {
    file: null,
    originalFile: null,
    currentImageData: null,
    downloadFileName: null,
    // Track adjustment values for live adjustments
    adjustments: {
      brightness: 1.0,
      contrast: 1.0,
      saturation: 1.0,
      blur: 0,
      isAdjusting: false,
    },
  },
};

// Initialize
document.addEventListener("DOMContentLoaded", function () {
  console.log("App initialized");
  setupEventListeners();
  loadAvailableModels();
});

// Setup Event Listeners
function setupEventListeners() {
  // Editor Tab
  const uploadAreaEditor = document.getElementById("upload-area-editor");
  const fileInputEditor = document.getElementById("file-input-editor");

  if (uploadAreaEditor && fileInputEditor) {
    uploadAreaEditor.addEventListener("click", () => fileInputEditor.click());
    uploadAreaEditor.addEventListener("dragover", handleDragOver);
    uploadAreaEditor.addEventListener("dragleave", handleDragLeave);
    uploadAreaEditor.addEventListener("drop", (e) => handleDrop(e, "editor"));
    fileInputEditor.addEventListener("change", (e) =>
      handleFileSelect(e, "editor"),
    );
  }

  // Remove Background Tab
  const uploadAreaRemove = document.getElementById("upload-area-remove");
  const fileInputRemove = document.getElementById("file-input-remove");

  uploadAreaRemove.addEventListener("click", () => fileInputRemove.click());
  uploadAreaRemove.addEventListener("dragover", handleDragOver);
  uploadAreaRemove.addEventListener("dragleave", handleDragLeave);
  uploadAreaRemove.addEventListener("drop", (e) => handleDrop(e, "remove"));
  fileInputRemove.addEventListener("change", (e) =>
    handleFileSelect(e, "remove"),
  );

  // Color Background Tab
  const uploadAreaColor = document.getElementById("upload-area-color");
  const fileInputColor = document.getElementById("file-input-color");
  const colorPicker = document.getElementById("color-picker");
  const previewBtn = document.getElementById("preview-btn");

  uploadAreaColor.addEventListener("click", () => fileInputColor.click());
  uploadAreaColor.addEventListener("dragover", handleDragOver);
  uploadAreaColor.addEventListener("dragleave", handleDragLeave);
  uploadAreaColor.addEventListener("drop", (e) => handleDrop(e, "color"));
  fileInputColor.addEventListener("change", (e) =>
    handleFileSelect(e, "color"),
  );

  colorPicker.addEventListener("input", handleColorChange);
  previewBtn.addEventListener("click", previewColor);
}

// Tab Switching
function switchTab(tabName) {
  // Hide all tabs
  document.querySelectorAll(".tab-content").forEach((tab) => {
    tab.classList.remove("active");
  });
  document.querySelectorAll(".tab-btn").forEach((btn) => {
    btn.classList.remove("active");
  });

  // Show selected tab
  document.getElementById(tabName).classList.add("active");
  document.querySelector(`[data-tab="${tabName}"]`).classList.add("active");
}

// Drag and Drop Handlers
function handleDragOver(e) {
  e.preventDefault();
  e.stopPropagation();
  e.currentTarget.classList.add("dragover");
}

function handleDragLeave(e) {
  e.preventDefault();
  e.stopPropagation();
  e.currentTarget.classList.remove("dragover");
}

function handleDrop(e, tab) {
  e.preventDefault();
  e.stopPropagation();
  e.currentTarget.classList.remove("dragover");

  const files = e.dataTransfer.files;
  if (files.length > 0) {
    handleFileSelect({ target: { files: files } }, tab);
  }
}

// File Selection Handler
function handleFileSelect(e, tab) {
  const files = e.target.files;
  if (files.length === 0) return;

  const file = files[0];

  // Validate file type
  if (!file.type.startsWith("image/")) {
    showError("Please select an image file", tab);
    return;
  }

  // Validate file size (50MB max)
  if (file.size > 50 * 1024 * 1024) {
    showError("File size must be less than 50MB", tab);
    return;
  }

  if (tab === "editor") {
    state.editor.file = file;
    state.editor.originalFile = file;
    editorLoadImage(file);
  } else if (tab === "remove") {
    state.removeTab.file = file;
    showNotification(`File selected: ${file.name}`, tab);
    processRemoveBackground();
  } else if (tab === "color") {
    state.colorTab.file = file;
    document.getElementById("preview-btn").disabled = false;
    showNotification(`File selected: ${file.name}`, tab);
  }
}

// Remove Background Process
async function processRemoveBackground() {
  const file = state.removeTab.file;
  const model = state.removeTab.model;

  if (!file) {
    showError("Please select a file first", "remove");
    return;
  }

  // Show progress
  showProgress("remove");
  hideResult("remove");
  hideError("remove");

  try {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("model", model);

    const response = await fetch("/api/remove-background", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.error || "Failed to remove background");
    }

    const data = await response.json();

    hideProgress("remove");
    state.removeTab.downloadFileName = data.download_filename;

    // Show result
    showRemoveResult(data.download_filename);
    showNotification("Background removed successfully!", "remove");
  } catch (error) {
    hideProgress("remove");
    showError(`Error: ${error.message}`, "remove");
  }
}

// Show Remove Result
function showRemoveResult(filename) {
  const resultArea = document.getElementById("remove-result");
  const preview = document.getElementById("remove-preview");

  // Create a temporary image from the processed file
  preview.src = `/api/download/${filename}`;
  preview.onload = function () {
    resultArea.classList.remove("hidden");
  };
  preview.onerror = function () {
    showError("Could not load result image", "remove");
  };
}

// Color Picker Handler
function handleColorChange(e) {
  const color = e.target.value;
  state.colorTab.color = color;

  // Update display
  document.getElementById("color-display").style.backgroundColor = color;

  // Convert hex to RGB
  const rgb = hexToRgb(color);
  document.getElementById("rgb-display").textContent =
    `(${rgb.r}, ${rgb.g}, ${rgb.b})`;
}

// Set Preset Color
function setColor(hexColor) {
  document.getElementById("color-picker").value = hexColor;
  handleColorChange({ target: { value: hexColor } });
}

// Preview Color
async function previewColor() {
  const file = state.colorTab.file;
  const color = state.colorTab.color;

  if (!file) {
    showError("Please select a file first", "color");
    return;
  }

  try {
    const rgb = hexToRgb(color);
    const formData = new FormData();
    formData.append("file", file);
    formData.append("r", rgb.r);
    formData.append("g", rgb.g);
    formData.append("b", rgb.b);

    const response = await fetch("/api/preview-color", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Failed to generate preview");
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);

    document.getElementById("preview-image").src = url;
    document.getElementById("color-preview").classList.remove("hidden");
  } catch (error) {
    showError(`Error: ${error.message}`, "color");
  }
}

// Process Color Background
async function processColorBackground() {
  const file = state.colorTab.file;
  const color = state.colorTab.color;

  if (!file) {
    showError("Please select a file first", "color");
    return;
  }

  // Show progress
  showProgress("color");
  hideResult("color");
  hideError("color");

  try {
    const rgb = hexToRgb(color);
    const formData = new FormData();
    formData.append("file", file);
    formData.append("r", rgb.r);
    formData.append("g", rgb.g);
    formData.append("b", rgb.b);

    const response = await fetch("/api/set-background-color", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.error || "Failed to set background color");
    }

    const data = await response.json();

    hideProgress("color");
    state.colorTab.downloadFileName = data.download_filename;

    // Show result
    showColorResult(data.download_filename);
    showNotification("Background color set successfully!", "color");
  } catch (error) {
    hideProgress("color");
    showError(`Error: ${error.message}`, "color");
  }
}

// Show Color Result
function showColorResult(filename) {
  const resultArea = document.getElementById("color-result");
  const preview = document.getElementById("color-result-img");

  preview.src = `/api/download/${filename}`;
  preview.onload = function () {
    resultArea.classList.remove("hidden");
  };
  preview.onerror = function () {
    showError("Could not load result image", "color");
  };
}

// Download Remove Result
function downloadRemove() {
  if (state.removeTab.downloadFileName) {
    window.location.href = `/api/download/${state.removeTab.downloadFileName}`;
  }
}

// Download Color Result
function downloadColor() {
  if (state.colorTab.downloadFileName) {
    window.location.href = `/api/download/${state.colorTab.downloadFileName}`;
  }
}

// Reset Remove Tab
function resetRemove() {
  state.removeTab.file = null;
  state.removeTab.downloadFileName = null;
  document.getElementById("file-input-remove").value = "";
  hideResult("remove");
  hideProgress("remove");
  hideError("remove");
}

// Reset Color Tab
function resetColor() {
  state.colorTab.file = null;
  state.colorTab.downloadFileName = null;
  state.colorTab.previewLink = null;
  document.getElementById("file-input-color").value = "";
  document.getElementById("preview-btn").disabled = true;
  document.getElementById("color-preview").classList.add("hidden");
  hideResult("color");
  hideProgress("color");
  hideError("color");
}

// UI Helper Functions
function showProgress(tab) {
  document.getElementById(`${tab}-progress`).classList.remove("hidden");
}

function hideProgress(tab) {
  document.getElementById(`${tab}-progress`).classList.add("hidden");
}

function showResult(tab) {
  document.getElementById(`${tab}-result`).classList.remove("hidden");
}

function hideResult(tab) {
  document.getElementById(`${tab}-result`).classList.add("hidden");
}

function showError(message, tab) {
  const errorDiv = document.getElementById(`${tab}-error`);
  errorDiv.textContent = message;
  errorDiv.classList.remove("hidden");
}

function hideError(tab) {
  document.getElementById(`${tab}-error`).classList.add("hidden");
}

function showNotification(message, tab) {
  console.log(`[${tab}] ${message}`);
  // You can add a toast notification here if needed
}

// Utility Functions
function hexToRgb(hex) {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result
    ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16),
      }
    : { r: 255, g: 255, b: 255 };
}

function rgbToHex(r, g, b) {
  return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

// Load Available Models
async function loadAvailableModels() {
  try {
    const response = await fetch("/api/models");
    const models = await response.json();

    const select = document.getElementById("model-select");
    select.innerHTML = "";

    models.forEach((model) => {
      const option = document.createElement("option");
      option.value = model.name;
      option.textContent = `${model.display} (${model.size})`;
      select.appendChild(option);
    });

    // Update state when model changes
    select.addEventListener("change", (e) => {
      state.removeTab.model = e.target.value;
    });
  } catch (error) {
    console.error("Error loading models:", error);
  }
}

// ================================
// EDITOR FUNCTIONS (NEW)
// ================================

function editorLoadImage(file) {
  const reader = new FileReader();
  reader.onload = function (e) {
    const preview = document.getElementById("editor-preview");
    preview.src = e.target.result;
    preview.style.display = "block";
    document.getElementById("no-image-msg").style.display = "none";
    document.getElementById("editor-download-btn").disabled = false;

    // Store image data
    state.editor.currentImageData = e.target.result;
  };
  reader.readAsDataURL(file);
}

async function editorApplyEffect(endpoint, params = {}) {
  if (!state.editor.file) {
    showError("Please upload an image first", "editor");
    return;
  }

  try {
    showProgress("editor");
    const formData = new FormData();
    formData.append("file", state.editor.file);

    // Add parameters
    Object.keys(params).forEach((key) => {
      formData.append(key, params[key]);
    });

    const response = await fetch(endpoint, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Failed to apply effect");
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);

    // Create new file from blob for subsequent operations
    state.editor.file = new File([blob], "edited.png", { type: "image/png" });

    const preview = document.getElementById("editor-preview");
    preview.src = url;
    preview.style.display = "block";

    hideProgress("editor");
    showNotification("Effect applied!", "editor");
  } catch (error) {
    hideProgress("editor");
    showError(`Error: ${error.message}`, "editor");
  }
}

function editorRotate(angle) {
  editorApplyEffect("/api/rotate-image", { angle: angle });
}

function editorFlip(direction) {
  editorApplyEffect("/api/flip-image", { direction: direction });
}

function editorBrightness(factor) {
  document.getElementById("brightness-value").textContent = factor;
  state.editor.adjustments.brightness = parseFloat(factor);
  editorApplyAdjustments();
}

function editorContrast(factor) {
  document.getElementById("contrast-value").textContent = factor;
  state.editor.adjustments.contrast = parseFloat(factor);
  editorApplyAdjustments();
}

function editorSaturation(factor) {
  document.getElementById("saturation-value").textContent = factor;
  state.editor.adjustments.saturation = parseFloat(factor);
  editorApplyAdjustments();
}

function editorBlur(radius) {
  document.getElementById("blur-value").textContent = radius;
  state.editor.adjustments.blur = parseInt(radius);
  editorApplyAdjustments();
}

// New function to apply all adjustments cumulatively to original file
async function editorApplyAdjustments() {
  if (!state.editor.originalFile) {
    showError("No original file available", "editor");
    return;
  }

  // Prevent multiple simultaneous adjustments
  if (state.editor.adjustments.isAdjusting) {
    return;
  }

  try {
    state.editor.adjustments.isAdjusting = true;
    showProgress("editor");

    const adj = state.editor.adjustments;
    let currentFile = state.editor.originalFile;

    // Apply brightness
    if (adj.brightness !== 1.0) {
      currentFile = await applyAdjustmentEffect(
        currentFile,
        "/api/adjust-brightness",
        { factor: adj.brightness },
      );
    }

    // Apply contrast
    if (adj.contrast !== 1.0) {
      currentFile = await applyAdjustmentEffect(
        currentFile,
        "/api/adjust-contrast",
        { factor: adj.contrast },
      );
    }

    // Apply saturation
    if (adj.saturation !== 1.0) {
      currentFile = await applyAdjustmentEffect(
        currentFile,
        "/api/adjust-saturation",
        { factor: adj.saturation },
      );
    }

    // Apply blur
    if (adj.blur > 0) {
      currentFile = await applyAdjustmentEffect(
        currentFile,
        "/api/blur-background",
        { radius: adj.blur },
      );
    }

    // Update state and display
    state.editor.file = currentFile;
    const reader = new FileReader();
    reader.onload = function (e) {
      const preview = document.getElementById("editor-preview");
      preview.src = e.target.result;
      preview.style.display = "block";
    };
    reader.readAsDataURL(currentFile);

    hideProgress("editor");
    showNotification("Adjustments applied!", "editor");
  } catch (error) {
    hideProgress("editor");
    showError(`Error applying adjustments: ${error.message}`, "editor");
  } finally {
    state.editor.adjustments.isAdjusting = false;
  }
}

// Helper function to apply a single effect and return the result as File
async function applyAdjustmentEffect(file, endpoint, params = {}) {
  const formData = new FormData();
  formData.append("file", file);

  Object.keys(params).forEach((key) => {
    formData.append(key, params[key]);
  });

  const response = await fetch(endpoint, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`Failed to apply effect at ${endpoint}`);
  }

  const blob = await response.blob();
  return new File([blob], "adjusted.png", { type: "image/png" });
}

function editorResize() {
  const width = document.getElementById("resize-width").value;
  const height = document.getElementById("resize-height").value;
  editorApplyEffect("/api/resize-image", { width: width, height: height });
}

function editorGrayscale() {
  editorApplyEffect("/api/grayscale-image");
}

function editorSharpen() {
  editorApplyEffect("/api/sharpen-image");
}

function editorEdgeDetect() {
  editorApplyEffect("/api/edge-detect");
}

function editorInvert() {
  editorApplyEffect("/api/invert-colors");
}

function editorReset() {
  if (!state.editor.originalFile) return;

  state.editor.file = state.editor.originalFile;
  editorLoadImage(state.editor.file);

  // Reset all sliders
  document.getElementById("brightness-slider").value = "1";
  document.getElementById("contrast-slider").value = "1";
  document.getElementById("saturation-slider").value = "1";
  document.getElementById("blur-slider").value = "0";

  document.getElementById("brightness-value").textContent = "1.0";
  document.getElementById("contrast-value").textContent = "1.0";
  document.getElementById("saturation-value").textContent = "1.0";
  document.getElementById("blur-value").textContent = "0";

  // Reset adjustment state
  state.editor.adjustments = {
    brightness: 1.0,
    contrast: 1.0,
    saturation: 1.0,
    blur: 0,
    isAdjusting: false,
  };

  showNotification("All changes reset!", "editor");
}

async function editorDownload() {
  const preview = document.getElementById("editor-preview");
  if (!preview.src || preview.style.display === "none") {
    showError("No image to download", "editor");
    return;
  }

  try {
    // Create canvas and draw image
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    const img = new Image();

    img.onload = function () {
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0);

      // Download
      canvas.toBlob(function (blob) {
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `rembg-fuse-${Date.now()}.png`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      }, "image/png");
    };

    img.src = preview.src;
  } catch (error) {
    showError(`Error downloading: ${error.message}`, "editor");
  }
}

// Attach processColorBackground to window so it can be called from HTML
window.processColorBackground = processColorBackground;
window.editorRotate = editorRotate;
window.editorFlip = editorFlip;
window.editorBrightness = editorBrightness;
window.editorContrast = editorContrast;
window.editorSaturation = editorSaturation;
window.editorBlur = editorBlur;
window.editorResize = editorResize;
window.editorGrayscale = editorGrayscale;
window.editorSharpen = editorSharpen;
window.editorEdgeDetect = editorEdgeDetect;
window.editorInvert = editorInvert;
window.editorReset = editorReset;
window.editorDownload = editorDownload;
