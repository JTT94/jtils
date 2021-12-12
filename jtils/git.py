from git import Repo

def git_push():

  COMMIT_MESSAGE = 'MODEL RUN'
  
  
  repo = Repo(search_parent_directories=True)
  repo.git.add(update=True)
  repo.index.commit(COMMIT_MESSAGE)
  origin = repo.remote(name='origin')
  origin.push()
  return repo.head.object.hexsha