import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AssessmentProvider } from './contexts/AssessmentContext';
import Header from './components/Header/Header';
import AppRoutes from './routes/Routes';

function App() {
  return (
    <Router>
      <AssessmentProvider>
        <div className="App">
          <Header />
          <AppRoutes />
        </div>
      </AssessmentProvider>
    </Router>
  );
}

export default App;