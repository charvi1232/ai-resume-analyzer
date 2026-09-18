import re


SKILLS = [
    # Programming Languages
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "SQL",

    # Core CS
    "Data Structures",
    "Algorithms",
    "Data Structures & Algorithms",
    "OOP",
    "Object Oriented Programming",
    "DBMS",

    # Web / Backend
    "HTML",
    "CSS",
    "React.js",
    "React",
    "Flask",
    "Django",
    "FastAPI",
    "Node.js",

    # Data Science / Machine Learning
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "Scikit Learn",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "NLP",
    "Data Science",
    "Data Analysis",
    "Data Visualization",

    # AI
    "Artificial Intelligence",
    "AI",
    "Generative AI",
    "Computer Vision",
    "CNN",

    # Tools
    "Git",
    "GitHub",
    "VS Code",
    "Jupyter Notebook",
    "Jupyter",

    # Databases / Cloud
    "MySQL",
    "MongoDB",
    "PostgreSQL",
    "Cloud Computing",

    # Other
    "Socket Programming",
    "Multithreading",
    "Regex",
    "REST API",
    "API"
]


def extract_skills(text):
    """
    Find technical skills mentioned in resume text.
    Returns a list of unique skills.
    """

    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:

        skill_lower = skill.lower()

        # Escape special characters so skills like C++ and React.js
        # are searched correctly.
        escaped_skill = re.escape(skill_lower)

        # Word-boundary search for normal skills.
        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    # Remove duplicates while preserving order
    unique_skills = []

    for skill in found_skills:
        if skill not in unique_skills:
            unique_skills.append(skill)

    return unique_skills