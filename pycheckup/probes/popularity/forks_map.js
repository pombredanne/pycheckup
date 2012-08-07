function() {
  this.popularity.forEach(function(doc) {
    emit(doc.date, {
      sum: doc.data.forks,
      min: doc.data.forks,
      max: doc.data.forks,
      count: 1,
      diff: 0
    });
  });
}
