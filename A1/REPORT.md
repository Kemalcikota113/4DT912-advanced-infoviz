s# Task 1: Data Set Visualization Report

**Course:** 4DT912 - Advanced Information Visualization  
**Assignment:** Assignment 1  
**Date:** November 23, 2025

---

## 1. Data Overview

### 1.1 Data Description
The dataset contains publication statistics from **Pendelton State University (PSU)**, tracking research output across different organizational levels. The data is structured as a JSON array of researcher publication records.

### 1.2 Data Characteristics

**Structure:**
- **Format:** JSON array of objects
- **Total Records:** 199 researcher-year records
- **Time Period:** 2019-2020 (2 years)
- **Unique Researchers:** 199 individual researchers

**Variables:**
- `id`: Unique researcher identifier (string)
- `name`: Researcher's full name (string)
- `year`: Publication year (integer)
- `pubs`: Number of publications (integer)
- `department`: Academic department with abbreviation (string)
- `faculty`: Faculty/college affiliation (string)
- `university`: University name - Pendelton State University (string)

**Hierarchical Structure:**
```
University (PSU)
└── Faculty (3 faculties)
    └── Department (3 departments)
        └── Researcher (individual records)
```

**Departments:**
1. Dept. of Computer Science and Media Technology (DM)
2. Dept. of Mathematics (MA)
3. Dept. of Languages (SPR)

**Faculties:**
1. Faculty of Technology (FTK)
2. Faculty of Arts and Humanities (FKH)

---

## 2. Visualization Design

### 2.1 Visualization Approach

The visualization uses a **multi-view dashboard approach** combining several complementary visualizations to provide both overview and detail:

1. **Main Dashboard (6 coordinated views)**
   - Publications by Department (horizontal bar chart)
   - Publications over time by Faculty (line chart)
   - Publication distribution (histogram)
   - Top 15 researchers (horizontal bar chart)
   - Average publications per department over time (line chart)
   - Department contribution by faculty (stacked bar chart)

2. **Sunburst Diagram**
   - Hierarchical view: Faculty → Department → Researcher
   - Interactive drill-down capability
   - Color-coded by publication count

3. **Treemap**
   - Alternative hierarchical representation
   - Area proportional to publications
   - Easy comparison of contributions

4. **Scatter Plot**
   - Individual researcher view
   - Year vs. publications
   - Color-coded by department
   - Size represents publication count

### 2.2 Design Rationale

**Choice of Library:** Plotly (Python)
- Interactive visualizations with hover details
- Export to standalone HTML files
- Professional, publication-ready graphics
- Responsive and web-friendly
- No server required—works offline in any browser

**Multi-View Dashboard Justification:**

The decision to create a 6-panel coordinated dashboard rather than a single visualization stems from the multifaceted nature of the data:

1. **Horizontal Bar Chart (Publications by Department):** Chosen for easy length comparison of three departments. Horizontal orientation accommodates long department names and facilitates reading from a common baseline.

2. **Line Chart (Publications Over Time by Faculty):** Temporal data requires position encoding along the x-axis. Lines show trends and facilitate comparison between two faculties. The declining trend from 2019 to 2020 is immediately visible.

3. **Histogram (Publication Distribution):** Reveals the underlying distribution shape—the strong right skew indicating publication inequality. Essential for understanding that mean (2.86) doesn't represent typical researcher output due to outliers.

4. **Horizontal Bar Chart (Top 15 Researchers):** Highlights individual excellence. Horizontal orientation prevents label overlap. Limiting to top 15 balances detail with readability—showing all 199 would be overwhelming.

5. **Line Chart (Average Publications per Department by Year):** Reveals per-capita productivity trends, showing Mathematics actually has higher average (3.44) than CS (2.86) despite lower total output. This insight requires averaging, not just totals.

6. **Stacked Bar Chart (Department Contribution by Faculty):** Shows composition within faculties, making clear that Technology faculty consists of CS + Math, while Arts & Humanities is just Languages.

**Hierarchical Visualizations:**

