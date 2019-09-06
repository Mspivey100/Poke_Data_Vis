function handleSubmitStatCompare() {
    d3.event.preventDefault();

    var pokemonA = d3.select("#pokemonInputA").node().value;
    console.log(pokemonA);
    d3.select("#pokemonInputA").node().value = "";

    var pokemonB = d3.select("#pokemonInputB").node().value;
    console.log(pokemonB);
    d3.select("#pokemonInputB").node().value = "";

    buildStatComparePlot(pokemonA,pokemonB);
}

function buildStatComparePlot(pokemonA,pokemonB) {
    var url = "/pokemon";
    d3.json(url).then(function(datalist) {
        console.log(datalist);
        var PokemonA = datalist.filter(name = pokemonA);
        var nameA = PokemonA.Name;
        var TotalA = PokemonA.Total;
        var HPA = PokemonA.HP;
        var AttackA = PokemonA.Attack;
        var DefenseA = PokemonA.Defense;
        var SpAtkA = PokemonA.SpAtk;
        var SpDefA = PokemonA.SpDef;
        var SpeedA = PokemonA.Speed;
        var PokemonStatsA = [nameA, TotalA,HPA,AttackA,,DefenseA,SpAtkA,SpDefA,SpeedA];

        var trace1 = {
            type: "bar",
            name: name,
            x: automap,
            y: PokemonStatsA
        };
        var PokemonB = datalist.filter(name = PokemonB);
        var nameB = PokemonB.Name;
        var TotalB = PokemonB.Total;
        var HPB = PokemonB.HP;
        var AttackB = PokemonB.Attack;
        var DefenseB = PokemonB.Defense;
        var SpAtkB= PokemonB.SpAtk;
        var SpDefB = PokemonB.SpDef;
        var SpeedB = PokemonB.Speed;
        var PokemonStatsB = [nameB, TotalB,HPB,AttackB,,DefenseB,SpAtkB,SpDefB,SpeedB];

        var trace2 = {
            type: "bar",
            name: name,
            x:automap,
            y: PokemonStatsB
        };
        var data = [trace1, trace2];
        var layout = { 
            title: "Stat Compare",
            barmode: "group"
        };
        Plotly.newPlot("statComparePlot", data, layout);
    });
}
