from random import randint

dict_yaml_class_id_reference = {'AimConstraint': 895512359, 'AnchoredJoint2D': 229, 'AndroidAssetPackImporter': 1736697216, 'Animation': 111, 'AnimationClip': 74, 'Animator': 95, 'AnimatorController': 91, 'AnimatorOverrideController': 221, 'AnimatorState': 1102, 'AnimatorStateMachine': 1107, 'AnimatorStateTransition': 1101, 'AnimatorTransition': 1109, 'AnimatorTransitionBase': 1111, 'AnnotationManager': 1049, 'AreaEffector2D': 249, 'ArticulationBody': 171741748, 'AssemblyDefinitionAsset': 1152215463, 'AssemblyDefinitionImporter': 1766753193, 'AssemblyDefinitionReferenceAsset': 662584278, 'AssemblyDefinitionReferenceImporter': 294290339, 'AssetBundle': 142, 'AssetBundleManifest': 290, 'AssetImporter': 1003, 'AssetImportInProgressProxy': 369655926, 'AssetMetaData': 1028, 'AudioBehaviour': 180, 'AudioBuildInfo': 641289076, 'AudioChorusFilter': 166, 'AudioClip': 83, 'AudioDistortionFilter': 170, 'AudioEchoFilter': 168, 'AudioFilter': 181, 'AudioHighPassFilter': 165, 'AudioImporter': 1020, 'AudioListener': 81, 'AudioLowPassFilter': 169, 'AudioManager': 11, 'AudioMixer': 240, 'AudioMixerController': 241, 'AudioMixerEffectController': 244, 'AudioMixerGroup': 273, 'AudioMixerGroupController': 243, 'AudioMixerLiveUpdateBool': 100009, 'AudioMixerLiveUpdateFloat': 100008, 'AudioMixerSnapshot': 272, 'AudioMixerSnapshotController': 245, 'AudioReverbFilter': 164, 'AudioReverbZone': 167, 'AudioSource': 82, 'Avatar': 90, 'AvatarMask': 319, 'BaseAnimationTrack': 110, 'BaseVideoTexture': 237, 'Behaviour': 8, 'BillboardAsset': 226, 'BillboardRenderer': 227, 'BlendTree': 206, 'bool': 100001, 'BoxCollider': 65, 'BoxCollider2D': 61, 'BrokenPrefabAsset': 1731078267, 'BuildReport': 1125, 'BuildSettings': 141, 'BuiltAssetBundleInfoSet': 668709126, 'BuoyancyEffector2D': 253, 'C4DImporter': 1541671625, 'CachedSpriteAtlas': 214, 'CachedSpriteAtlasRuntimeData': 644342135, 'Camera': 20, 'Canvas': 223, 'CanvasGroup': 225, 'CanvasRenderer': 222, 'CapsuleCollider': 136, 'CapsuleCollider2D': 70, 'CharacterController': 143, 'CharacterJoint': 144, 'CircleCollider2D': 58, 'Cloth': 183, 'ClusterInputManager': 236, 'Collider': 56, 'Collider2D': 53, 'Collision': 100004, 'Collision2D': 100007, 'Component': 2, 'CompositeCollider2D': 66, 'ComputeShader': 72, 'ComputeShaderImporter': 1008, 'ConfigurableJoint': 153, 'ConstantForce': 75, 'ConstantForce2D': 247, 'Cubemap': 89, 'CubemapArray': 188, 'CustomCollider2D': 893571522, 'CustomRenderTexture': 86, 'DefaultAsset': 1029, 'DefaultImporter': 1030, 'DelayedCallManager': 98, 'DistanceJoint2D': 232, 'EdgeCollider2D': 68, 'EditorBuildSettings': 1045, 'EditorExtension': 18, 'EditorExtensionImpl': 1002, 'EditorProjectAccess': 426301858, 'EditorSettings': 159, 'EditorUserBuildSettings': 1051, 'EditorUserSettings': 162, 'Effector2D': 248, 'FBXImporter': 1041, 'FixedJoint': 138, 'FixedJoint2D': 255, 'Flare': 121, 'FlareLayer': 124, 'float': 100002, 'Font': 128, 'FrictionJoint2D': 256, 'GameManager': 9, 'GameObject': 1, 'GameObjectRecorder': 1268269756, 'GlobalGameManager': 6, 'GraphicsSettings': 30, 'Grid': 156049354, 'GridLayout': 1742807556, 'Halo': 122, 'HierarchyState': 1026, 'HingeJoint': 59, 'HingeJoint2D': 233, 'HumanTemplate': 1105, 'IConstraint': 285090594, 'IHVImageFormatImporter': 1055, 'ImportLog': 41386430, 'InputManager': 13, 'InspectorExpandedState': 1048, 'int': 100000, 'Joint': 57, 'Joint2D': 230, 'LensFlare': 123, 'LevelGameManager': 3, 'LibraryAssetImporter': 1038, 'Light': 108, 'LightingDataAsset': 1120, 'LightingDataAssetParent': 1325145578, 'LightingSettings': 850595691, 'LightmapParameters': 1113, 'LightmapSettings': 157, 'LightProbeGroup': 220, 'LightProbeProxyVolume': 259, 'LightProbes': 258, 'LineRenderer': 120, 'LocalizationAsset': 2083778819, 'LocalizationImporter': 1027052791, 'LODGroup': 205, 'LookAtConstraint': 1183024399, 'LowerResBlitTexture': 1480428607, 'Material': 21, 'MemorySettings': 387306366, 'Mesh': 43, 'Mesh3DSImporter': 1005, 'MeshCollider': 64, 'MeshFilter': 33, 'MeshRenderer': 23, 'ModelImporter': 1040, 'MonoBehaviour': 114, 'MonoImporter': 1035, 'MonoManager': 116, 'MonoObject': 100003, 'MonoScript': 115, 'Motion': 207, 'MovieTexture': 152, 'MultiArtifactTestImporter': 1223240404, 'NamedObject': 130, 'NativeFormatImporter': 1034, 'NavMeshAgent': 195, 'NavMeshData': 238, 'NavMeshObstacle': 208, 'NavMeshProjectSettings': 126, 'NavMeshSettings': 196, 'NewAnimationTrack': 118, 'Object': 0, 'OcclusionArea': 192, 'OcclusionCullingData': 363, 'OcclusionCullingSettings': 29, 'OcclusionPortal': 41, 'OffMeshLink': 191, 'PackageManifest': 1896753125, 'PackageManifestImporter': 1896753126, 'PackedAssets': 1126, 'ParentConstraint': 1773428102, 'ParticleSystem': 198, 'ParticleSystemForceField': 330, 'ParticleSystemRenderer': 199, 'PhysicMaterial': 134, 'Physics2DSettings': 19, 'PhysicsManager': 55, 'PhysicsMaterial2D': 62, 'PhysicsUpdateBehaviour2D': 246, 'PlatformEffector2D': 251, 'PlatformModuleSetup': 877146078, 'PlayableDirector': 320, 'PlayerSettings': 129, 'PluginBuildInfo': 382020655, 'PluginImporter': 1050, 'PointEffector2D': 250, 'Polygon2D': 100010, 'PolygonCollider2D': 60, 'PositionConstraint': 1818360608, 'Prefab': 1001480554, 'PrefabImporter': 468431735, 'PrefabInstance': 1001, 'PreloadData': 150, 'Preset': 181963792, 'PresetManager': 1386491679, 'PreviewAnimationClip': 1108, 'PreviewImporter': 815301076, 'ProceduralMaterial': 185, 'ProceduralTexture': 186, 'Projector': 119, 'QualitySettings': 47, 'RayTracingShader': 825902497, 'RayTracingShaderImporter': 747330370, 'RectTransform': 224, 'ReferencesArtifactGenerator': 1114811875, 'ReflectionProbe': 215, 'RelativeJoint2D': 254, 'Renderer': 25, 'RenderSettings': 104, 'RenderTexture': 84, 'ResourceManager': 147, 'Rigidbody': 54, 'Rigidbody2D': 50, 'RootMotionData': 100006, 'RoslynAdditionalFileAsset': 1597193336, 'RoslynAdditionalFileImporter': 1642787288, 'RoslynAnalyzerConfigAsset': 947337230, 'RoslynAnalyzerConfigImporter': 1903396204, 'RotationConstraint': 1818360609, 'RuleSetFileAsset': 954905827, 'RuleSetFileImporter': 1777034230, 'RuntimeAnimatorController': 93, 'RuntimeInitializeOnLoadManager': 300, 'SampleClip': 271, 'ScaleConstraint': 1818360610, 'SceneAsset': 1032, 'SceneRoots': 1660057539, 'ScenesUsingAssets': 156483287, 'SceneVisibilityState': 1154873562, 'ScriptedImporter': 2089858483, 'Shader': 48, 'ShaderContainer': 1557264870, 'ShaderImporter': 1007, 'ShaderInclude': 109, 'ShaderIncludeImporter': 2103361453, 'ShaderNameRegistry': 94, 'ShaderVariantCollection': 200, 'SketchUpImporter': 1124, 'SkinnedMeshRenderer': 137, 'Skybox': 45, 'SliderJoint2D': 234, 'SortingGroup': 210, 'SparseTexture': 171, 'SpeedTreeImporter': 1110, 'SpeedTreeWindAsset': 228, 'SphereCollider': 135, 'SpringJoint': 145, 'SpringJoint2D': 231, 'Sprite': 213, 'SpriteAtlas': 687078895, 'SpriteAtlasAsset': 612988286, 'SpriteAtlasDatabase': 638013454, 'SpriteAtlasImporter': 1210832254, 'SpriteMask': 331, 'SpriteRenderer': 212, 'SpriteShapeRenderer': 1971053207, 'StreamingController': 1542919678, 'StreamingManager': 1403656975, 'SubstanceArchive': 184, 'SubstanceImporter': 1112, 'SurfaceEffector2D': 252, 'TagManager': 78, 'TargetJoint2D': 257, 'Terrain': 218, 'TerrainCollider': 154, 'TerrainData': 156, 'TerrainLayer': 1953259897, 'TextAsset': 49, 'TextMesh': 102, 'TextScriptImporter': 1031, 'Texture': 27, 'Texture2D': 28, 'Texture2DArray': 187, 'Texture3D': 117, 'TextureImporter': 1006, 'Tilemap': 1839735485, 'TilemapCollider2D': 19719996, 'TilemapRenderer': 483693784, 'TimeManager': 5, 'TrailRenderer': 96, 'Transform': 4, 'Tree': 193, 'TrueTypeFontImporter': 1042, 'UnityConnectSettings': 310, 'Vector3f': 100005, 'VersionControlSettings': 890905787, 'VFXManager': 937362698, 'VFXRenderer': 73398921, 'VideoBuildInfo': 1521398425, 'VideoClip': 329, 'VideoClipImporter': 1127, 'VideoPlayer': 328, 'VisualEffect': 2083052967, 'VisualEffectAsset': 2058629509, 'VisualEffectImporter': 2058629510, 'VisualEffectObject': 2059678085, 'VisualEffectResource': 2058629511, 'VisualEffectSubgraph': 994735392, 'VisualEffectSubgraphBlock': 994735404, 'VisualEffectSubgraphOperator': 994735403, 'void': 100011, 'WebCamTexture': 158, 'WheelCollider': 146, 'WheelJoint2D': 235, 'WindZone': 182}
'''
Unity classes have unique IDs for YAML file format.
This dictionary will be used to convert class names to their respective IDs.
'''

