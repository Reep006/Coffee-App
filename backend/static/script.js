const coffeeList = document.getElementById("coffeeList");
async function loadCoffees() {
    const response = await fetch("/get_coffees");
    const coffees = await response.json();
    coffeeList.innerHTML = "";
    coffees.forEach(coffee => {
        coffeeList.innerHTML += `
        <div class="coffee-card">
            <div class="left">
                <img src="images/${coffee.image}" alt="coffee">
                <div class="info">
                    <h2>${coffee.name}</h2>
                    <p>Votes: ${coffee.votes}</p>
                </div>
            </div>
            <button class="vote-btn"
            onclick="voteCoffee('${coffee._id}')">
            +
            </button>
        </div>
        `;
    });
}
async function voteCoffee(id){
    await fetch(`/vote/${id}`, {
        method:"POST"
    });
    loadCoffees();
}
loadCoffees();