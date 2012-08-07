function() {
  this.swearing.forEach(function(doc) {
    for (i in doc.data) {
      emit(doc.date, {word: i, count: doc.data[i]});
    }
  });
}
