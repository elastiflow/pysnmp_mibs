# SNMP MIB module (DIGI-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-SMI.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:31 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DigiEnterprise_ObjectIdentity = ObjectIdentity
digiEnterprise = _DigiEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332)
)
_DigiCommon_ObjectIdentity = ObjectIdentity
digiCommon = _DigiCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10)
)
_DigiProtocols_ObjectIdentity = ObjectIdentity
digiProtocols = _DigiProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11)
)
_DigiModbus_ObjectIdentity = ObjectIdentity
digiModbus = _DigiModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 11)
)
_DigiIA_ObjectIdentity = ObjectIdentity
digiIA = _DigiIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12)
)
_DigiUdpSerial_ObjectIdentity = ObjectIdentity
digiUdpSerial = _DigiUdpSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13)
)
_DigiResources_ObjectIdentity = ObjectIdentity
digiResources = _DigiResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 12)
)
_DigiInterfaces_ObjectIdentity = ObjectIdentity
digiInterfaces = _DigiInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 13)
)
_DigiMei_ObjectIdentity = ObjectIdentity
digiMei = _DigiMei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 11)
)
_DigiPowerSupply_ObjectIdentity = ObjectIdentity
digiPowerSupply = _DigiPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 12)
)
_DigiWLan_ObjectIdentity = ObjectIdentity
digiWLan = _DigiWLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 13)
)
_DigiPowerMgmt_ObjectIdentity = ObjectIdentity
digiPowerMgmt = _DigiPowerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14)
)
_ConnWLan_ObjectIdentity = ObjectIdentity
connWLan = _ConnWLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 15)
)
_DigiFeatures_ObjectIdentity = ObjectIdentity
digiFeatures = _DigiFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14)
)
_DigiPortBuffering_ObjectIdentity = ObjectIdentity
digiPortBuffering = _DigiPortBuffering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 11)
)
_DigiKeywordNotify_ObjectIdentity = ObjectIdentity
digiKeywordNotify = _DigiKeywordNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 12)
)
_DigiSocketID_ObjectIdentity = ObjectIdentity
digiSocketID = _DigiSocketID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 13)
)
_DigiLoginTraps_ObjectIdentity = ObjectIdentity
digiLoginTraps = _DigiLoginTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 14)
)
_DigiSecureAccess_ObjectIdentity = ObjectIdentity
digiSecureAccess = _DigiSecureAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 15)
)
_DigiPowerManagementTraps_ObjectIdentity = ObjectIdentity
digiPowerManagementTraps = _DigiPowerManagementTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 16)
)
_DigiSerialTraps_ObjectIdentity = ObjectIdentity
digiSerialTraps = _DigiSerialTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 17)
)
_DigiModemTestTraps_ObjectIdentity = ObjectIdentity
digiModemTestTraps = _DigiModemTestTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 18)
)
_DigiSerialAlarmTraps_ObjectIdentity = ObjectIdentity
digiSerialAlarmTraps = _DigiSerialAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 19)
)
_DigiActiveDetectionTraps_ObjectIdentity = ObjectIdentity
digiActiveDetectionTraps = _DigiActiveDetectionTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 20)
)
_DigiNFSTraps_ObjectIdentity = ObjectIdentity
digiNFSTraps = _DigiNFSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 21)
)
_DigiIPMINotify_ObjectIdentity = ObjectIdentity
digiIPMINotify = _DigiIPMINotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 22)
)
_DigiPowerTraps_ObjectIdentity = ObjectIdentity
digiPowerTraps = _DigiPowerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 23)
)
_DigiMobileTraps_ObjectIdentity = ObjectIdentity
digiMobileTraps = _DigiMobileTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 24)
)
_DigiWiPointWanUpTraps_ObjectIdentity = ObjectIdentity
digiWiPointWanUpTraps = _DigiWiPointWanUpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 25)
)
_DigiProducts_ObjectIdentity = ObjectIdentity
digiProducts = _DigiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11)
)
_DigiDeviceDrivers_ObjectIdentity = ObjectIdentity
digiDeviceDrivers = _DigiDeviceDrivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 1)
)
_DigiRasAdapters_ObjectIdentity = ObjectIdentity
digiRasAdapters = _DigiRasAdapters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 2)
)
_DigiDataFireRAST1E1_ObjectIdentity = ObjectIdentity
digiDataFireRAST1E1 = _DigiDataFireRAST1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 2, 1)
)
_DigiDataFireRASBRI_ObjectIdentity = ObjectIdentity
digiDataFireRASBRI = _DigiDataFireRASBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 2, 2)
)
_DigiAcceleportRAS_ObjectIdentity = ObjectIdentity
digiAcceleportRAS = _DigiAcceleportRAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 2, 3)
)
_DigiSerialAdapters_ObjectIdentity = ObjectIdentity
digiSerialAdapters = _DigiSerialAdapters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 3)
)
_DigiDigitalAdapters_ObjectIdentity = ObjectIdentity
digiDigitalAdapters = _DigiDigitalAdapters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4)
)
_DigiSyncAdapters_ObjectIdentity = ObjectIdentity
digiSyncAdapters = _DigiSyncAdapters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4, 1)
)
_DigiSync2000_ObjectIdentity = ObjectIdentity
digiSync2000 = _DigiSync2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4, 1, 1)
)
_DigiSync2000CPCI_ObjectIdentity = ObjectIdentity
digiSync2000CPCI = _DigiSync2000CPCI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4, 1, 2)
)
_DigiSync570_ObjectIdentity = ObjectIdentity
digiSync570 = _DigiSync570_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4, 1, 3)
)
_DigiISDNAdapters_ObjectIdentity = ObjectIdentity
digiISDNAdapters = _DigiISDNAdapters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4, 2)
)
_DigiDataFirePRIme_ObjectIdentity = ObjectIdentity
digiDataFirePRIme = _DigiDataFirePRIme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4, 2, 1)
)
_DigiDataFireBRI_ObjectIdentity = ObjectIdentity
digiDataFireBRI = _DigiDataFireBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 4, 2, 2)
)
_DigiTerminalServers_ObjectIdentity = ObjectIdentity
digiTerminalServers = _DigiTerminalServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5)
)
_DigiEtherlites_ObjectIdentity = ObjectIdentity
digiEtherlites = _DigiEtherlites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 1)
)
_DigiSCSIs_ObjectIdentity = ObjectIdentity
digiSCSIs = _DigiSCSIs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 2)
)
_DigiPortServers_ObjectIdentity = ObjectIdentity
digiPortServers = _DigiPortServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3)
)
_DigiPortServer_ObjectIdentity = ObjectIdentity
digiPortServer = _DigiPortServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 1)
)
_DigiPortServer2_ObjectIdentity = ObjectIdentity
digiPortServer2 = _DigiPortServer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 2)
)
_DigiPortServerTS_ObjectIdentity = ObjectIdentity
digiPortServerTS = _DigiPortServerTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 3, 3)
)
_DigiMultiModeCons_ObjectIdentity = ObjectIdentity
digiMultiModeCons = _DigiMultiModeCons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 4)
)
_DigiConnectPortLTS_ObjectIdentity = ObjectIdentity
digiConnectPortLTS = _DigiConnectPortLTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 5, 5)
)
_DigiConnect_ObjectIdentity = ObjectIdentity
digiConnect = _DigiConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 6)
)
_DigiDeviceInfo_ObjectIdentity = ObjectIdentity
digiDeviceInfo = _DigiDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 1)
)
_DigiDeviceIdent_ObjectIdentity = ObjectIdentity
digiDeviceIdent = _DigiDeviceIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 2)
)
_DigiMobileInfo_ObjectIdentity = ObjectIdentity
digiMobileInfo = _DigiMobileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3)
)
_DigiMobileStatus_ObjectIdentity = ObjectIdentity
digiMobileStatus = _DigiMobileStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 4)
)
_DigiCwmNotifications_ObjectIdentity = ObjectIdentity
digiCwmNotifications = _DigiCwmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 100)
)
_DigiCM_ObjectIdentity = ObjectIdentity
digiCM = _DigiCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 7)
)
_DigiPassport_ObjectIdentity = ObjectIdentity
digiPassport = _DigiPassport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 8)
)
_DigiWiPoint_ObjectIdentity = ObjectIdentity
digiWiPoint = _DigiWiPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 9)
)
_DigiPassportFips_ObjectIdentity = ObjectIdentity
digiPassportFips = _DigiPassportFips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 11, 10)
)
_DigiCapabilities_ObjectIdentity = ObjectIdentity
digiCapabilities = _DigiCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 12)
)
_DigiRequirements_ObjectIdentity = ObjectIdentity
digiRequirements = _DigiRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 13)
)
_DigiExperimental_ObjectIdentity = ObjectIdentity
digiExperimental = _DigiExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-SMI",
    **{"digiEnterprise": digiEnterprise,
       "digiCommon": digiCommon,
       "digiProtocols": digiProtocols,
       "digiModbus": digiModbus,
       "digiIA": digiIA,
       "digiUdpSerial": digiUdpSerial,
       "digiResources": digiResources,
       "digiInterfaces": digiInterfaces,
       "digiMei": digiMei,
       "digiPowerSupply": digiPowerSupply,
       "digiWLan": digiWLan,
       "digiPowerMgmt": digiPowerMgmt,
       "connWLan": connWLan,
       "digiFeatures": digiFeatures,
       "digiPortBuffering": digiPortBuffering,
       "digiKeywordNotify": digiKeywordNotify,
       "digiSocketID": digiSocketID,
       "digiLoginTraps": digiLoginTraps,
       "digiSecureAccess": digiSecureAccess,
       "digiPowerManagementTraps": digiPowerManagementTraps,
       "digiSerialTraps": digiSerialTraps,
       "digiModemTestTraps": digiModemTestTraps,
       "digiSerialAlarmTraps": digiSerialAlarmTraps,
       "digiActiveDetectionTraps": digiActiveDetectionTraps,
       "digiNFSTraps": digiNFSTraps,
       "digiIPMINotify": digiIPMINotify,
       "digiPowerTraps": digiPowerTraps,
       "digiMobileTraps": digiMobileTraps,
       "digiWiPointWanUpTraps": digiWiPointWanUpTraps,
       "digiProducts": digiProducts,
       "digiDeviceDrivers": digiDeviceDrivers,
       "digiRasAdapters": digiRasAdapters,
       "digiDataFireRAST1E1": digiDataFireRAST1E1,
       "digiDataFireRASBRI": digiDataFireRASBRI,
       "digiAcceleportRAS": digiAcceleportRAS,
       "digiSerialAdapters": digiSerialAdapters,
       "digiDigitalAdapters": digiDigitalAdapters,
       "digiSyncAdapters": digiSyncAdapters,
       "digiSync2000": digiSync2000,
       "digiSync2000CPCI": digiSync2000CPCI,
       "digiSync570": digiSync570,
       "digiISDNAdapters": digiISDNAdapters,
       "digiDataFirePRIme": digiDataFirePRIme,
       "digiDataFireBRI": digiDataFireBRI,
       "digiTerminalServers": digiTerminalServers,
       "digiEtherlites": digiEtherlites,
       "digiSCSIs": digiSCSIs,
       "digiPortServers": digiPortServers,
       "digiPortServer": digiPortServer,
       "digiPortServer2": digiPortServer2,
       "digiPortServerTS": digiPortServerTS,
       "digiMultiModeCons": digiMultiModeCons,
       "digiConnectPortLTS": digiConnectPortLTS,
       "digiConnect": digiConnect,
       "digiDeviceInfo": digiDeviceInfo,
       "digiDeviceIdent": digiDeviceIdent,
       "digiMobileInfo": digiMobileInfo,
       "digiMobileStatus": digiMobileStatus,
       "digiCwmNotifications": digiCwmNotifications,
       "digiCM": digiCM,
       "digiPassport": digiPassport,
       "digiWiPoint": digiWiPoint,
       "digiPassportFips": digiPassportFips,
       "digiCapabilities": digiCapabilities,
       "digiRequirements": digiRequirements,
       "digiExperimental": digiExperimental}
)
