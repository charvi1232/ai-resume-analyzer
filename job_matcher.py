import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_roles(csv_path="data/job_roles.csv"):
    """
    Load job roles and their required skills from CSV.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Job role file not found: {csv_path}")

    return pd.read_csv(csv_path)


def calculate_skill_match(resume_skills, required_skills):
    """
    Calculate percentage of required skills found in the resume.
    """

    resume_set = {
        skill.strip().lower()
        for skill in resume_skills
    }

    required_set = {
        skill.strip().lower()
        for skill in required_skills.split(",")
    }

    if not required_set:
        return 0

    matched_skills = resume_set.intersection(required_set)

    score = (len(matched_skills) / len(required_set)) * 100

    return round(score, 2)


def calculate_text_similarity(resume_text, required_skills):
    """
    Calculate TF-IDF cosine similarity between resume text
    and required job skills.
    """

    documents = [
        resume_text.lower(),
        required_skills.lower()
    ]

    vectorizer = TfidfVectorizer()

    try:
        vectors = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        return round(similarity * 100, 2)

    except ValueError:
        return 0


def calculate_role_scores(resume_text, resume_skills, job_roles):
    """
    Calculate a combined score for every job role.

    70% skill matching
    30% TF-IDF text similarity
    """

    results = []

    for _, row in job_roles.iterrows():

        role = row["role"]
        required_skills = row["required_skills"]

        skill_score = calculate_skill_match(
            resume_skills,
            required_skills
        )

        similarity_score = calculate_text_similarity(
            resume_text,
            required_skills
        )

        final_score = (
            (skill_score * 0.70) +
            (similarity_score * 0.30)
        )

        results.append({
            "role": role,
            "match_score": round(final_score, 2),
            "skill_score": skill_score,
            "similarity_score": similarity_score
        })

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="match_score",
        ascending=False
    ).reset_index(drop=True)

    return results_df


def find_missing_skills(resume_skills, required_skills):
    """
    Find job-related skills required by a role
    that are not present in the resume.
    """

    resume_set = {
        skill.strip().lower()
        for skill in resume_skills
    }

    required_list = [
        skill.strip()
        for skill in required_skills.split(",")
    ]

    missing = []

    for skill in required_list:

        if skill.lower() not in resume_set:
            missing.append(skill)

    return missing