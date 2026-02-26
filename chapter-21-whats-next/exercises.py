# Chapter 21 - Your Learning Plan Template
#
# Fill this in for yourself:

my_plan = {
    "next_3_months": [
        "Build: ___________________",
        "Learn: ___________________",
        "Deploy: __________________",
    ],
    "portfolio_projects": [
        "Project 1: ______________",
        "Project 2: ______________",
        "Project 3: ______________",
    ],
    "weekly_habits": [
        "Read AI news (15 min)",
        "Code one small project",
        "Write about what you learned",
    ],
}

for section, items in my_plan.items():
    print(f"\n{section.replace('_', ' ').title()}:")
    for item in items:
        print(f"  - {item}")