def init()-> str:
    start_tag = f"""%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
"""
    return start_tag
"""
This function returns the start tag of the YAML file.
Unity YAML files MUST start with the following lines.
  
return: 
  str: start tag of the YAML file.
"""

def OcclusionCullingSettings()-> str:
    setting = f"""--- !u!29 &1
OcclusionCullingSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_OcclusionBakeSettings:
    smallestOccluder: 5
    smallestHole: 0.25
    backfaceThreshold: 100
  m_SceneGUID: 00000000000000000000000000000000
  m_OcclusionCullingData: {{fileID: 0}}
"""
    return setting
"""
This function returns the YAML setting for OcclusionCullingSettings.
* the number next to "!u!" is the ID of the class.
* the number next to "&" is the ID of the object in YAML file.

return:
  str: YAML setting for OcclusionCullingSettings.
"""

def RenderSettings()-> str:
    setting = f"""--- !u!104 &2
RenderSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 10
  m_Fog: 0
  m_FogColor: {{r: 0.5, g: 0.5, b: 0.5, a: 1}}
  m_FogMode: 3
  m_FogDensity: 0.01
  m_LinearFogStart: 0
  m_LinearFogEnd: 300
  m_AmbientSkyColor: {{r: 0.212, g: 0.227, b: 0.259, a: 1}}
  m_AmbientEquatorColor: {{r: 0.114, g: 0.125, b: 0.133, a: 1}}
  m_AmbientGroundColor: {{r: 0.047, g: 0.043, b: 0.035, a: 1}}
  m_AmbientIntensity: 1
  m_AmbientMode: 0
  m_SubtractiveShadowColor: {{r: 0.42, g: 0.478, b: 0.627, a: 1}}
  m_SkyboxMaterial: {{fileID: 10304, guid: 0000000000000000f000000000000000, type: 0}}
  m_HaloStrength: 0.5
  m_FlareStrength: 1
  m_FlareFadeSpeed: 3
  m_HaloTexture: {{fileID: 0}}
  m_SpotCookie: {{fileID: 10001, guid: 0000000000000000e000000000000000, type: 0}}
  m_DefaultReflectionMode: 0
  m_DefaultReflectionResolution: 128
  m_ReflectionBounces: 1
  m_ReflectionIntensity: 1
  m_CustomReflection: {{fileID: 0}}
  m_Sun: {{fileID: 705507994}}
  m_UseRadianceAmbientProbe: 0
"""
    return setting
