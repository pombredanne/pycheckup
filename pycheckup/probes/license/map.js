function () {
  if (this.license == null) {
    emit('none', 1);
  }
  else {
    emit(this.license, 1);
  }
}
