import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Job-related skills that can be detected in a job description
JD_SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "SQL",
    "HTML",
    "CSS",
    "React.js",
    "Node.js",
    "Flask",
    "Django",
    "FastAPI",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Generative AI",
    "NLP",
    "Natural Language Processing",
    "Computer Vision",
    "OpenCV",
    "Data Science",
    "Data Analysis",
    "Data Visualization",
    "Statistics",
    "Excel",
    "Power BI",
    "Git",
    "GitHub",
    "Cloud Computing",
    "REST API",
    "API",
    "Data Structures",
    "Algorithms",
    "OOP",
    "DBMS",
    "MongoDB",
    "PostgreSQL",
    "MySQL",
    "CNN"
]


def extract_jd_skills(jd_text):
    """
    Extract technical skills mentioned in a job description.
    """

    found_skills = []

    text_lower = jd_text.lower()

    for skill in JD_SKILLS:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill.lower())
            + r"(?!\w)"
        )

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    # Remove duplicates
    unique_skills = []

    for skill in found_skills:
        if skill not in unique_skills:
            unique_skills.append(skill)

    return unique_skills


def calculate_jd_match(resume_skills, jd_skills):
    """
    Calculate the percentage of JD skills
    that are present in the resume.
    """

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    jd_set = {
        skill.lower()
        for skill in jd_skills
    }

    if not jd_set:
        return 0

    matched = resume_set.intersection(jd_set)

    score = (len(matched) / len(jd_set)) * 100

    return round(score, 2)


def calculate_jd_text_similarity(resume_text, jd_text):
    """
    Calculate TF-IDF cosine similarity between
    the resume and job description.
    """

    documents = [
        resume_text.lower(),
        jd_text.lower()
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    try:

        vectors = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        return round(similarity * 100, 2)

    except ValueError:

        return 0


def analyze_job_description(
    resume_text,
    resume_skills,
    jd_text
):
    """
    Perform complete resume vs job-description analysis.
    """

    jd_skills = extract_jd_skills(jd_text)

    skill_match = calculate_jd_match(
        resume_skills,
        jd_skills
    )

    text_similarity = calculate_jd_text_similarity(
        resume_text,
        jd_text
    )

    # 70% skill match + 30% text similarity
    final_score = (
        (skill_match * 0.70)
        + (text_similarity * 0.30)
    )

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    missing_skills = [
        skill
        for skill in jd_skills
        if skill.lower() not in resume_set
    ]

    matched_skills = [
        skill
        for skill in jd_skills
        if skill.lower() in resume_set
    ]

    return {
        "match_score": round(final_score, 2),
        "skill_match": skill_match,
        "text_similarity": text_similarity,
        "jd_skills": jd_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }