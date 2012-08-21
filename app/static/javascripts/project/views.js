var Project = {

  LineCount: Backbone.View.extend({
    el: '#project-line-count',

    render: function() {
      var data = _.map(PyCheckupData.line_count, function(d) {
        return {x: new Date(d.date), y: d.data.py};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#project-line-count .graph-container');
    }
  }),

  Commits: Backbone.View.extend({
    el: '#project-commits',

    render: function() {
      var data = _.map(PyCheckupData.commits, function(d) {
        return {x: new Date(d.date), y: d.data.count};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#project-commits .graph-container');
    }
  }),

  LinesChanged: Backbone.View.extend({
    el: '#project-lines-changed',

    render: function() {
      var data = _.map(PyCheckupData.commits, function(d) {
        return {x: new Date(d.date), y: d.data.lines_changed};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#project-lines-changed .graph-container');
    }
  }),

  Pyflakes: Backbone.View.extend({
    el: '#project-pyflakes',

    render: function() {
      var data = _.map(PyCheckupData.pyflakes, function(d) {
        return {x: new Date(d.date), y: d.data.total};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#project-pyflakes .graph-container');
    }
  }),

  Pep8: Backbone.View.extend({
    el: '#project-pep8',

    render: function() {
      var data = _.map(PyCheckupData.pep8, function(d) {
        return {x: new Date(d.date), y: d.data.total};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#project-pep8 .graph-container');
    }
  }),

  Swearing: Backbone.View.extend({
    el: '#project-swearing',

    render: function() {
      var data = _.map(PyCheckupData.swearing, function(d) {
        return {x: new Date(d.date), y: d.data.total};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#project-swearing .graph-container');
    }
  })

}
