import pandas as pd

PROVINCES = [
    "Gilgit-Baltistan",
    "Khyber Pakhtunkhwa (KPK)",
    "Punjab",
    "Sindh",
    "Balochistan",
    "Azad Jammu and Kashmir (AJK)",
    "Islamabad Capital Territory (ICT)",
]

RIVERS = [
["Indus","Indus Basin","Gilgit-Baltistan; Khyber Pakhtunkhwa (KPK); Punjab; Sindh","Main river",
 "Upper Indus system","Arabian Sea / Indus Delta","Gilgit; Kabul; Kurram; Gomal; Panjnad",
 "Main trunk of Pakistan's Indus Basin."],
["Gilgit","Indus Basin","Gilgit-Baltistan","Tributary","Upper Gilgit-Baltistan","Indus near Bunji","Indus","Upper Indus tributary."],
["Shyok","Indus Basin","Gilgit-Baltistan","Tributary","Upper Shyok basin","Indus system","Indus","Upper Indus tributary."],
["Shigar","Indus Basin","Gilgit-Baltistan","Tributary","Shigar valley","Indus near Skardu","Indus","Upper Indus tributary."],
["Kabul","Indus Basin","Khyber Pakhtunkhwa (KPK)","Tributary","Kabul basin","Indus near Attock","Indus","Major western tributary."],
["Swat","Indus Basin","Khyber Pakhtunkhwa (KPK)","Tributary","Upper Swat","Kabul near Charsadda","Kabul","Important KP river."],
["Kurram","Indus Basin","Khyber Pakhtunkhwa (KPK)","Tributary","Kurram valley","Indus system","Indus","Western tributary."],
["Gomal","Indus Basin","Khyber Pakhtunkhwa (KPK); Balochistan","Tributary","Gomal basin","Indus system","Indus","Cross-regional western tributary."],
["Jhelum","Indus Basin","Azad Jammu and Kashmir (AJK); Punjab","Main tributary","Kashmir/Jhelum headwaters","Trimmu/Punjab river system","Chenab","Regulated by Mangla/Rasul system."],
["Neelum","Indus Basin","Azad Jammu and Kashmir (AJK)","Tributary","Upper Neelum Valley","Jhelum at Muzaffarabad","Jhelum","Important AJK river."],
["Poonch","Indus Basin","Azad Jammu and Kashmir (AJK); Punjab","Tributary","Poonch region","Jhelum system","Jhelum","Tributary of the Jhelum system."],
["Chenab","Indus Basin","Punjab","Main tributary","Upper Chenab","Panjnad","Jhelum; Panjnad","Central Punjab river."],
["Ravi","Indus Basin","Punjab","Main tributary","Upper Ravi","Panjnad system","Chenab/Panjnad","Part of Punjab irrigation network."],
["Sutlej","Indus Basin","Punjab","Main tributary","Upper Sutlej","Panjnad","Chenab/Panjnad","Eastern river in the Punjab system."],
["Panjnad","Indus Basin","Punjab","Confluence channel","Punjab-river confluence system","Indus near Mithankot","Indus","Combined Punjab-river flow toward Indus."],
["Hub","Coastal basin","Balochistan; Sindh","River","Hub basin","Arabian Sea","Coastal drainage","Important local water-supply basin."],
["Hingol","Balochistan coastal basin","Balochistan","River","Balochistan uplands","Arabian Sea","Coastal drainage","Major Balochistan coastal river."],
["Dasht","Balochistan coastal basin","Balochistan","River","Central Balochistan","Arabian Sea/coastal basin","Coastal drainage","Major Balochistan river system."],
["Mula","Balochistan basin","Balochistan","River","Jhal Magsi region","Lower basin","Local drainage","Associated with Naulong project."],
["Gaj","Sindh local basin","Sindh","River","Kirthar Range","Lower Sindh","Local drainage","Associated with Nai Gaj project."],
]
RIVER_COLUMNS = ["name","river_system","province_region","type","upstream","downstream","confluences","notes"]

