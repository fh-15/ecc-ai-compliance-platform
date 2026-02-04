from dataclasses import dataclass
from typing import List


@dataclass
class ECCControl:
    id: int
    code: str
    name: str
    objective: str
    required_evidence: List[str]
    weight: int


ECC_CONTROLS = [
    ECCControl(
        id=1,
        code="1-1",
        name="Cybersecurity Strategy",
        objective="Ensure that cybersecurity plans, goals, initiatives, and projects align with applicable laws and regulations.",
        required_evidence=[
            "Approved cybersecurity strategy document",
            "Cybersecurity roadmap",
            "Management approval records"
        ],
        weight=10
    ),
    ECCControl(
        id=2,
        code="1-2",
        name="Cybersecurity Management",
        objective="Ensure effective management and governance of cybersecurity within the organization.",
        required_evidence=[
            "Cybersecurity organizational structure",
            "Defined roles and responsibilities",
            "Governance framework documentation"
        ],
        weight=10
    ),
    ECCControl(
        id=3,
        code="1-3",
        name="Cybersecurity Policies and Procedures",
        objective="Ensure cybersecurity policies and procedures are documented, approved, and implemented.",
        required_evidence=[
            "Approved cybersecurity policies",
            "Documented procedures",
            "Policy review records"
        ],
        weight=10
    ),
    ECCControl(
        id=4,
        code="1-4",
        name="Cybersecurity Roles and Responsibilities",
        objective="Ensure cybersecurity roles and responsibilities are clearly defined and assigned.",
        required_evidence=[
            "Role descriptions",
            "Responsibility matrix",
            "Assignment approvals"
        ],
        weight=10
    ),
    ECCControl(
        id=5,
        code="1-5",
        name="Cybersecurity Risk Management",
        objective="Ensure cybersecurity risks are identified, assessed, and treated appropriately.",
        required_evidence=[
            "Risk assessment reports",
            "Risk treatment plans",
            "Risk register"
        ],
        weight=10
    ),
    ECCControl(
        id=6,
        code="1-6",
        name="Cybersecurity in Information and Technology Projects",
        objective="Ensure cybersecurity requirements are integrated into IT projects.",
        required_evidence=[
            "Project cybersecurity requirements",
            "Secure SDLC documentation",
            "Project risk assessments"
        ],
        weight=10
    ),
    ECCControl(
        id=7,
        code="1-7",
        name="Cybersecurity Regulatory Compliance",
        objective="Ensure compliance with applicable cybersecurity laws and regulations.",
        required_evidence=[
            "Compliance register",
            "Regulatory mapping documents",
            "Compliance assessment reports"
        ],
        weight=10
    ),
    ECCControl(
        id=8,
        code="1-8",
        name="Periodical Cybersecurity Review and Audit",
        objective="Ensure periodic reviews and audits of cybersecurity controls.",
        required_evidence=[
            "Internal audit reports",
            "External audit reports",
            "Corrective action plans"
        ],
        weight=10
    ),
    ECCControl(
        id=9,
        code="1-9",
        name="Cybersecurity in Human Resources",
        objective="Ensure cybersecurity requirements are applied throughout the employee lifecycle.",
        required_evidence=[
            "HR cybersecurity procedures",
            "Background check records",
            "Employee onboarding/offboarding records"
        ],
        weight=10
    ),
    ECCControl(
        id=10,
        code="1-10",
        name="Cybersecurity Awareness and Training Program",
        objective="Ensure cybersecurity awareness and training are provided to all personnel.",
        required_evidence=[
            "Training plans",
            "Awareness materials",
            "Training attendance records"
        ],
        weight=10
    ),
]

