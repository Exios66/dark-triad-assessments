# Dark Triad Assessments Web Application

This web application provides various assessments related to the Dark Triad personality traits: Machiavellianism, Narcissism, and Psychopathy. It includes multiple assessment types and visualizations of results.

## Features

- Multiple assessment types (SDT3, SDT4, MACH-IV, Dirty Dozens)
- Interactive user interface
- Visualization of results
- Responsive design

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- npm (v6 or later)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/dark-triad-assessments-webapp.git
   ```

2. Navigate to the project directory:
   ```
   cd dark-triad-assessments-webapp
   ```

3. Install dependencies:

   ```
   npm install
   ```

4. Start the development server:
   ```
   npm start
   ```

5. Open your browser and visit `http://localhost:3000`

## Running Tests

To run the test suite:

```
npm test
```

## Built With

- React
- React Router
- Context API for state management

## Project Structure

```
dark-triad-assessments-webapp/
├── public/
├── src/
│   ├── components/
│   │   ├── Assessment/
│   │   ├── common/
│   │   ├── Header/
│   │   ├── Footer/
│   │   └── Visualization/
│   ├── contexts/
│   ├── hooks/
│   ├── routes/
│   ├── services/
│   └── utils/
├── tests/
└── ...
```

## Changelog and Versioning

This project uses [Semantic Versioning](https://semver.org/) and maintains a changelog to document notable changes. The changelog is automatically updated using a Python script.

### Viewing the Changelog

The full changelog can be found in the [CHANGELOG.md](CHANGELOG.md) file in the root of the project.

### Updating the Changelog

The changelog is automatically updated after each commit using a Git post-commit hook. The update script analyzes the commit message to determine the type of change and updates the CHANGELOG.md file accordingly.

If you need to manually update the changelog, you can run the following command:

```
python update_changelog.py
```

When writing commit messages, use the following prefixes to categorize your changes:

- `feat:` for new features (increments the minor version)
- `fix:` for bug fixes (increments the patch version)
- `BREAKING CHANGE:` for breaking changes (increments the major version)
- `docs:`, `style:`, `refactor:`, `perf:`, `test:` for other changes (updates the changelog without changing the version)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Short Dark Triad (SD3)](https://openpsychometrics.org/tests/SD3/)
- [Short Dark Tetrad (SD4)](https://openpsychometrics.org/tests/SD4/)
- [MACH-IV](https://openpsychometrics.org/tests/MACH-IV/)
- [Dirty Dozen](https://openpsychometrics.org/tests/DD/)