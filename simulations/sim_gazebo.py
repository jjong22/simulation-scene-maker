def start_sdf() ->str:
    settings = f"""<sdf version='1.10'>
"""
    return settings

def end_sdf() ->str:
    settings = f"""</sdf>
"""
    return settings

def start_world(name:str) ->str:
    settings = f"""  <world name='{name}'>
"""
    return settings

def end_world() ->str:
    settings = f"""  </world>
"""
    return settings

def physics_setting()-> str:
    setting = f"""    <physics name='1ms' type='ignored'>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
    </physics>
"""
    return setting

def plugin_setting()-> str:
    setting = f"""    <plugin name='gz::sim::systems::Physics' filename='gz-sim-physics-system'/>
    <plugin name='gz::sim::systems::UserCommands' filename='gz-sim-user-commands-system'/>
    <plugin name='gz::sim::systems::SceneBroadcaster' filename='gz-sim-scene-broadcaster-system'/>
    <plugin name='gz::sim::systems::Contact' filename='gz-sim-contact-system'/>
"""
    return setting
def env_setting()-> str:
    setting = f"""    <gravity>0 0 -9.8000000000000007</gravity>
    <magnetic_field>5.5644999999999998e-06 2.2875799999999999e-05 -4.2388400000000002e-05</magnetic_field>
    <atmosphere type='adiabatic'/>
"""
    return setting

def scene_setting()-> str:
    setting = f"""    <scene>
      <ambient>0.400000006 0.400000006 0.400000006 1</ambient>
      <background>0.699999988 0.699999988 0.699999988 1</background>
      <shadows>true</shadows>
    </scene>
"""
    return setting

def default_ground_plane()-> str:
    setting = f"""    <model name='ground_plane'>
      <static>true</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode/>
            </friction>
            <bounce/>
            <contact/>
          </surface>
        </collision>
        <visual name='visual'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <ambient>0.800000012 0.800000012 0.800000012 1</ambient>
            <diffuse>0.800000012 0.800000012 0.800000012 1</diffuse>
            <specular>0.800000012 0.800000012 0.800000012 1</specular>
          </material>
        </visual>
        <pose>0 0 0 0 0 0</pose>
        <inertial>
          <pose>0 0 0 0 0 0</pose>
          <mass>1</mass>
          <inertia>
            <ixx>1</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>1</iyy>
            <iyz>0</iyz>
            <izz>1</izz>
          </inertia>
        </inertial>
        <enable_wind>false</enable_wind>
      </link>
      <pose>0 0 0 0 0 0</pose>
      <self_collide>false</self_collide>
    </model>
"""
    # TODO: what the hell is this?
    return setting

def sphere(name: str, position = [0,0,1], rotation = [0,0,0], radius=0.5)-> str:
    setting = f"""<model name='{name}'>
      <pose>{position[0]} {position[1]} {position[2]} {rotation[0]} {rotation[1]} {rotation[2]}</pose>
      <link name='sphere_link'>
        <inertial>
          <inertia>
            <ixx>0.10000000000000001</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.10000000000000001</iyy>
            <iyz>0</iyz>
            <izz>0.10000000000000001</izz>
          </inertia>
          <mass>1</mass>
          <pose>0 0 0 0 0 0</pose>
        </inertial>
        <collision name='sphere_collision'>
          <geometry>
            <sphere>
              <radius>{radius}</radius>
            </sphere>
          </geometry>
          <surface>
            <friction>
              <ode/>
            </friction>
            <bounce/>
            <contact/>
          </surface>
        </collision>
        <visual name='sphere_visual'>
          <geometry>
            <sphere>
              <radius>{radius}</radius>
            </sphere>
          </geometry>
          <material>
            <ambient>0.300000012 0.300000012 0.300000012 1</ambient>
            <diffuse>0.699999988 0.699999988 0.699999988 1</diffuse>
            <specular>1 1 1 1</specular>
          </material>
        </visual>
        <pose>0 0 0 0 0 0</pose>
        <enable_wind>false</enable_wind>
      </link>
      <static>false</static>
      <self_collide>false</self_collide>
    </model>
"""
    # TODO: can be added more parameters about rigid body?
    return setting

def light_setting()->str:
    setting = f"""    <light name='sun' type='directional'>
      <pose>0 0 10 0 0 0</pose>
      <cast_shadows>true</cast_shadows>
      <intensity>1</intensity>
      <direction>-0.5 0.10000000000000001 -0.90000000000000002</direction>
      <diffuse>0.800000012 0.800000012 0.800000012 1</diffuse>
      <specular>0.200000003 0.200000003 0.200000003 1</specular>
      <attenuation>
        <range>1000</range>
        <linear>0.0099999997764825821</linear>
        <constant>0.89999997615814209</constant>
        <quadratic>0.0010000000474974513</quadratic>
      </attenuation>
      <spot>
        <inner_angle>0</inner_angle>
        <outer_angle>0</outer_angle>
        <falloff>0</falloff>
      </spot>
    </light>
"""
    return setting

if __name__ == "__main__":
    with open("result.sdf", "w", encoding='utf-8') as f:
        f.write(start_sdf())
        f.write(start_world("testest"))
        f.write(physics_setting())
        f.write(plugin_setting())
        f.write(env_setting())
        f.write(scene_setting())
        f.write(default_ground_plane())
        f.write(sphere("sphere"))
        f.write(sphere("sphere2", position=[0,0,10]))
        f.write(sphere("sphere3", position=[0,0,15]))
        f.write(light_setting())
        f.write(end_world())
        f.write(end_sdf())