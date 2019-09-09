function handleSubmitIndividual() {
    d3.event.preventDefault();

    var pokemonC = d3.select("#pokemonInputC").node().value;
    console.log(pokemonC);
    d3.select("#pokemonInputC").node().value = "";

    buildStatIndividual(pokemonC);
}

function buildStatIndividual(pokemonC) {
    var url = "/pokemon";
    d3.json(url).then(function(response) {
        console.log(response);
        
        var filteredPokemonC = response.filter(function(item) {
            return item["Name"] === pokemonC;
        });
        PokemonC = filteredPokemonC[0];
        console.log(`Pokemon C is ${Object.getOwnPropertyNames(PokemonC)}`)
        var PokemonStatsC = {
            Total: PokemonC["Total"], 
            HP: PokemonC["HP"], 
            Attack: PokemonC["Attack"], 
            Defense: PokemonC["Defense"], 
            SpAtk: PokemonC["SpAtk"],
            SpDef: PokemonC["SpDef"], 
            Speed: PokemonC["Speed"]}
        console.log(PokemonStatsC);

        var traceC = {
            x: Object.getOwnPropertyNames(PokemonStatsC),
            y: Object.values(PokemonStatsC),
            name: PokemonC["Name"],
            type: "bar"
        }

        var data = [traceC];
        var layout = { 
            title: "Individual Stats"
        };
        Plotly.newPlot("IndividualStats", data, layout);
        console.log(Object.values(PokemonStatsC));
    });
}
d3.select("#SubmitPokemonC").on("click", handleSubmitIndividual);
