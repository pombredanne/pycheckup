function (key, values) {
  // Algorithm from https://gist.github.com/1886960
  var results = values[0];

  // i starts at 1 *not* 0 because results starts as values[0]
  for (var i = 1; i < values.length; i++) {
    var d = values[i];

    // results.mean - d.mean
    var delta = (results.sum / results.count) - (d.sum / d.count);
    var weight = (results.count * d.count) / (results.count + d.count);

    results.diff += d.diff + (delta * delta * weight);
    results.sum += d.sum;
    results.count += d.count;
    results.min = Math.min(results.min, d.min);
    results.max = Math.max(results.max, d.max);
  };

  return results;
}
