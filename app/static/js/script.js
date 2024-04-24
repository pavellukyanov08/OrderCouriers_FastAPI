 async function send(){

        // получаем введеное в поле имя и возраст
        const name = document.getElementById("name").value;
        // const userage = document.getElementById("userage").value;

        // отправляем запрос
        const response = await fetch("/registr_courier", {
                method: "POST",
                headers: { "Accept": "application/json", "Content-Type": "application/json" },
                body: JSON.stringify({
                    name: name,
                })
            });
            if (response.ok) {
                const data = await response.json();
                document.getElementById("message").textContent = data.message;
            }
            else
                console.log(response);
    }