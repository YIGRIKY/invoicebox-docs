function setModifiedDate(url,date)
{
  if (document.getElementById('last-modified')) {
    fetch("https://api.github.com/repos/"+url)
      .then((response) => {
        return response.json();
      })
      .then((commits) => {
        console.log(commits);
        var modifiedText = "история изменений";
        if (typeof commits != "undefined" && Array.isArray(commits))
        {
           var modified = commits[0]['commit']['committer']['date'].slice(0,10);
           if(modified != date) {
              modifiedText = "обновлено: " + modified.split("-").reverse().join(".");
            }; //
        }; //
        document.getElementById('last-modified').innerHTML = "<a target='_blank' href='https://github.com/"+url+"' title='" + modifiedText + "'>" + modifiedText + "</a>";
      });
  }
};