- **Sunburst Diagram:** Chosen for its ability to show part-to-whole relationships in a radial space-efficient layout. The circular design is aesthetically pleasing and intuitively shows "zooming in" through hierarchical levels. Click interactions feel natural—clicking a segment expands it.

- **Treemap:** Provides an alternative hierarchical view using rectangular area encoding. Area is perceptually easier to compare than arc length, making it superior for precise quantitative comparison of contributions. The color scale (green to red) provides redundant encoding of publication counts.

- **Scatter Plot:** Shows individual researcher data points with multiple encodings: position (year, publications), color (department), and size (publications). This high information density allows outlier identification and pattern detection while maintaining individual context.

**Visual Encodings:**
- **Position:** Primary quantitative encoding (publications, time)—most accurate perceptual channel
- **Color:** Categorical encoding (departments, faculties)—effective for grouping and distinction
- **Size:** Quantitative encoding in scatter plot (publication count)—reinforces position encoding
- **Length:** Bar charts for easy comparison—second most accurate quantitative channel after position

**Color Scheme Rationale:**
- Distinct colors for three departments ensure clear differentiation
- Blue (CS), pink (Math), green (Languages) provide sufficient contrast
- Colorblind-friendly palette considered
- Continuous color scales (Viridis, RdYlGn) for hierarchical views aid in identifying high/low values

---

## 3. Insights Extracted

### 3.1 Key Findings

Based on the generated visualizations, several important insights emerge from the publication data:

1. **Departmental Productivity:**
   - **Computer Science and Media Technology (DM)** dominates with 306 total publications (53.7% of all university publications)
   - Mathematics (MA) contributes 141 publications (24.7%)
   - Languages (SPR) accounts for 123 publications (21.6%)
   - However, department size varies: CS has 107 researchers vs. Math with 41, affecting per-capita productivity
   - The distribution histogram reveals most researchers publish 1-3 papers per year, with a strong right skew indicating a few highly productive individuals

2. **Temporal Trends:**
   - Overall publications **decreased from 2019 to 2020**: from 312 to 258 publications (17.3% decline)
   - Faculty of Technology shows a declining trend across both years
   - Faculty of Arts and Humanities remains relatively stable but at lower absolute numbers
   - Average publications per department shows diverging trends: Languages declining while Math shows slight increase
   - This decline could indicate various factors: COVID-19 impact, funding changes, or natural variation

3. **Faculty Differences:**
   - **Faculty of Technology (FTK)** overwhelmingly dominates with 447 publications (78.4% of total)
   - Faculty of Arts and Humanities (FKH) contributes 123 publications (21.6%)
   - Average per researcher: FTK = 3.02, FKH = 2.41
   - This reflects typical STEM vs. humanities publication patterns, where STEM fields often have higher publication rates

4. **Individual Contributors - Publication Inequality:**
   - Top performers show exceptional productivity:
     - **Rachel Preston** (Mathematics): 19 publications in 2020
     - **Mel Cantrell** (Mathematics): 17 publications in 2019
     - **Kendra Hodges** (CS): 12 publications in 2019
     - **Mona Montes** (CS): 12 publications in 2019
   - The histogram shows **~90 researchers** (45%) published only 1 paper
   - A small elite group (top 15 researchers) accounts for a disproportionate share of output
   - This reflects the well-known **Pareto principle** in academic publishing

5. **Hierarchical Patterns (from Sunburst/Treemap):**
   - Clear organizational structure visible: University → Faculty → Department → Researcher
   - Within Faculty of Technology, CS department occupies the largest "slice"
   - Visual hierarchy reveals publication concentration: few departments within faculties, but many individual researchers
   - Color coding in treemap immediately highlights top performers (Rachel Preston, Mel Cantrell in bright green/yellow)
   - Sunburst interaction reveals drill-down capabilities: clicking Faculty expands to show departments, then individual researchers

6. **Scatter Plot Insights:**
   - Clear clustering by year (2019 vs 2020) with distinct vertical separation
   - Outliers are easily identifiable: researchers with 10+ publications stand out
   - Department color coding shows CS (blue) and Math (pink) produce the highest individual outputs
   - Languages (green) shows more consistent moderate output (fewer extreme values)
   - Size encoding reinforces publication count, making high performers immediately visible

