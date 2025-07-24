# CLAUDE.md - Project Memory

## Project Overview
This is a matplotlib styles package (`mplstyles-seaborn`) that provides seaborn-style matplotlib stylesheets. The package contains 120 pre-generated .mplstyle files covering all combinations of seaborn v0.8 styles, palettes, and contexts.

## Package Structure
```
mplstyles-seaborn/
├── src/mplstyles_seaborn/
│   ├── __init__.py              # Main package with convenience functions
│   ├── py.typed                 # Type hints marker
│   └── styles/                  # 120 .mplstyle files (5×6×4 combinations)
├── examples/                    # Comprehensive usage examples
│   ├── README.md                # Examples documentation
│   ├── basic_usage.py           # Basic usage patterns
│   ├── style_comparison.py      # Style comparison demonstrations
│   └── comprehensive_demo.py    # Advanced usage examples
├── scripts/                     # Development utilities
│   ├── build_styles.py          # Combined script to generate and fix all style files
│   └── research_seaborn_styles.py # Research script for seaborn configurations
├── pyproject.toml             # Package configuration
└── README.md                  # Project documentation
```

## Available Style Combinations
- **Styles** (5): darkgrid, whitegrid, dark, white, ticks
- **Palettes** (6): dark, colorblind, muted, bright, pastel, deep
- **Contexts** (4): paper, notebook, talk, poster
- **Total**: 120 unique style files

## Usage Methods
1. **Convenience function**: `mplstyles_seaborn.use_style('whitegrid', 'colorblind', 'talk')`
2. **Direct matplotlib**: `plt.style.use('seaborn-v0_8-whitegrid-colorblind-talk')`
3. **Auto-registration**: All styles are automatically registered with matplotlib on import

## Work Completed

### Style File Generation and Fixes (2025-07-24)
- **Problem**: Generated .mplstyle files had formatting issues:
  1. `axes.prop_cycle` used cycler syntax instead of matplotlib's expected comma-separated format
  2. `axes.facecolor` had inconsistent quote formatting
  3. Missing `font.family` setting causing font fallback issues

- **Solution**: Updated `fix_styles.py` to properly format parameters:
  - `axes.prop_cycle`: Changed from cycler syntax to comma-separated colors
  - `axes.facecolor`: Ensured consistent unquoted hex color format
  - `font.family`: Added `sans-serif` to all style files
  - `lines.solid_capstyle`: Fixed enum references to simple strings

### Font Configuration Fixed
- **Issue**: Fonts defaulting to Arial instead of preferred fonts
- **Root Cause**: `font.sans-serif` was set but `font.family` was missing
- **Solution**: Added `font.family: sans-serif` to all style files

Font selection priority:
1. Source Sans 3 (if available)
2. Arial (fallback)
3. DejaVu Sans (further fallback)
4. System fonts

### Examples Reorganization (2025-07-24)
- **Task**: Reorganized example files into structured examples directory
- **Approach**: Based examples on matplotlib's `style_sheets_reference.py` for consistency and comprehensiveness
- **New Structure**:
  - `examples/basic_usage.py`: Demonstrates fundamental usage patterns
  - `examples/style_comparison.py`: Side-by-side comparisons using matplotlib's reference approach
  - `examples/comprehensive_demo.py`: Advanced demonstrations with publication-ready examples
  - `examples/README.md`: Complete documentation for all examples
  - Legacy files have been removed after reorganization

## Testing and Development

### Development Workflow
- **IMPORTANT**: Always create a new branch before starting any development work
- Branch naming convention: Use descriptive names like `reorganize-examples`, `fix-font-issues`, etc.
- Create branch with: `git checkout -b <branch-name>`

### Environment Setup
- Use `uv` for package management and Python environment
- Dependencies: matplotlib>=3.5, seaborn>=0.11

### Testing Commands
```bash
# Test package installation and import
uv run python -c "import mplstyles_seaborn; print(len(mplstyles_seaborn.list_available_styles()))"

# Test specific style
uv run python -c "import matplotlib.pyplot as plt; plt.style.use('seaborn-v0_8-whitegrid-colorblind-talk')"

# Run examples
uv run python examples/basic_usage.py
uv run python examples/style_comparison.py
uv run python examples/comprehensive_demo.py
```

### Key Scripts
- `scripts/build_styles.py`: Combined script to generate and fix all 120 style files from seaborn configurations
  - Default: Generate and fix styles in one workflow
  - `--generate-only`: Only generate new style files
  - `--fix-only`: Only fix existing style files

### Examples Directory
- `examples/basic_usage.py`: Fundamental usage patterns and basic plot types
- `examples/style_comparison.py`: Side-by-side style comparisons based on matplotlib's reference
- `examples/comprehensive_demo.py`: Advanced demonstrations with complex layouts and publication-ready figures
- `examples/README.md`: Comprehensive documentation for all examples

## Current Status
- ✅ 120 style files generated covering all seaborn v0.8 combinations
- ✅ Fixed `axes.prop_cycle` formatting (cycler → comma-separated)
- ✅ Fixed `axes.facecolor` formatting (consistent unquoted hex)
- ✅ Added `font.family: sans-serif` to all styles
- ✅ Fixed `lines.solid_capstyle` enum references
- ✅ Package auto-registers styles with matplotlib
- ✅ Convenience functions for easy style application
- ✅ Reorganized examples into structured directory with comprehensive demonstrations
- ✅ Created examples based on matplotlib's official style reference approach

## Package Features
- **Zero seaborn dependency**: Use seaborn-style plots without requiring seaborn
- **Complete coverage**: All seaborn v0.8 style/palette/context combinations
- **Easy integration**: Styles automatically available to matplotlib
- **Type hints**: Full type annotation support
- **Flexible usage**: Multiple ways to apply styles