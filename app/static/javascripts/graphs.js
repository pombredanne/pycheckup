var pyCheckupGraphs = function() {

  function getDataDomain(data) {
    var xs = _.pluck(data, 'x');
    var ys = _.pluck(data, 'y');

    return {
      x: [_.min(xs), _.max(xs)],
      y: [0, _.max(ys)]
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


  function getLine(scale) {
    return d3.svg.line()
                  .x(function(d, i) {
                    return scale.x(d.x);
                  })
                  .y(function(d) {
                    return scale.y(d.y);
                  });
  }


  function drawFill(svg, data, line, domain) {
    var this_data = data.slice();

    this_data.push({x: domain.x[1], y: 0});
    this_data.push({x: domain.x[0], y: 0});

    svg.append('svg:path')
      .attr('d', line(this_data))
      .attr('class', 'featured-fill');
  }


  function drawCircles(svg, data, scale) {
    svg.selectAll('circle')
          .data(data)
          .enter()
          .append('svg:circle')
          .attr('cx', function(d) {
            return scale.x(d.x);
          })
          .attr('cy', function(d) {
            return scale.y(d.y);
          })
          .attr('r', function(d) {
            return 4;
          });
  }


  function drawLine(svg, data, line, scale) {
    svg.append('svg:path')
      .attr('d', line(data))
      .attr('class', 'featured-stroke');

    drawCircles(svg, data, scale);
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
    var line = getLine(scale);

    drawFill(svg, data, line, domain);
    drawAxis(svg, axis, h, padding, y_offset);
    drawLine(svg, data, line, scale);
  }


  return {
    timeSeriesGraph: timeSeriesGraph
  }
}
