function() {
  this.commits.forEach(function(doc) {
    emit(doc.date, {
      sum: doc.data.count,
      min: doc.data.count,
      max: doc.data.count,
      count: 1,
      diff: 0
    });
  });
}
