# DevSecOps Portfolio: Automated Infrastructure Security

## Project Overview
This repository demonstrates a **Shift-Left** security approach by integrating automated security scanning into the Infrastructure as Code (IaC) lifecycle.

## Technical Implementation
- **Infrastructure:** AWS resources defined using **Terraform**.
- **Security Scanning:** Integrated **Trivy** to perform Static Application Security Testing (SAST) on Terraform configurations.
- **CI/CD Pipeline:** Utilized **GitHub Actions** to automate security audits on every code push.

## Lab Objectives
1. Identify misconfigured cloud resources (e.g., Public S3 Buckets) before deployment.
2. Enforce the **Principle of Least Privilege** in IAM roles.
3. Automate the "Fail-Fast" mechanism to block insecure infrastructure changes.

## Tools Used
- Terraform
- GitHub Actions
- Trivy / Checkov
- AWS (IAM, S3)