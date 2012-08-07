function (key, values) {
  var result = {};

  values.forEach(function(d) {
    if (result[d.word] === undefined) {
      result[d.word] = 0;
    }

    result[d.word] += d.count;
  });

  return result;
}
