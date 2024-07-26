const startListening = document.getElementById("startListening");
const speechInput = document.getElementById("speech");
const questionForm = document.getElementById("questionForm");

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();

recognition.lang = 'en-US';
recognition.continuous = true; 
recognition.interimResults = true;

recognition.onresult = (event) => {
  for (let i = event.resultIndex; i < event.results.length; i++) {
      if (event.results[i].isFinal) {
          const result = event.results[i][0].transcript;
          speechInput.value = result + '\n';
          questionForm.submit();
      }
  }
};

startListening.addEventListener("click", () => {
    recognition.start();
});