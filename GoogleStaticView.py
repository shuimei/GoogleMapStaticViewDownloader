import requests
class StaticView(object):
	"""docstring for StaticView"""
	def __init__(self, url, params):
		super(StaticView, self).__init__()
		self.src_url = url
		self.params = params 
		self.request = self.make_request()
	def make_request(self):
		session = requests.Session()
		request =  session.get(self.src_url, params=self.params)
		return session.get(self.src_url, params=self.params)
	def download_image(self, output_folder="", output_name="static_view",output_format="png"):
		with open("%s%s.%s"%(output_folder, output_name, output_format), "wb+") as img:
			img.write(self.request.content)

class CityViewLocations(object):
	"""docstring for Locations"""
	def __init__(self, centers):
		"""centers are arranged by [south, north, west, east]"""
		super(CityViewLocations, self).__init__()
		self.centers = centers
		self.south, self.north, self.west, self.east = centers
		self.locations = self.make_locations()
	def make_locations(self, rows=100, columns=100):
		lat_step = (float(self.north) - float(self.south)) / rows
		lng_step = (float(self.east) - float(self.west)) / columns
		lats = [self.south + i*lat_step for i in range(rows)]
		lngs = [self.west + i*lng_step for i in range(columns)]
		locations = [(lat, lng) for lat in lats for lng in lngs]
		return locations
	def write_locations(self, output_folder="./", output_name="locations"):
		with open("%s%s.txt"%(output_folder, output_name), "w+") as location:
			for loc in self.make_locations():
				location.write("%f,%f\n"%(loc[0], loc[1]))
		return None




		

