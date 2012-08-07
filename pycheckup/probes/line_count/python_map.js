function() {
  this.line_count.forEach(function(doc) {
    if (doc.data.py !== undefined) {
      emit(doc.date, {
        sum: doc.data.py,
        min: doc.data.py,
        max: doc.data.py,
        count: 1,
        diff: 0
      });
    }
  });
}
