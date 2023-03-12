// id=user_id, message=text string , sent=true|false
function constructMessage(id, message, sent=true) {
    const msgDom = document.createElement("div");
    const date = moment().format('hh:mm A | Do MMM');
    const uid = +id * 10; 
    const profile_pic = `https://picsum.photos/id/${uid}/100`;
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
							src=${profile_pic}
							alt="sender profile picture"
                            class="p-img"
                            style="width: 45px; height: 45px; border-radius: 50%;"
                            width="45px"
                            height="45px"
						/>`
    } else {
        msgDom.className = "d-flex flex-row justify-content-start mb-2";
        msgDom.style.maxWidth = "60%";
        msgDom.innerHTML = `<img
                src=${profile_pic}
                alt="recipient profile picture"
                class="p-img"
                style="width: 45px; height: 45px; border-radius: 50%;"
                width="45px"
                height="45px"
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

function displayMessage(id, message, sent=true) {
    const msgsContainer = document.querySelector("#messages-container");
    const newMessageDom = constructMessage(id, message, sent);
    msgsContainer.append(newMessageDom);
    msgsContainer.scrollTop = msgsContainer.scrollHeight
}