"""
This function returns the YAML setting for RenderSettings.

return:
  str: YAML setting for RenderSettings.
"""

def LightmapSettings()-> str:
    setting = f"""--- !u!157 &3
LightmapSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 13
  m_BakeOnSceneLoad: 0
  m_GISettings:
    serializedVersion: 2
    m_BounceScale: 1
    m_IndirectOutputScale: 1
    m_AlbedoBoost: 1
    m_EnvironmentLightingMode: 0
    m_EnableBakedLightmaps: 1
    m_EnableRealtimeLightmaps: 0
  m_LightmapEditorSettings:
    serializedVersion: 12
    m_Resolution: 2
    m_BakeResolution: 40
    m_AtlasSize: 1024
    m_AO: 0
    m_AOMaxDistance: 1
    m_CompAOExponent: 1
    m_CompAOExponentDirect: 0
    m_ExtractAmbientOcclusion: 0
    m_Padding: 2
    m_LightmapParameters: {{fileID: 0}}
    m_LightmapsBakeMode: 1
    m_TextureCompression: 1
    m_ReflectionCompression: 2
    m_MixedBakeMode: 2
    m_BakeBackend: 1
    m_PVRSampling: 1
    m_PVRDirectSampleCount: 32
    m_PVRSampleCount: 500
    m_PVRBounces: 2
    m_PVREnvironmentSampleCount: 500
    m_PVREnvironmentReferencePointCount: 2048
    m_PVRFilteringMode: 2
    m_PVRDenoiserTypeDirect: 0
    m_PVRDenoiserTypeIndirect: 0
    m_PVRDenoiserTypeAO: 0
    m_PVRFilterTypeDirect: 0
    m_PVRFilterTypeIndirect: 0
    m_PVRFilterTypeAO: 0
    m_PVREnvironmentMIS: 0
    m_PVRCulling: 1
    m_PVRFilteringGaussRadiusDirect: 1
    m_PVRFilteringGaussRadiusIndirect: 5
    m_PVRFilteringGaussRadiusAO: 2
    m_PVRFilteringAtrousPositionSigmaDirect: 0.5
    m_PVRFilteringAtrousPositionSigmaIndirect: 2
    m_PVRFilteringAtrousPositionSigmaAO: 1
    m_ExportTrainingData: 0
    m_TrainingDataDestination: TrainingData
    m_LightProbeSampleCountMultiplier: 4
  m_LightingDataAsset: {{fileID: 20201, guid: 0000000000000000f000000000000000, type: 0}}
  m_LightingSettings: {{fileID: 0}}
"""
    return setting
