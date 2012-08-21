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

  getHistory: function(data, names) {
    var result = {};
    _.each(data, function(d) {
      _.each(names, function(name) {
        if (result[name] === undefined) {
          result[name] = [];
        }
        result[name].push(d.value[name]);
      });
    });

    return result;
  },

  sparkline_settings: {
    lineColor: '#3d8ba5',
    fillColor: '#ebf3f6',
    minSpotColor: '#5da53d',
    maxSpotColor: '#a53d3e',
    spotColor: '#3d8ba5',
    highlightLineColor: '#3d8ba5',
    highlightSpotColor: '#3d8ba5'
  }
});


var Overview = {

  Commits: BaseView.extend({
    el: '#overview-commits',

    events: {
      'click #commits-count': 'count',
      'click #commits-lines': 'linesChanged'
    },

    graphResult: function(raw) {
      var data = _.map(raw, function(d) {
        return {x: new Date(d._id), y: d.value.sum};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#overview-commits .graph-container');
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

    graphResult: function(raw) {
      var data = _.map(raw, function(d) {
        return {x: new Date(d._id), y: d.value.total};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#overview-pyflakes .graph-container');
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
        var history = this.getHistory(data, _.keys(latest));
        var compiled = _.template(this.$('#tmpl_pyflakes').html());
        var table = this.$('table tbody').html('');

        _.each(this.sortObject(latest), function(v) {
          if (DisplayNames.pyflakes[v.name] !== undefined) {
            table.append(compiled({
              name: DisplayNames.pyflakes[v.name],
              count: v.count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","),
              history: history[v.name]
            }));
          }
        });

        this.$('.sparkline').sparkline('html', this.sparkline_settings);
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

    graphResult: function(raw) {
      var data = _.map(raw, function(d) {
        return {x: new Date(d._id), y: d.value.total};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#overview-pep8 .graph-container');
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
        var history = this.getHistory(data, _.keys(latest));
        var compiled = _.template(this.$('#tmpl_pep8').html());
        var table = this.$('table tbody').html('');

        _.each(this.sortObject(latest), function(v) {
          if (DisplayNames.pep8[v.name] !== undefined) {
            table.append(compiled({
              name: DisplayNames.pep8[v.name],
              count: v.count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","),
              history: history[v.name]
            }));
          }
        });

        this.$('.sparkline').sparkline('html', this.sparkline_settings);
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

    graphResult: function(raw) {
      var data = _.map(raw, function(d) {
        return {x: new Date(d._id), y: d.value.total};
      });

      pyCheckupGraphs().timeSeriesGraph(data, '#overview-swearing .graph-container');
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
        var history = this.getHistory(data, _.keys(latest));
        var compiled = _.template(this.$('#tmpl_swearing').html());
        var table = this.$('table tbody').html('');

        _.each(this.sortObject(latest), function(v) {
          table.append(compiled({
            word: v.name,
            count: v.count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","),
            history: history[v.name]
          }));
        });

        this.$('.sparkline').sparkline('html', this.sparkline_settings);
      }, this));
    },

    render: function() {
      this.total();
    }
  })

}
