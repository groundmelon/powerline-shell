
def add_ros_master_segment(powerline):
    import os
    uri = os.getenv('ROS_MASTER_URI')
    if uri.find('tegra-ubuntu')!=-1:
        msg = 'RmtROS'
        fgcolor = Color.SSH_FG
        bgcolor = Color.SSH_BG
        powerline.append(msg, fgcolor, bgcolor)
    else:
        return

