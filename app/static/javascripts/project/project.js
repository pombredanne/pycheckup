$(function() {
  var views = [];
  views.push(new Project.LineCount());

  _.map(views, function(v) { v.render(); });
});
