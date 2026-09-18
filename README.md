# AI Resume Analyzer and Job Recommendation System

An NLP-based Streamlit application that analyzes resumes, identifies technical skills, compares resumes with predefined job roles and specific job descriptions, identifies skill gaps, and generates personalized learning roadmaps.

## Objective

The objective of this project is to build an intelligent resume analysis system that helps users understand how their resume matches different job roles.

The system:
- Extracts information from PDF and DOCX resumes
- Detects technical skills
- Compares skills with predefined job roles
- Calculates role match scores
- Identifies suitable job roles
- Finds missing skills
- Generates a personalized learning roadmap
- Compares a resume with a specific job description

## Features

- Upload resumes in PDF or DOCX format
- Extract and clean resume text
- Automatically detect technical skills
- Support for 20+ technical skills
- Compare resumes with 10 predefined job roles
- Calculate job-role match scores
- Display top 3 matching job roles
- Display match scores for all job roles
- Identify missing skills
- Generate a personalized learning roadmap
- Paste a custom job description
- Calculate resume-to-job-description match
- Display skill match and TF-IDF text similarity
- Identify skills already present in the resume
- Identify skills missing for a specific job
- Generate a job-specific learning roadmap
- Interactive Streamlit dashboard
- Responsible AI considerations

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- pypdf
- python-docx
- Regular Expressions
- TF-IDF
- Cosine Similarity

## System Workflow

```text
Resume Upload
      ↓
PDF/DOCX Text Extraction
      ↓
Text Cleaning
      ↓
Technical Skill Extraction
      ↓
Job Role Requirements
      ↓
Skill Matching + TF-IDF Similarity
      ↓
Match Score Calculation
      ↓
Top Job Role Recommendations
      ↓
Missing Skill Analysis
      ↓
Personalized Learning Roadmap