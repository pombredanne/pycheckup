$(function() {
  var views = [];
  views.push(new Overview.Commits());
  views.push(new Overview.Pyflakes());
  views.push(new Overview.Pep8());
  views.push(new Overview.Swearing());

  _.map(views, function(v) { v.render(); });
});