### 3.2 Statistical Summary

| Metric | Value |
|--------|-------|
| Total Publications | 570 |
| Total Researchers | 199 |
| Average per Researcher | 2.86 |
| Median Publications | 2 (estimated from histogram) |
| Most Productive Department | Computer Science & Media Tech (306 pubs) |
| Most Productive Faculty | Faculty of Technology (447 pubs, 78.4%) |
| Highest Individual Output | Rachel Preston - 19 publications (2020) |
| Year 2019 Total | 312 publications (104 researchers) |
| Year 2020 Total | 258 publications (95 researchers) |
| Publications per Researcher 2019 | 3.00 average |
| Publications per Researcher 2020 | 2.72 average |

---

## 4. Interaction Possibilities

### 4.1 Implemented Interactions

The current Plotly-based visualization includes:

1. **Hover Details:**
   - On-demand information for each data point
   - Context-specific tooltips showing researcher names, exact values
   - Non-intrusive information access

2. **Zoom and Pan:**
   - Explore dense regions of data
   - Focus on specific time periods or value ranges
   - Useful for scatter plot and line charts

3. **Legend Interactions:**
   - Toggle visibility of categories
   - Isolate specific departments or faculties
   - Compare subsets of data

4. **Hierarchical Drill-down:**
   - Sunburst and treemap allow clicking to zoom into levels
   - Navigate from faculty → department → individual researchers

### 4.2 Recommended Additional Interactions

Based on the data structure and the insights discovered, the following interactions would significantly enhance analytical capabilities:

1. **Filtering Controls:**
   - **By Department:** Toggle buttons to show/hide CS, Math, or Languages data
   - **By Faculty:** Filter between Technology and Arts & Humanities
   - **By Year:** Slider or buttons to isolate 2019 or 2020 data
   - **By Publication Count:** Range slider to focus on high performers (e.g., >5 publications) or moderate publishers
   - **Rationale:** With 199 researchers across 3 departments and 2 faculties, filtering would allow focused comparison. For example, comparing only 2019 CS researchers vs. 2020 CS researchers to understand temporal changes within a single department.

2. **Linked Brushing Across Views:**
   - Selecting a researcher in the scatter plot highlights their bar in the top-15 chart and their segment in sunburst/treemap
   - Selecting a department in one view filters or highlights that department across all 6 dashboard panels
   - Brushing a time range in the temporal line chart updates histograms and bar charts
   - **Rationale:** The dashboard contains 6 coordinated views showing different perspectives. Linking them would maintain context when exploring. For instance, hovering over "Rachel Preston" in the top-15 chart could highlight her data point in the scatter plot and her segment in the sunburst, revealing she's from Mathematics.

3. **Dynamic Sorting and Ranking:**
   - Sort department bar chart by total publications, average per researcher, or alphabetically
   - Re-rank top-N researchers dynamically (show top 5, 10, 15, or 20)
   - Sort by year to see yearly winners
   - **Rationale:** Different questions require different orderings. Sorting by average reveals that Mathematics (3.44 avg) is more productive per capita than CS (2.86 avg), despite CS having more total publications. This insight is hidden without sorting controls.

4. **Aggregation Level Switching:**
   - Toggle between individual, department, and faculty granularity
   - Switch from raw counts to percentages (e.g., "CS represents 53.7% of publications")
   - View cumulative vs. per-year statistics
   - **Rationale:** The hierarchical nature (Faculty → Department → Researcher) suggests different analytical questions at each level. University administrators might care about faculty comparisons, while department chairs need department-level insights, and researchers want individual benchmarking.

5. **Temporal Animation:**
   - Animate scatter plot showing researchers' publication trajectories
   - Animate bar chart transitions from 2019 to 2020 rankings
   - Show department rise/fall over time with smooth transitions
   - **Rationale:** While we only have 2 years, animation would effectively communicate the 17.3% overall decline and highlight which departments/researchers changed most dramatically. This could be extended if more years were added.

