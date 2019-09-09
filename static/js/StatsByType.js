function handleSubmitTypes() {
    d3.event.preventDefault();
    buildStatByType();
}
function buildStatByType() {
    var url = "/graphcount";
    d3.json(url).then(function(response) {
        console.log(response);
        
        var traceA = {
            x: Object.keys(response),
            y: Object.values(response),
            type: "bar"
        }
        var layout = { 
            title:"Pokemon Count",
            barmode: "group",
            height: 600
        };
        Plotly.newPlot("StatsByType", traceA, layout);
    });   
}

d3.select("#TypeCount").on("click", handleSubmitTypes);
