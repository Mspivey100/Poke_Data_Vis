function handleSubmitStatCompareA() {
    d3.event.preventDefault();

    var pokemonA = d3.select("#pokemonInputA").node().value;
    console.log(pokemonA);
    d3.select("#pokemonInputA").node().value = "";

    var pokemonB = d3.select("#pokemonInputB").node().value;
    console.log(pokemonB);
    d3.select("#pokemonInputB").node().value = "";

    buildStatComparePlot(pokemonA,pokemonB);
}

function buildStatComparePlot(pokemonA, pokemonB) {
    var url = "/pokemon";
    d3.json(url).then(function(response) {
        console.log(response);
        var filteredPokemonA = response.filter(function(item) {
            return item["Name"] === pokemonA;
        });
        var PokemonA = filteredPokemonA[0];
        console.log(`Pokemon A is ${Object.getOwnPropertyNames(PokemonA)}`)
        var PokemonStatsA = {
            Total: PokemonA["Total"], 
            HP: PokemonA["HP"], 
            Attack: PokemonA["Attack"], 
            Defense: PokemonA["Defense"], 
            SpAtk: PokemonA["SpAtk"],
            SpDef: PokemonA["SpDef"], 
            Speed: PokemonA["Speed"]}
        console.log(PokemonStatsA);

        var traceA = {
            x: Object.getOwnPropertyNames(PokemonStatsA),
            y: Object.values(PokemonStatsA),
            name: PokemonA["Name"],
            type: "bar"
        }

        var filteredPokemonB = response.filter(function(item) {
            return item["Name"] === pokemonB;
        });
        PokemonB = filteredPokemonB[0];
        console.log(`Pokemon B is ${Object.getOwnPropertyNames(PokemonB)}`)
        var PokemonStatsB = {
            Total: PokemonB["Total"], 
            HP: PokemonB["HP"], 
            Attack: PokemonB["Attack"], 
            Defense: PokemonB["Defense"], 
            SpAtk: PokemonB["SpAtk"],
            SpDef: PokemonB["SpDef"], 
            Speed: PokemonB["Speed"]}
        console.log(PokemonStatsB);

        var traceB = {
            x: Object.getOwnPropertyNames(PokemonStatsB),
            y: Object.values(PokemonStatsB),
            name: PokemonB["Name"],
            type: "bar"
        }

        var data = [traceA, traceB];
        var layout = { 
            title: "Stat Compare",
            barmode: "group"
        };
        Plotly.newPlot("statComparePlot", data, layout);
        console.log(Object.values(PokemonStatsA));
    });
      
}

d3.select("#SubmitPokemonA").on("click", handleSubmitStatCompareA);
