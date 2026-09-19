import streamlit as st
import pandas as pd
from data_loader import (
    get_provinces, get_rivers, get_structures, get_links, get_confluences,
    get_socioeconomic, get_agroeconomic, get_geopolitical,
    get_india_projects, get_china_hydropower, get_legal_mechanisms,
    get_diamer_bhasha, get_sources
)
from map_view import water_system_map
from network_view import river_network
from hydraulic_model import run_scenario
from domain_views import domain_summary, china_portfolio_chart, india_design_table, legal_pathway

st.set_page_config(
    page_title="Pakistan Water, River & Geopolitical Dashboard",
    page_icon="🌊",
    layout="wide",
)

st.title("🌊 Pakistan Water, River & Geopolitical Dashboard")
st.caption(
    "Interactive reference dashboard covering Pakistan's provinces/regions, major river systems, "
    "water infrastructure, socio-economic and agro-economic dimensions, hydro-politics, "
    "inter-provincial water governance, Chinese hydropower investment, and Indus Waters Treaty cases."
)

st.warning(
    "This is an informational engineering/civic research dashboard. It distinguishes documented facts "
    "from claims or positions attributed to Pakistan, India, provincial stakeholders, or other sources. "
    "Coordinates are representative and are not survey-grade GIS."
)

with st.sidebar:
    st.header("Filters")
    province = st.selectbox(
        "Province / Region",
        ["All"] + get_provinces()
    )
    river = st.selectbox(
        "River",
        ["All"] + sorted(get_rivers()["name"].unique().tolist())
    )
    st.divider()
    st.header("Scenario explorer")
    flow_change = st.slider(
        "Illustrative flow change (%)", -50, 50, 0,
        help="A transparent what-if calculation, not a forecast or observed-flow claim."
    )
    storage = st.slider("Illustrative available storage (%)", 0, 100, 70)
    demand = st.slider("Illustrative demand (%)", 50, 150, 100)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "🗺️ Water System",
    "📈 Socio-Economic",
    "🌾 Agro-Economic",
    "🌐 Geo-Political & Strategic",
    "🇨🇳 China Hydropower",
    "🇮🇳 Chenab Projects & IWT",
    "⚖️ Legal / IRSA",
    "🏗️ Diamer-Bhasha",
])

rivers = get_rivers()
structures = get_structures()
links = get_links()
confluences = get_confluences()

def filter_df(df):
    out = df.copy()
    if province != "All":
        out = out[out["province_region"].str.contains(province, case=False, na=False)]
    if river != "All" and "river" in out.columns:
        out = out[out["river"].str.contains(river, case=False, na=False)]
    return out

with tab1:
    st.subheader("Provinces / Regions and Water Infrastructure")
    pcols = st.columns(7)
    for i, p in enumerate(get_provinces()):
        pcols[i].metric(p, int((rivers["province_region"].str.contains(p, na=False)).sum()))

    st.markdown("### Interactive reference map")
    st.plotly_chart(
        water_system_map(filter_df(rivers), filter_df(structures), filter_df(links), filter_df(confluences)),
        use_container_width=True
    )

    st.markdown("### Rivers")
    st.dataframe(
        filter_df(rivers)[[
            "name","river_system","province_region","type","upstream","downstream","confluences","notes"
        ]],
        use_container_width=True, hide_index=True
    )

    st.markdown("### Dams, barrages and other control structures")
    st.dataframe(
        filter_df(structures)[[
            "asset_type","name","river","province_region","status","upstream","downstream","notes"
        ]],
        use_container_width=True, hide_index=True
    )

    st.markdown("### Link canals")
    st.dataframe(
        filter_df(links)[[
            "name","source_river","receiving_river","offtake","outfall","province_region","status","notes"
        ]],
        use_container_width=True, hide_index=True
    )

    st.markdown("### River confluences")
    st.dataframe(filter_df(confluences), use_container_width=True, hide_index=True)

    st.markdown("### Conceptual river network")
    st.plotly_chart(river_network(), use_container_width=True)

