from pathlib import Path

RESOURCES_ABSOLUTE_PATH = (Path(__file__).parent.parent.__str__() + '/resources/video/geeration/').replace('\\', '/')

# TODO: This resources should be urls to make a download when generating
# because the project will become very large, or we should generate a 
# a method that downloads the resources package and stores it in a local
# folder
GOOGLE_SEARCH_IMAGE_ABSOLUTE_PATH = RESOURCES_ABSOLUTE_PATH + 'google_search.jpg'