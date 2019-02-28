from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import numpy as np

spark = SparkSession.builder.appName('generador_schema').getOrCreate()
train_path = 'data/train_final_2/*.csv'
train = spark.read.csv(train_path, header=True, inferSchema=True)

train.persist()
print(train.count(), '\n')

dict_finished = {
'IsBeta': np.int8,                                                              
'RtpStateBitfield': np.int8,                                                    
'IsSxsPassiveMode': np.int8,                                                    
'DefaultBrowsersIdentifier': np.int16,                                          
'AVProductStatesIdentifier': np.int32,                                          
'AVProductsInstalled': np.int8,                                                 
'AVProductsEnabled': np.int8,                                                   
'HasTpm': np.int8,                                                              
'CountryIdentifier': np.int16,                                                  
'CityIdentifier': np.int32,                                                     
'OrganizationIdentifier': np.int8,                                              
'GeoNameIdentifier': np.int16,                                                  
'LocaleEnglishNameIdentifier': np.int16,                                        
'OsBuild': np.int16,                                                            
'OsSuite': np.int16,                                                            
'IsProtected': np.int8,                                                         
'AutoSampleOptIn': np.int8,                                                     
'SMode': np.int8,                                                               
'IeVerIdentifier': np.int16,                                                    
'Firewall': np.int8,                                                            
'UacLuaenable': np.int32,                                                       
'Census_OEMNameIdentifier': np.int16,                                           
'Census_OEMModelIdentifier': np.int32,                                          
'Census_ProcessorCoreCount': np.int16,                                          
'Census_ProcessorManufacturerIdentifier': np.int8,                              
'Census_ProcessorModelIdentifier': np.int16,                                    
'Census_PrimaryDiskTotalCapacity': np.int32,                                    
'Census_SystemVolumeTotalCapacity': np.int32,                                   
'Census_HasOpticalDiskDrive': np.int8,                                          
'Census_TotalPhysicalRAM': np.int32,                                            
'Census_InternalPrimaryDiagonalDisplaySizeInInches': np.int16,                  
'Census_InternalPrimaryDisplayResolutionHorizontal': np.int16,                  
'Census_InternalPrimaryDisplayResolutionVertical': np.int16,                    
'Census_InternalBatteryNumberOfCharges': np.int32,                              
'Census_OSBuildNumber': np.int16,                                               
'Census_OSBuildRevision': np.int32,                                             
'Census_OSInstallLanguageIdentifier': np.int8,                                  
'Census_OSUILocaleIdentifier': np.int16,                                        
'Census_IsPortableOperatingSystem': np.int8,                                    
'Census_IsFlightingInternal': np.int8,                                          
'Census_IsFlightsDisabled': np.int8,                                            
'Census_ThresholdOptIn': np.int8,                                               
'Census_FirmwareManufacturerIdentifier': np.int16,                              
'Census_FirmwareVersionIdentifier': np.int32,                                   
'Census_IsSecureBootEnabled': np.int8,                                          
'Census_IsWIMBootEnabled': np.int8,                                             
'Census_IsVirtualDevice': np.int8,                                              
'Census_IsTouchEnabled': np.int8,                                               
'Census_IsPenCapable': np.int8,                                                 
'Census_IsAlwaysOnAlwaysConnectedCapable': np.int8,                             
'Wdft_IsGamer': np.int8,                                                        
'Wdft_RegionIdentifier': np.int8,                                               
'HasDetections': np.int8,                                                       
'Census_InternalBatteryType_informed': np.int8,                                 
'ProductName_index': np.int8,                                                   
'Platform_index': np.int8,                                                      
'Processor_index': np.int8,                                                     
'SkuEdition_index': np.int8,                                                    
'PuaMode_index': np.int8,                                                       
'SmartScreen_index': np.int8,                                                   
'Census_MDC2FormFactor_index': np.int8,                                         
'Census_DeviceFamily_index': np.int8,                                           
'Census_ProcessorClass_index': np.int8,                                         
'Census_PrimaryDiskTypeName_index': np.int8,                                    
'Census_ChassisTypeName_index': np.int8,                                        
'Census_PowerPlatformRoleName_index': np.int8,                                    
'Census_OSBranch_index': np.int8,                                               
'Census_OSSkuName_index': np.int8,                                              
'Census_OSInstallTypeName_index': np.int8,                                      
'Census_OSWUAutoUpdateOptionsName_index': np.int8,                              
'Census_GenuineStateName_index': np.int8,                                       
'Census_ActivationChannel_index': np.int8,                                      
'Census_FlightRing_index': np.int8,                                             
'ProductName_windowsintune': np.int8,                                           
'ProductName_mse': np.int8,                                                     
'ProductName_mseprerelease': np.int8,                                           
'ProductName_scep': np.int8,                                                    
'ProductName_fep': np.int8,                                                     
'ProductName_win8defender': np.int8,                                            
'Platform_windows10': np.int8,                                                  
'Platform_windows2016': np.int8,                                                
'Platform_windows8': np.int8,                                                   
'Platform_windows7': np.int8,                                                   
'Processor_x86': np.int8,                                                       
'Processor_x64': np.int8,                                                       
'Processor_arm64': np.int8,                                                     
'SkuEdition_Education': np.int8,                                                
'SkuEdition_Home': np.int8,                                                     
'SkuEdition_Pro': np.int8,                                                      
'SkuEdition_Server': np.int8,                                                   
'SkuEdition_Invalid': np.int8,                                                  
'SkuEdition_Enterprise': np.int8,                                               
'SkuEdition_Cloud': np.int8,                                                    
'SkuEdition_Enterprise LTSB': np.int8,                                          
'PuaMode_on': np.int8,                                                          
'PuaMode_UNKNOWN': np.int8,                                                     
'PuaMode_audit': np.int8,                                                       
'SmartScreen_OFF': np.int8,                                                     
'SmartScreen_Prompt': np.int8,                                                  
'SmartScreen_Unknown': np.int8,                                                 
'SmartScreen_Warn': np.int8,                                                    
'SmartScreen_ON': np.int8,                                                      
'SmartScreen_RequiredAdmin': np.int8,                                           
'SmartScreen_BLOCK': np.int8,                                                   
'SmartScreen_Deny': np.int8,                                                    
'SmartScreen_ExistsNotSet': np.int8,                                            
'Census_MDC2FormFactor_Convertible': np.int8,                                   
'Census_MDC2FormFactor_PCOther': np.int8,                                       
'Census_MDC2FormFactor_Other': np.int8,                                         
'Census_MDC2FormFactor_LargeServer': np.int8,                                   
'Census_MDC2FormFactor_IoTOther': np.int8,                                      
'Census_MDC2FormFactor_Detachable': np.int8,                                    
'Census_MDC2FormFactor_SmallServer': np.int8,                                   
'Census_MDC2FormFactor_Notebook': np.int8,                                      
'Census_MDC2FormFactor_ServerOther': np.int8,                                   
'Census_MDC2FormFactor_MediumServer': np.int8,                                  
'Census_MDC2FormFactor_Desktop': np.int8,                                       
'Census_MDC2FormFactor_LargeTablet': np.int8,                                   
'Census_MDC2FormFactor_AllInOne': np.int8,                                      
'Census_MDC2FormFactor_SmallTablet': np.int8,
'Census_DeviceFamily_Windows': np.int8,                                         
'Census_ProcessorClass_low': np.int8,                                           
'Census_ProcessorClass_UNKNOWN': np.int8,                                       
'Census_ProcessorClass_high': np.int8,                                          
'Census_ProcessorClass_mid': np.int8,                                           
'Census_PrimaryDiskTypeName_SSD': np.int8,                                      
'Census_PrimaryDiskTypeName_HDD': np.int8,                                      
'Census_PrimaryDiskTypeName_UNKNOWN': np.int8,                                  
'Census_ChassisTypeName_AllinOne': np.int8,                                     
'Census_ChassisTypeName_Tablet': np.int8,                                       
'Census_ChassisTypeName_PeripheralChassis': np.int8,                            
'Census_ChassisTypeName_Numerico': np.int8,                                     
'Census_ChassisTypeName_EmbeddedPC': np.int8,                                   
'Census_ChassisTypeName_SpaceSaving': np.int8,                                  
'Census_ChassisTypeName_HandHeld': np.int8,                                     
'Census_ChassisTypeName_StickPC': np.int8,                                      
'Census_ChassisTypeName_Convertible': np.int8,                                  
'Census_ChassisTypeName_SubChassis': np.int8,                                   
'Census_ChassisTypeName_Portable': np.int8,                                     
'Census_ChassisTypeName_MiniPC': np.int8,                                       
'Census_ChassisTypeName_UNKNOWN': np.int8,                                      
'Census_ChassisTypeName_Desktop': np.int8,                                      
'Census_ChassisTypeName_LowProfileDesktop': np.int8,                            
'Census_ChassisTypeName_SealedCasePC': np.int8,                                 
'Census_ChassisTypeName_ExpansionChassis': np.int8,                             
'Census_ChassisTypeName_Detachable': np.int8,                                   
'Census_ChassisTypeName_RackMountChassis': np.int8,                             
'Census_ChassisTypeName_SubNotebook': np.int8,                                  
'Census_ChassisTypeName_BusExpansionChassis': np.int8,                          
'Census_ChassisTypeName_Notebook': np.int8,                                     
'Census_ChassisTypeName_Laptop': np.int8,                                       
'Census_ChassisTypeName_Tower': np.int8,                                        
'Census_ChassisTypeName_BladeEnclosure': np.int8,                               
'Census_ChassisTypeName_IoTGateway': np.int8,                                   
'Census_ChassisTypeName_LunchBox': np.int8,                                     
'Census_ChassisTypeName_MultisystemChassis': np.int8,                           
'Census_ChassisTypeName_DockingStation': np.int8,                               
'Census_ChassisTypeName_CompactPCI': np.int8,                                   
'Census_ChassisTypeName_MiniTower': np.int8,                                    
'Census_ChassisTypeName_MainServerChassis': np.int8,                            
'Census_ChassisTypeName_PizzaBox': np.int8,                                     
'Census_ChassisTypeName_Blade': np.int8,                                        
'Census_PowerPlatformRoleName_SOHOServer': np.int8,                             
'Census_PowerPlatformRoleName_EnterpriseServer': np.int8,                       
'Census_PowerPlatformRoleName_AppliancePC': np.int8,                            
'Census_PowerPlatformRoleName_UNKNOWN': np.int8,                                
'Census_PowerPlatformRoleName_Desktop': np.int8,                                
'Census_PowerPlatformRoleName_PerformanceServer': np.int8,                      
'Census_PowerPlatformRoleName_Workstation': np.int8,                            
'Census_PowerPlatformRoleName_Mobile': np.int8,                                 
'Census_PowerPlatformRoleName_Slate': np.int8,                                  
'Census_OSBranch_rs5_release_sigma': np.int8,                                   
'Census_OSBranch_win7sp1_ldr': np.int8,                                         
'Census_OSBranch_rs5_release_sign': np.int8,                                    
'Census_OSBranch_th2_release_sec': np.int8,                                     
'Census_OSBranch_rs5_release': np.int8,                                         
'Census_OSBranch_rs1_release_sec': np.int8,                                     
'Census_OSBranch_rs_shell': np.int8,                                            
'Census_OSBranch_rs4_release': np.int8,                                         
'Census_OSBranch_rs_prerelease_flt': np.int8,                                   
'Census_OSBranch_win7sp1_gdr': np.int8,                                         
'Census_OSBranch_rs_xbox': np.int8,                                             
'Census_OSBranch_rs3_release_svc_escrow': np.int8,                              
'Census_OSBranch_rs1_release_inmarket': np.int8,                                
'Census_OSBranch_win8_gdr': np.int8,                                            
'Census_OSBranch_rs1_release_srvmedia': np.int8,                                
'Census_OSBranch_rs_onecore_base_cobalt': np.int8,                              
'Census_OSBranch_th1_st1': np.int8,                                             
'Census_OSBranch_winblue_ltsb': np.int8,                                        
'Census_OSBranch_Khmer OS': np.int8,                                            
'Census_OSBranch_winblue_ltsb_escrow': np.int8,                                 
'Census_OSBranch_rs_onecore_stack_per1': np.int8,                               
'Census_OSBranch_rs_onecore_sigma_dplat_d7': np.int8,                           
'Census_OSBranch_win7sp1_ldr_escrow': np.int8,                                  
'Census_OSBranch_rs_edge': np.int8,                                             
'Census_OSBranch_rs3_release_svc_escrow_im': np.int8,                           
'Census_OSBranch_rs3_release_svc': np.int8,                                     
'Census_OSBranch_rs2_release': np.int8,                                         
'Census_OSBranch_rs2_release_svc_d': np.int8,                                   
'Census_OSBranch_rs5_release_sigma_dev': np.int8,                               
'Census_OSBranch_th1': np.int8,                                                 
'Census_OSBranch_rs1_release': np.int8,                                         
'Census_OSBranch_rs_prerelease': np.int8,                                       
'Census_OSBranch_rs5_release_edge': np.int8,                                    
'Census_OSBranch_rsmaster': np.int8,                                            
'Census_OSBranch_win8_ldr': np.int8,                                            
'Census_OSBranch_rs_onecore_dep': np.int8,                                      
'Census_OSBranch_th2_release': np.int8,                                         
'Census_OSBranch_rs3_release': np.int8,                                         
'Census_OSBranch_rs1_release_svc': np.int8,                                     
'Census_OSBranch_rs_onecore_sigma_grfx_dev': np.int8,                           
'Census_OSSkuName_ULTIMATE': np.int8,                                           
'Census_OSSkuName_CORE_COUNTRYSPECIFIC': np.int8,                               
'Census_OSSkuName_EDUCATION_N': np.int8,                                        
'Census_OSSkuName_UNLICENSED': np.int8,                                         
'Census_OSSkuName_ENTERPRISEG': np.int8,                                        
'Census_OSSkuName_PRO_CHINA': np.int8,                                          
'Census_OSSkuName_PROFESSIONAL_N': np.int8,                                     
'Census_OSSkuName_DATACENTER_SERVER': np.int8,                                  
'Census_OSSkuName_ENTERPRISE_S_N': np.int8,                                     
'Census_OSSkuName_ENTERPRISE': np.int8,                                         
'Census_OSSkuName_PRO_WORKSTATION_N': np.int8,                                  
'Census_OSSkuName_CORE_SINGLELANGUAGE': np.int8,                                
'Census_OSSkuName_HOME_BASIC': np.int8,                                         
'Census_OSSkuName_SB_SOLUTION_SERVER': np.int8,                                 
'Census_OSSkuName_DATACENTER_EVALUATION_SERVER': np.int8,                       
'Census_OSSkuName_PROFESSIONAL': np.int8,                                       
'Census_OSSkuName_STANDARD_SERVER': np.int8,                                    
'Census_OSSkuName_HOME_PREMIUM': np.int8,                                       
'Census_OSSkuName_PRO_WORKSTATION': np.int8,                                    
'Census_OSSkuName_CORE': np.int8,                                               
'Census_OSSkuName_STANDARD_EVALUATION_SERVER': np.int8,                         
'Census_OSSkuName_ENTERPRISE_N': np.int8,                                       
'Census_OSSkuName_PRO_FOR_EDUCATION': np.int8,                                  
'Census_OSSkuName_SERVERRDSH': np.int8,                                         
'Census_OSSkuName_CLOUD': np.int8,                                              
'Census_OSSkuName_ENTERPRISE_S': np.int8,                                       
'Census_OSSkuName_EDUCATION': np.int8,                                          
'Census_OSSkuName_CORE_N': np.int8,                                             
'Census_OSSkuName_PRO_SINGLE_LANGUAGE': np.int8,                                
'Census_OSSkuName_CLOUDN': np.int8,                                             
'Census_OSSkuName_UNDEFINED': np.int8,                                          
'Census_OSSkuName_STARTER': np.int8,                                            
'Census_OSInstallTypeName_Reset': np.int8,                                      
'Census_OSInstallTypeName_Refresh': np.int8,                                    
'Census_OSInstallTypeName_Clean': np.int8,                                      
'Census_OSInstallTypeName_Other': np.int8,                                      
'Census_OSInstallTypeName_UUPUpgrade': np.int8,                                 
'Census_OSInstallTypeName_IBSClean': np.int8,                                   
'Census_OSInstallTypeName_CleanPCRefresh': np.int8,                             
'Census_OSInstallTypeName_Update': np.int8,                                     
'Census_OSInstallTypeName_Upgrade': np.int8,                                    
'Census_OSWUAutoUpdateOptionsName_DownloadNotify': np.int8,                     
'Census_OSWUAutoUpdateOptionsName_UNKNOWN': np.int8,                            
'Census_OSWUAutoUpdateOptionsName_Off': np.int8,                                
'Census_OSWUAutoUpdateOptionsName_FullAuto': np.int8,                           
'Census_OSWUAutoUpdateOptionsName_Notify': np.int8,                             
'Census_OSWUAutoUpdateOptionsName_AutoInstallAndRebootAtMaintenanceTime': np.int8,
'Census_GenuineStateName_IS_GENUINE': np.int8,                                  
'Census_GenuineStateName_UNKNOWN': np.int8,                                     
'Census_GenuineStateName_TAMPERED': np.int8,                                    
'Census_GenuineStateName_INVALID_LICENSE': np.int8,                             
'Census_GenuineStateName_OFFLINE': np.int8,                                     
'Census_ActivationChannel_Retail': np.int8,                                     
'Census_ActivationChannel_Volume:MAK': np.int8,                                 
'Census_ActivationChannel_OEM:NONSLP': np.int8,                                 
'Census_ActivationChannel_Retail:TB:Eval': np.int8,                             
'Census_ActivationChannel_OEM:DM': np.int8,                                     
'Census_ActivationChannel_Volume:GVLK': np.int8,                                
'Census_FlightRing_OSG': np.int8,                                               
'Census_FlightRing_Unknown': np.int8,                                           
'Census_FlightRing_Canary': np.int8,                                            
'Census_FlightRing_Retail': np.int8,                                            
'Census_FlightRing_Invalid': np.int8,                                           
'Census_FlightRing_WIF': np.int8,                                               
'Census_FlightRing_Disabled': np.int8,                                          
'Census_FlightRing_RP': np.int8,                                                
'Census_FlightRing_WIS': np.int8,                                               
'Census_FlightRing_CBCanary': np.int8,                                          
'Census_FlightRing_NOT_SET': np.int8,                                           
'Census_OSVersion_0': np.int8,                                                  
'Census_OSVersion_1': np.int8,                                                  
'Census_OSVersion_2': np.int16,                                                 
'Census_OSVersion_3': np.int32,                                                 
'EngineVersion_2': np.int16,                                                    
'EngineVersion_3': np.int8,                                                     
'AppVersion_1': np.int8,                                                        
'AppVersion_2': np.int16,                                                       
'AppVersion_3': np.int16,                                                       
'AvSigVersion_0': np.int8,                                                      
'AvSigVersion_1': np.int16,                                                     
'AvSigVersion_2': np.int16,                                                     
'OsVer_0': np.int8,                                                             
'OsVer_1': np.int8,                                                             
'OsVer_2': np.int16,                                                            
'OsVer_3': np.int16,                                                            
'OsBuildLab_diff': np.int8,                                                     
'AvSigVersion_diff': np.int16,                                                  
'OSVersion_diff': np.int8,                                                      
'OSBuild_fulldiff': np.int8,                                                    
'AvSigVersion_fulldiff': np.int8,                                               
'OsBuildLab_difftotal': np.int16,                                               
'DateAvSigVersion_difftotal': np.int16,                                         
'DateOSVersion_difftotal': np.int16,                                            
'DateAvSigVersion_fulldifftotal': np.int8,                                      
'OsBuildLab_fulldifftotal': np.int8,                                            
'DateAvSigVersion_ratio': np.int8,                                              
'OsBuildLab_ratio': np.int8,                                                    
'OSVersion_ratio': np.int8,                                                     
'DateAvSigVersion_fullratio': np.int8,                                          
'OsBuildLab_fullratio': np.int8,                                                
'OsBuildLab_dayOfWeek': np.int8,                                                
'AvSigVersion_dayOfWeek': np.int8,                                              
'prediction_2': np.int8,                                                        
'prediction_4': np.int8,                                                        
'prediction_8': np.int8,                                                        
'prediction_16': np.int8,                                                       
'prediction_32': np.int8,                                                       
'prediction_64': np.int8
}

cols = train.columns
cols.remove('MachineIdentifier')
for i in dict_finished:
	print(i)
	cols.remove(i)

cols.remove('Census_DeviceFamily_Windows.Server')
cols.remove('Census_DeviceFamily_Windows.Desktop')

print('{} columnas a procesar'.format(len(cols)))

for c in cols:
    maximo = train.select(c).agg(max(col(c))).collect()[0][0]
    if maximo > 2**7:
            if maximo > 2**15:
                    print("'{}': np.int32,".format(c))
            else:
                    print("'{}': np.int16,".format(c))
    else:
            print("'{}': np.int8,".format(c))



