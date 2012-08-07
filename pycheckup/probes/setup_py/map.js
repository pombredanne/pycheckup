function () {
  if (this.setup_py) {
    emit('yes', 1);
  }
  else {
    emit('no', 1);
  }
}
