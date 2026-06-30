import pandas as pd
import random

roles = {
    "BackendDeveloper": [
        "Python", "FastAPI", "Django", "Flask",
        "SQL", "PostgreSQL", "MongoDB",
        "Docker", "Redis", "REST API"
    ],

    "FrontendDeveloper": [
        "React", "JavaScript", "HTML",
        "CSS", "TypeScript", "NextJS",
        "Redux", "Tailwind", "Bootstrap"
    ],

    "FullStackDeveloper": [
        "React", "NodeJS", "Express",
        "MongoDB", "PostgreSQL",
        "JavaScript", "TypeScript",
        "REST API", "Docker"
    ],

    "AIEngineer": [
        "Python", "TensorFlow", "PyTorch",
        "MachineLearning", "DeepLearning",
        "NLP", "LangChain", "FAISS",
        "Transformers", "ComputerVision"
    ],

    "DataScientist": [
        "Python", "Pandas", "NumPy",
        "MachineLearning", "Statistics",
        "ScikitLearn", "DataMining",
        "Visualization", "Research"
    ],

    "DataAnalyst": [
        "SQL", "Excel", "PowerBI",
        "Tableau", "Pandas",
        "Reporting", "Statistics",
        "DataVisualization"
    ],

    "MobileDeveloper": [
        "Flutter", "Dart", "Firebase",
        "Android", "Kotlin",
        "Java", "Swift",
        "ReactNative"
    ],

    "DevOpsEngineer": [
        "Docker", "Kubernetes", "AWS",
        "Azure", "Linux",
        "Terraform", "Jenkins",
        "CI/CD", "Monitoring"
    ],

    "CloudEngineer": [
        "AWS", "Azure", "GCP",
        "CloudSecurity", "Terraform",
        "Docker", "Kubernetes",
        "Networking"
    ],

    "CyberSecurityEngineer": [
        "NetworkSecurity", "PenTesting",
        "SIEM", "Linux",
        "CyberSecurity", "Wireshark",
        "IncidentResponse",
        "VulnerabilityAssessment"
    ],

    "QAEngineer": [
        "Selenium", "ManualTesting",
        "AutomationTesting",
        "JUnit", "PyTest",
        "TestCases", "API Testing"
    ],

    "UIUXDesigner": [
        "Figma", "AdobeXD",
        "Wireframing", "Prototyping",
        "UserResearch",
        "DesignSystems"
    ],

    "BusinessAnalyst": [
        "RequirementsGathering",
        "StakeholderManagement",
        "SQL", "Excel",
        "PowerBI", "Documentation"
    ],

    "MachineLearningEngineer": [
        "Python", "ScikitLearn",
        "TensorFlow", "PyTorch",
        "MLOps", "FeatureEngineering",
        "ModelDeployment"
    ],

    "DatabaseAdministrator": [
        "SQL", "PostgreSQL",
        "MySQL", "Oracle",
        "DatabaseDesign",
        "PerformanceTuning",
        "BackupRecovery"
    ]
}


rows = []

for role, skills in roles.items():

    for _ in range(80):  # 80 rows per role

        selected = random.sample(
            skills,
            random.randint(4, 6)
        )

        rows.append({
            "skills": " ".join(selected),
            "role": role
        })

df = pd.DataFrame(rows)

df.to_csv(
    "Data/resumes.csv",
    index=False
)

print(f"Created {len(df)} rows")