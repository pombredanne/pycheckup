var BaseView = Backbone.View.extend({
  setPill: function(name) {
    this.$('.pills a').removeClass('active');
    this.$('#' + name).addClass('active');
  },

  sortObject: function(data) {
      result = [];
      _.each(data, function(v, k) {
        result.push({name: k, count: v});
      });

      result = _.sortBy(result, function(e) { return e.count; }).reverse();
      return result;
    },
});


var Overview = {

  Commits: BaseView.extend({
    el: '#overview-commits',

    events: {
      'click #commits-count': 'count',
      'click #commits-lines': 'linesChanged'
    },

    graphResult: function(data) {
      var result = {featured: {data: data, yAttr: 'sum'}};
      var graph = new pyCheckupGraphs();
      graph.timeSeriesGraph(result, '#overview-commits .graph-container');
    },

    count: function() {
      this.setPill('commits-count');
      amplify.request('summary.commits.count', this.graphResult);
    },

    linesChanged: function() {
      this.setPill('commits-lines');
      amplify.request('summary.commits.lines', this.graphResult);
    },

    render: function() {
      this.count();
    }
  }),


  Pyflakes: BaseView.extend({
    el: '#overview-pyflakes',

    events: {
      'click #pyflakes-total': 'total',
      'click #pyflakes-violations': 'violations'
    },

    graphResult: function(data) {
      var result = {featured: {data: data, yAttr: 'total'}};
      var graph = new pyCheckupGraphs();
      graph.timeSeriesGraph(result, '#overview-pyflakes .graph-container');
    },

    total: function() {
      this.setPill('pyflakes-total');
      this.$('.graph-container').show();
      this.$('table').hide();
      amplify.request('summary.pyflakes', this.graphResult);
    },

    violations: function() {
      this.setPill('pyflakes-violations');
      this.$('.graph-container').hide();
      this.$('table').show();

      amplify.request('summary.pyflakes', _.bind(function(data) {
        var latest = data[data.length - 1].value;
        var compiled = _.template(this.$('#tmpl_pyflakes').html());
        var table = this.$('table tbody').html('');

        _.each(this.sortObject(latest), function(v) {
          table.append(compiled({
            name: DisplayNames.pyflakes[v.name], count: v.count
          }));
        });
      }, this));
    },

    render: function() {
      this.total();
    }
  }),


  Pep8: BaseView.extend({
    el: '#overview-pep8',

    events: {
      'click #pep8-total': 'total',
      'click #pep8-violations': 'violations'
    },

    graphResult: function(data) {
      var result = {featured: {data: data, yAttr: 'total'}};
      var graph = new pyCheckupGraphs();
      graph.timeSeriesGraph(result, '#overview-pep8 .graph-container');
    },

    total: function() {
      this.setPill('pep8-total');
      this.$('.graph-container').show();
      this.$('table').hide();
      amplify.request('summary.pep8', this.graphResult);
    },

    violations: function() {
      this.setPill('pep8-violations');
      this.$('.graph-container').hide();
      this.$('table').show();

      amplify.request('summary.pep8', _.bind(function(data) {
        var latest = data[data.length - 1].value;
        var compiled = _.template(this.$('#tmpl_pep8').html());
        var table = this.$('table tbody').html('');

        _.each(this.sortObject(latest), function(v) {
          table.append(compiled({
            name: DisplayNames.pep8[v.name], count: v.count
          }));
        });
      }, this));
    },

    render: function() {
      this.total();
    }
  }),


  Swearing: BaseView.extend({
    el: '#overview-swearing',

    events: {
      'click #swearing-total': 'total',
      'click #swearing-words': 'words'
    },

    graphResult: function(data) {
      var result = {featured: {data: data, yAttr: 'total'}};
      var graph = new pyCheckupGraphs();
      graph.timeSeriesGraph(result, '#overview-swearing .graph-container');
    },

    total: function() {
      this.setPill('swearing-total');
      this.$('.graph-container').show();
      this.$('table').hide();
      amplify.request('summary.swearing', this.graphResult);
    },

    words: function() {
      this.setPill('swearing-words');
      this.$('.graph-container').hide();
      this.$('table').show();

      amplify.request('summary.swearing', _.bind(function(data) {
        var latest = data[data.length - 1].value;
        var compiled = _.template(this.$('#tmpl_swearing').html());
        var table = this.$('table tbody').html('');

        _.each(this.sortObject(latest), function(v) {
          table.append(compiled({
            word: v.name, count: v.count
          }));
        });
      }, this));
    },

    render: function() {
      this.total();
    }
  })

}