6. **Search and Highlight Functionality:**
   - Search box to find researchers by name (e.g., type "Preston" to locate Rachel Preston)
   - Highlight all occurrences across all views
   - Show researcher profile card with all their statistics
   - **Rationale:** With 199 researchers, direct search is essential for targeted lookup. A department chair wanting to review a specific faculty member's productivity shouldn't need to manually scan through charts.

7. **Comparison Mode:**
   - Side-by-side department comparison showing publications, averages, distributions
   - Difference highlighting: "CS has 165 more publications than Math"
   - Before/after year comparison with delta values
   - **Rationale:** Key analytical tasks involve comparison. "How does my department compare to others?" or "How did we perform this year vs. last year?" These questions require explicit comparison interfaces, not just visual estimation.

8. **Details-on-Demand Panels:**
   - Click researcher name to open modal with: all publications by year, department rank, university rank, percentile
   - Click department to show: full researcher list, summary statistics, distribution within department
   - Click faculty to reveal: all departments, budget per publication, efficiency metrics
   - **Rationale:** The hierarchical structure and 199 individual records contain more detail than can fit on static charts. The sunburst shows this hierarchy but lacks detailed statistics. Expandable panels would combine overview with comprehensive details.

9. **Statistical Overlays and Benchmarks:**
   - Toggle mean/median lines on the histogram (mean=2.86, median≈2)
   - Show percentile bands (25th, 50th, 75th percentiles)
   - Add department average lines to scatter plot
   - Display confidence intervals or standard deviations
   - **Rationale:** The distribution shows the mean (2.86) is pulled up by outliers like Rachel Preston (19) and Mel Cantrell (17). Showing median (≈2) would reveal that most researchers are below the mean, providing context for individual performance evaluation. A researcher with 5 publications might wonder "Am I doing well?" Statistical overlays would show they're in the top 25%.

10. **Cross-Tabulation and Pivot Views:**
   - Interactive pivot table: rows=departments, columns=years, values=publications
   - Switch metrics: total, average, count, min, max
   - Export filtered data subsets for further analysis
   - **Rationale:** The data has multiple dimensions (department, faculty, year, individual) that could be cross-tabulated in various ways. Some users prefer tabular data to charts. A pivot interface would let users construct custom views.

### 4.3 Interaction Design Principles Applied

- **Overview First:** Dashboard shows aggregate statistics
- **Zoom and Filter:** Hierarchical views allow drilling down
- **Details-on-Demand:** Hover tooltips provide context
- **Visual Information Seeking Mantra:** "Overview first, zoom and filter, then details-on-demand" (Shneiderman, 1996)

---

## 5. Technical Implementation

### 5.1 Tools and Libraries
- **Python 3.x**
- **Pandas:** Data manipulation and aggregation
- **Plotly:** Interactive visualization generation
- **JSON:** Data loading

### 5.2 Files Generated
1. `publications_dashboard.html` - Main multi-view dashboard
2. `publications_sunburst.html` - Hierarchical sunburst diagram
3. `publications_treemap.html` - Hierarchical treemap
4. `publications_scatter.html` - Individual researcher scatter plot

### 5.3 Running the Visualization

```bash
# Install dependencies
pip install -r requirements.txt

# Run the visualization script
python visualize_publications.py
```

The script will:
1. Load and analyze the data
2. Print summary statistics to console
3. Generate 4 interactive HTML files
4. Open any HTML file in a web browser to explore

---

## 6. Conclusion

This visualization project successfully addresses the challenge of presenting complex, hierarchical publication data through a comprehensive, multi-view interactive dashboard. The implementation demonstrates several key principles of effective information visualization:

**Successful Design Elements:**

1. **Multiple Coordinated Views:** The 6-panel dashboard provides complementary perspectives—departmental totals, temporal trends, distribution patterns, top performers, averages over time, and faculty breakdowns—allowing users to cross-reference insights and build comprehensive understanding.

2. **Hierarchical Exploration:** The sunburst and treemap visualizations effectively communicate the three-level organizational structure (Faculty → Department → Researcher), with interactive drill-down enabling seamless navigation from overview to detail.

