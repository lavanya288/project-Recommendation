# AI-Based Project Recommendation System

A smart project recommendation system that uses machine learning to suggest suitable projects based on user preferences, skills, and experience level.

## 🎯 Features

- **Personalized Recommendations**: Get project suggestions based on your domain, programming language, framework, and skill level
- **Content-Based Filtering**: Uses TF-IDF vectorization and cosine similarity for accurate recommendations
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Save & Share**: Save favorite projects and share them with others
- **Real-time Processing**: Instant recommendations powered by Python and scikit-learn

## 📋 System Overview

```
User Input (Preferences)
        ↓
Flask Backend API
        ↓
Recommendation Engine (scikit-learn)
        ↓
Project Dataset (JSON)
        ↓
Ranked Recommendations
        ↓
Display on Frontend
```

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3 (Responsive Design)
- JavaScript (Vanilla JS)

### Backend
- Python 3.8+
- Flask (Web Framework)
- scikit-learn (Machine Learning)
- pandas (Data Processing)
- Flask-CORS (Cross-Origin Resource Sharing)

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Windows/Mac/Linux

### Step 1: Clone or Download the Project
```bash
cd "c:\Users\Admin\OneDrive\Desktop\eye gaze"
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Browser
Open your web browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
eye gaze/
├── app.py                      # Flask application and API endpoints
├── requirements.txt            # Python dependencies
├── projects_dataset.json       # Project database
├── templates/
│   └── index.html             # Main HTML template
└── static/
    ├── style.css              # CSS styling
    └── script.js              # JavaScript logic
```

## 🎮 How to Use

1. **Select Your Preferences**:
   - Choose a Domain (AI, Web, Mobile, etc.)
   - Select Programming Language
   - Pick a Framework/Technology
   - Choose Difficulty Level (Beginner, Intermediate, Advanced)
   - Select your known skills (multiple selections allowed)

2. **Get Recommendations**:
   - Click "Get Recommendations" button
   - Wait for the system to process your preferences

3. **Review Results**:
   - View recommended projects ranked by match percentage
   - See project details including domain, technology, skills required, and description

4. **Take Action**:
   - **Save Project**: Save projects for later reference (stored in browser)
   - **Share Project**: Share project recommendations with friends
   - **Match Score**: Each recommendation shows percentage match with your preferences

## 🧠 Recommendation Algorithm

The system uses **Content-Based Filtering** with the following approach:

1. **Feature Extraction**: Converts project attributes and user preferences into feature vectors
2. **Vectorization**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer
3. **Similarity Calculation**: Computes cosine similarity between user input and projects
4. **Ranking**: Projects are ranked by similarity score (0-1, where 1 is perfect match)

### Attributes Considered:
- Domain/Field
- Programming Language
- Framework/Technology
- Difficulty Level
- Required Skills
- Team Size

## 📊 Dataset Structure

The `projects_dataset.json` contains 15+ projects with the following structure:

```json
{
    "id": 1,
    "name": "AI Chatbot",
    "domain": "AI",
    "language": "Python",
    "framework": "Flask",
    "difficulty": "Intermediate",
    "skills": ["Python", "NLP", "Machine Learning"],
    "team_size": 2,
    "description": "Build an intelligent chatbot..."
}
```

## 🔌 API Endpoints

### 1. Get Recommendations
- **Endpoint**: `POST /api/get-recommendations`
- **Input**:
```json
{
    "domain": "AI",
    "language": "Python",
    "framework": "Flask",
    "difficulty": "Intermediate",
    "skills": ["Python", "ML"]
}
```
- **Output**:
```json
{
    "success": true,
    "recommendations": [
        {
            "id": 1,
            "name": "AI Chatbot",
            "similarity_score": 0.85
            ...
        }
    ]
}
```

### 2. Get All Projects
- **Endpoint**: `GET /api/get-projects`
- **Output**: List of all projects in dataset

### 3. Save Project
- **Endpoint**: `POST /api/save-project`
- **Input**:
```json
{
    "project_id": 1,
    "project_name": "AI Chatbot"
}
```

## 🎓 Learning Outcomes

By working with this project, you'll learn:
- Web application development with Flask
- Frontend development (HTML, CSS, JavaScript)
- Machine learning basics (Content-based filtering)
- API design and REST principles
- CSS Grid and Flexbox for responsive design
- Asynchronous JavaScript (Fetch API)
- Data processing with pandas

## 🚀 Future Enhancements

1. **User Accounts**: Add user authentication and persistent data storage
2. **Advanced ML**: Implement collaborative filtering and deep learning recommendations
3. **GitHub Integration**: Fetch real projects from GitHub
4. **Project Editor**: Allow admins to add/edit projects
5. **Analytics**: Track which projects are most recommended
6. **Skill Gap Analysis**: Show what skills to learn to match projects
7. **Mobile App**: Convert to React Native or Flutter
8. **AI-Generated Descriptions**: Use GPT-3 to generate project descriptions

## 🐛 Troubleshooting

### Issue: "Module not found" error
**Solution**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Port 5000 already in use
**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Issue: CORS errors
**Solution**: Flask-CORS is already configured, but ensure it's installed:
```bash
pip install Flask-CORS
```

### Issue: Static files not loading (CSS/JS)
**Solution**: Make sure the `static` and `templates` folders are in the same directory as `app.py`

## 📝 Sample Preferences for Testing

### Beginner Web Developer
- Domain: Web
- Language: JavaScript
- Framework: React
- Difficulty: Beginner
- Skills: JavaScript, React

### AI/ML Enthusiast
- Domain: AI
- Language: Python
- Framework: Flask
- Difficulty: Intermediate
- Skills: Python, Machine Learning, NLP

### Advanced Full-Stack Developer
- Domain: Web
- Language: JavaScript
- Framework: Next.js
- Difficulty: Advanced
- Skills: JavaScript, React, Node.js

## 📞 Support & Contributing

For questions or issues, feel free to check the code or modify as needed.

## 📄 License

This project is open-source and available for educational purposes.

## ✨ Credits

Developed as an AI-based recommendation system Project.

---

Happy Learning! 🎉
