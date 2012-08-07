function() {
  this.popularity.forEach(function(doc) {
    emit(doc.date, {
      sum: doc.data.num_collaborators,
      min: doc.data.num_collaborators,
      max: doc.data.num_collaborators,
      count: 1,
      diff: 0
    });
  });
}
