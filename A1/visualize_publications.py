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

# Create comprehensive visualization dashboard with all plots
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        'Total Publications by Department',
        'Publications Over Time by Faculty',
        'Publication Distribution (Histogram)',
        'Top 15 Most Productive Researchers',
        'Individual Publications by Year and Department',
        'Hierarchical Treemap: Faculty → Department → Researcher'
    ),
    specs=[
        [{"type": "bar"}, {"type": "scatter"}],
        [{"type": "histogram"}, {"type": "bar"}],
        [{"type": "scatter"}, {"type": "treemap"}]
    ],
    vertical_spacing=0.10,
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

# 5. Scatter plot for individual analysis
for dept in df['department'].unique():
    dept_data = df[df['department'] == dept]
    fig.add_trace(
        go.Scatter(
            x=dept_data['year'],
            y=dept_data['pubs'],
            mode='markers',
            name=dept.split('(')[0].strip(),
            marker=dict(size=dept_data['pubs'], sizemode='diameter', sizeref=0.5, sizemin=3),
            text=dept_data['name'],
            hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Publications: %{y}<extra></extra>'
        ),
        row=3, col=1
    )

# 6. Treemap for hierarchical view
sunburst_data = df.groupby(['faculty', 'department', 'name'])['pubs'].sum().reset_index()

# Create labels and parents for treemap
labels = ['PSU']
parents = ['']
values = [0]
colors = [0]

for faculty in sunburst_data['faculty'].unique():
    labels.append(faculty.split('(')[0].strip())
    parents.append('PSU')
    faculty_total = sunburst_data[sunburst_data['faculty'] == faculty]['pubs'].sum()
    values.append(faculty_total)
    colors.append(faculty_total)
    
    for dept in sunburst_data[sunburst_data['faculty'] == faculty]['department'].unique():
        dept_name = dept.split('(')[0].strip()
        labels.append(dept_name)
        parents.append(faculty.split('(')[0].strip())
        dept_total = sunburst_data[sunburst_data['department'] == dept]['pubs'].sum()
        values.append(dept_total)
        colors.append(dept_total)
        
        dept_data = sunburst_data[sunburst_data['department'] == dept]
        for _, row in dept_data.iterrows():
            labels.append(row['name'])
            parents.append(dept_name)
            values.append(row['pubs'])
            colors.append(row['pubs'])

fig.add_trace(
    go.Treemap(
        labels=labels,
        parents=parents,
        values=values,
        marker=dict(
            colorscale='RdYlGn',
            cmid=sum(colors)/len(colors),
            colorbar=dict(title="Publications")
        ),
        hovertemplate='<b>%{label}</b><br>Publications: %{value}<extra></extra>'
    ),
    row=3, col=2
)

# Update layout
fig.update_layout(
    title_text="<b>Pendelton State University (PSU) - Publication Statistics Dashboard</b>",
    title_x=0.5,
    title_font_size=20,
    showlegend=True,
    height=1400,
    hovermode='closest'
)

# Update axes labels
fig.update_xaxes(title_text="Total Publications", row=1, col=1)
fig.update_xaxes(title_text="Year", row=1, col=2)
fig.update_xaxes(title_text="Number of Publications", row=2, col=1)
fig.update_xaxes(title_text="Total Publications", row=2, col=2)
fig.update_xaxes(title_text="Year", row=3, col=1)

fig.update_yaxes(title_text="Department", row=1, col=1)
fig.update_yaxes(title_text="Publications", row=1, col=2)
fig.update_yaxes(title_text="Frequency", row=2, col=1)
fig.update_yaxes(title_text="Researcher", row=2, col=2)
fig.update_yaxes(title_text="Publications", row=3, col=1)

# Save the comprehensive dashboard
fig.write_html('publications_dashboard.html')
print("Comprehensive dashboard saved as 'publications_dashboard.html'")

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
print("Visualization complete! Open 'publications_dashboard.html' to view all plots.")
print("=" * 60)
