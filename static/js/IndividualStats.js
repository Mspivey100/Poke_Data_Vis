function handleSubmitStatCompare() {
    d3.event.preventDefault();

    var pokemonA = d3.select("#pokemonInputC").node().value;
    console.log(pokemonA);
    d3.select("#pokemonInputC").node().value = "";

    var pokemonB = d3.select("#pokemonInputC").node().value;
    console.log(pokemonB);
    d3.select("#pokemonInputC").node().value = "";

    buildStatComparePlot(pokemonC);
}

function buildStatComparePlot(pokemonC) {
    var url = "/pokemon";
    d3.json(url).then(function(datalist) {
        console.log(datalist);
        var PokemonC = datalist.filter(name = pokemonC);
        var nameC = PokemonC.Name;
        var TotalC = PokemonC.Total;
        var HPC = PokemonC.HP;
        var AttackC = PokemonC.Attack;
        var DefenseC = PokemonC.Defense;
        var SpAtkC = PokemonC.SpAtk;
        var SpDefC = PokemonC.SpDef;
        var SpeedC = PokemonC.Speed;
        var PokemonStatsC = [nameC, TotalC ,HPC ,AttackC ,,DefenseC ,SpAtkC ,SpDefC ,SpeedC ];

        var trace = {
            type: "bar",
            name: name,
            x: PokemonStatsC,
            y: Range(auntomap)
        };
        var data = [trace];
        var layout = { 
            title: "Stat Compare",
            barmode: "group"
        };
        Plotly.newPlot("IndividualStats", data, layout);
    });
}
