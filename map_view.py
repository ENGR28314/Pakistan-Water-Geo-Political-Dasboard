import plotly.graph_objects as go
from coordinates import ASSET_COORDINATES

def _coord(name):
    return ASSET_COORDINATES.get(name, (30.5, 71.5))

def water_system_map(rivers, structures, links, confluences):
    fig = go.Figure()
    paths = {
        "Indus": [(35.9,74.58),(34.08,72.70),(33.99,72.24),(32.44,71.39),(30.70,70.65),(28.43,69.74),(27.71,68.86),(25.38,68.31)],
        "Jhelum": [(34.37,73.47),(33.15,73.65),(32.77,73.45),(31.24,72.12)],
        "Chenab": [(32.67,74.46),(32.41,73.75),(32.22,73.75),(31.24,72.12),(29.35,71.05)],
        "Ravi": [(32.67,74.20),(31.22,73.84),(30.49,72.21),(29.35,71.05)],
        "Sutlej": [(30.66,73.08),(29.91,72.26),(29.35,71.05)],
        "Kabul": [(34.15,71.78),(33.99,72.24)],
        "Swat": [(35.00,72.35),(34.15,71.78)],
    }
    selected = set(rivers["name"])
    for name, coords in paths.items():
        if name not in selected:
            continue
        fig.add_trace(go.Scattermap(
            lat=[x[0] for x in coords], lon=[x[1] for x in coords],
            mode="lines", name=name, line=dict(width=4),
            hovertemplate=f"{name}<extra></extra>"
        ))

    def points(df, label):
        if df.empty:
            return
        lat, lon, txt = [], [], []
        for _, r in df.iterrows():
            y, x = _coord(r["name"])
            lat.append(y); lon.append(x); txt.append(r["name"])
        fig.add_trace(go.Scattermap(
            lat=lat, lon=lon, mode="markers+text", text=txt,
            textposition="top center", name=label,
            marker=dict(size=9),
            hovertemplate="%{text}<extra></extra>"
        ))

    points(structures[structures["asset_type"]=="Dam"], "Dams")
    points(structures[structures["asset_type"]=="Barrage"], "Barrages")
    points(confluences, "Confluences")

    fig.update_layout(
        map=dict(style="open-street-map", center=dict(lat=30.8, lon=71.5), zoom=4.8),
        height=700, margin=dict(l=0,r=0,t=0,b=0)
    )
    return fig
