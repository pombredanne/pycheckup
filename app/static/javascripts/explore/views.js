var Explore = {

  Main: Backbone.View.extend({
    el: '#explore',

    events: {
      'change #pick-analysis': 'changeScreen'
    },

    changeScreen: function() {
      var value = $('#pick-analysis').val();
      if (value.substring(0, 4) == 'dist') {
        this.distribution(value.substring(5));
      }
      else {
        var pieces = value.split(':');
        this.correlation(pieces[0], pieces[1]);
      }
    },

    barGraph: function(title, data) {
      var bar_html = '';
      var axis_html = '';

      _.each(data.data, function(d) {
        var height_percent = (d[2] / data.max) * 100;
        bar_html += '<td><div class="label">' + d[2] + '</div>' +
                    '<div class="bar" style="height: ' +
                    height_percent + '%">&nbsp;</div></td>';

        axis_html += '<td>' + d[0] + '-' + d[1] + '</td>';
      });

      $('#explore-content').html(
        '<h3>' + title + '</h3>' +
        '<table class="bar-graph">' +
        '<tr>' + bar_html + '</tr>' +
        '<tr class="bar-axis">' + axis_html + '</tr>' +
        '</table>'
      );
    },

    setupScatterplot: function(x, y) {
      $('#explore-content').html(
        '<h3>' + x + ' vs ' + y + '</h3>' +
        '<div id="r-value"></div>' +
        '<div id="scatter-y-axis" class="scatter-axis">' + y + '</div>' +
        '<div id="scatterplot"></div>' +
        '<div id="scatter-x-axis" class="scatter-axis">' + x + '</div>'
      );
    },

    distribution: function(name) {
      titles = {
        watchers: '# Watchers',
        issues: 'Open Issues',
        forks: '# Forks',
        collaborators: '# Collaborators'
      };

      amplify.request('distribution.' + name, _.bind(function(data) {
        this.barGraph('Distribution of ' + titles[name], data);
      }, this));
    },

    transformCorrelationData: function(data) {
      // Puts each datapoint into an object for graphing
      var result = [];
      _.each(_.zip(data.x, data.y), function(d) {
        result.push({x: d[0], y: d[1]});
      });

      return result;
    },

    correlation: function(x, y) {
      titles = {
        'line-count': 'Line count',
        watchers: 'Watchers',
        issues: 'Open Issues',
        forks: 'Forks',
        collaborators: '# Collaborators',
        swearing: '# Swear words',
        pep8: 'PEP8 Violations',
        pyflakes: 'Pyflakes Violations'
      }

      this.setupScatterplot(titles[x], titles[y]);

      amplify.request('correlation.' + x + '.' + y, _.bind(function(data) {
        var dataset = this.transformCorrelationData(data);
        this.displayRValue(data.r);
        pyCheckupGraphs().scatterplot(dataset, '#scatterplot')
      }, this));
    },

    displayRValue: function(r) {
      var multiple = Math.pow(10, 3);
      var rounded = Math.round(r * multiple) / multiple;
      $('#r-value').html('r = ' + rounded);
    },

    render: function() {
      this.distribution('watchers');
    }
  })
}
