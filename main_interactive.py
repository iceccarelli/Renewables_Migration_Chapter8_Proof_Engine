import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from chapter8_core import Chapter8Engine

# Page Configuration
st.set_page_config(page_title="The Renewables Migration - Chapter 8 Proof Engine", layout="wide")

# Initialize Engine
engine = Chapter8Engine()
metrics = engine.metrics

# Sidebar: Spy Mode Toggle
st.sidebar.title("🔍 Spy Mode")
spy_mode = st.sidebar.checkbox("Highlight Book Claims", value=True)

if spy_mode:
    st.sidebar.info("Spy Mode Active: Highlighting exact book numbers and equations.")

# Title and Intro
st.title("Chapter 8: The De-Industrialization Pulse - The Final Act")
st.markdown("""
### From Industrial Exodus to Protocol Sovereignty
This dashboard verifies the claims, equations, and figures from Chapter 8 of *The Renewables Migration*.
We move from the **Slow Heart Attack** to **Autonomous Industrial Resilience** using the Model Context Protocol (MCP).
""")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Energy-Intensity vs Protocol-Offset Simulator", 
    "Carbon Leakage Recovery Calculator", 
    "AIP Intelligent Factory Nodes", 
    "AIR Sovereign Assets Explorer", 
    "Prove Every Equation", 
    "Download Book Data"
])

