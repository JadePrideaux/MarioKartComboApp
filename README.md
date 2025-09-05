# Mario Kart Combo App

## Overview
A full-stack application to generate and explore Mario Kart component combinations. The backend provides a RESTful API that serves random kart combo data, while the frontend displays combos using a React interface. A Python web scraper automates the collection of Mario Kart component data from the mario kart wiki.

## Tech Stack
- **Backend:** C#, ASP.NET Core Web API
- **Frontend:** React, TypeScript, Vite
- **Automation:** Python web scraper for dataset generation
- **Version Control:** Git/GitHub with feature branching

## Features
- RESTful API endpoint serving dynamically generated kart combo JSON data
- Strongly typed C# backend with interfaces and loaders to parse JSON
- Custom React hook for fetching combo data from the API
- Python scraper to extract Mario Kart component data from mario wiki tables into JSON

## Database / Storage
- JSON files for storing kart component and combo data
- Backend loads JSON into strongly typed C# objects for flexibility and maintainability

## Run etc.
- Run though Visual Studio, React Typescript + ASP.NET template used

## Screenshots
The frontend page, showing the randomised combo along with all of its overall stats.
<img width="599" height="922" alt="image" src="https://github.com/user-attachments/assets/ddf0c207-1995-4002-afb8-c7f11c93555e" />

