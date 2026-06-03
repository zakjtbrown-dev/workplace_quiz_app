# Workplace Cyber Security Quiz Application

## 1. Introduction

## 2. Design Section

### 2.1 GUI Design

The (GUI) was designed in Figma before development commenced. The objective was to create a simple and intuitive application that could be used by workplace staff with minimal technical knowledge.

The application consists of three main screens:

- A Start Screen where users enter their name before beginning the quiz.
- A Question Screen where users answer multiple-choice questions.
- A Result Screen where users receive their final score.

#### Start Screen

![Start Screen Wireframe](docs/screenshots/Start_wireframe.png)

The Start Screen allows users to enter their name and begin the quiz.

#### Question Screen

![Question Screen Wireframe](docs/screenshots/Question_wireframe.png)

The Question Screen presents questions and answer options in a clear format using radio button selections.

#### Result Screen

![Result Screen Wireframe](docs/screenshots/Result_wireframe.png)

The Result Screen displays the user's final score after completing all questions.

### 2.2 User Journey
### 2.2 User Journey

The user journey was designed to be simple and efficient. Users enter their name, answer quiz questions, receive a score, and have their results automatically saved to a CSV file.

![User Journey](docs/screenshots/user_journey.png)

### 2.3 Functional Requirements
### 2.3 Functional Requirements

| ID | Requirement |
|----|-------------|
| FR1 | The user shall be able to enter their name. |
| FR2 | The user shall be able to start the quiz. |
| FR3 | The user shall be able to answer multiple-choice questions. |
| FR4 | The application shall calculate a final score. |
| FR5 | The application shall display the final score. |
| FR6 | The application shall save results to a CSV file. |
| FR7 | The application shall validate user inputs. |

### 2.4 Non-Functional Requirements
### 2.4 Non-Functional Requirements

| ID | Requirement |
|----|-------------|
| NFR1 | The application should be easy to use. |
| NFR2 | The application should run on Python 3.9 or above. |
| NFR3 | The application should provide fast response times. |
| NFR4 | Data should be stored persistently using CSV files. |
| NFR5 | The application should be maintainable and documented. |
| NFR6 | The application should be testable using automated unit tests. |

### 2.5 Tech Stack
### 2.5 Tech Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| GUI Framework | Tkinter |
| Data Storage | CSV |
| Testing Framework | Pytest |
| Version Control | Git |
| Repository Hosting | GitHub |
| Continuous Integration | GitHub Actions |
| Design Tool | Figma |

### 2.6 Code Design
### 2.6 Code Design

The application was developed using object-oriented programming principles.

Three primary classes were used:

- Question
- Quiz
- QuizApp

The Question class stores individual question information.

The Quiz class manages questions, user answers, and score calculation.

The QuizApp class controls the graphical user interface and overall application flow.

![Class Diagram](docs/screenshots/Class_diagram.png)

## 3. Development Section

## 4. Testing Section

### 4.1 Testing Strategy

### 4.2 Manual Testing

### 4.3 Unit Testing

### 4.4 Continuous Integration

## 5. Documentation Section

### 5.1 User Documentation

### 5.2 Technical Documentation

## 6. Evaluation Section