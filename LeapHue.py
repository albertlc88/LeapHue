#Uses Phue https://github.com/studioimaginaire/phue
#Uses Leap Motion to control Philips Hue: Hold up 1-5 fingers, and the lights will change colors


#Only uses 1 light


import Leap, sys
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


from phue import Bridge



b = Bridge('192.168.100.102')

b.connect()


class HueListener(Leap.Listener):

	def on_frame(self, controller):
			# Get the most recent frame and report some basic information
			frame = controller.frame()

			numFingers = len(frame.fingers)
			

			if (numFingers == 0):
				result = b.get_light(1, 'on')
				if result:
					b.set_light(1, 'on', False)

				
			
			elif (numFingers == 1):
				result = b.get_light(1, 'on')
				if not result:
					b.set_light(1, 'on', True)
				b.set_light(1, 'xy', [.2, .02])


			elif (numFingers == 2):
				result = b.get_light(1, 'on')
				if not result:
					b.set_light(1, 'on', True)
				b.set_light(1, 'xy', [.1, .7])



			elif (numFingers == 3):
				result = b.get_light(1, 'on')
				if not result:
					b.set_light(1, 'on', True)
				b.set_light(1, 'xy', [.5, .45])


			elif (numFingers == 4):
				result = b.get_light(1, 'on')
				if not result:
					b.set_light(1, 'on', True)
				b.set_light(1, 'xy', [.55, .4])

			elif (numFingers == 5):
				result = b.get_light(1, 'on')
				if not result:
					b.set_light(1, 'on', True)
				b.set_light(1, 'xy', [.6, .3])
				result = b.get_light(3, 'on')


controller = Leap.Controller()
listener = HueListener()

# Have the sample listener receive events from the controller
controller.add_listener(listener)

# Keep this process running until Enter is pressed
print "Press Enter to quit..."
sys.stdin.readline()

# Remove the sample listener when done
controller.remove_listener(listener)