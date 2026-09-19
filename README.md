# Pakistan Water, River & Geopolitical Dashboard

## Purpose

A modular Streamlit research dashboard covering:

- Gilgit-Baltistan
- Khyber Pakhtunkhwa (KPK)
- Punjab
- Sindh
- Balochistan
- Azad Jammu and Kashmir (AJK)
- Islamabad Capital Territory (ICT)
- Major rivers, tributaries and confluences
- Dams and barrages/headworks
- Link canals
- Upstream/downstream relationships
- Socio-economic themes
- Agro-economic themes and IBIS
- Geo-political and strategic context
- Punjab–Sindh inter-provincial water disputes
- IRSA/CCI/legal mechanisms
- Chinese-linked hydropower projects
- Karot 720 MW
- Suki Kinari 884 MW
- Kohala 1,124 MW
- Azad Pattan 700.7 MW
- Diamer-Bhasha Dam: storage, hydropower, engineering and financing context
- Pakal Dul 1,000 MW and Ratle 850 MW
- Indus Waters Treaty (IWT) Court of Arbitration proceedings
- An illustrative, explicitly non-operational flow/storage/demand scenario

## Important neutrality and evidence rule

This application is intended as an informational engineering/civic research tool. It does not
endorse a political position.

Claims such as "devastating crop impacts", "deadlock", "veto", or "dominant FDI share" can be
contested or depend on definitions and dates. The app therefore uses attribution and source notes
instead of presenting contested conclusions as established facts.

## Installation

Python 3.11+ recommended.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Files

- app.py — main Streamlit dashboard
- data_loader.py — core reference data
- coordinates.py — representative map coordinates
- map_view.py — interactive water map
- network_view.py — river-network schematic
- hydraulic_model.py — transparent educational what-if indicator
- domain_views.py — domain charts and legal/design tables
- socio_economic.py — socio-economic module
- agro_economic.py — agro-economic module
- geopolitical_strategic.py — strategic domain module
- china_hydropower.py — Chinese hydropower portfolio module
- india_iwt.py — India/IWT module
- legal_mechanisms.py — IRSA/CCI/legal module
- diamer_bhasha.py — Diamer-Bhasha module

## Official/reference sources used

1. PCA, Indus Waters Western Rivers Arbitration (Pakistan v. India):
   https://pca-cpa.org/en/cases/284/
2. PPIB CPEC projects, updated June 30, 2026:
   https://www.ppib.gov.pk/cpec.html
3. CPEC Energy Projects:
   https://cpec.gov.pk/energy
4. CPEC Karot:
   https://cpec.gov.pk/project-details/16
5. CPEC Suki Kinari:
   https://cpec.gov.pk/project-details/15
6. CPEC Kohala:
   https://www.cpec.gov.pk/project-details/23
7. CPEC Azad Pattan:
   https://cpec.gov.pk/project-details/91
8. WAPDA Diamer-Bhasha:
   https://wapda.gov.pk/diamer-basha-dam-project/
9. Ministry of Economic Affairs clarification, 29 Aug 2026:
   https://www.ead.gov.pk/NewsDetail/ODI1M2E0ODYtMjkyMi00NzdkLWE2ODQtMDk5NWIwZGY4YmE1
10. Council of Common Interests:
   https://www.cci.gov.pk/Detail/NDZhY2I2ZDUtZTgzNy00MWEzLWE2M2ItZjU2NTkyODc4ZGJm
11. World Bank — Pakistan Indus Basin groundwater:
   https://www.worldbank.org/en/news/feature/2021/03/25/managing-groundwater-resources-in-pakistan-indus-basin

## Data limitations

The coordinates are representative visualization coordinates and are not survey-grade GIS.
The river and infrastructure tables are a major-feature reference inventory, not a complete
national asset registry.

For a production engineering/GIS edition, connect verified GeoJSON/Shapefile/GeoPackage layers,
PostGIS, official discharge and reservoir time series, provincial crop calendars, canal command
areas, and source/version metadata for every record.

## Compiled files

Python's normal compiled artifacts are `.pyc` files under `__pycache__`, with names such as
`coordinates.cpython-311.pyc`. They are interpreter-version-specific and are not required to
run the Streamlit source application. The release ZIP includes compiled files for convenience.
