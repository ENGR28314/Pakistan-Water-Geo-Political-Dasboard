import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def domain_summary(df, title):
    # A simple count of thematic rows, not an impact score.
    counts = pd.DataFrame({"Theme": df.iloc[:,0].tolist(), "Items": [1]*len(df)})
    return px.bar(counts, x="Theme", y="Items", title=title + " — thematic coverage")

def china_portfolio_chart(df):
    return px.bar(
        df, x="project", y="capacity_mw", color="status",
        title="Chinese-linked hydropower portfolio listed in the dashboard",
        labels={"capacity_mw":"Installed capacity (MW)"}
    )

def india_design_table():
    return pd.DataFrame([
        ["Pondage capacity","Pakistan challenged how storage/pondage should be interpreted under the IWT rules for run-of-river projects.","Pakistan's position as presented in the proceedings","PCA awards and case documents should be read for the exact legal holding."],
        ["Freeboard / dam elevation","Pakistan raised concerns about design parameters and their relationship to treaty limits.","Pakistan's position","Treaty/design interpretation issue"],
        ["Deep-level outlets","Pakistan raised concerns about outlet configuration and possible implications for river flows.","Pakistan's position","Treaty/design interpretation issue"],
        ["Gated spillways","Pakistan raised concerns about spillway design and operation under IWT constraints.","Pakistan's position","Treaty/design interpretation issue"],
        ["Court of Arbitration","PCA issued competence, interpretation, pondage and 2026 treaty-status/Ratle-related decisions listed on its case page.","Documented procedural record","PCA case 2023-01"],
    ], columns=["technical_topic","description","attribution","interpretation_note"])

def legal_pathway():
    labels = ["IRSA / technical process","Provincial & federal consultation","CCI / Article 155","Judicial or constitutional review"]
    values = [1,1,1,1]
    fig = go.Figure(go.Funnel(y=labels, x=values, textinfo="text"))
    fig.update_layout(title="Illustrative legal/governance pathway — not a mandatory sequence in every dispute")
    return fig