with tab2:
    st.subheader("📈 Socio-Economic Domain")
    st.write(
        "Water infrastructure and river reliability interact with food security, employment, "
        "urban growth, tourism, domestic/industrial utility, climate vulnerability and energy generation."
    )
    st.dataframe(get_socioeconomic(), use_container_width=True, hide_index=True)
    st.plotly_chart(domain_summary(get_socioeconomic(), "Socio-Economic Domain"), use_container_width=True)

with tab3:
    st.subheader("🌾 Agro-Economic Domain")
    st.write(
        "The Indus Basin Irrigation System (IBIS) is described by the World Bank as the world's "
        "largest contiguous surface-water irrigation system. The dashboard therefore treats irrigation, "
        "crop cultivation, rural livelihoods, GDP/employment linkages and water reliability as connected topics."
    )
    st.dataframe(get_agroeconomic(), use_container_width=True, hide_index=True)
    st.plotly_chart(domain_summary(get_agroeconomic(), "Agro-Economic Domain"), use_container_width=True)

with tab4:
    st.subheader("🌐 Geo-Political & Strategic Domains")
    st.dataframe(get_geopolitical(), use_container_width=True, hide_index=True)
    st.markdown("### Internal inter-provincial water dispute: Punjab and Sindh")
    st.markdown(
        """
**Sindh's position (attributed):** Lower-riparian stakeholders have raised concerns about
water availability, distribution, shortages at downstream locations and the operation of
upstream infrastructure.

**Punjab's position (attributed):** Upper-riparian stakeholders have raised concerns about
overall system accounting, allocations, reservoir operations, shortages, and the need to
manage water for multiple provinces and sectors.

The dashboard does not select a winner. It presents the dispute as a governance and
water-accounting issue involving IRSA, provincial governments and constitutional institutions.
"""
    )
    st.markdown("### Kashmir and maritime infrastructure")
    st.info(
        "The Kashmir hydro-politics section is presented as a treaty, infrastructure and "
        "river-basin governance topic. Maritime trade infrastructure is included as a strategic "
        "context because the Indus system ultimately reaches the Arabian Sea and Pakistan's "
        "water/energy economy connects with ports and trade corridors."
    )

with tab5:
    st.subheader("🇨🇳 Financial Footprint of China's Hydropower Investments")
    china = get_china_hydropower()
    st.dataframe(china, use_container_width=True, hide_index=True)
    st.plotly_chart(china_portfolio_chart(china), use_container_width=True)

    total_mw = china["capacity_mw"].sum()
    total_cost = china["official_project_cost_usd_m"].sum()
    c1, c2 = st.columns(2)
    c1.metric("Listed portfolio capacity", f"{total_mw:,.1f} MW")
    c2.metric("Project-cost figures in this table", f"${total_cost/1000:.2f} bn")

    st.info(
        "PPIB's June 30, 2026 CPEC table lists the four hydropower projects together as "
        "3,428 MW and US$7.419 billion. Individual project pages can show slightly different "
        "cost figures, so the dashboard retains the source figure beside each project rather "
        "than presenting the sum as a single audited investment total."
    )

