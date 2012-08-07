function() {
  this.pyflakes.forEach(function(doc) {
    for (i in doc.data) {
      emit(doc.date, {violation: i, count: doc.data[i]});
    }
  });
}
