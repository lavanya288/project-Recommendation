from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load project dataset from CSV
projects_df = pd.read_csv('projects_dataset.csv')

# Handle the skills column - it's stored as pipe-separated strings
projects_df['skills'] = projects_df['skills'].apply(lambda x: x.split('|') if isinstance(x, str) else [])

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 2))

def prepare_features(df):
    """Prepare feature vectors for projects"""
    features = []
    for idx, row in df.iterrows():
        feature_str = f"{row['domain']} {row['language']} {row['framework']} {row['difficulty']} {' '.join(row['skills'])}"
        features.append(feature_str)
    return features

def calculate_similarity(user_prefs, projects_list):
    """Calculate cosine similarity between user preferences and projects"""
    all_features = projects_list + [user_prefs]
    
    # Vectorize features
    tfidf_matrix = vectorizer.fit_transform(all_features)
    
    # Get similarity scores (last row is user input)
    similarities = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1])[0]
    
    return similarities

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get-recommendations', methods=['POST'])
def get_recommendations():
    """API endpoint to get project recommendations"""
    try:
        data = request.json
        
        # Extract user preferences
        domain = data.get('domain', '')
        language = data.get('language', '')
        framework = data.get('framework', '')
        difficulty = data.get('difficulty', '')
        skills = ' '.join(data.get('skills', []))
        
        # Create user preference string
        user_pref_str = f"{domain} {language} {framework} {difficulty} {skills}"
        
        # Prepare project features
        project_features = prepare_features(projects_df)
        
        # Calculate similarities
        similarities = calculate_similarity(user_pref_str, project_features)
        
        # Add scores to dataframe
        projects_df['similarity_score'] = similarities
        
        # Sort by similarity and get top 5
        top_projects = projects_df.nlargest(5, 'similarity_score')
        
        # Format output
        recommendations = []
        for idx, project in top_projects.iterrows():
            rec = {
                'id': int(project['id']),
                'name': str(project['name']),
                'domain': str(project['domain']),
                'language': str(project['language']),
                'framework': str(project['framework']),
                'difficulty': str(project['difficulty']),
                'skills': list(project['skills']) if isinstance(project['skills'], list) else [project['skills']],
                'team_size': int(project['team_size']),
                'description': str(project['description']),
                'similarity_score': round(float(project['similarity_score']), 2)
            }
            print(f"Backend returning project: {rec}")  # Debug logging
            recommendations.append(rec)
        
        print(f"Total recommendations: {len(recommendations)}")  # Debug logging
        return jsonify({'success': True, 'recommendations': recommendations})
    
    except Exception as e:
        print(f"Error in get_recommendations: {str(e)}")  # Debug logging
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/get-projects', methods=['GET'])
def get_projects():
    """API endpoint to get all projects"""
    try:
        projects = projects_df.to_dict('records')
        return jsonify({'success': True, 'projects': projects})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/save-project', methods=['POST'])
def save_project():
    """API endpoint to save a project"""
    try:
        data = request.json
        # In a real application, save to database
        return jsonify({'success': True, 'message': 'Project saved successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
