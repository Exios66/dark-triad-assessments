# Changelog

## [Unreleased]

### Added

- Complete MACH-IV assessment with all validated questions
- Improved dark mode functionality for better UI inversion
- Updated chart colors to match dark mode theme
- Auto-advance feature for questions after 4 seconds of inactivity
- Patient ID and timestamp added to exported results
- Simulated local storage for exported results
- Functionality to upload and visualize stored results
- Improved typography using Lato and Roboto fonts
- Statistical analysis functionality including:
  - Cronbach's Alpha
  - Split-Half Reliability
  - ANOVA
  - Inter-Item Validity
  - Psychometric Analysis
- Ability to upload data files for statistical analysis
- Math.js library for advanced mathematical calculations
- Footer section with links to repository wiki and scientific articles
- Modal window displaying relevant scientific articles
- Improved styling for footer and modal
- Data visualization for statistical analyses
- Display of formulas and logic used in calculations
- Integration of MathJax for rendering LaTeX formulas
- Enhanced result display for all statistical analyses

### Changed

- Refactored dark mode toggle function for better performance
- Enhanced createChart function to support dynamic color changes and uploaded data visualization
- Modified export function to include patient ID and timestamp
- Updated UI to include a new Statistics section in the main menu

### Fixed

- Dark mode now properly inverts all UI elements, including assessments and results
- Improved data parsing for CSV and JSON files