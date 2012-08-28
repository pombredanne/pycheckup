$(function($) {
  $('#projects-search').autocomplete('/api/autocomplete', {
    minChars: 2,
    remoteDataType: 'json',
    onItemSelect: function(li) {
      window.location = '/projects/' + li.value;
    }
  });
});
