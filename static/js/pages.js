function getData() {
    axios.get(`${location.origin}/api/pages`)
        .then(response => {
            const data = response.data;
            const nav = document.getElementById('nav');
            data.forEach(function (item) {
                const listItem = document.createElement("a");
                listItem.innerText = item.title;
                listItem.classList.add("button_article");
                listItem.setAttribute("href", `/pages/${item.slug}`);
                nav.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error(error);
        });
}