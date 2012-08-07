function() {
  this.popularity.forEach(function(doc) {
    emit(doc.date, {
      sum: doc.data.open_issues,
      min: doc.data.open_issues,
      max: doc.data.open_issues,
      count: 1,
      diff: 0
    });
  });
}
