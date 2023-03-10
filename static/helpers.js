function constructMessage(message, sent) {
    const msgDom = document.createElement("div");
    const date = moment().format('hh:mm A | Do MMM');
    if (sent) {
        msgDom.className = "d-flex flex-row justify-content-end mb-2";
        msgDom.style.maxWidth = "60%";
        msgDom.style.marginLeft = "auto";
        msgDom.innerHTML = `<div>
						<p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">
							${message}
						</p>
                        <p class="small me-3 mb-3 rounded-3 text-muted">${date}</p>
						</div>
						<img
							src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp"
							alt="avatar 1"
							style="width: 45px; height: 100%"
						/>`
    } else {
        msgDom.className = "d-flex flex-row justify-content-start mb-2";
        msgDom.style.maxWidth = "60%";
        msgDom.innerHTML = `<img
                src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp"
                alt="avatar 2"
                style="width: 45px; height: 100%"
            />
            <div>
                <p
                    class="small p-2 ms-3 mb-1 rounded-3"
                    style="background-color: #f5f6f7"
                >
                    ${message}
                </p>
                <p class="small ms-3 mb-3 rounded-3 text-muted float-end">${date}</p>
            </div>`
    }
    return msgDom;
}

function displayMessage(message, sent) {
    const msgsContainer = document.querySelector("#messages-container");
    const newMessageDom = constructMessage(message, sent);
    msgsContainer.append(newMessageDom);
    msgsContainer.scrollTop = msgsContainer.scrollHeight
}