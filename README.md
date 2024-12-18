# Tripwise

Tripwise is a tourism-based web application designed to provide a comprehensive trip planning experience. With Tripwise, users can explore destinations, create travel itineraries, and receive personalized recommendations for their trips. This project is built using Django for the backend and HTML, CSS, and JavaScript for the frontend.

## Features

- **Destination Exploration**: Browse a wide range of destinations with detailed descriptions and images.
- **Itinerary Planner**: Create and manage custom travel itineraries.
- **AI Chatbot**: Plan a detailed trip by interacting with an AI chatbot that suggests activities and destinations based on user input.
- **Weather Forecast**: Get real-time weather updates for selected destinations.
- **Community Features**: Share trip experiences, post photos, and engage in group chats.

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL (hosted on Supabase)
- **AI Integration**: Chatbot powered by GPT-like models
- **APIs**: 
  - OpenWeatherMap API for weather updates
  - Stormglass API for additional weather insights

## Installation

### Prerequisites

- Python 3.9+
- Node.js and npm
- PostgreSQL

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tripwise.git
   cd tripwise
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:

   Create a `.env` file in the project root and add the following:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   OPENWEATHER_API_KEY=your_openweathermap_api_key
   STORMGLASS_API_KEY=your_stormglass_api_key
   ```

5. Run database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Trip Planning**: Interact with the chatbot or manually create itineraries.
- **Community Interaction**: Share experiences and connect with other travelers.
- **Weather Insights**: Use the weather forecast feature to plan trips better.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add feature-name"
   ```

4. Push your changes:

   ```bash
   git push origin feature-name
   ```

5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenWeatherMap for weather data
- Stormglass for marine weather insights
- Django and Python community for excellent frameworks and libraries



------****************************************************----------



# Recommendation Engine

This project is a Flask-based web application that provides personalized recommendations to users using machine learning algorithms. It incorporates content-based filtering and sentiment analysis to deliver accurate and user-specific suggestions.

## Features

- **Content-Based Filtering**: Recommends items based on user preferences and item similarity.
- **Sentiment Analysis**: Analyzes user feedback to improve recommendations.
- **Interactive Interface**: Simple and intuitive user interface for interaction.

## Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: Content-based filtering, Sentiment Analysis (using libraries like scikit-learn and nltk)
- **Frontend**: HTML, CSS, JavaScript

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/recommendation-engine.git
   cd recommendation-engine
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:

   Create a `.env` file in the project root and add the following:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   ```

5. Start the application:

   ```bash
   flask run
   ```

6. Access the application at `http://127.0.0.1:5000/`.

## Usage

- **Getting Recommendations**: Input preferences to receive tailored recommendations.
- **Feedback**: Submit feedback on recommendations to enhance the system.

## Machine Learning Models

1. **Content-Based Filtering**:
   - Uses item features and user profiles to recommend similar items.
   - Techniques: Cosine similarity, TF-IDF, etc.

2. **Sentiment Analysis**:
   - Analyzes user reviews or feedback to understand sentiment.
   - Techniques: Text preprocessing, Naive Bayes classifier, etc.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add feature-name"
   ```

4. Push your changes:

   ```bash
   git push origin feature-name
   ```

5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask and Python community for excellent frameworks and libraries
- scikit-learn and nltk for machine learning and natural language processing tools


# Note : Run both engine and app on different servers

# author: Narayan Prashant Naik
# please star my repo
 
 
