$(function() {

  ajaxGet = function(name, url) {
    amplify.request.define(name, 'ajax', {
      url: url,
      dataType: 'json',
      type: 'GET'
    });
  }

  ajaxGet('summary.commits.count', '/api/commits/count');
  ajaxGet('summary.commits.lines', '/api/commits/lines');
  ajaxGet('summary.license', '/api/license');
  ajaxGet('summary.line-count', '/api/line-count');
  ajaxGet('summary.line-count.python', '/api/line-count/python');
  ajaxGet('summary.pep8', '/api/pep8');
  ajaxGet('summary.popularity.collaborators', '/api/popularity/collaborators');
  ajaxGet('summary.popularity.forks', '/api/popularity/forks');
  ajaxGet('summary.popularity.issues', '/api/popularity/issues');
  ajaxGet('summary.popularity.watchers', '/api/popularity/watchers');
  ajaxGet('summary.pyflakes', '/api/pyflakes');
  ajaxGet('summary.readme', '/api/readme');
  ajaxGet('summary.setup-py', '/api/setup.py');
  ajaxGet('summary.swearing', '/api/swearing');
  ajaxGet('summary.tabs-spaces', '/api/tabs-or-spaces');

});
