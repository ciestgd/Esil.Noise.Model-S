import yaml

class _Config:
    def __init__(self, config_path:str='configs.yml'):
        self.config_path = config_path
    
    def load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            configs = yaml.safe_load(f)
            
        return configs
    
    @property
    def data_sources(self):
        return self.load_config().get('DataSources', None)
    
    @property
    def features(self):
        return self.load_config().get('Features', None)
    
    @property
    def tags(self):
        return self.load_config().get('Tags', None)
    
    @property
    def train(self):
        return self.load_config().get('Train', None)
    
config = _Config()