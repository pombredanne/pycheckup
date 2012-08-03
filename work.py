from pycheckup.git import GitRepo
import tasks


tasks.bootstrap_repo.delay('facebook', 'tornado')
