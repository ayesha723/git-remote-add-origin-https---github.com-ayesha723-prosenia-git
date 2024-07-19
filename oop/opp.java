// Function to send user message to chatbot
function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    displayUserMessage(userInput);

    // Call backend API (e.g., via AJAX) to handle user input
    // For simplicity, simulate chatbot response here
    const chatbotResponse = simulateChatbotResponse(userInput);
    displayChatbotMessage(chatbotResponse);

    // Clear user input
    document.getElementById('userInput').value = '';
}

// Function to display user message in chat
function displayUserMessage(message) {
    const chatMessages = document.getElementById('chatMessages');
    const userMessageElement = document.createElement('div');
    userMessageElement.classList.add('userMessage');
    userMessageElement.textContent = `You: ${message}`;
    chatMessages.appendChild(userMessageElement);
}

// Function to display chatbot message in chat
function displayChatbotMessage(message) {
    const chatMessages = document.getElementById('chatMessages');
    const chatbotMessageElement = document.createElement('div');
    chatbotMessageElement.classList.add('chatbotMessage');
    chatbotMessageElement.textContent = `Chatbot: ${message}`;
    chatMessages.appendChild(chatbotMessageElement);
}

// Simulate chatbot response based on user input
function simulateChatbotResponse(userInput) {
    // Dummy logic to handle user input and generate chatbot response
    if (userInput.toLowerCase().includes('skills')) {
        return 'Here are your skills: HTML, CSS, JavaScript, C++, Python';
    } else if (userInput.toLowerCase().includes('projects')) {
        return 'You have completed multiple projects. Great job!';
    } else if (userInput.toLowerCase().includes('recommend')) {
        return 'Based on your profile, you should explore machine learning and AI.';
    } else {
        return "I'm sorry, I can't understand that. Please ask about skills, projects, or recommendations.";
    }
}
