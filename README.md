# Schema Designer Pro

> **数据模式设计专业版** - A professional schema design and JSON generation tool with minimalist German/Nordic design aesthetic.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/schema-designer-pro)

## Overview

Schema Designer Pro is a sophisticated desktop application designed for creating, managing, and exporting structured data schemas. Built with PyQt5 and featuring a minimalist German/Nordic design aesthetic, it provides an intuitive interface for schema design with support for multiple variable types, templates, and JSON export capabilities.

### Key Features

- **Minimalist Design**: Clean, professional interface with German/Nordic design principles
- **Dark/Light Mode**: Toggle between dark and light themes
- **Template System**: Pre-built templates for common use cases
- **Real-time Preview**: Live JSON preview with formatting
- **Variable Types**: Support for basic, image, URL, array, and language variables
- **Auto-save**: Automatic saving every minute
- **Export Options**: Export individual or all schemas
- **Keyboard Shortcuts**: Efficient workflow with keyboard navigation
- **Bilingual Support**: English and Chinese interface

## Quick Start

### Prerequisites

- Python 3.8 or higher
- PyQt5 5.15 or higher

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/schema-designer-pro.git
   cd schema-designer-pro
   ```

2. **Create virtual environment**

   ```bash
   python -m venv appenv
   ```

3. **Activate virtual environment**

   ```bash
   # Windows
   appenv\Scripts\activate
   
   # macOS/Linux
   source appenv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**

   ```bash
   python main.py
   ```

## User Guide

### Getting Started

1. **Launch the Application**
   - Run `python main.py` from the project directory
   - The application will open with a clean, minimalist interface

2. **Create Your First Schema**
   - Click the "+" button in the Schemas panel
   - Enter a unique schema name
   - Fill in the basic information fields

3. **Use Templates**
   - Click the "⊞" button to create from template
   - Choose from available templates:
     - E-commerce Product
     - Blog Post
     - User Profile
     - Event
     - API Documentation
     - Simple Form
     - Gallery Website
     - Artist Website

### Interface Overview

#### Left Panel - Schema Management
- **Schema List**: View and select existing schemas
- **Search**: Filter schemas by name
- **Actions**: Create, duplicate, delete schemas
- **File Operations**: Import/export JSON files

#### Center Panel - Schema Editor
- **Basic Information**: Schema name, page titles, options
- **Variables Tab**: Add and manage different variable types
- **Auto-save**: Changes are automatically saved

#### Right Panel - JSON Preview
- **Live Preview**: Real-time JSON output
- **Format**: Pretty-print JSON with proper indentation
- **Copy**: Copy JSON to clipboard with one click

### Variable Types

#### Basic Variables
Simple text fields for essential information:
- Product names, titles, descriptions
- User information, contact details
- Basic metadata

#### More Variables
Extended text areas for detailed content:
- Long descriptions, specifications
- Content, excerpts, biographies
- Detailed information

#### Image Variables
Media fields for visual content:
- Main images, galleries
- Avatars, banners
- Visual assets

#### URL Variables
Link fields for external resources:
- Product URLs, permalinks
- Reference links, documentation
- External resources

#### Array Variables
List fields for multiple items:
- Categories, tags
- Skills, interests
- Collections of related data

