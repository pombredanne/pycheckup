function() {
  this.popularity.forEach(function(doc) {
    emit(doc.date, {
      sum: doc.data.watchers,
      min: doc.data.watchers,
      max: doc.data.watchers,
      count: 1,
      diff: 0
    });
  });
}