"""
This function returns the YAML setting for LightmapSettings.

return:
  str: YAML setting for LightmapSettings.
"""

def NavMeshSettings()-> str:
    setting = f"""--- !u!196 &4
NavMeshSettings:
  serializedVersion: 2
  m_ObjectHideFlags: 0
  m_BuildSettings:
    serializedVersion: 3
    agentTypeID: 0
    agentRadius: 0.5
    agentHeight: 2
    agentSlope: 45
    agentClimb: 0.4
    ledgeDropHeight: 0
    maxJumpAcrossDistance: 0
    minRegionArea: 2
    manualCellSize: 0
    cellSize: 0.16666667
    manualTileSize: 0
    tileSize: 256
    buildHeightMesh: 0
    maxJobWorkers: 0
    preserveTilesOutsideBounds: 0
    debug:
      m_Flags: 0
  m_NavMeshData: {{fileID: 0}}
"""
    return setting
"""
This function returns the YAML setting for NavMeshSettings.

return:
  str: YAML setting for NavMeshSettings.
"""
    
##########################
# default scene settings #
##########################

def add_cube():
    pass
# TODO: implement another function to add a 3d object.
# ex) cube, capsule, cyclinder, plane, quad, etc.

def add_sphere(name: str, mesh_id=10207,
               radius=0.5, center=[0, 0, 0], 
               position=[0, 0, 0], rotation=[0, 0, 0, 1], scale=[1, 1, 1],
               has_rigidbody_component=True, mass=1, linear_drag=0, angular_drag=0.05, center_of_mass=[0, 0, 0])-> tuple[str, int]:
    id_target = randint(0xffffff, 0x1fffffffffffffff)
    id_this = id_target+1

    num_of_component = 4
    if (has_rigidbody_component):
        num_of_component += 1
    ## TODO: implement the case when another component is added.

    setting = f""""""
    setting += GameObject(id_target, name, num_of_component)
    setting += SphereCollider(id_this, id_target, radius, center)
    id_this += 1
    setting += MeshRenderer(id_this, id_target)
    id_this += 1
    setting += MeshFilter(id_this, id_target, mesh_id)
    id_this += 1
    if (has_rigidbody_component):
        setting += Rigidbody(id_this, id_target, mass, linear_drag, angular_drag, center_of_mass)
        id_this += 1
    setting += Transform(id_this, id_target, position, rotation, scale)
    # TODO: implement the case when another component is added.
    # ex) anthor property of physics?

    return setting, id_this