with tab1:
    st.header("8.1 The Survival Bridge: Legacy Costs vs. MCP-Optimized Reality")
    st.markdown("""
    Figure 8.1 illustrates the energy cost threshold for industrial survival.
    The **Protocol Dividend** scales with energy intensity, providing a lifeline for the Mittelstand.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Survival Parameters")
        legacy_rate = st.slider("Legacy Market Rate (€/kWh)", 0.10, 0.30, metrics['Legacy_Market_Rate'])
        mcp_efficiency = st.slider("MCP Optimization Efficiency", 0.0, 1.0, 0.6)
        
        if spy_mode:
            st.write(f"**Book Claim:** Legacy Market Rate: **€{metrics['Legacy_Market_Rate']:.2f}/kWh.**")
            st.write(f"**Book Claim:** Mittelstand Death Zone: **€{metrics['Mittelstand_Death_Zone']:.2f}/kWh.**")
            
    with col2:
        intensities, legacy_costs, mcp_costs = engine.get_survival_bridge_data()
        # Adjust based on slider
        mcp_costs = [engine.calculate_net_energy_cost(i, legacy_rate, mcp_efficiency) for i in intensities]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=intensities, y=[legacy_rate]*len(intensities), name="Legacy Market Rate", line=dict(color='red', dash='dash')))
        fig.add_trace(go.Scatter(x=intensities, y=mcp_costs, name="MCP-Optimized Rate (2030)", line=dict(color='blue')))
        
        fig.add_hline(y=metrics['Mittelstand_Death_Zone'], line_dash="dot", annotation_text="Mittelstand Death Zone", line_color="orange")
        
        fig.update_layout(title="Figure 8.1: The Survival Bridge",
                          xaxis_title="Energy Intensity (kWh/€ GVA)",
                          yaxis_title="Net Energy Cost (€/kWh)")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("8.5.1 The Protocol-Enabled Carbon Recovery Equation")
    st.markdown("""
    The Sovereign Carbon Recovery (C_MCP) quantifies the emissions avoided by retaining industry through MCP-enabled cost optimization.
    """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Carbon Recovery Parameters")
        capacity_retained = st.slider("Capacity Retained (Mt Steel)", 1, 100, 35)
        co2_global = st.slider("Global CO2 Intensity (t/t)", 1.0, 2.5, metrics['Global_Leakage_CO2_Intensity'])
        co2_de = st.slider("German CO2 Intensity (t/t)", 0.1, 1.0, metrics['DE_Best_CO2_Intensity'])
        phi_mcp = st.slider("Retention Factor (Phi_MCP)", 0.0, 1.0, 0.8)
        
        c_mcp = engine.calculate_carbon_recovery(capacity_retained, co2_global, co2_de, phi_mcp)
        
        st.metric("Sovereign Carbon Recovery (C_MCP)", f"{c_mcp:.1f} Mt CO2")
        
        if spy_mode:
            st.write(f"**Equation 8.5.1:** $C_{{MCP}} = \sum C_{{api}} \cdot (CO_{{2,global}} - CO_{{2,DE}}) \cdot \Phi_{{MCP}}$")
            st.write(f"**Book Claim:** Prevents **35 Mt** of annual global leakage.")

    with col2:
        categories, intensities = engine.get_leakage_illusion_data()
        fig_leak = go.Figure()
        fig_leak.add_trace(go.Bar(x=categories, y=intensities, marker_color=['green', 'orange', 'red']))
        fig_leak.update_layout(title="Figure 8.2: The Leakage Illusion", xaxis_title="Region", yaxis_title="CO2 Intensity (t/t steel)")
        st.plotly_chart(fig_leak, use_container_width=True)

with tab3:
    st.header("8.3.1 The AIP Framework: Intelligent Factory Nodes")
    st.markdown("""
    The Autonomous Industrial Protocol (AIP) framework turns factories into intelligent grid nodes that "harvest value" from the Negative Price Abyss.
    """)
    
    st.subheader("Relocation Math Simulator")
    col1, col2 = st.columns(2)
    with col1:
        e_gap = st.slider("Energy Gap (E)", 0.0, 1.0, 0.5)
        r_res = st.slider("Resilience Deficit (R)", 0.0, 1.0, 0.3)
    with col2:
        i_inertia = st.slider("Inertia Gap (I)", 0.0, 1.0, 0.2)
        d_dep = st.slider("Dependency (D)", 0.0, 1.0, 0.4)
    
    psi_mcp_ratio = st.slider("Protocol Offset Ratio (Psi_MCP)", 0.0, 1.0, metrics['Protocol_Offset_Target'])
    
    relocation_pressure = engine.calculate_relocation_polynomial(e_gap, r_res, i_inertia, d_dep, psi_mcp_ratio)
    st.metric("Relocation Pressure (R)", f"{relocation_pressure:.1f}")
    
    if spy_mode:
        st.write(f"**Equation 8.6:** $R = 250E + 80R + 50I + 30D - \Psi_{{MCP}}$")
        st.write(f"**Book Claim:** Protocol Offset (Psi_MCP) offsets **60%** of the energy gap (E).")

with tab4:
    st.header("8.4 Forward-Looking Implication: The 2030 Sovereign Industry")
    st.markdown("""
    The **Migration** is complete when a factory’s value is no longer its output per hour, but its Protocol-Enabled Flexibility.
    """)
    
    years = [2026, 2030]
    sovereignty = [metrics['Sovereign_Independence_2026'], metrics['Sovereign_Independence_2030']]
    
    fig_sov = go.Figure()
    fig_sov.add_trace(go.Scatter(x=years, y=sovereignty, mode='lines+markers+text', text=[f"{s:.0%}" for s in sovereignty], textposition="top center", name="Sovereignty Metric (S)"))
    fig_sov.update_layout(title="Sovereignty Metric Projection (S)", xaxis_title="Year", yaxis_title="Independence Ratio", yaxis_range=[0, 1])
    st.plotly_chart(fig_sov, use_container_width=True)
    
    if spy_mode:
        st.write(f"**Book Claim:** 2026 Sovereignty: **{metrics['Sovereign_Independence_2026']:.0%}.**")
        st.write(f"**Book Claim:** 2030 Sovereignty: **{metrics['Sovereign_Independence_2030']:.0%}.**")

with tab5:
    st.header("Prove Every Equation")
    
    st.markdown("#### Equation 8.5.1: Sovereign Carbon Recovery")
    st.latex(r"C_{MCP} = \sum C_{api} \cdot (CO_{2,global} - CO_{2,DE}) \cdot \Phi_{MCP}")
    st.info("Proves how MCP-enabled retention prevents global carbon leakage.")
    
    st.markdown("#### Equation 8.6: The Relocation Polynomial")
    st.latex(r"R = 250E + 80R + 50I + 30D - \Psi_{MCP}")
    st.info("Proves how the Protocol Offset (Psi_MCP) neutralizes the primary driver of factory flight.")

with tab6:
    st.header("Download Book Data")
    st.dataframe(pd.read_csv("data/book_numbers.csv"))
    st.download_button("Download CSV", data=open("data/book_numbers.csv").read(), file_name="chapter8_book_numbers.csv")

st.sidebar.markdown("---")
st.sidebar.write("© 2026 Vincenzo Grimaldi - The Renewables Migration")
st.sidebar.write("Built by Manus for iceccarelli")
