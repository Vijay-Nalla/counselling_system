const API_BASE_URL = 'http://localhost:5000/api';

export const getDropoutRisk = async (studentData) => {
  const response = await fetch(`${API_BASE_URL}/risk`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(studentData)
  });
  return await response.json();
};
