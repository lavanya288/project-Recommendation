import csv
import random

# Define lists for generating varied data
domains = ['AI', 'Web', 'Machine Learning', 'Data Science', 'Mobile', 'DevOps', 'Blockchain', 'Cybersecurity', 'IoT', 'Game Development']
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust', 'TypeScript', 'C#', 'PHP', 'Ruby']
frameworks = ['Flask', 'Django', 'React', 'Vue.js', 'Angular', 'Next.js', 'Express', 'Spring Boot', 'FastAPI', 'Svelte', 'Ember', 'Nuxt']
difficulties = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
skills_options = [
    ['Python', 'NLP', 'Machine Learning'],
    ['JavaScript', 'React', 'Node.js'],
    ['Python', 'ML', 'Data Analysis'],
    ['Python', 'NLP', 'Text Processing'],
    ['JavaScript', 'Vue.js', 'API Integration'],
    ['JavaScript', 'React', 'State Management'],
    ['Python', 'Deep Learning', 'Computer Vision'],
    ['JavaScript', 'React', 'Node.js', 'Database'],
    ['Python', 'Data Analysis', 'Visualization'],
    ['Java', 'Spring', 'Microservices'],
    ['C++', 'Game Engine', 'Graphics'],
    ['Go', 'Concurrency', 'Scalability'],
    ['Rust', 'Memory Safety', 'Performance'],
    ['TypeScript', 'OOP', 'Design Patterns'],
    ['DevOps', 'Docker', 'Kubernetes'],
    ['Blockchain', 'Smart Contracts', 'Crypto'],
    ['Cybersecurity', 'Encryption', 'Penetration Testing'],
    ['IoT', 'Embedded Systems', 'Hardware'],
]

project_names = [
    'ChatBot', 'Chat Application', 'Recommendation System', 'Resume Analyzer', 'Weather Dashboard',
    'Task Manager', 'Image Classifier', 'E-Commerce', 'Stock Analyzer', 'Blog Platform',
    'Social Network', 'Video Streaming', 'File Manager', 'Music Player', 'Photo Editor',
    'Document Generator', 'Data Pipeline', 'REST API', 'Mobile App', 'Dashboard',
    'Scheduler', 'Notification System', 'Payment Gateway', 'Search Engine', 'Analytics Tool',
    'CRM System', 'ERP Solution', 'Wiki Platform', 'Forum App', 'Email Client',
    'Password Manager', 'VPN Client', 'Firewall', 'Intrusion Detector', 'Backup Tool',
    'Cloud Storage', 'Container Registry', 'Monitoring System', 'Log Aggregator', 'CI/CD Pipeline',
    'Virtual Machine', 'Network Simulator', 'Traffic Monitor', 'Load Balancer', 'API Gateway',
    '3D Game', 'Puzzle Game', 'Strategy Game', 'Racing Game', 'AR Application',
]

# Create CSV file
with open('projects_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'domain', 'language', 'framework', 'difficulty', 'skills', 'team_size', 'description'])
    
    for i in range(1, 651):  # Generate 650 projects
        name = f"{random.choice(project_names)} {i}"
        domain = random.choice(domains)
        language = random.choice(languages)
        framework = random.choice(frameworks)
        difficulty = random.choice(difficulties)
        skills = '|'.join(random.choice(skills_options))
        team_size = random.randint(1, 5)
        description = f"Build a {domain.lower()} project using {language} and {framework} framework."
        
        writer.writerow([i, name, domain, language, framework, difficulty, skills, team_size, description])

print('CSV file created successfully: projects_dataset.csv')
print('Total records: 650')
