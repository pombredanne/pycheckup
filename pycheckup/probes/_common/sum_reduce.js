function (key, values) {
  var count = 0;

  values.forEach(function(num) {
    count += num;
  });

  return count;
}
