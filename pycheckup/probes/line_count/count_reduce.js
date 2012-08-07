function (key, values) {
  var result = {};

  values.forEach(function(d) {
    if (result[d.ext] === undefined) {
      result[d.ext] = 0;
    }

    result[d.ext] += d.count;
  });

  return result;
}
