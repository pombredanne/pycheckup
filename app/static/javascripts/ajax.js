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


  ajaxGet('distribution.watchers', '/api/distribution/watchers');
  ajaxGet('distribution.issues', '/api/distribution/open_issues');
  ajaxGet('distribution.forks', '/api/distribution/forks');
  ajaxGet('distribution.collaborators', '/api/distribution/num_collaborators');


  ajaxGet('correlation.line-count.issues', '/api/correlate/line_count/open_issues');
  ajaxGet('correlation.line-count.forks', '/api/correlate/line_count/forks');
  ajaxGet('correlation.line-count.watchers', '/api/correlate/line_count/watchers');
  ajaxGet('correlation.line-count.collaborators', '/api/correlate/line_count/num_collaborators');
  ajaxGet('correlation.line-count.swearing', '/api/correlate/line_count/swearing');
  ajaxGet('correlation.line-count.pep8', '/api/correlate/line_count/pep8');
  ajaxGet('correlation.line-count.pyflakes', '/api/correlate/line_count/pyflakes');

  ajaxGet('correlation.issues.forks', '/api/correlate/open_issues/forks');
  ajaxGet('correlation.issues.watchers', '/api/correlate/open_issues/watchers');
  ajaxGet('correlation.issues.collaborators', '/api/correlate/open_issues/num_collaborators');
  ajaxGet('correlation.issues.swearing', '/api/correlate/open_issues/swearing');
  ajaxGet('correlation.issues.pep8', '/api/correlate/open_issues/pep8');
  ajaxGet('correlation.issues.pyflakes', '/api/correlate/open_issues/pyflakes');

  ajaxGet('correlation.forks.watchers', '/api/correlate/forks/watchers');
  ajaxGet('correlation.forks.collaborators', '/api/correlate/forks/num_collaborators');
  ajaxGet('correlation.forks.swearing', '/api/correlate/forks/swearing');
  ajaxGet('correlation.forks.pep8', '/api/correlate/forks/pep8');
  ajaxGet('correlation.forks.pyflakes', '/api/correlate/forks/pyflakes');

  ajaxGet('correlation.watchers.collaborators', '/api/correlate/watchers/num_collaborators');
  ajaxGet('correlation.watchers.swearing', '/api/correlate/watchers/swearing');
  ajaxGet('correlation.watchers.pep8', '/api/correlate/watchers/pep8');
  ajaxGet('correlation.watchers.pyflakes', '/api/correlate/watchers/pyflakes');

  ajaxGet('correlation.collaborators.swearing', '/api/correlate/num_collaborators/swearing');
  ajaxGet('correlation.collaborators.pep8', '/api/correlate/num_collaborators/pep8');
  ajaxGet('correlation.collaborators.pyflakes', '/api/correlate/num_collaborators/pyflakes');

  ajaxGet('correlation.swearing.pep8', '/api/correlate/swearing/pep8');
  ajaxGet('correlation.swearing.pyflakes', '/api/correlate/swearing/pyflakes');

  ajaxGet('correlation.pep8.pyflakes', '/api/correlate/pep8/pyflakes');

});