STRUCTURES = [
["Dam","Tarbela Dam","Indus","Khyber Pakhtunkhwa (KPK)","Operational","Upper Indus","Indus downstream","Storage/hydropower."],
["Dam","Diamer Bhasha Dam","Indus","Gilgit-Baltistan; Khyber Pakhtunkhwa (KPK)","Under construction","Upper Indus near Chilas","Indus toward Tarbela","Storage and hydropower project."],
["Dam","Mohmand Dam","Swat","Khyber Pakhtunkhwa (KPK)","Under construction","Swat River","Swat downstream","Flood, irrigation and hydropower objectives."],
["Dam","Warsak Dam","Kabul","Khyber Pakhtunkhwa (KPK)","Operational","Kabul River","Kabul downstream","Hydropower and irrigation."],
["Dam","Mangla Dam","Jhelum","Azad Jammu and Kashmir (AJK)","Operational","Upper Jhelum","Jhelum downstream","Major storage/hydropower."],
["Barrage","Nowshera Headworks","Kabul","Khyber Pakhtunkhwa (KPK)","Existing","Kabul upstream reach","Kabul downstream","Kabul control location."],
["Barrage","Chashma Barrage","Indus","Punjab","Operational","Indus upstream","Indus downstream","Associated with CJ Link."],
["Barrage","Rasul Barrage","Jhelum","Punjab","Operational","Jhelum upstream","Jhelum downstream","Major Jhelum control point."],
["Barrage","Marala Headworks","Chenab","Punjab","Operational","Chenab upstream","Chenab downstream","Associated with link canals."],
["Barrage","Khanki Barrage","Chenab","Punjab","Operational","Chenab upstream","Chenab downstream","Major Chenab control."],
["Barrage","Qadirabad Barrage","Chenab","Punjab","Operational","Chenab upstream","Chenab downstream","Major Chenab control."],
["Barrage","Trimmu Barrage","Chenab","Punjab","Operational","Chenab/Jhelum system","Lower Chenab","Major lower Chenab control."],
["Barrage","Balloki Headworks","Ravi","Punjab","Operational","Ravi upstream","Ravi downstream","Link-canal node."],
["Barrage","Sidhnai Barrage","Ravi","Punjab","Operational","Ravi upstream","Ravi downstream","Link-canal node."],
["Barrage","Sulemanki Barrage","Sutlej","Punjab","Operational","Sutlej upstream","Sutlej downstream","Sutlej irrigation control."],
["Barrage","Islam Barrage","Sutlej","Punjab","Operational","Sutlej upstream","Sutlej downstream","Sutlej control."],
["Barrage","Panjnad Barrage","Panjnad","Punjab","Operational","Punjab-river system","Indus system","Combined-river control."],
["Barrage","Taunsa Barrage","Indus","Punjab","Operational","Indus upstream","Indus downstream","Major Indus control."],
["Barrage","Guddu Barrage","Indus","Sindh","Operational","Indus upstream","Indus downstream","Major Sindh diversion."],
["Barrage","Sukkur Barrage","Indus","Sindh","Operational","Indus upstream","Indus downstream","Major Sindh irrigation structure."],
["Barrage","Kotri Barrage","Indus","Sindh","Operational","Indus upstream","Indus Delta/Arabian Sea","Lowest major barrage."],
]
STRUCTURE_COLUMNS = ["asset_type","name","river","province_region","status","upstream","downstream","notes"]

LINKS = [
["Chashma-Jhelum Link","Indus","Jhelum","Chashma Barrage","Jhelum system","Punjab; KPK","Operational","Inter-river transfer."],
["Rasul-Qadirabad Link","Jhelum","Chenab","Rasul Barrage","Qadirabad Barrage","Punjab","Operational","Jhelum-to-Chenab link."],
["Marala-Ravi Link","Chenab","Ravi","Marala Headworks","Ravi system","Punjab","Operational","Chenab-to-Ravi link."],
["Qadirabad-Balloki Link","Chenab","Ravi","Qadirabad Barrage","Balloki Headworks","Punjab","Operational","Chenab-to-Ravi link."],
["Balloki-Sulemanki Link","Ravi","Sutlej","Balloki Headworks","Sulemanki Barrage","Punjab","Operational","Ravi-to-Sutlej link."],
["Trimmu-Sidhnai Link","Chenab","Ravi","Trimmu Barrage","Sidhnai Barrage","Punjab","Operational","Chenab-to-Ravi transfer."],
["Taunsa-Panjnad Link","Indus","Panjnad","Taunsa Barrage","Panjnad Barrage","Punjab","Operational","Indus-to-Panjnad transfer."],
]
LINK_COLUMNS = ["name","source_river","receiving_river","offtake","outfall","province_region","status","notes"]

CONFLUENCES = [
["Indus + Kabul","Kabul","Indus","Near Attock","Khyber Pakhtunkhwa (KPK)","Kabul joins Indus."],
["Neelum + Jhelum","Neelum","Jhelum","Muzaffarabad","Azad Jammu and Kashmir (AJK)","Neelum joins Jhelum."],
["Swat + Kabul","Swat","Kabul","Charsadda region","Khyber Pakhtunkhwa (KPK)","Swat joins Kabul."],
["Jhelum + Chenab","Jhelum","Chenab","Trimmu/Jhang region","Punjab","Jhelum contributes to combined flow."],
["Sutlej + Chenab","Sutlej","Chenab","Panjnad","Punjab","Sutlej joins the Punjab-river system."],
["Panjnad + Indus","Panjnad","Indus","Near Mithankot","Punjab","Combined Punjab rivers join Indus."],
]
CONFLUENCE_COLUMNS = ["name","river_a","river_b","location","province_region","notes"]

