import json
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Load the data
with open('publications-stats.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(data)

# Data exploration
print("=" * 60)
print("DATA OVERVIEW")
print("=" * 60)
print(f"Total number of records: {len(df)}")
print(f"Years covered: {df['year'].min()} - {df['year'].max()}")
print(f"Number of unique researchers: {df['id'].nunique()}")
print(f"Total publications: {df['pubs'].sum()}")
print(f"\nDepartments: {df['department'].nunique()}")
print(df['department'].unique())
print(f"\nFaculties: {df['faculty'].nunique()}")
print(df['faculty'].unique())
print("\n")

# Create comprehensive visualization dashboard
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Total Publications by Department',
        'Publications Over Time by Faculty',
        'Publication Distribution (Histogram)',
        'Top 15 Most Productive Researchers'
    ),
    specs=[
        [{"type": "bar"}, {"type": "scatter"}],
        [{"type": "histogram"}, {"type": "bar"}]
    ],
    vertical_spacing=0.12,
    horizontal_spacing=0.12
)

# 1. Publications by Department (Total)
dept_pubs = df.groupby('department')['pubs'].sum().sort_values(ascending=True)
fig.add_trace(
    go.Bar(
        y=[d.split('(')[0].strip() for d in dept_pubs.index],
        x=dept_pubs.values,
        orientation='h',
        marker=dict(color='#1f77b4'),
        name='Publications',
        hovertemplate='<b>%{y}</b><br>Total: %{x}<extra></extra>'
    ),
    row=1, col=1
)

# 2. Publications Over Time by Faculty
time_faculty = df.groupby(['year', 'faculty'])['pubs'].sum().reset_index()
for faculty in time_faculty['faculty'].unique():
    faculty_data = time_faculty[time_faculty['faculty'] == faculty]
    fig.add_trace(
        go.Scatter(
            x=faculty_data['year'],
            y=faculty_data['pubs'],
            mode='lines+markers',
            name=faculty.split('(')[1].replace(')', ''),
            hovertemplate='<b>%{fullData.name}</b><br>Year: %{x}<br>Publications: %{y}<extra></extra>'
        ),
        row=1, col=2
    )

# 3. Publication Distribution (Histogram)
fig.add_trace(
    go.Histogram(
        x=df['pubs'],
        nbinsx=20,
        marker=dict(color='#2ca02c'),
        name='Distribution',
        hovertemplate='Publications: %{x}<br>Count: %{y}<extra></extra>'
    ),
    row=2, col=1
)

# 4. Top 15 Most Productive Researchers
top_researchers = df.groupby('name')['pubs'].sum().sort_values(ascending=False).head(15)
fig.add_trace(
    go.Bar(
        y=top_researchers.index[::-1],
        x=top_researchers.values[::-1],
        orientation='h',
        marker=dict(color='#d62728'),
        name='Top Researchers',
        hovertemplate='<b>%{y}</b><br>Publications: %{x}<extra></extra>'
    ),
    row=2, col=2
)

# Update layout
fig.update_layout(
    title_text="<b>Pendelton State University (PSU) - Publication Statistics Dashboard</b>",
    title_x=0.5,
    title_font_size=20,
    showlegend=True,
    height=900,
    hovermode='closest'
)

# Update axes labels
fig.update_xaxes(title_text="Total Publications", row=1, col=1)
fig.update_xaxes(title_text="Year", row=1, col=2)
fig.update_xaxes(title_text="Number of Publications", row=2, col=1)
fig.update_xaxes(title_text="Total Publications", row=2, col=2)

fig.update_yaxes(title_text="Department", row=1, col=1)
fig.update_yaxes(title_text="Publications", row=1, col=2)
fig.update_yaxes(title_text="Frequency", row=2, col=1)
fig.update_yaxes(title_text="Researcher", row=2, col=2)

# Save the visualization
fig.write_html('publications_dashboard.html')
print("Dashboard saved as 'publications_dashboard.html'")

# Create a treemap for hierarchical perspective
sunburst_data = df.groupby(['faculty', 'department', 'name'])['pubs'].sum().reset_index()
fig_treemap = px.treemap(
    sunburst_data,
    path=['faculty', 'department', 'name'],
    values='pubs',
    title='<b>Treemap View: Faculty → Department → Researcher</b>',
    color='pubs',
    color_continuous_scale='RdYlGn',
    hover_data={'pubs': ':,'}
)

fig_treemap.update_layout(
    height=800,
    title_x=0.5,
    title_font_size=20
)

fig_treemap.write_html('publications_treemap.html')
print("Treemap saved as 'publications_treemap.html'")

# Create scatter plot for individual analysis
fig_scatter = px.scatter(
    df,
    x='year',
    y='pubs',
    color='department',
    hover_data=['name', 'faculty'],
    title='<b>Individual Publications by Year and Department</b>',
    labels={'pubs': 'Number of Publications', 'year': 'Year'},
    size='pubs',
    size_max=15
)

fig_scatter.update_layout(
    height=700,
    title_x=0.5,
    title_font_size=20,
    hovermode='closest'
)

fig_scatter.write_html('publications_scatter.html')
print("Scatter plot saved as 'publications_scatter.html'")

# Generate summary statistics
print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print("\nPublications by Department:")
dept_stats = df.groupby('department')['pubs'].agg(['sum', 'mean', 'count'])
dept_stats.columns = ['Total', 'Average', 'Researchers']
print(dept_stats.sort_values('Total', ascending=False))

print("\nPublications by Faculty:")
faculty_stats = df.groupby('faculty')['pubs'].agg(['sum', 'mean', 'count'])
faculty_stats.columns = ['Total', 'Average', 'Researchers']
print(faculty_stats.sort_values('Total', ascending=False))

print("\nPublications by Year:")
year_stats = df.groupby('year')['pubs'].agg(['sum', 'mean', 'count'])
year_stats.columns = ['Total', 'Average', 'Researchers']
print(year_stats)

print("\n" + "=" * 60)
print("Visualization complete! Open the HTML files in a browser to view.")
print("=" * 60)