"""
This function makes the YAML setting for a sphere object.
Default sphere has 4 components: SphereCollider, MeshRenderer, MeshFilter, Transform.
For test, Rigidbody component is added.

param:
  1st line: name: str - name of the sphere object.
            mesh_id: int - ID of the mesh object. (sphere mesh)
  2nd line: radius: float - radius of the sphere.
            center: list[int] - center of the sphere.
  3rd line: position: list[int] - position of the sphere.
            rotation: list[int] - rotation of the sphere.
            scale: list[int] - scale of the sphere.
  4th line: has_rigidbody_component: bool - whether the sphere has Rigidbody component.
            mass: float - mass of the sphere.
            linear_drag: float - linear drag of the sphere.
            angular_drag: float - angular drag of the sphere.

return:
  setting: str - YAML setting for the sphere object.
  id_this: int - ID of the "Transform" component for SceneRoots.
"""

def GameObject(id_target: int, name: str, num_of_component: int)-> str:
    setting = f"""--- !u!1 &{id_target}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
"""
    for i in range(num_of_component, 0, -1):
        setting += f"""  - component: {{fileID: {id_target + i}}}
"""
    setting += f"""  m_Layer: 0
  m_Name: {name}
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
"""
    return setting
"""
This function makes the YAML setting for a GameObject.

param:
  id_target: int - ID of THIS GameObject.
  name: str - name of the GameObject.
  num_of_component: int - number of components in the GameObject.

return:
  setting: str - YAML setting for the GameObject.
"""

