# Sample Outputs

## Sample Analysis Output

```json
{
  "overall_score": 7,
  "strengths": [
    "Clear leadership experience managing cross-functional projects",
    "Strong technical skills with Python, SQL, and Excel",
    "Relevant internships in product operations and analytics"
  ],
  "weaknesses": [
    "Achievements lack measurable outcomes",
    "The resume has inconsistent bullet formatting",
    "No clear summary that highlights role fit"
  ],
  "role_fit": "Good fit for operations analyst or business analyst roles, but the resume should emphasize data-driven outcomes and stakeholder collaboration.",
  "formatting_issues": "Use consistent bullet points, add section headers, and limit each bullet to one achievement statement.",
  "suggested_actions": [
    "Add an executive summary with role goals",
    "Quantify results for each project",
    "Standardize the format across work experience entries"
  ]
}
```

## Sample Improvement Output

```json
{
  "analysis": {
    "source_role": "Business Analyst",
    "source_length": 520
  },
  "improved_resume": "Jane Doe\nBusiness Analyst | Data-driven Operations Specialist\n\nProfessional Summary\nBusiness Analyst with 3+ years of experience driving process improvements and data-backed recommendations. Delivered a 18% efficiency gain by redesigning reporting workflows and improving stakeholder communication.\n\nExperience\nOperations Analyst, TechCorp Inc.\n- Transformed monthly reporting operations by implementing a dashboard that reduced data preparation time by 40%.\n- Collaborated with sales and finance to identify cost-saving opportunities that improved margin visibility by $120K.\n\nProjects\nAnalytics Automation\n- Designed and automated a KPI dashboard that tracked customer retention and revenue growth, enabling executive decisions with real-time insights.",
  "summary_of_changes": [
    "Added a stronger professional summary",
    "Reworded achievements with clear metrics",
    "Improved section structure and readability"
  ],
  "strength_statement": "The candidate now appears more aligned to analytical roles by emphasizing measurable business outcomes and collaborative delivery.",
  "recommended_formatting": "Use a header, tailor bullet points to the target role, and keep technical skills grouped separately."
}
```

## Memory Output Example

```json
[
  {
    "timestamp": "2026-04-09T12:00:00Z",
    "target_role": "Business Analyst",
    "resume_text": "...",
    "analysis": {
      "source_role": "Business Analyst",
      "source_length": 520
    },
    "improved_resume": "..."
  }
]
```