def get_provinces(): return PROVINCES
def get_rivers(): return pd.DataFrame(RIVERS, columns=RIVER_COLUMNS)
def get_structures(): return pd.DataFrame(STRUCTURES, columns=STRUCTURE_COLUMNS)
def get_links(): return pd.DataFrame(LINKS, columns=LINK_COLUMNS)
def get_confluences(): return pd.DataFrame(CONFLUENCES, columns=CONFLUENCE_COLUMNS)

def get_socioeconomic():
    rows = [
        ["Food Security","Irrigation reliability supports crop production and food supply.","IBIS / river regulation","High basin dependence","World Bank IBIS sources"],
        ["Employment","Water-dependent agriculture and infrastructure create direct/indirect employment.","Agriculture, construction, services","High","World Bank / official project sources"],
        ["Urban Growth","Cities depend on rivers, reservoirs, canals and groundwater recharge.","Urban water / industry","High and location-specific","World Bank"],
        ["Tourism","Rivers, lakes, valleys and hydropower corridors support tourism economies.","GB, KP, AJK","Regional","Contextual domain"],
        ["Domestic & Industrial Utility","Urban and industrial systems depend on reliable freshwater supplies.","Municipal / industrial water","High","Water-sector literature"],
        ["Climate & Vulnerability","Floods, droughts, heat and changing precipitation affect water security.","All provinces/regions","High","World Bank / climate literature"],
        ["Energy Generation","Dams and run-of-river projects provide hydropower capacity.","Indus and tributary systems","High","WAPDA / CPEC / PPIB"],
    ]
    return pd.DataFrame(rows, columns=["domain","relationship","water_system","importance_context","source_note"])

def get_agroeconomic():
    rows = [
        ["Indus Basin Irrigation System (IBIS)","World Bank describes IBIS as the world's largest contiguous surface-water irrigation system.","Major rivers, barrages, canals","Food and water security","World Bank"],
        ["Crop Cultivation","Canal irrigation supports major crop zones, including wheat, rice, cotton and sugarcane regions.","Punjab, Sindh and irrigated areas","Water allocation affects cropping reliability","Agricultural/water literature"],
        ["Rural Livelihoods","Farm production, livestock and rural services depend on irrigation reliability.","Irrigated command areas","High","World Bank"],
        ["GDP Contribution","Agriculture is a major part of Pakistan's economy; water is a key production input.","National","Macro-economic linkage","Pakistan economic statistics should be added for a dated series"],
        ["Employment Contribution","Agriculture is a major source of employment; irrigation influences labor demand and farm activity.","National","Macro-economic linkage","Pakistan economic statistics should be added for a dated series"],
    ]
    return pd.DataFrame(rows, columns=["topic","documented_context","water_link","impact_context","source_note"])

def get_geopolitical():
    rows = [
        ["Hydro-politics of Kashmir","Jhelum/Chenab infrastructure intersects with the Kashmir dispute and the Indus Waters Treaty framework.","Jhelum, Chenab","Treaty and basin governance","PCA; CPEC/PPIB"],
        ["Indus Waters Treaty (IWT) Crisis","The PCA case record shows continuing arbitration over interpretation and hydro-project design, with 2025-2026 decisions listed.","Western rivers / IWT","Legal and diplomatic process","PCA case 2023-01"],
        ["Maritime Trade Infrastructure","The Indus reaches the Arabian Sea; ports and trade corridors form the downstream strategic context.","Sindh coast / Arabian Sea","Trade and logistics context","Strategic context"],
        ["Punjab-Sindh water dispute","Provincial positions differ over allocations, shortages, flows and upstream operations.","Indus / Sindh barrages","Domestic federation-province issue","CCI / IRSA framework"],
    ]
    return pd.DataFrame(rows, columns=["topic","description","geographic_scope","policy_context","source_note"])

