import React from 'react';
import { Link } from 'react-router-dom';
import { ASSESSMENT_TYPES } from '../../utils/constants';
import './Home.css';

function Home() {
  return (
    <div className="home">
      <h1>Personality Assessments</h1>
      <nav>
        <ul>
          <li>
            <Link to="/assessment/sdt3">
              {ASSESSMENT_TYPES.SDT3} Assessment
            </Link>
          </li>
          <li>
            <Link to="/assessment/sdt4">
              {ASSESSMENT_TYPES.SDT4} Assessment
            </Link>
          </li>
          <li>
            <Link to="/assessment/dirty-dozen">
              {ASSESSMENT_TYPES.DIRTY_DOZEN} Assessment
            </Link>
          </li>
          <li>
            <Link to="/assessment/secs">
              {ASSESSMENT_TYPES.SECS} Assessment
            </Link>
          </li>
          <li>
            <Link to="/assessment/sba">
              {ASSESSMENT_TYPES.SBA} Assessment
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;