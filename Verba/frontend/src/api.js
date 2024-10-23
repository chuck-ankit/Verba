import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const sendMessageToBackend = async (userMessage) => {
  const instruction = "Translate the sentence to Hindi."; // Example instruction
  const response = await axios.post(`${API_URL}/chat/`, {
    instruction: instruction,
    input_text: userMessage
  });
  return response.data.response;
};
