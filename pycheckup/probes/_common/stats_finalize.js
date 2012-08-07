function (key, value) {
  value.avg = value.sum / value.count;
  value.variance = value.diff / value.count;
  value.stdev = Math.sqrt(value.variance);

  return value;
}
