import React from 'react';
import { Link } from 'react-router-dom';
import { ASSESSMENT_TYPES } from '../../utils/constants';
import './AssessmentSelector.css';

function AssessmentSelector() {
  return (
    <div className="assessment-selector">
      <h2>Choose an Assessment</h2>
      <ul>
        <li>
          <Link to="/assessment/sdt3">{ASSESSMENT_TYPES.SDT3}</Link>
        </li>
        <li>
          <Link to="/assessment/sdt4">{ASSESSMENT_TYPES.SDT4}</Link>
        </li>
        {/* Add other assessment types here */}
      </ul>
    </div>
  );
}

export default AssessmentSelector;