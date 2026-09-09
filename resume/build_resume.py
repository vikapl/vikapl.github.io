from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

FONT_DIR = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("Sans", FONT_DIR + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", FONT_DIR + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Italic", FONT_DIR + "LiberationSans-Italic.ttf"))

ACCENT = colors.HexColor("#b5502e")
INK = colors.HexColor("#211c15")
INK2 = colors.HexColor("#443c30")
INK3 = colors.HexColor("#5b5142")

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name", parent=styles["Normal"], fontName="Sans-Bold",
    fontSize=20, textColor=INK, spaceAfter=2, leading=23,
)
title_style = ParagraphStyle(
    "Title", parent=styles["Normal"], fontName="Sans",
    fontSize=10.3, textColor=ACCENT, spaceAfter=3, leading=13,
)
contact_style = ParagraphStyle(
    "Contact", parent=styles["Normal"], fontName="Sans",
    fontSize=9, textColor=INK3, spaceAfter=8, leading=12,
)
section_style = ParagraphStyle(
    "Section", parent=styles["Normal"], fontName="Sans-Bold",
    fontSize=10.3, textColor=INK, spaceBefore=8, spaceAfter=3,
    letterSpacing=0.6,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Sans",
    fontSize=9.2, textColor=INK2, leading=12.3, spaceAfter=2,
    alignment=TA_LEFT,
)
role_style = ParagraphStyle(
    "Role", parent=styles["Normal"], fontName="Sans-Bold",
    fontSize=9.8, textColor=INK, spaceAfter=0, leading=12,
)
company_style = ParagraphStyle(
    "Company", parent=styles["Normal"], fontName="Sans-Italic",
    fontSize=9, textColor=INK3, spaceAfter=3, leading=11,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style, leftIndent=12, bulletIndent=0, spaceAfter=2,
)
skills_label_style = ParagraphStyle(
    "SkillsLabel", parent=styles["Normal"], fontName="Sans-Bold",
    fontSize=8.8, textColor=INK, leading=12,
)

doc = SimpleDocTemplate(
    "Vika-Plamadeala-Resume.pdf", pagesize=letter,
    leftMargin=0.62 * inch, rightMargin=0.62 * inch,
    topMargin=0.45 * inch, bottomMargin=0.45 * inch,
    title="Vika Plamadeala - Resume", author="Vika Plamadeala",
)

story = []

story.append(Paragraph("Vika Plamadeala", name_style))
story.append(Paragraph("DevOps Engineer · AWS · Kubernetes · Terraform · Agentic AI Workflows", title_style))
story.append(Paragraph(
    "Atlanta, GA &nbsp;·&nbsp; vika_plamadeala@yahoo.com &nbsp;·&nbsp; 331-803-8338 &nbsp;·&nbsp; "
    "linkedin.com/in/vika-plamadeala", contact_style
))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e3d7bf"), spaceAfter=8))

story.append(Paragraph("SUMMARY", section_style))
story.append(Paragraph(
    "DevOps Engineer with 4+ years running production Kubernetes for an 18-microservice, "
    "consumer-facing booking platform on AWS. Cut incident resolution time from 50 to 18 minutes "
    "through symptom-based alerting. Built AI-assisted automation spanning PR review across 30 "
    "repositories and a policy-gated EKS remediation pipeline.",
    body_style
))

story.append(Paragraph("EXPERIENCE", section_style))

story.append(Paragraph("DevOps Engineer &nbsp;|&nbsp; Hyatt Hotels Corporation &nbsp;|&nbsp; Remote", role_style))
story.append(Paragraph("Jan 2024 — Present", company_style))
hyatt_bullets = [
    "Scaled EKS infrastructure for a consumer-facing booking platform from 8 to 24 nodes (250 to 600 pods) during peak promotions while holding sub-second API latency.",
    "Standardized GitOps delivery for 18 microservices with GitHub Actions and ArgoCD, automating builds, security checks, Helm deployments, and canary/blue-green releases.",
    "Replaced all-at-once Lambda releases with gated canary deployments using CodeDeploy and CloudWatch, automatically rolling back releases when error rates increased.",
    "Reduced incident resolution time from 50 to 18 minutes by redesigning Prometheus and CloudWatch alerts around customer-facing symptoms and linking them to service-specific runbooks.",
    "Automated container vulnerability response with Amazon Inspector, EventBridge, and Lambda, routing Critical/High findings directly to Slack for developer response.",
    "Automated PR review across 30 repositories with a Claude Code agent that validates Jira requirements and detects exposed secrets before merge, flagging issues for developer review.",
    "Personal project: built a policy-gated EKS remediation pipeline (EventBridge, Lambda) that diagnoses CloudWatch alarm incidents and, for a narrow allow-listed set of failure types, automatically restarts the affected workload or scales the node group; validated end-to-end against real alarm fixtures.",
]
for b in hyatt_bullets:
    story.append(Paragraph(f"–&nbsp; {b}", bullet_style))

story.append(Spacer(1, 3))
story.append(Paragraph("Cloud Engineer &nbsp;|&nbsp; HelloFresh &nbsp;|&nbsp; Remote", role_style))
story.append(Paragraph("May 2022 — Jan 2024", company_style))
hellofresh_bullets = [
    "Standardized infrastructure across 10 AWS environments by developing reusable Terraform and CloudFormation modules for repeatable provisioning and configuration.",
    "Hardened AWS access for 25 developers by implementing least-privilege IAM policies scoped to role-specific responsibilities.",
    "Implemented AWS VPC networking across subnets, NACLs, and bastion hosts for isolated, secure cross-environment access.",
    "Automated dev/staging resource scheduling to eliminate idle non-production spend.",
]
for b in hellofresh_bullets:
    story.append(Paragraph(f"–&nbsp; {b}", bullet_style))

story.append(Paragraph("SKILLS", section_style))
skills_data = [
    ["Cloud & Infrastructure:", "AWS, EKS, Lambda, EventBridge, VPC, IAM, Terraform, CloudFormation"],
    ["Kubernetes & GitOps:", "Kubernetes, ArgoCD, Helm, Docker"],
    ["CI/CD & Delivery:", "GitHub Actions, Git, AWS CodeDeploy, Jira"],
    ["Observability & Reliability:", "Prometheus, CloudWatch, EFK, Alerting, Incident Response, Runbooks"],
    ["Security:", "Amazon Inspector, IAM, Container Security, Vulnerability Management"],
    ["AI-Assisted Engineering:", "Claude Code, Agentic AI Workflows, Prompt Engineering"],
    ["Scripting:", "Python, Bash"],
]
skill_rows = [[Paragraph(k, skills_label_style), Paragraph(v, body_style)] for k, v in skills_data]
skills_table = Table(skill_rows, colWidths=[1.55 * inch, 5.1 * inch])
skills_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 1.5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
]))
story.append(skills_table)

story.append(Paragraph("EDUCATION & CERTIFICATIONS", section_style))
cert_lines = [
    "CKA — Certified Kubernetes Administrator — 2024",
    "CKAD — Certified Kubernetes Application Developer — 2023",
    "HashiCorp Certified: Terraform Associate (004) — 2026",
    "Master's Degree in Social Work | Ion Creangă State Pedagogical University, Chisinau — 2014",
]
for c in cert_lines:
    story.append(Paragraph(f"–&nbsp; {c}", bullet_style))

doc.build(story)
print("done")