3. **Appropriate Visual Encodings:** Bar charts for categorical comparisons, line charts for temporal trends, histograms for distributions, and scatter plots for individual analysis—each chart type matches its data characteristics and analytical purpose.

4. **Interactivity for Engagement:** Plotly's hover tooltips, zoom capabilities, legend filtering, and click-to-explore features transform static data into an explorable information space, following Shneiderman's mantra of "overview first, zoom and filter, then details-on-demand."

**Key Insights Revealed:**

The visualization reveals significant patterns in PSU's research output: the dominance of Computer Science (53.7% of publications), the Faculty of Technology's overwhelming contribution (78.4%), the publication inequality where top performers like Rachel Preston (19 pubs) far exceed typical output (median ≈2), and the concerning 17.3% decline from 2019 to 2020 that warrants administrative attention.

**Interaction Design Opportunities:**

While the current implementation provides solid exploratory capabilities, the recommended additional interactions—particularly linked brushing across views, dynamic filtering, search functionality, and statistical overlays—would transform this from a presentation tool into an analytical platform suitable for university administrators, department chairs, and researchers making data-driven decisions about resource allocation, hiring, and research strategy.

**Scalability and Extension:**

The modular design allows easy extension to additional years, departments, or metrics (citations, grants, collaborations). The hierarchical data structure could accommodate more levels (research groups, individual projects) or additional dimensions (publication types, funding sources, international collaborations).

**Technical Success:**

The choice of Python with Pandas for data manipulation and Plotly for visualization proved effective, generating publication-quality, web-ready HTML outputs that require no additional infrastructure—any stakeholder with a web browser can explore the data. The clean, commented code ensures maintainability and reproducibility.

In summary, this visualization project demonstrates that thoughtful design choices, appropriate chart types, and interactive features can transform raw publication statistics into actionable insights about research productivity, revealing both aggregate patterns and individual contributions while maintaining the hierarchical context essential for organizational decision-making.

---

## 7. References

- Shneiderman, B. (1996). The eyes have it: A task by data type taxonomy for information visualizations. *Proceedings 1996 IEEE Symposium on Visual Languages*, 336-343.
- Plotly Technologies Inc. (2024). Collaborative data science. https://plot.ly

---

## Appendix: Sample Visualizations

Below are screenshots from the four generated interactive visualizations. Each visualization is available as a standalone HTML file that can be opened in any web browser for full interactivity.

### A.1 Main Dashboard

**File:** `publications_dashboard.html`

The main dashboard presents six coordinated views providing comprehensive overview of PSU publication statistics:

- **Top-left:** Total publications by department showing Computer Science's dominance (306 pubs)
- **Top-right:** Temporal trends revealing 17.3% decline from 2019 to 2020
- **Middle-left:** Distribution histogram showing right-skewed pattern with ~90 researchers publishing only 1 paper
- **Middle-right:** Top 15 most productive researchers led by Rachel Preston (19) and Mel Cantrell (17)
- **Bottom-left:** Average publications per department over time showing diverging trends
- **Bottom-right:** Department contributions by faculty showing Faculty of Technology's 78.4% dominance

**Key Features:**
- Interactive hover tooltips on all data points
- Legend filtering to isolate specific departments/faculties
- Zoom and pan capabilities
- Coordinated color scheme across all panels

### A.2 Sunburst Diagram

**File:** `publications_sunburst.html`

The sunburst diagram visualizes the three-level hierarchy: Faculty → Department → Researcher. The radial layout efficiently uses space while maintaining visual clarity.

**Visual Encoding:**
- **Inner ring:** Two faculties (Technology in blue/teal, Arts & Humanities in purple)
- **Middle ring:** Three departments within their respective faculties
- **Outer ring:** Individual researchers (199 total)
- **Color intensity:** Publication count (darker = fewer, brighter/yellow = more)

**Interaction:**
- Click on Faculty level to zoom into departments
- Click on Department level to zoom into individual researchers
- Click center to zoom back out
- Hover for exact publication counts and names
- Immediately reveals Rachel Preston (bright yellow) and Mel Cantrell as top contributors

