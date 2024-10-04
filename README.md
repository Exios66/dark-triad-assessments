# Dark Triad Assessments Web Application

This web application provides various psychological assessments related to the Dark Triad personality traits and other personality measures, as well as statistical analysis tools.

## Features

- Multiple assessments:
  - Short Dark Triad (SDT3)
  - Dirty Dozen
  - Short Dark Tetrad (SDT4)
  - MACH IV (Complete validated version)
  - MMPI-style Assessment
  - HEXACO Personality Assessment
  - OCEAN (Big Five) Personality Assessment
- Dark mode support with full UI inversion
- Interactive radar chart for result visualization
- Progress bar for assessment completion
- Ability to export results in TXT or CSV format with patient ID and timestamp
- Auto-advance feature for questions after 4 seconds of inactivity
- Functionality to upload and visualize stored results
- Improved typography using Lato and Roboto fonts
- Statistical analysis tools with data visualization:
  - Cronbach's Alpha
  - Split-Half Reliability
  - ANOVA
  - Inter-Item Validity
  - Psychometric Analysis
- Display of formulas and logic used in statistical calculations
- Footer with links to repository wiki and scientific articles
- Modal window displaying relevant scientific articles for each assessment

## Recent Updates

- Added statistical analysis functionality
- Implemented data file upload for analysis
- Integrated Math.js library for advanced calculations
- Added footer with links to additional resources
- Implemented modal window for displaying scientific articles
- Added data visualization for statistical analyses
- Implemented display of formulas and logic used in calculations
- Integrated MathJax for rendering LaTeX formulas

## Usage

1. Open the `index.html` file in a web browser.
2. Choose an assessment from the available options or select "Statistics" for data analysis.
3. For assessments:
   - Answer all questions honestly. If you don't respond within 4 seconds, the assessment will automatically move to the next question.
   - View your results and the radar chart visualization.
   - Optionally export your results in TXT or CSV format.
4. For statistical analysis:
   - Upload a CSV or JSON file containing your data.
   - Select the type of analysis you want to perform.
   - View the results of the analysis, including:
     - Numerical results
     - Data visualization
     - Formula used in the calculation
     - Step-by-step logic of the analysis

## Development

To modify or extend this application:

1. Clone the repository
2. Make changes to the `index.html` file
3. Test your changes locally
4. Commit and push your changes to the `gh-pages` branch for automatic deployment

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).