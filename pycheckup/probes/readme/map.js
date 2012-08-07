function () {
  if (this.readme) {
    emit('yes', 1);
  }
  else {
    emit('no', 1);
  }
}
