    try:
      self.repo.remotes.origin.exists()
      if self.repo.remotes.origin.url != config.FILES_REPO_URL:
        raise TelegramError('Links repository path seems to be conflicting with another repo')
    except AttributeError:
      self.repo.create_remote('origin', config.FILES_REPO_URL)