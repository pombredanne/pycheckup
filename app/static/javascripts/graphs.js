var pyCheckupGraphs = function() {

  function getMin(collection, fn) {
    var e = _.min(collection, fn);
    return fn(e);
  }


  function getMax(collection, fn) {
    var e = _.max(collection, fn);
    return fn(e);
  }


  function getDataDomain(data) {
    var x_mins = [], x_maxs = [], y_mins = [], y_maxs = [];
    var xFn = function(e) { return new Date(e._id); }

    _.each(data, function(v, k) {
      var yFn = function(e) { return e.value[v.yAttr]; }

      x_mins.push(getMin(v.data, xFn));
      x_maxs.push(getMax(v.data, xFn));

      y_mins.push(getMin(v.data, yFn));
      y_maxs.push(getMax(v.data, yFn));
    });

    return {
      x: [_.min(x_mins), _.max(x_maxs)],
      y: [0, _.max(y_maxs)]
    }
  }

  function dateFormat(i) {
    var format = d3.time.format('%b. %d');
    return format(new Date(i))
  }


  function getScale(domain, w, h, padding, y_offset) {
    return {
      x: d3.scale.linear().domain(domain.x).range([y_offset, w - padding]),
      y: d3.scale.linear().domain(domain.y).range([h - padding, padding])
    }
  }


  function getAxis(scale) {
    return {
      x: d3.svg.axis().scale(scale.x).orient('bottom').tickFormat(dateFormat),
      y: d3.svg.axis().scale(scale.y).orient('left').ticks(5)
    }
  }


  function drawAxis(svg, axis, h, padding, y_offset) {
    svg.append('svg:g')
        .attr('class', 'axis')
        .attr("transform", "translate(0," + (h - padding) + ")")
        .call(axis.x);

    svg.append('svg:g')
        .attr('class', 'axis')
        .attr('transform', 'translate(' + y_offset + ', 0)')
        .call(axis.y);
  }


  function getLine(scale, yAttr) {
    return d3.svg.line()
                  .x(function(d, i) {
                    return scale.x(new Date(d._id));
                  })
                  .y(function(d) {
                    return scale.y(d.value[yAttr]);
                  });
  }


  function drawFills(svg, data, line, domain) {
    _.each(data, function(v, k) {
      var this_data = v.data.slice();

      var value = {}
      value[v.yAttr] = 0;

      this_data.push({_id: domain.x[1], value: value});
      this_data.push({_id: domain.x[0], value: value});

      svg.append('svg:path')
        .attr('d', line(this_data))
        .attr('class', k + '-fill');
    });
  }


  function drawCircles(svg, data, scale, yAttr) {
    svg.selectAll('circle')
          .data(data)
          .enter()
          .append('svg:circle')
          .attr('cx', function(d) {
            return scale.x(new Date(d._id));
          })
          .attr('cy', function(d) {
            return scale.y(d.value[yAttr]);
          })
          .attr('r', function(d) {
            return 4;
          });
  }


  function drawLines(svg, data, line, scale) {
    _.each(data, function(v, k) {
      svg.append('svg:path')
        .attr('d', line(v.data))
        .attr('class', k + '-stroke');

      drawCircles(svg, v.data, scale, v.yAttr);
    });
  }


  function timeSeriesGraph(data, container) {
    $(container).html('');
    var w = $(container).width();
    var h = $(container).height();
    var y_offset = 60;
    var padding = 30;

    var domain = getDataDomain(data);
    var scale = getScale(domain, w, h, padding, y_offset);
    var axis = getAxis(scale);
    var svg = d3.select(container).append('svg');
    var line = getLine(scale, data.featured.yAttr);

    drawFills(svg, data, line, domain);
    drawAxis(svg, axis, h, padding, y_offset);
    drawLines(svg, data, line, scale);
  }


  return {
    timeSeriesGraph: timeSeriesGraph
  }
}