with tab6:
    st.subheader("🇮🇳 Chenab Projects, Flow Concerns and Indus Waters Treaty")
    st.markdown("### Pakal Dul (1,000 MW) and Ratle (850 MW)")
    st.dataframe(get_india_projects(), use_container_width=True, hide_index=True)

    st.markdown("### Technical points raised by Pakistan in the IWT proceedings")
    st.dataframe(india_design_table(), use_container_width=True, hide_index=True)

    st.markdown("### Head Marala / crop-impact issue")
    st.write(
        "The dashboard records reported concerns about reduced Chenab flows at Head Marala and "
        "potential consequences for irrigation and crops as stakeholder claims, rather than "
        "asserting a causal crop-loss estimate without a hydrological dataset."
    )

    st.markdown("### Court of Arbitration (PCA) timeline")
    st.dataframe(
        pd.DataFrame([
            ["2016", "Pakistan instituted arbitration under Annexure G of the IWT.", "PCA case record"],
            ["2023", "Court issued an award on competence.", "PCA"],
            ["2025-06-27", "Supplemental Award on competence.", "PCA"],
            ["2025-08-08", "Award on issues of general interpretation of the IWT.", "PCA"],
            ["2025-11-08", "Decision on Pakistan's clarification request.", "PCA"],
            ["2026-05-15", "Award concerning maximum pondage.", "PCA"],
            ["2026-08-31", "Award concerning treaty status and order on interim measures concerning Ratle.", "PCA"],
        ], columns=["Date","Development","Source"]),
        use_container_width=True, hide_index=True
    )

    st.info(
        "The PCA case page states that the proceedings concern interpretation/application of the "
        "IWT to design elements of run-of-river hydro-electric projects on the western rivers. "
        "The PCA case record is the authoritative source for the procedural timeline shown here."
    )

with tab7:
    st.subheader("⚖️ Legal Mechanisms for Inter-Provincial Water Disputes")
    st.dataframe(get_legal_mechanisms(), use_container_width=True, hide_index=True)
    st.plotly_chart(legal_pathway(), use_container_width=True)
    st.markdown(
        """
### Governance pathway represented in the dashboard

**IRSA / technical process → provincial/federal consultation → Council of Common Interests (CCI)
under Article 155 → constitutional/legal review where applicable.**

Article 155 provides a constitutional route for complaints where the interests of a province,
the Federal Capital or inhabitants in water from a natural source or reservoir are prejudicially
affected. The CCI's official site describes its role in water disputes under Article 155.

The dashboard does not treat the phrase "veto power" as an unlimited legal veto. It instead
separates institutional roles, voting/consensus questions and formal constitutional mechanisms.
"""
    )

with tab8:
    st.subheader("🏗️ Diamer-Bhasha Dam: Engineering, Storage and Economic Context")
    st.dataframe(get_diamer_bhasha(), use_container_width=True, hide_index=True)
    st.markdown(
        """
**Engineering / progress:** WAPDA identifies the project on the Indus near Chilas, at the
GB/KP interface, with an RCC dam, 8.1 MAF gross storage, 6.4 MAF live storage and 4,500 MW
installed generation.

**Strategic storage:** WAPDA and the Ministry of Water Resources describe the project in
terms of water, food and energy security, irrigation support and hydropower.

**Chinese engineering participation:** WAPDA lists PowerChina-FWO for the main dam contract
and a consultancy consortium that includes China Water Resources Beifang Investigation,
Design and Research Company.

**Power postponement:** official 2026 clarification from the Ministry of Economic Affairs
states that Pakistan has not cancelled the 4,500 MW power-generation component. The dashboard
therefore labels cancellation claims as disputed/incorrect according to that official statement.
"""
    )

st.divider()
st.subheader("🔬 Transparent what-if hydraulic indicator")
result = run_scenario(flow_change=flow_change, storage_percent=storage, demand_percent=demand)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Adjusted flow index", f"{result['flow_index']:.1f}")
c2.metric("Storage index", f"{result['storage_index']:.1f}")
c3.metric("Demand index", f"{result['demand_index']:.1f}")
c4.metric("Stress indicator", result["stress_label"])
st.caption(
    "This is an illustrative index for exploring relationships between flow, storage and demand. "
    "It is not a hydrological forecast, crop-loss model, treaty assessment, or operational water-allocation calculation."
)

st.divider()
st.subheader("📚 Sources")
for source_name, url in get_sources():
    st.markdown(f"- **{source_name}** — {url}")

st.caption(
    "Data structure is intentionally modular. Official GIS layers, PostGIS, river-discharge time series, "
    "reservoir levels, crop calendars and verified provincial datasets can be connected later."
)