**Insights Visible:**
- Computer Science occupies largest arc in Technology faculty
- Mathematics contains the brightest colors (highest individual performers)
- Languages department shows more uniform purple (consistent moderate output)

### A.3 Treemap

**File:** `publications_treemap.html`

The treemap provides an alternative hierarchical representation using rectangular area to encode publication counts. This makes quantitative comparison easier than the sunburst's arc lengths.

**Layout:**
- **Large rectangles:** Faculties (Faculty of Technology dominates left side)
- **Medium rectangles:** Departments within faculties
- **Small rectangles:** Individual researchers
- **Color scale:** Green (high) → Yellow → Orange → Red (low) publications

**Advantages over Sunburst:**
- Area is easier to compare perceptually than arc length
- Better space utilization for large datasets
- Names are more readable in rectangular spaces
- Color scale provides redundant quantitative encoding

**Observable Patterns:**
- Kendra Hodges, Brett Santana, Mona Montes visible as large green rectangles in CS section
- Rachel Preston and Mel Cantrell stand out as brightest (greenest) in Mathematics
- Languages section shows many small, similarly-sized rectangles indicating consistent moderate output
- Clear size disparity shows publication inequality

### A.4 Scatter Plot

**File:** `publications_scatter.html`

The scatter plot displays individual researchers as points, with year on x-axis and publication count on y-axis.

**Encodings:**
- **X-position:** Year (2019 or 2020)
- **Y-position:** Number of publications
- **Color:** Department (Blue=CS, Pink=Math, Green=Languages)
- **Size:** Publication count (larger circles = more publications)

**Key Observations:**
- Clear vertical separation between 2019 and 2020 data
- Outliers immediately visible: Rachel Preston at (2020, 19) appears as large pink circle
- 2019 shows Mel Cantrell (17), Kendra Hodges (12), Mona Montes (12) as notable outliers
- Most points cluster at bottom (1-5 publications) regardless of year
- Size encoding reinforces y-position, making high performers doubly salient
- Color clustering shows department patterns: Math (pink) has several high outliers despite smaller total size

**Interactive Features:**
- Hover reveals researcher name, exact publication count, department, and faculty
- Zoom into dense regions to see overlapping points
- Legend click to hide/show specific departments
- Demonstrates the long-tail distribution of academic productivity

---

### A.5 Data Quality and Limitations

**Data Characteristics:**
- Clean dataset with no missing values
- Consistent formatting and structure
- Each researcher appears once per year (no duplicates)
- Limited temporal scope (only 2 years)

**Limitations:**
- Cannot assess long-term trends with only 2 years
- No information about publication quality, citations, or impact
- Department size differences not encoded in all visualizations
- No information about researcher seniority, position, or tenure status
- Cannot distinguish between different publication types (journal vs conference)

**Potential Biases:**
- Publication count favors quantity over quality
- Different fields have different publication norms
- Does not account for authorship position or contribution percentage
- May disadvantage researchers who publish longer, higher-impact papers less frequently

---

### A.6 Recommendations for University Administration

Based on the insights from these visualizations:

1. **Investigate 2020 Decline:** The 17.3% drop in publications from 2019 to 2020 warrants investigation. Is this COVID-19 related? Funding changes? Natural variation?

2. **Support Low Publishers:** With 45% of researchers publishing only 1 paper, consider mentorship programs pairing low publishers with high performers like Rachel Preston.

3. **Department Resource Allocation:** While CS has highest total (306), Mathematics has highest per-capita productivity (3.44 avg). Resource allocation should consider both metrics.

4. **Cross-Department Learning:** Mathematics produces exceptional individuals (Rachel Preston: 19, Mel Cantrell: 17). What practices can other departments learn?

5. **Faculty Balance:** Arts & Humanities contributes only 21.6% of publications. Is this acceptable given different field norms? Should support be increased?

6. **Recognize Excellence:** The top 15 researchers shown in the dashboard deserve recognition and should be studied for best practices.

---

*Note: To view the interactive versions of these visualizations, open the corresponding HTML files in a web browser. All files are self-contained and work offline without requiring any server infrastructure.*
