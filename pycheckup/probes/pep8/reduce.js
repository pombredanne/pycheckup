function (key, values) {
  var result = {};

  values.forEach(function(d) {
    if (result[d.violation] === undefined) {
      result[d.violation] = 0;
    }

    result[d.violation] += d.count;
  });

  return result;
}
