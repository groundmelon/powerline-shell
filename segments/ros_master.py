
def add_ros_master_segment(powerline):
    import os
    uri = os.getenv('ROS_MASTER_URI')
    if uri is not None and uri.find('localhost')==-1:
        rst = re.match('http://(.*):11311', uri)
        if rst is None:
            msg = "ParseRosFail"
        else:
            msg = rst.groups()[0]
        fgcolor = Color.SSH_FG
        bgcolor = 129
        powerline.append(msg, fgcolor, bgcolor)
    else:
        return
