#!/usr/bin/env python3
"""
Comprehensive demonstration of mplstyles-seaborn package.

This script showcases advanced usage patterns and demonstrates the full
range of capabilities of the mplstyles-seaborn package, including all
available style combinations and different plot types.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
import mplstyles_seaborn

# Set random seed for reproducibility  
np.random.seed(19680801)

def create_advanced_subplot_demo():
    """Create a comprehensive subplot demonstration."""
    import os
    
    output_dir = "examples/comprehensive_demo_output"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Creating comprehensive subplot demonstration...")
    
    # Use a vibrant style combination
    mplstyles_seaborn.use_style("whitegrid", "bright", "talk")
    
    fig = plt.figure(figsize=(16, 12))
    
    # Create a complex subplot layout
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Line plot with multiple series
    ax1 = fig.add_subplot(gs[0, :2])
    x = np.linspace(0, 4*np.pi, 100)
    for i, (func, label) in enumerate([(np.sin, 'sin'), (np.cos, 'cos'), 
                                      (lambda x: np.sin(x)*np.cos(x), 'sin·cos')]):
        ax1.plot(x, func(x), label=label, linewidth=2.5)
    ax1.set_title('Trigonometric Functions', fontsize=16, fontweight='bold')
    ax1.set_xlabel(r'$x$')
    ax1.set_ylabel(r'$f(x)$')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Scatter plot with color coding
    ax2 = fig.add_subplot(gs[0, 2])
    prng = np.random.RandomState(42)
    n_points = 150
    x_scatter = prng.randn(n_points)
    y_scatter = prng.randn(n_points)
    colors = prng.randn(n_points)
    scatter = ax2.scatter(x_scatter, y_scatter, c=colors, alpha=0.7, s=50)
    ax2.set_title('Scatter Plot', fontweight='bold')
    ax2.set_xlabel(r'$X$')
    ax2.set_ylabel(r'$Y$')
    plt.colorbar(scatter, ax=ax2, shrink=0.8)
    
    # 3. Bar chart with error bars
    ax3 = fig.add_subplot(gs[1, 0])
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    errors = [3, 5, 4, 6, 3]
    bars = ax3.bar(categories, values, yerr=errors, capsize=5, alpha=0.8)
    ax3.set_title('Bar Chart with Error Bars', fontweight='bold')
    ax3.set_ylabel('Values')
    
    # 4. Histogram with density curve
    ax4 = fig.add_subplot(gs[1, 1])
    data = prng.normal(0, 1, 1000)
    n, bins, patches = ax4.hist(data, bins=30, density=True, alpha=0.7, 
                               color='C0', edgecolor='black', linewidth=0.5)
    # Add density curve
    x_curve = np.linspace(-4, 4, 100)
    y_curve = (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * x_curve**2)
    ax4.plot(x_curve, y_curve, 'r-', linewidth=2, label='Normal PDF')
    ax4.set_title('Histogram with PDF', fontweight='bold')
    ax4.set_xlabel('Value')
    ax4.set_ylabel('Density')
    ax4.legend()
    
    # 5. Box plot
    ax5 = fig.add_subplot(gs[1, 2])
    box_data = [prng.normal(0, std, 100) for std in range(1, 5)]
    bp = ax5.boxplot(box_data, tick_labels=[r'$\sigma=1$', r'$\sigma=2$', r'$\sigma=3$', r'$\sigma=4$'], patch_artist=True)
    for patch, color in zip(bp['boxes'], plt.rcParams['axes.prop_cycle']()):
        patch.set_facecolor(color['color'])
        patch.set_alpha(0.7)
    ax5.set_title('Box Plot', fontweight='bold')
    ax5.set_ylabel('Values')
    
    # 6. Polar plot
    ax6 = fig.add_subplot(gs[2, 0], projection='polar')
    theta = np.linspace(0, 2*np.pi, 100)
    r1 = 1 + 0.3*np.sin(5*theta)
    r2 = 1 + 0.3*np.cos(3*theta)
    ax6.plot(theta, r1, linewidth=2, label='5 petals')
    ax6.plot(theta, r2, linewidth=2, label='3 petals')
    ax6.set_title('Polar Plot', fontweight='bold', pad=20)
    ax6.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    
    # 7. Contour plot
    ax7 = fig.add_subplot(gs[2, 1:])
    x_contour = np.linspace(-3, 3, 100)
    y_contour = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x_contour, y_contour)
    Z = np.exp(-(X**2 + Y**2)/2) * np.sin(2*X) * np.cos(3*Y)
    contour = ax7.contourf(X, Y, Z, levels=20, alpha=0.8)
    ax7.contour(X, Y, Z, levels=20, colors='black', linewidths=0.5, alpha=0.6)
    ax7.set_title('Contour Plot', fontweight='bold')
    ax7.set_xlabel(r'$X$')
    ax7.set_ylabel(r'$Y$')
    plt.colorbar(contour, ax=ax7, shrink=0.8)
    
    plt.suptitle('Comprehensive Plot Demonstration', fontsize=20, fontweight='bold', y=0.98)
    filename = f'{output_dir}/comprehensive_demo.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

def demonstrate_palette_comparison():
    """Show all palettes with the same plot type."""
    import os
    
    output_dir = "examples/comprehensive_demo_output"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Creating palette comparison...")
    
    palettes = mplstyles_seaborn.PALETTES
    n_palettes = len(palettes)
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    # Common data for all plots
    x = np.linspace(0, 2*np.pi, 100)
    n_lines = 6
    
    for i, palette in enumerate(palettes):
        # Apply style with current palette
        mplstyles_seaborn.use_style("whitegrid", palette, "notebook")
        
        ax = axes[i]
        
        # Plot multiple lines to show the full palette
        for j in range(n_lines):
            y = np.sin(x + j * np.pi/3) * np.exp(-j * 0.1)
            ax.plot(x, y, linewidth=2.5, label=f'Line {j+1}')
        
        ax.set_title(f'Palette: {palette}', fontsize=14, fontweight='bold')
        ax.set_xlabel(r'$x$')
        ax.set_ylabel(r'$y$')
        if i == 0:  # Only show legend for first subplot to save space
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    filename = f'{output_dir}/palette_comparison.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

def demonstrate_style_comparison():
    """Show all base styles with the same plot type."""
    import os
    
    output_dir = "examples/comprehensive_demo_output"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Creating style comparison...")
    
    styles = mplstyles_seaborn.STYLES
    n_styles = len(styles)
    
    fig, axes = plt.subplots(1, n_styles, figsize=(20, 4))
    
    # Common data
    prng = np.random.RandomState(42)
    x = np.linspace(-2, 2, 100)
    y1 = np.exp(-x**2) * np.sin(4*x)
    y2 = np.exp(-x**2) * np.cos(4*x)
    
    # Scatter data
    x_scatter = prng.randn(50) * 0.5
    y_scatter = prng.randn(50) * 0.5
    
    for i, style in enumerate(styles):
        # Apply current style
        mplstyles_seaborn.use_style(style, "colorblind", "notebook")
        
        ax = axes[i]
        
        # Plot lines and scatter
        ax.plot(x, y1, linewidth=2, label='Function 1')
        ax.plot(x, y2, linewidth=2, label='Function 2')
        ax.scatter(x_scatter, y_scatter, alpha=0.6, s=30, color='red', zorder=5)
        
        ax.set_title(f'Style: {style}', fontsize=12, fontweight='bold')
        ax.set_xlabel(r'$x$')
        if i == 0:
            ax.set_ylabel(r'$y$')
            ax.legend()
        
        # Show grid for grid styles
        if 'grid' in style:
            ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    filename = f'{output_dir}/style_comparison.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

def create_publication_ready_figure():
    """Create a publication-ready figure demonstrating best practices."""
    import os
    
    output_dir = "examples/comprehensive_demo_output"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Creating publication-ready figure...")
    
    # Use paper context for publication
    mplstyles_seaborn.use_style("white", "colorblind", "paper")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left plot: Time series data
    t = np.linspace(0, 10, 200)
    signal = np.sin(2*np.pi*t) * np.exp(-t/5)
    noise = np.random.normal(0, 0.1, len(t))
    
    ax1.plot(t, signal, 'b-', linewidth=2, label='Signal', alpha=0.8)
    ax1.plot(t, signal + noise, 'r-', linewidth=1, alpha=0.6, label='Signal + Noise')
    ax1.fill_between(t, signal - 0.2, signal + 0.2, alpha=0.2, color='blue', 
                     label='±0.2 uncertainty')
    
    ax1.set_xlabel(r'Time (s)', fontsize=12)
    ax1.set_ylabel(r'Amplitude', fontsize=12)
    ax1.set_title('Time Series Analysis', fontsize=14, fontweight='bold')
    ax1.legend(frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3)
    
    # Right plot: Statistical comparison
    categories = ['Control', 'Treatment A', 'Treatment B', 'Treatment C']
    means = [20, 35, 30, 45]
    stds = [3, 5, 4, 6]
    
    x_pos = np.arange(len(categories))
    bars = ax2.bar(x_pos, means, yerr=stds, capsize=5, alpha=0.8, 
                   color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    
    # Add value labels on bars
    for bar, mean, std in zip(bars, means, stds):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + std + 1,
                f'{mean}±{std}', ha='center', va='bottom', fontsize=10)
    
    ax2.set_xlabel(r'Experimental Conditions', fontsize=12)
    ax2.set_ylabel(r'Response Variable', fontsize=12)
    ax2.set_title('Treatment Comparison', fontsize=14, fontweight='bold')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(categories)
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    png_filename = f'{output_dir}/publication_ready.png'
    pdf_filename = f'{output_dir}/publication_ready.pdf'
    plt.savefig(png_filename, dpi=300, bbox_inches='tight')
    plt.savefig(pdf_filename, bbox_inches='tight')
    plt.close()
    print(f"Saved: {png_filename} and {pdf_filename}")

if __name__ == "__main__":
    print("mplstyles-seaborn Comprehensive Demo")
    print("=" * 40)
    
    create_advanced_subplot_demo()
    demonstrate_palette_comparison()
    demonstrate_style_comparison()
    create_publication_ready_figure()
    
    print(f"\n✓ All comprehensive examples completed successfully!")
    print(f"✓ Generated plots showcase all {len(mplstyles_seaborn.STYLES)} styles,")
    print(f"  {len(mplstyles_seaborn.PALETTES)} palettes, and {len(mplstyles_seaborn.CONTEXTS)} contexts")
    print(f"✓ Total available combinations: {len(mplstyles_seaborn.list_available_styles())}")