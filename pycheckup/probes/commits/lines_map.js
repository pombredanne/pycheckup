function() {
  this.commits.forEach(function(doc) {
    emit(doc.date, {
      sum: doc.data.lines_changed,
      min: doc.data.lines_changed,
      max: doc.data.lines_changed,
      count: 1,
      diff: 0
    });
  });
}