def get_china_hydropower():
    rows = [
        ["Karot Hydropower Project",720,"Jhelum","AJK/Punjab",1698.26,"Operational","China Three Gorges / CSAIL; Chinese lenders listed by PPIB","PPIB/CPEC"],
        ["Suki Kinari (SK) Hydropower Station",884,"Kunhar","Khyber Pakhtunkhwa (KPK)",2000.0,"Operational","China Gezhouba Group; Chinese lenders listed by PPIB","CPEC/PPIB"],
        ["Kohala Hydropower Project",1124,"Jhelum","AJK",2400.0,"Pipeline / project on hold in PPIB June 2026 table","China Three Gorges / CWEI","PPIB/CPEC"],
        ["Azad Pattan Hydropower Project",700.7,"Jhelum","AJK/Punjab",1600.0,"Pipeline / project on hold in PPIB June 2026 table","China Gezhouba Group / Laraib Energy","PPIB/CPEC"],
    ]
    return pd.DataFrame(rows, columns=[
        "project","capacity_mw","river","province_region","official_project_cost_usd_m",
        "status","sponsor_or_financing_note","source"
    ])

def get_india_projects():
    rows = [
        ["Pakal Dul","1000","Chenab basin","India","Pakistan has raised IWT design objections in the western-rivers proceedings.","PCA / public reporting"],
        ["Ratle","850","Chenab","India","Pakistan has raised design objections; PCA proceedings include Ratle-related measures/status.","PCA / public reporting"],
    ]
    return pd.DataFrame(rows, columns=["project","capacity_mw","river_system","country","issue_summary","source"])

def get_legal_mechanisms():
    rows = [
        ["IRSA","Technical river-flow, allocation and system-management institution","Indus River System","Technical/administrative","IRSA framework"],
        ["Council of Common Interests (CCI)","Article 155 provides a constitutional complaint route for water-supply disputes between federation/provinces","Federation + provinces","Constitutional","CCI official site"],
        ["Constitutional / judicial review","Courts may become relevant where a justiciable legal question reaches the judicial system, subject to constitutional jurisdiction","Pakistan","Judicial","Constitutional framework"],
        ["International IWT mechanisms","Permanent Indus Commission and treaty dispute-resolution mechanisms; PCA arbitration is one track in the current western-rivers case","India-Pakistan","International treaty","PCA"],
    ]
    return pd.DataFrame(rows, columns=["mechanism","role","scope","type","source_note"])

def get_diamer_bhasha():
    rows = [
        ["Location","Indus River near Chilas; GB/KP area","WAPDA"],
        ["Dam type","Roller Compacted Concrete (RCC)","WAPDA"],
        ["Gross storage","8.1 MAF","WAPDA"],
        ["Live storage","6.4 MAF","WAPDA"],
        ["Installed power","4,500 MW","WAPDA / Ministry of Water Resources"],
        ["Annual generation","18,097 GWh (WAPDA project page)","WAPDA"],
        ["Main dam contractor","PowerChina-FWO JV","WAPDA"],
        ["Chinese engineering participation","China Water Resources Beifang Investigation, Design and Research Company is listed in the consultant JV","Ministry of Water Resources"],
        ["2026 power-component clarification","Ministry of Economic Affairs stated on 29 Aug 2026 that the 4,500 MW power component had not been cancelled","Economic Affairs Division"],
    ]
    return pd.DataFrame(rows, columns=["item","value","source"])

def get_sources():
    return [
        ("PCA — Indus Waters Western Rivers Arbitration (Pakistan v. India)", "https://pca-cpa.org/en/cases/284/"),
        ("PCA — June 2025 Supplemental Award on Competence", "https://pca-cpa.org/en/news/pca-press-release-pca-case-no-2023-01-proceedings-under-the-indus-waters-treaty-islamic-republic-of-pakistan-v-republic-of-india-3/"),
        ("PPIB — CPEC Projects (updated June 30, 2026)", "https://www.ppib.gov.pk/cpec.html"),
        ("CPEC — Energy Projects", "https://cpec.gov.pk/energy"),
        ("CPEC — Karot", "https://cpec.gov.pk/project-details/16"),
        ("CPEC — Suki Kinari", "https://cpec.gov.pk/project-details/15"),
        ("CPEC — Kohala", "https://www.cpec.gov.pk/project-details/23"),
        ("CPEC — Azad Pattan", "https://cpec.gov.pk/project-details/91"),
        ("WAPDA — Diamer Basha Dam", "https://wapda.gov.pk/diamer-basha-dam-project/"),
        ("Ministry of Economic Affairs — Diamer Basha clarification, 29 Aug 2026", "https://www.ead.gov.pk/NewsDetail/ODI1M2E0ODYtMjkyMi00NzdkLWE2ODQtMDk5NWIwZGY4YmE1"),
        ("CCI — Functions / Article 155", "https://www.cci.gov.pk/Detail/NDZhY2I2ZDUtZTgzNy00MWEzLWE2M2ItZjU2NTkyODc4ZGJm"),
        ("World Bank — Indus Basin groundwater / IBIS", "https://www.worldbank.org/en/news/feature/2021/03/25/managing-groundwater-resources-in-pakistan-indus-basin"),
    ]
