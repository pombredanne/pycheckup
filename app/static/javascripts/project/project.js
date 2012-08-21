$(function() {
  var views = [];
  views.push(new Project.LineCount());
  views.push(new Project.Commits());
  views.push(new Project.LinesChanged());
  views.push(new Project.Pyflakes());
  views.push(new Project.Pep8());
  views.push(new Project.Swearing());

  _.map(views, function(v) { v.render(); });
});
