function() {
  var num_swears = this.swearing[this.swearing.length - 1].data.total;
  var num_lines = this.line_count[this.line_count.length - 1].data.total;

  if (num_swears == 0 || num_lines == 0) {
    emit(this._id, 0);
  }
  else {
    emit(this._id, num_swears / num_lines);
  }
}
