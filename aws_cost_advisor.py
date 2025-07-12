# aws_cost_advisor.py
"""
Simulated backend logic for AI Cost Optimization Advisor
Note: This is a mockup, not connected to actual AWS APIs.
"""

import random

def get_mock_cost_data(service):
    mock_costs = {
        "EC2": round(random.uniform(120.0, 500.0), 2),
        "S3": round(random.uniform(10.0, 50.0), 2),
        "RDS": round(random.uniform(50.0, 200.0), 2),
        "Lambda": round(random.uniform(5.0, 20.0), 2),
    }
    return mock_costs.get(service, 0.0)

def suggest_cost_optimizations(service):
    suggestions = {
        "EC2": [
            "Consider using Spot Instances for non-critical workloads.",
            "Right-size your EC2 instances using Trusted Advisor recommendations.",
            "Shut down idle instances using automated schedules."
        ],
        "S3": [
            "Enable S3 lifecycle policies to move infrequently accessed data to Glacier.",
            "Use S3 Intelligent-Tiering to optimize costs."
        ],
        "RDS": [
            "Switch to reserved instances if usage is consistent.",
            "Enable automatic backups and delete unused snapshots."
        ],
        "Lambda": [
            "Review memory allocation and reduce if not needed.",
            "Minimize function execution time by optimizing code."
        ]
    }
    return suggestions.get(service, ["No specific suggestions available."])

def analyze_costs():
    services = ["EC2", "S3", "RDS", "Lambda"]
    report = "\n=== AWS Cost Analysis Report ===\n"
    for service in services:
        cost = get_mock_cost_data(service)
        report += f"\nService: {service}\nEstimated Cost: ${cost}"
        suggestions = suggest_cost_optimizations(service)
        for s in suggestions:
            report += f"\n- {s}"
    return report

if __name__ == "__main__":
    print(analyze_costs())
