from GoogleStaticView import StaticView, CityViewLocations
import time
import os
BASIC_URL = "https://maps.googleapis.com/maps/api/staticmap"
params = {
	"center":"",
	"zoom":"16",
	"maptype":"satellite",
	"size":"1000x1000",
	"scale":"2",
	"key":"AIzaSyDofbBFjOiyEjbU5E69h15D3-wwdwSlvF4",
	# "key":"AIzaSyC6PEy5m1jeMEKptkS91Tff3NKdt786D20",
	# "key": "AIzaSyCena0WA3XVSOzO-HYuBnG50Y0oV3I-Aeg",
	# "key": "AIzaSyDyXqlLmgYdV-4bM3SUz5EwR_GBMyqK4y0",
}

# img = StaticView(BASIC_URL,params)
# img.download_image(output_name="tmp3_size1000")
locs = CityViewLocations([30.666944, 31.537080, 120.835369, 122.160622])
output_folder = "shanghai"
locs.write_locations(output_name=output_folder)

with open("%s.txt" % output_folder, "r") as f:
	exists_images = os.listdir(output_folder)
	exists_locations = map(lambda exists_image: exists_image.rstrip(".png").replace("_",",") , exists_images)
	i = 0
	while True:
		center = f.next().rstrip("\n")
		if center in exists_locations:
			pass
		else:
			params["center"] = center
			img = StaticView(BASIC_URL,params)
			img.download_image(output_folder="./shanghai/", output_name=center.replace(",","_"))
			print "we have got %d static view images."%(i+1)
			i += 1
			time.sleep(0.2)
