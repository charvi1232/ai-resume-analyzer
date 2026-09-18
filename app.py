import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_resume_text, clean_resume_text
from skill_extractor import extract_skills
from job_matcher import (
    load_job_roles,
    calculate_role_scores,
    find_missing_skills
)
from roadmap_generator import generate_roadmap
from jd_matcher import analyze_job_description


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume, compare it with job roles, "
    "identify missing skills, and get a personalized "
    "learning roadmap."
)


# =========================================================
# RESUME UPLOAD
# =========================================================

st.subheader("📤 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


# =========================================================
# MAIN APPLICATION
# =========================================================

if uploaded_file is not None:

    st.success(
        f"Resume uploaded successfully: {uploaded_file.name}"
    )

    # -----------------------------------------------------
    # EXTRACT RESUME TEXT
    # -----------------------------------------------------

    extracted_text = extract_resume_text(uploaded_file)

    cleaned_text = clean_resume_text(extracted_text)

    if not cleaned_text:

        st.error(
            "Could not extract text from this resume. "
            "Please try another PDF or DOCX file."
        )

        st.stop()


    # =====================================================
    # EXTRACTED RESUME TEXT
    # =====================================================

    st.subheader("📋 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        cleaned_text,
        height=350
    )

    st.success(
        "Resume text extracted successfully!"
    )


    # =====================================================
    # SKILL EXTRACTION
    # =====================================================

    st.subheader("🛠️ Skills Detected")

    skills = extract_skills(cleaned_text)

    if skills:

        st.write(", ".join(skills))

        st.success(
            f"{len(skills)} skills detected."
        )

    else:

        st.warning(
            "No technical skills detected."
        )


    # =====================================================
    # JOB ROLE ANALYSIS
    # =====================================================

    st.divider()

    st.header("💼 Job Role Analysis")

    try:

        job_roles = load_job_roles(
            "data/job_roles.csv"
        )

    except Exception as error:

        st.error(
            f"Could not load job roles: {error}"
        )

        st.stop()


    # -----------------------------------------------------
    # CALCULATE ROLE SCORES
    # -----------------------------------------------------

    role_scores = calculate_role_scores(
        cleaned_text,
        skills,
        job_roles
    )


    # =====================================================
    # TOP 3 RECOMMENDED ROLES
    # =====================================================

    st.subheader("🏆 Top 3 Recommended Job Roles")

    top_three = role_scores.head(3)

    columns = st.columns(3)

    for index, (_, row) in enumerate(
        top_three.iterrows()
    ):

        with columns[index]:

            st.metric(
                label=row["role"],
                value=f'{row["match_score"]}%'
            )

            st.caption(
                f'Skill Match: {row["skill_score"]}%'
            )

            st.caption(
                f'Text Similarity: '
                f'{row["similarity_score"]}%'
            )


    # =====================================================
    # ALL JOB ROLE SCORES
    # =====================================================

    st.subheader("📈 Match Score for All Job Roles")

    display_scores = role_scores.copy()

    display_scores["match_score"] = (
        display_scores["match_score"].astype(str)
        + "%"
    )

    display_scores["skill_score"] = (
        display_scores["skill_score"].astype(str)
        + "%"
    )

    display_scores["similarity_score"] = (
        display_scores["similarity_score"].astype(str)
        + "%"
    )

    display_scores = display_scores.rename(
        columns={
            "role": "Job Role",
            "match_score": "Overall Match",
            "skill_score": "Skill Match",
            "similarity_score": "Text Similarity"
        }
    )

    st.dataframe(
        display_scores,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # JOB ROLE COMPARISON CHART
    # =====================================================

    st.subheader("📊 Job Role Comparison")

    chart = px.bar(
        role_scores,
        x="role",
        y="match_score",
        text="match_score",
        labels={
            "role": "Job Role",
            "match_score": "Match Score (%)"
        },
        title="Resume Match Score by Job Role"
    )

    chart.update_traces(
        texttemplate="%{text}%",
        textposition="outside"
    )

    chart.update_layout(
        xaxis_tickangle=-35,
        yaxis_range=[
            0,
            min(
                100,
                max(
                    100,
                    role_scores["match_score"].max() + 10
                )
            )
        ]
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )


    # =====================================================
    # DETAILED ROLE ANALYSIS
    # =====================================================

    st.subheader("🎯 Detailed Role Analysis")

    selected_role = st.selectbox(
        "Select a job role to see missing skills and roadmap:",
        role_scores["role"].tolist()
    )


    selected_row = job_roles[
        job_roles["role"] == selected_role
    ]


    if not selected_row.empty:

        required_skills = selected_row.iloc[0][
            "required_skills"
        ]

        selected_score = role_scores[
            role_scores["role"] == selected_role
        ].iloc[0]


        # -------------------------------------------------
        # SELECTED ROLE SCORE
        # -------------------------------------------------

        st.metric(
            "Selected Role Match Score",
            f'{selected_score["match_score"]}%'
        )


        # -------------------------------------------------
        # MISSING SKILLS
        # -------------------------------------------------

        st.subheader("❌ Missing Skills")

        missing_skills = find_missing_skills(
            skills,
            required_skills
        )

        if missing_skills:

            for skill in missing_skills:

                st.write(
                    f"• {skill}"
                )

            st.warning(
                f"{len(missing_skills)} skill(s) "
                "may need improvement for this role."
            )

        else:

            st.success(
                "Excellent! No missing required skills "
                "were identified for this role."
            )


        # -------------------------------------------------
        # LEARNING ROADMAP
        # -------------------------------------------------

        st.subheader("🗺️ Personalized Learning Roadmap")

        roadmap = generate_roadmap(
            missing_skills
        )

        if roadmap:

            for item in roadmap:

                with st.expander(
                    f"📚 Learn: {item['skill']}"
                ):

                    for step_number, step in enumerate(
                        item["steps"],
                        start=1
                    ):

                        st.write(
                            f"{step_number}. {step}"
                        )

        else:

            st.success(
                "No additional roadmap items are required."
            )


    # =====================================================
    # CUSTOM JOB DESCRIPTION ANALYSIS
    # =====================================================

    st.divider()

    st.header("🎯 Resume vs Job Description")

    st.write(
        "Paste a job description below to compare your "
        "resume with a specific internship or job."
    )


    job_description = st.text_area(
        "Paste Job Description",
        height=250,
        placeholder=(
            "Example: We are looking for a Python developer "
            "with SQL, Machine Learning, Pandas, Git and "
            "REST API experience..."
        )
    )


    # -----------------------------------------------------
    # ANALYZE JOB DESCRIPTION
    # -----------------------------------------------------

    if st.button(
        "🔍 Analyze Job Description"
    ):

        if not job_description.strip():

            st.warning(
                "Please paste a job description first."
            )

        else:

            with st.spinner(
                "Analyzing resume against the job description..."
            ):

                jd_result = analyze_job_description(
                    cleaned_text,
                    skills,
                    job_description
                )


            # -------------------------------------------------
            # JD MATCH SCORE
            # -------------------------------------------------

            st.subheader(
                "📊 Job Description Match Score"
            )

            score = jd_result["match_score"]

            if score >= 75:

                st.success(
                    f"Excellent Match: {score}%"
                )

            elif score >= 50:

                st.info(
                    f"Good Match: {score}%"
                )

            elif score >= 30:

                st.warning(
                    f"Moderate Match: {score}%"
                )

            else:

                st.error(
                    f"Low Match: {score}%"
                )


            # -------------------------------------------------
            # SCORE BREAKDOWN
            # -------------------------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Skill Match",
                    f'{jd_result["skill_match"]}%'
                )

            with col2:

                st.metric(
                    "Text Similarity",
                    f'{jd_result["text_similarity"]}%'
                )


            # -------------------------------------------------
            # SKILLS FOUND IN JD
            # -------------------------------------------------

            st.subheader(
                "🔎 Skills Found in Job Description"
            )

            jd_skills = jd_result["jd_skills"]

            if jd_skills:

                st.write(
                    ", ".join(jd_skills)
                )

            else:

                st.warning(
                    "No supported technical skills were "
                    "detected in the job description."
                )


            # -------------------------------------------------
            # MATCHED SKILLS
            # -------------------------------------------------

            st.subheader(
                "✅ Skills You Already Have"
            )

            matched_skills = jd_result[
                "matched_skills"
            ]

            if matched_skills:

                for skill in matched_skills:

                    st.write(
                        f"✅ {skill}"
                    )

            else:

                st.warning(
                    "No matching technical skills were detected."
                )


            # -------------------------------------------------
            # MISSING SKILLS
            # -------------------------------------------------

            st.subheader(
                "❌ Skills Missing for This Job"
            )

            jd_missing_skills = jd_result[
                "missing_skills"
            ]

            if jd_missing_skills:

                for skill in jd_missing_skills:

                    st.write(
                        f"❌ {skill}"
                    )

                st.warning(
                    f"{len(jd_missing_skills)} skill(s) "
                    "may need improvement."
                )

            else:

                st.success(
                    "No missing technical skills were detected!"
                )


            # -------------------------------------------------
            # JD LEARNING ROADMAP
            # -------------------------------------------------

            st.subheader(
                "🗺️ Job-Specific Learning Roadmap"
            )

            jd_roadmap = generate_roadmap(
                jd_missing_skills
            )

            if jd_roadmap:

                for item in jd_roadmap:

                    with st.expander(
                        f"📚 {item['skill']}"
                    ):

                        for number, step in enumerate(
                            item["steps"],
                            start=1
                        ):

                            st.write(
                                f"{number}. {step}"
                            )

            else:

                st.success(
                    "Your detected skills already cover "
                    "the technical skills identified in "
                    "this job description."
                )


    # =====================================================
    # HOW THE SYSTEM WORKS
    # =====================================================

    st.divider()

    st.subheader("ℹ️ How the Analyzer Works")

    st.write(
        """
        **1. Resume Parsing:** Extracts text from PDF or DOCX resumes.

        **2. Text Cleaning:** Removes unnecessary blank lines and formatting noise.

        **3. Skill Extraction:** Identifies technical skills mentioned in the resume.

        **4. Job Role Matching:** Compares detected skills with predefined job-role requirements.

        **5. TF-IDF Similarity:** Calculates textual similarity between the resume and job requirements.

        **6. Match Score:** Combines skill matching and text similarity.

        **7. Role Recommendation:** Displays the top 3 recommended job roles.

        **8. Skill Gap Analysis:** Identifies skills required for a selected role but not detected in the resume.

        **9. Learning Roadmap:** Provides learning steps for missing skills.

        **10. Job Description Matching:** Allows users to paste a specific job description and compare it directly with their resume.
        """
    )


    # =====================================================
    # RESPONSIBLE AI NOTICE
    # =====================================================

    st.divider()

    st.subheader("⚠️ Responsible AI Notice")

    st.info(
        """
        Match scores are estimates based on detected job-related
        skills and text similarity. They should not be treated as
        hiring decisions.

        The system focuses on job-related information and does
        not intentionally evaluate protected personal attributes
        such as gender, age, religion, nationality, marital status,
        disability, or photograph.

        A missing keyword does not necessarily mean that a person
        lacks the underlying ability.
        """
    )