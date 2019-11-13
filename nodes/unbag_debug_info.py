  ### for viewing debugging bag files
import rosbag

bag = rosbag.Bag('ledpanels_debug.bag')
with open('debug_data.txt','w') as f:
    for msg in bag.read_messages():  
         print(msg.message)
         f.write('{}'.format(msg.message))
bag.close()
