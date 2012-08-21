var Project = {

  LineCount: Backbone.View.extend({
    el: '#project-line-count',

    graphResult: function(data) {
      var result = {
        featured: {
          data: PyCheckupData.line_count,
          xAttr: 'date',
          yAttr: 'total'
        }
      };

      var graph = new pyCheckupGraphs();
      graph.timeSeriesGraph(result, '#project-line-count .graph-container');
    },

    render: function() {
      // console.log(PyCheckupData.line_count);
      this.graphResult();
    }
  })

}
