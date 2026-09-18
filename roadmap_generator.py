ROADMAP = {
    "Python": [
        "Learn Python fundamentals",
        "Practice functions, modules, and exception handling",
        "Build small Python projects"
    ],

    "SQL": [
        "Learn SQL basics",
        "Practice JOINs, GROUP BY, subqueries, and aggregate functions",
        "Practice SQL using real datasets"
    ],

    "Pandas": [
        "Learn Pandas Series and DataFrames",
        "Practice data cleaning and filtering",
        "Perform exploratory data analysis on datasets"
    ],

    "NumPy": [
        "Learn NumPy arrays",
        "Practice indexing and mathematical operations",
        "Use NumPy for data-processing tasks"
    ],

    "Matplotlib": [
        "Learn basic plotting",
        "Create bar, line, scatter, and histogram charts",
        "Practice visualizing datasets"
    ],

    "Scikit-learn": [
        "Learn machine learning fundamentals",
        "Practice preprocessing and model training",
        "Build classification and regression projects"
    ],

    "Machine Learning": [
        "Learn supervised and unsupervised learning",
        "Study classification, regression, and clustering",
        "Build machine learning projects"
    ],

    "Deep Learning": [
        "Learn neural network fundamentals",
        "Study CNNs and other deep learning architectures",
        "Build a deep learning project"
    ],

    "TensorFlow": [
        "Learn TensorFlow basics",
        "Build and train neural networks",
        "Practice with an image or text dataset"
    ],

    "PyTorch": [
        "Learn PyTorch tensors and datasets",
        "Build a basic neural network",
        "Train a deep learning model"
    ],

    "NLP": [
        "Learn NLP fundamentals",
        "Practice text preprocessing and feature extraction",
        "Build a text classification project"
    ],

    "Natural Language Processing": [
        "Learn NLP fundamentals",
        "Practice text preprocessing",
        "Build an NLP application"
    ],

    "Computer Vision": [
        "Learn image-processing fundamentals",
        "Practice image classification and object detection",
        "Build a computer vision project"
    ],

    "OpenCV": [
        "Learn OpenCV basics",
        "Practice image and video processing",
        "Build a computer vision application"
    ],

    "JavaScript": [
        "Learn JavaScript fundamentals",
        "Practice DOM manipulation and APIs",
        "Build an interactive web application"
    ],

    "React.js": [
        "Learn React components and props",
        "Practice state and event handling",
        "Build a React-based project"
    ],

    "Node.js": [
        "Learn Node.js fundamentals",
        "Build REST APIs",
        "Connect a Node.js backend to a database"
    ],

    "Flask": [
        "Learn Flask fundamentals",
        "Build REST APIs",
        "Connect Flask applications to databases"
    ],

    "FastAPI": [
        "Learn FastAPI fundamentals",
        "Build REST APIs",
        "Connect APIs with machine learning models"
    ],

    "REST API": [
        "Learn REST architecture",
        "Practice GET, POST, PUT, and DELETE requests",
        "Build and test a REST API"
    ],

    "Statistics": [
        "Learn descriptive statistics",
        "Study probability and distributions",
        "Practice statistics using real datasets"
    ],

    "Excel": [
        "Learn Excel formulas and functions",
        "Practice data cleaning and pivot tables",
        "Create dashboards using Excel"
    ],

    "Power BI": [
        "Learn Power BI fundamentals",
        "Practice data transformation",
        "Create interactive dashboards"
    ],

    "Git": [
        "Learn Git basics",
        "Practice branching and merging",
        "Use Git in software projects"
    ],

    "Cloud Computing": [
        "Learn cloud computing fundamentals",
        "Study basic cloud services",
        "Deploy a small application to the cloud"
    ],

    "Data Visualization": [
        "Learn principles of effective visualization",
        "Practice charts and dashboards",
        "Create visual reports from datasets"
    ],

    "Data Science": [
        "Learn the data science workflow",
        "Practice data cleaning, analysis, and visualization",
        "Build an end-to-end data science project"
    ],

    "Artificial Intelligence": [
        "Learn AI fundamentals",
        "Study machine learning and deep learning",
        "Build an AI-based application"
    ],

    "AI": [
        "Learn AI fundamentals",
        "Study machine learning and deep learning",
        "Build an AI-based application"
    ],

    "C++": [
        "Learn C++ fundamentals",
        "Practice OOP and STL",
        "Solve data structures and algorithm problems"
    ],

    "Java": [
        "Learn Java fundamentals",
        "Practice OOP and collections",
        "Build a Java-based application"
    ],

    "Data Structures": [
        "Study arrays, linked lists, stacks, and queues",
        "Learn trees, graphs, and hash tables",
        "Practice coding problems"
    ],

    "Algorithms": [
        "Learn searching and sorting algorithms",
        "Study recursion and dynamic programming",
        "Practice algorithmic problems"
    ],

    "OOP": [
        "Learn classes and objects",
        "Study inheritance, polymorphism, and abstraction",
        "Build an object-oriented project"
    ],

    "DBMS": [
        "Learn database fundamentals",
        "Study normalization and transactions",
        "Practice database design and SQL"
    ]
}


def generate_roadmap(missing_skills):
    """
    Generate a learning roadmap based on missing skills.
    """

    roadmap = []

    for skill in missing_skills:

        if skill in ROADMAP:

            roadmap.append({
                "skill": skill,
                "steps": ROADMAP[skill]
            })

        else:

            roadmap.append({
                "skill": skill,
                "steps": [
                    f"Learn the fundamentals of {skill}",
                    f"Practice {skill} using small exercises",
                    f"Build a project using {skill}"
                ]
            })

    return roadmap