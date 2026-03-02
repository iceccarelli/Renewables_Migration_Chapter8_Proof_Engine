import matplotlib.pyplot as plt
import numpy as np
import os

def generate_figure_8_1():
    """
    Reproduces Figure 8.1: The Survival Bridge.
    """
    intensities = np.linspace(0, 10, 100)
    legacy_costs = np.full_like(intensities, 0.20)
    # Dividend scales with intensity
    mcp_costs = 0.20 - 0.12 * (intensities / 10.0) * 0.6
    
    plt.figure(figsize=(10, 6))
    plt.plot(intensities, legacy_costs, 'r--', label='Legacy Market Rate (0.20 €/kWh)')
    plt.plot(intensities, mcp_costs, 'b-', label='MCP-Optimized Rate (2030 Roadmap)')
    plt.axhline(y=0.15, color='orange', linestyle=':', label='Mittelstand Death Zone (0.15 €/kWh)')
    
    plt.xlabel('Energy Intensity (kWh/€ GVA)')
    plt.ylabel('Net Energy Cost (€/kWh)')
    plt.title('Figure 8.1: The Survival Bridge')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('plots/energy_intensity_vs_protocol_offset.png')
    plt.close()

def generate_figure_8_2():
    """
    Reproduces Figure 8.2: The Leakage Illusion.
    """
    categories = ["DE Best", "DE Avg", "Global Destination"]
    intensities = [0.6, 1.0, 1.8]
    
    plt.figure(figsize=(10, 6))
    colors = ['green', 'orange', 'red']
    plt.bar(categories, intensities, color=colors, alpha=0.7)
    
    plt.title('Figure 8.2: The Leakage Illusion')
    plt.xlabel('Region')
    plt.ylabel('CO2 Intensity (t/t steel)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('plots/carbon_leakage_recovery.png')
    plt.close()

def generate_industrial_migration_projection():
    """
    Generates a projection of the Industrial Migration concept.
    """
    years = np.arange(2025, 2036)
    migration_legacy = 100 * np.exp(0.1 * (years - 2025))
    migration_mcp = 100 * np.exp(0.02 * (years - 2025))
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, migration_legacy, 'r--', label='Legacy Relocation Pressure')
    plt.plot(years, migration_mcp, 'b-', label='MCP-Stabilized Industrial Core')
    plt.title('2030 Industrial Migration Projection')
    plt.xlabel('Year')
    plt.ylabel('Relocation Index (2025=100)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('plots/industrial_migration_projection.png')
    plt.close()

if __name__ == "__main__":
    os.makedirs('plots', exist_ok=True)
    generate_figure_8_1()
    generate_figure_8_2()
    generate_industrial_migration_projection()
    print("Chapter 8 figures generated successfully in plots/ directory.")