#### Language Item Variables
Bilingual content fields:
- Translations
- Multi-language descriptions
- Localized content

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+N` | Create new schema |
| `Ctrl+T` | Create from template |
| `Ctrl+S` | Save schema |
| `Ctrl+O` | Import JSON |
| `Ctrl+E` | Export JSON |
| `Delete` | Delete schema |
| `F2` | Edit variable |
| `Ctrl+D` | Toggle dark mode |

### Templates

#### E-commerce Product
Complete product schema with:
- Product details (name, price, SKU, stock)
- Descriptions and specifications
- Image gallery and categories
- Product URLs and tags

#### Blog Post
Article schema featuring:
- Title, author, publish date
- Content and excerpts
- Featured images
- Categories and tags
- Translation support

#### User Profile
User information schema with:
- Personal details (name, email, bio)
- Avatar and preferences
- Skills and interests
- Social media links

#### Event
Event management schema including:
- Event details (name, dates, location)
- Description and agenda
- Venue images and banners
- Registration links
- Speakers and sponsors

#### API Documentation
Technical documentation schema:
- Endpoint and method information
- Request/response examples
- Parameters and headers
- Error codes

#### Gallery Website
Product showcase schema:
- Product information
- Image galleries
- Categories and tags
- Product links

#### Artist Website
Comprehensive artist portfolio:
- Artist biography and statement
- Accomplishments and awards
- Artwork galleries
- Event information
- Writings and media
- Bilingual support

## Development

### Project Structure

```
DataSchemaJSONGeneratorApp/
├── assets/
│   ├── design_system.py      # Design tokens and stylesheets
│   ├── dialogs.py           # Custom dialog components
│   ├── main_window.py       # Main application window
│   ├── models.py            # Data models and schemas
│   ├── schema_manager.py    # Schema management logic
│   ├── template_dialog.py   # Template selection dialog
│   ├── templates.py         # Schema templates
│   └── widgets.py           # Custom UI components
├── appenv/                  # Virtual environment
├── static/                  # Static assets
├── main.py                  # Application entry point
└── README.md               # This file
```

### Architecture

#### Design System
- **Colors**: Monochrome palette with dark/light mode support
- **Typography**: Inter font family with optimized sizing
- **Spacing**: Consistent spacing system (4px base unit)
- **Components**: Reusable UI components with consistent styling

#### Data Models
- **Schema**: Main schema container with metadata
- **Variable**: Individual data fields with type classification
- **VariableType**: Enumeration of supported variable types

#### Template System
- **SchemaTemplate**: Template definition with preview data
- **TemplateManager**: Template loading and management
- **Custom Templates**: Support for user-defined templates

### Contributing

1. **Fork the repository**

2. **Create a feature branch**

   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**

4. **Test thoroughly**

5. **Commit your changes**

   ```bash
   git commit -m 'Add amazing feature'
   ```

6. **Push to the branch**

   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Qt**: Use PyQt5 naming conventions
- **Comments**: Comprehensive docstrings for all functions
- **Type Hints**: Use type annotations where appropriate

## Deployment

### Building Executable

1. **Install PyInstaller**

   ```bash
   pip install pyinstaller
   ```

2. **Build executable**

   ```bash
   pyinstaller --onefile --windowed --name "Schema Designer Pro" main.py
   ```

3. **Distribute**
   - Executable will be created in `dist/` directory
   - Include required assets and dependencies

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SCHEMA_DATA_PATH` | Schema storage directory | `./schemas/` |
| `AUTO_SAVE_INTERVAL` | Auto-save interval (seconds) | `60` |
| `DEFAULT_LANGUAGE` | Default interface language | `en` |

### Settings File

Create `config.json` in the application directory:

```json
{
  "auto_save_interval": 60,
  "default_language": "en",
  "schema_data_path": "./schemas/",
  "theme": "light",
  "window_size": [1800, 1000]
}
```

## Troubleshooting

### Common Issues

#### Application Won't Start
- **Check Python version**: Ensure Python 3.8+ is installed
- **Verify PyQt5**: Install with `pip install PyQt5`
- **Virtual environment**: Activate the virtual environment

#### Import Errors
- **Dependencies**: Run `pip install -r requirements.txt`
- **Path issues**: Ensure you're in the correct directory
- **Python path**: Check PYTHONPATH environment variable

#### UI Issues
- **Display scaling**: Adjust system display scaling
- **Font rendering**: Install required system fonts
- **Theme issues**: Reset to default theme

#### Data Loss
- **Auto-save**: Check auto-save is enabled
- **File permissions**: Ensure write permissions to data directory
- **Backup**: Regular backups of schema data

### Logging

Enable debug logging by setting the log level:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

### Getting Help

- **Documentation**: Check this README and inline code comments
- **Issues**: Report bugs and feature requests on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact maintainers for direct support

### Community

- **Contributors**: See [CONTRIBUTORS.md](CONTRIBUTORS.md)
- **Changelog**: See [CHANGELOG.md](CHANGELOG.md)
- **Roadmap**: See [ROADMAP.md](ROADMAP.md)

## Acknowledgments

- **PyQt5**: Qt framework for Python
- **Design Inspiration**: German/Nordic minimalist design principles
- **Community**: Contributors and users who provide feedback

---

**Schema Designer Pro** - Professional schema design made simple.

*Built with dedication for the developer community*