def SphereCollider(id_this: int, id_target: int, radius=0.5, center=[0, 0, 0])-> str:
    setting = f"""--- !u!135 &{id_this}
SphereCollider:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {id_target}}}
  m_Material: {{fileID: 0}}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_LayerOverridePriority: 0
  m_IsTrigger: 0
  m_ProvidesContacts: 0
  m_Enabled: 1
  serializedVersion: 3
  m_Radius: {radius}
  m_Center: {{x: {center[0]}, y: {center[1]}, z: {center[2]}}}
"""
    return setting
"""
This function makes the YAML setting for a SphereCollider.

param:
  id_this: int - ID of THIS SphereCollider.
  id_target: int - ID of the GameObject.
  radius: float - radius of the sphere.
  center: list[int] - center of the sphere.

return:
  setting: str - YAML setting for a SphereCollider.
"""

def MeshRenderer(id_this: int, id_target: int):
    setting = f"""--- !u!23 &{id_this}
MeshRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {id_target}}}
  m_Enabled: 1
  m_CastShadows: 1
  m_ReceiveShadows: 1
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RayTracingMode: 2
  m_RayTraceProcedural: 0
  m_RayTracingAccelStructBuildFlagsOverride: 0
  m_RayTracingAccelStructBuildFlags: 1
  m_SmallMeshCulling: 1
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_Materials:
  - {{fileID: 10303, guid: 0000000000000000f000000000000000, type: 0}}
  m_StaticBatchInfo:
    firstSubMesh: 0
    subMeshCount: 0
  m_StaticBatchRoot: {{fileID: 0}}
  m_ProbeAnchor: {{fileID: 0}}
  m_LightProbeVolumeOverride: {{fileID: 0}}
  m_ScaleInLightmap: 1
  m_ReceiveGI: 1
  m_PreserveUVs: 0
  m_IgnoreNormalsForChartDetection: 0
  m_ImportantGI: 0
  m_StitchLightmapSeams: 1
  m_SelectedEditorRenderState: 3
  m_MinimumChartSize: 4
  m_AutoUVMaxDistance: 0.5
  m_AutoUVMaxAngle: 89
  m_LightmapParameters: {{fileID: 0}}
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 0
  m_AdditionalVertexStreams: {{fileID: 0}}
"""
    return setting
"""
This function makes the YAML setting for a MeshRenderer.

param:
  id_this: int - ID of THIS MeshRenderer.
  id_target: int - ID of the GameObject.

return:
  setting: str - YAML setting for a MeshRenderer.
"""

def MeshFilter(id_this: int, id_target: int, mesh_id: int):
    # TODO: edit mesh in this functoin?
    setting = f"""--- !u!33 &{id_this}
MeshFilter:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {id_target}}}
  m_Mesh: {{fileID: {mesh_id}, guid: 0000000000000000e000000000000000, type: 0}}
"""
    return setting
"""
This function makes the YAML setting for a MeshFilter.

param:
  id_this: int - ID of THIS MeshFilter.
  id_target: int - ID of the GameObject.
  mesh_id: int - ID of the mesh object.

return:
  setting: str - YAML setting for a MeshFilter.
"""

