function() {
  this.line_count.forEach(function(doc) {
    for (i in doc.data) {
      emit(doc.date, {ext: i, count: doc.data[i]});
    }
  });
}
