const socket = io();


document.getElementById('sendButton').addEventListener('click', function () {
    const message = document.getElementById('textAreaExample').value;
    addIncomingMessage(message)
    socket.emit('chat', message);
    addWaitingMessage();
    document.getElementById('textAreaExample').value = '';
});

socket.on('chat_response', function (data) {
    removeWaitingMessage();
    addOutgoingMessage(data)
});

function addIncomingMessage(message) {
    const messagesContainer = document.getElementById('messagesContainer');

    const outgoingMessage = document.createElement('div');
    outgoingMessage.classList.add('d-flex', 'flex-row', 'justify-content-end', 'mb-4');

    const messageBox = document.createElement('div');
    messageBox.classList.add('p-3', 'me-3', 'border', 'bg-body-tertiary');
    messageBox.style.borderRadius = '15px';
    messageBox.innerHTML = `<p class="small mb-0">${message}</p>`;

    const avatar = document.createElement('img');
    avatar.src = 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava2-bg.webp';
    avatar.alt = 'avatar';
    avatar.style.width = '45px';
    avatar.style.height = '100%';

    outgoingMessage.appendChild(messageBox);
    outgoingMessage.appendChild(avatar);
    messagesContainer.appendChild(outgoingMessage);
    console.log(message)
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Function to add an incoming message to the chat box
function addOutgoingMessage(message) {
    const messagesContainer = document.getElementById('messagesContainer');

    const incomingMessage = document.createElement('div');
    incomingMessage.classList.add('d-flex', 'flex-row', 'justify-content-start', 'mb-4');

    const avatar = document.createElement('img');
    avatar.src = 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp';
    avatar.alt = 'avatar';
    avatar.style.width = '45px';
    avatar.style.height = '100%';

    const messageBox = document.createElement('div');
    messageBox.classList.add('p-3', 'ms-3');
    messageBox.style.borderRadius = '15px';
    messageBox.style.backgroundColor = 'rgba(57, 192, 237, .2)';
    messageBox.innerHTML = `<p class="small mb-0">${message}</p>`;

    incomingMessage.appendChild(avatar);
    incomingMessage.appendChild(messageBox);
    messagesContainer.appendChild(incomingMessage);
    console.log(message)
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function addWaitingMessage() {
    const messagesContainer = document.getElementById('messagesContainer');

    // Temporary "waiting" message
    const waitingMessage = document.createElement('div');
    waitingMessage.id = 'waitingMessage'; // Give it an ID to remove later
    waitingMessage.classList.add('d-flex', 'flex-row', 'justify-content-start', 'mb-4');

    const avatar = document.createElement('img');
    avatar.src = 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp';
    avatar.alt = 'avatar';
    avatar.style.width = '45px';
    avatar.style.height = '100%';

    const messageBox = document.createElement('div');
    messageBox.classList.add('p-3', 'ms-3');
    messageBox.style.borderRadius = '15px';
    messageBox.style.backgroundColor = 'rgba(57, 192, 237, .2)';
    messageBox.innerHTML = `<p class="small mb-0">...</p>`; // "..." waiting text

    waitingMessage.appendChild(avatar);
    waitingMessage.appendChild(messageBox);
    messagesContainer.appendChild(waitingMessage);
    console.log("Waiting for response...");
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function removeWaitingMessage() {
    const waitingMessage = document.getElementById('waitingMessage');
    if (waitingMessage) {
        waitingMessage.remove();
    }
}