def Rigidbody(id_this: int, id_target: int, mass=1, linear_drag=0,
               angular_drag=0.05, center_of_mass=[0, 0, 0],):
    setting = f"""--- !u!54 &{id_this}
Rigidbody:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {id_target}}}
  serializedVersion: 4
  m_Mass: {mass}
  m_Drag: {linear_drag}
  m_AngularDrag: {angular_drag}
  m_CenterOfMass: {{x: {center_of_mass[0]}, y: {center_of_mass[1]}, z: {center_of_mass[2]}}}
  m_InertiaTensor: {{x: 1, y: 1, z: 1}}
  m_InertiaRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ImplicitCom: 1
  m_ImplicitTensor: 1
  m_UseGravity: 1
  m_IsKinematic: 0
  m_Interpolate: 0
  m_Constraints: 0
  m_CollisionDetection: 0
"""
    ##TODO: case of Constraints?
    return setting
"""
This function makes the YAML setting for a Rigidbody.

param:
  id_this: int - ID of THIS Rigidbody.
  id_target: int - ID of the GameObject.
  mass: float - mass of the Rigidbody.
  linear_drag: float - linear drag of the Rigidbody.
  angular_drag: float - angular drag of the Rigidbody.
  center_of_mass: list[int] - center of mass of the Rigidbody.

return:
  setting: str - YAML setting for a Rigidbody.
"""

def Transform(id_this: int, id_target: int, position: list[int],
              rotation: list[int], scale: list[int])-> str:
    setting = f"""--- !u!4 &{id_this}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {id_target}}}
  serializedVersion: 2
  m_LocalRotation: {{x: {rotation[0]}, y: {rotation[1]}, z: {rotation[2]}, w: {rotation[3]}}}
  m_LocalPosition: {{x: {position[0]}, y: {position[1]}, z: {position[2]}}}
  m_LocalScale: {{x: {scale[0]}, y: {scale[1]}, z: {scale[2]}}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
"""
    return setting
"""
This function makes the YAML setting for a Transform.

param:
  id_this: int - ID of THIS Transform.
  id_target: int - ID of the GameObject.
  position: list[int] - position of the object.
  rotation: list[int] - rotation of the object.
  scale: list[int] - scale of the object.

return:
  setting: str - YAML setting for a Transform.
"""

def add_light()-> tuple[str, int]:
    transform_id_num = 705507995
    setting = f"""--- !u!1 &705507993
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 705507995}}
  - component: {{fileID: 705507994}}
  m_Layer: 0
  m_Name: Directional Light
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!108 &705507994
Light:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 705507993}}
  m_Enabled: 1
  serializedVersion: 11
  m_Type: 1
  m_Color: {{r: 1, g: 0.95686275, b: 0.8392157, a: 1}}
  m_Intensity: 1
  m_Range: 10
  m_SpotAngle: 30
  m_InnerSpotAngle: 21.80208
  m_CookieSize: 10
  m_Shadows:
    m_Type: 2
    m_Resolution: -1
    m_CustomResolution: -1
    m_Strength: 1
    m_Bias: 0.05
    m_NormalBias: 0.4
    m_NearPlane: 0.2
    m_CullingMatrixOverride:
      e00: 1
      e01: 0
      e02: 0
      e03: 0
      e10: 0
      e11: 1
      e12: 0
      e13: 0
      e20: 0
      e21: 0
      e22: 1
      e23: 0
      e30: 0
      e31: 0
      e32: 0
      e33: 1
    m_UseCullingMatrixOverride: 0
  m_Cookie: {{fileID: 0}}
  m_DrawHalo: 0
  m_Flare: {{fileID: 0}}
  m_RenderMode: 0
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingLayerMask: 1
  m_Lightmapping: 1
  m_LightShadowCasterMode: 0
  m_AreaSize: {{x: 1, y: 1}}
  m_BounceIntensity: 1
  m_ColorTemperature: 6570
  m_UseColorTemperature: 0
  m_BoundingSphereOverride: {{x: 0, y: 0, z: 0, w: 0}}
  m_UseBoundingSphereOverride: 0
  m_UseViewFrustumForShadowCasterCull: 1
  m_ForceVisible: 0
  m_ShadowRadius: 0
  m_ShadowAngle: 0
  m_LightUnit: 1
  m_LuxAtDistance: 1
  m_EnableSpotReflector: 1
--- !u!4 &705507995
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 705507993}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0.40821788, y: -0.23456968, z: 0.10938163, w: 0.8754261}}
  m_LocalPosition: {{x: 0, y: 3, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 50, y: -30, z: 0}}
"""
    return setting, transform_id_num
"""
This function makes the YAML setting for a Light object.

return:
  setting: str - YAML setting for a Light object.
  transform_id_num: int - ID of the "Transform" component for Light object.
"""

def add_camera(position=[0, 1, -10], rotation=[0, 0, 0, 0], scale=[1, 1, 1])-> tuple[str, int]:
    transform_id_num = 1648527734
    setting = f"""--- !u!1 &1648527731
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 1648527734}}
  - component: {{fileID: 1648527733}}
  - component: {{fileID: 1648527732}}
  m_Layer: 0
  m_Name: Main Camera
  m_TagString: MainCamera
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!81 &1648527732
AudioListener:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 1648527731}}
  m_Enabled: 1
--- !u!20 &1648527733
Camera:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 1648527731}}
  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 1
  m_BackGroundColor: {{r: 0.19215687, g: 0.3019608, b: 0.4745098, a: 0}}
  m_projectionMatrixMode: 1
  m_GateFitMode: 2
  m_FOVAxisMode: 0
  m_Iso: 200
  m_ShutterSpeed: 0.005
  m_Aperture: 16
  m_FocusDistance: 10
  m_FocalLength: 50
  m_BladeCount: 5
  m_Curvature: {{x: 2, y: 11}}
  m_BarrelClipping: 0.25
  m_Anamorphism: 0
  m_SensorSize: {{x: 36, y: 24}}
  m_LensShift: {{x: 0, y: 0}}
  m_NormalizedViewPortRect:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  near clip plane: 0.3
  far clip plane: 1000
  field of view: 60
  orthographic: 0
  orthographic size: 5
  m_Depth: -1
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingPath: -1
  m_TargetTexture: {{fileID: 0}}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 1
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_ForceIntoRT: 0
  m_OcclusionCulling: 1
  m_StereoConvergence: 10
  m_StereoSeparation: 0.022
--- !u!4 &1648527734
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 1648527731}}
  serializedVersion: 2
  m_LocalRotation: {{x: {rotation[0]}, y: {rotation[1]}, z: {rotation[2]}, w: 1}}
  m_LocalPosition: {{x: {position[0]}, y: {position[1]}, z: {position[2]}}}
  m_LocalScale: {{x: {scale[0]}, y: {scale[1]}, z: {scale[2]}}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
"""
    return setting, transform_id_num
"""
This function makes the YAML setting for a Camera object.

return:
  setting: str - YAML setting for a Camera object.
  transform_id_num: int - ID of the "Transform" component for Camera object.
"""

# transform conponet goes to this list. Make a priority for components.
def SceneRoots(object_id_list: list)-> str:
    setting="""--- !u!1660057539 &9223372036854775807
SceneRoots:
  m_ObjectHideFlags: 0
  m_Roots:
"""
    for num in object_id_list:
        setting += f"  - {{fileID: {num}}}\n"

    return setting
"""
This function makes the YAML setting for SceneRoots.

param:
  object_id_list: list[int] - list of IDs of the objects in the scene. This should be in the order of the components.

return:
  setting: str - YAML setting for SceneRoots.
"""

# test simple scene
if __name__ == "__main__":
    id_list: list[int] = []
    with open("result.unity", "w", encoding='utf-8') as f:
        f.write(init())
        f.write(OcclusionCullingSettings())
        f.write(RenderSettings())
        f.write(LightmapSettings())
        f.write(NavMeshSettings())

        for i in range(10):
            object_setting, object_id = add_sphere(f"Sphere_{i}", position=[i, 0, 0])
            id_list.append(object_id)
            f.write(object_setting)
        
        light_setting, light_id = add_light()
        f.write(light_setting)
        id_list.insert(0, light_id)

        camera_setting, camera_id = add_camera()
        f.write(camera_setting)
        id_list.insert(0, camera_id)

        f.write(SceneRoots(id_list))