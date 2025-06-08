# SNMP MIB module (HH3C-NMS-BASIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-NMS-BASIC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:41:14 2025
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

(hh3cMpMemberlinkDescr,
 hh3cMpMemberlinkIfIndex) = mibBuilder.importSymbols(
    "HH3C-MP-MIB",
    "hh3cMpMemberlinkDescr",
    "hh3cMpMemberlinkIfIndex")

(hh3cNMIMCExtend,) = mibBuilder.importSymbols(
    "HH3C-NMS-EXTEND-MIB",
    "hh3cNMIMCExtend")

(hh3cNM,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cNM")

(hh3cwapiASIPAddress,
 hh3cwapiASIPAddressType,
 hh3cwapiCertificateInstalled,
 hh3cwapiModeEnabled) = mibBuilder.importSymbols(
    "HH3C-WAPI-MIB",
    "hh3cwapiASIPAddress",
    "hh3cwapiASIPAddressType",
    "hh3cwapiCertificateInstalled",
    "hh3cwapiModeEnabled")

(ifAdminStatus,
 ifAlias,
 ifDescr,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifAlias",
    "ifDescr",
    "ifIndex",
    "ifOperStatus")

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
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cNMIMCBaisic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cNMIMCBaisic.setRevisions(
        ("2015-11-14 14:03",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNMResource_ObjectIdentity = ObjectIdentity
hh3cNMResource = _Hh3cNMResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1)
)
_Hh3cNMResourceObjects_ObjectIdentity = ObjectIdentity
hh3cNMResourceObjects = _Hh3cNMResourceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1)
)
_Hh3cNMDeviceID_Type = Unsigned32
_Hh3cNMDeviceID_Object = MibScalar
hh3cNMDeviceID = _Hh3cNMDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 1),
    _Hh3cNMDeviceID_Type()
)
hh3cNMDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceID.setStatus("current")
_Hh3cNMDeviceDescription_Type = DisplayString
_Hh3cNMDeviceDescription_Object = MibScalar
hh3cNMDeviceDescription = _Hh3cNMDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 2),
    _Hh3cNMDeviceDescription_Type()
)
hh3cNMDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceDescription.setStatus("current")
_Hh3cNMLastDeviceModel_Type = DisplayString
_Hh3cNMLastDeviceModel_Object = MibScalar
hh3cNMLastDeviceModel = _Hh3cNMLastDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 4),
    _Hh3cNMLastDeviceModel_Type()
)
hh3cNMLastDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLastDeviceModel.setStatus("current")
_Hh3cNMCurrentDeviceModel_Type = DisplayString
_Hh3cNMCurrentDeviceModel_Object = MibScalar
hh3cNMCurrentDeviceModel = _Hh3cNMCurrentDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 5),
    _Hh3cNMCurrentDeviceModel_Type()
)
hh3cNMCurrentDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCurrentDeviceModel.setStatus("current")
_Hh3cNMServiceType_Type = Integer32
_Hh3cNMServiceType_Object = MibScalar
hh3cNMServiceType = _Hh3cNMServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 6),
    _Hh3cNMServiceType_Type()
)
hh3cNMServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMServiceType.setStatus("current")
_Hh3cNMServiceName_Type = DisplayString
_Hh3cNMServiceName_Object = MibScalar
hh3cNMServiceName = _Hh3cNMServiceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 7),
    _Hh3cNMServiceName_Type()
)
hh3cNMServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMServiceName.setStatus("current")
_Hh3cNMErrorInformation_Type = DisplayString
_Hh3cNMErrorInformation_Object = MibScalar
hh3cNMErrorInformation = _Hh3cNMErrorInformation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 8),
    _Hh3cNMErrorInformation_Type()
)
hh3cNMErrorInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMErrorInformation.setStatus("current")
_Hh3cNMLicsIP_Type = DisplayString
_Hh3cNMLicsIP_Object = MibScalar
hh3cNMLicsIP = _Hh3cNMLicsIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 9),
    _Hh3cNMLicsIP_Type()
)
hh3cNMLicsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLicsIP.setStatus("current")
_Hh3cNMStackMemberName_Type = DisplayString
_Hh3cNMStackMemberName_Object = MibScalar
hh3cNMStackMemberName = _Hh3cNMStackMemberName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 10),
    _Hh3cNMStackMemberName_Type()
)
hh3cNMStackMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStackMemberName.setStatus("current")
_Hh3cNMStackMemberSerialNumber_Type = DisplayString
_Hh3cNMStackMemberSerialNumber_Object = MibScalar
hh3cNMStackMemberSerialNumber = _Hh3cNMStackMemberSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 11),
    _Hh3cNMStackMemberSerialNumber_Type()
)
hh3cNMStackMemberSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStackMemberSerialNumber.setStatus("current")
_Hh3cNMStackMemberParentEntityID_Type = Integer32
_Hh3cNMStackMemberParentEntityID_Object = MibScalar
hh3cNMStackMemberParentEntityID = _Hh3cNMStackMemberParentEntityID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 12),
    _Hh3cNMStackMemberParentEntityID_Type()
)
hh3cNMStackMemberParentEntityID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStackMemberParentEntityID.setStatus("current")
_Hh3cNMStackMemberParentRelPosition_Type = Integer32
_Hh3cNMStackMemberParentRelPosition_Object = MibScalar
hh3cNMStackMemberParentRelPosition = _Hh3cNMStackMemberParentRelPosition_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 13),
    _Hh3cNMStackMemberParentRelPosition_Type()
)
hh3cNMStackMemberParentRelPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStackMemberParentRelPosition.setStatus("current")
_Hh3cNMLicsPort_Type = DisplayString
_Hh3cNMLicsPort_Object = MibScalar
hh3cNMLicsPort = _Hh3cNMLicsPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 14),
    _Hh3cNMLicsPort_Type()
)
hh3cNMLicsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLicsPort.setStatus("current")
_Hh3cNMDescription_Type = DisplayString
_Hh3cNMDescription_Object = MibScalar
hh3cNMDescription = _Hh3cNMDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 15),
    _Hh3cNMDescription_Type()
)
hh3cNMDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDescription.setStatus("current")
_Hh3cNMOtherDeviceIP_Type = DisplayString
_Hh3cNMOtherDeviceIP_Object = MibScalar
hh3cNMOtherDeviceIP = _Hh3cNMOtherDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 16),
    _Hh3cNMOtherDeviceIP_Type()
)
hh3cNMOtherDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMOtherDeviceIP.setStatus("current")
_Hh3cNMDuplicatedDeviceList_Type = DisplayString
_Hh3cNMDuplicatedDeviceList_Object = MibScalar
hh3cNMDuplicatedDeviceList = _Hh3cNMDuplicatedDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 1, 17),
    _Hh3cNMDuplicatedDeviceList_Type()
)
hh3cNMDuplicatedDeviceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDuplicatedDeviceList.setStatus("current")
_Hh3cNMResourceTraps_ObjectIdentity = ObjectIdentity
hh3cNMResourceTraps = _Hh3cNMResourceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2)
)
_Hh3cNMResourceTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMResourceTrapsPrefix = _Hh3cNMResourceTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0)
)
_Hh3cNMPerformance_ObjectIdentity = ObjectIdentity
hh3cNMPerformance = _Hh3cNMPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2)
)
_Hh3cNMPerformanceObjects_ObjectIdentity = ObjectIdentity
hh3cNMPerformanceObjects = _Hh3cNMPerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1)
)
_Hh3cNMPerfDeviceID_Type = Unsigned32
_Hh3cNMPerfDeviceID_Object = MibScalar
hh3cNMPerfDeviceID = _Hh3cNMPerfDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 1),
    _Hh3cNMPerfDeviceID_Type()
)
hh3cNMPerfDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMPerfDeviceID.setStatus("current")
_Hh3cNMTaskID_Type = Integer32
_Hh3cNMTaskID_Object = MibScalar
hh3cNMTaskID = _Hh3cNMTaskID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 2),
    _Hh3cNMTaskID_Type()
)
hh3cNMTaskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTaskID.setStatus("current")
_Hh3cNMTaskName_Type = DisplayString
_Hh3cNMTaskName_Object = MibScalar
hh3cNMTaskName = _Hh3cNMTaskName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 3),
    _Hh3cNMTaskName_Type()
)
hh3cNMTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTaskName.setStatus("current")
_Hh3cNMTemplateName_Type = DisplayString
_Hh3cNMTemplateName_Object = MibScalar
hh3cNMTemplateName = _Hh3cNMTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 4),
    _Hh3cNMTemplateName_Type()
)
hh3cNMTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTemplateName.setStatus("current")
_Hh3cNMInstanceID_Type = Integer32
_Hh3cNMInstanceID_Object = MibScalar
hh3cNMInstanceID = _Hh3cNMInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 5),
    _Hh3cNMInstanceID_Type()
)
hh3cNMInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInstanceID.setStatus("current")
_Hh3cNMInstanceOID_Type = DisplayString
_Hh3cNMInstanceOID_Object = MibScalar
hh3cNMInstanceOID = _Hh3cNMInstanceOID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 6),
    _Hh3cNMInstanceOID_Type()
)
hh3cNMInstanceOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInstanceOID.setStatus("current")
_Hh3cNMInstanceDescription_Type = DisplayString
_Hh3cNMInstanceDescription_Object = MibScalar
hh3cNMInstanceDescription = _Hh3cNMInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 7),
    _Hh3cNMInstanceDescription_Type()
)
hh3cNMInstanceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInstanceDescription.setStatus("current")
_Hh3cNMInstanceValue_Type = DisplayString
_Hh3cNMInstanceValue_Object = MibScalar
hh3cNMInstanceValue = _Hh3cNMInstanceValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 8),
    _Hh3cNMInstanceValue_Type()
)
hh3cNMInstanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInstanceValue.setStatus("current")
_Hh3cNMThresholdValue_Type = DisplayString
_Hh3cNMThresholdValue_Object = MibScalar
hh3cNMThresholdValue = _Hh3cNMThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 9),
    _Hh3cNMThresholdValue_Type()
)
hh3cNMThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMThresholdValue.setStatus("current")
_Hh3cNMAlarmLevel_Type = Integer32
_Hh3cNMAlarmLevel_Object = MibScalar
hh3cNMAlarmLevel = _Hh3cNMAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 10),
    _Hh3cNMAlarmLevel_Type()
)
hh3cNMAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAlarmLevel.setStatus("current")
_Hh3cNMInterfaceIndex_Type = DisplayString
_Hh3cNMInterfaceIndex_Object = MibScalar
hh3cNMInterfaceIndex = _Hh3cNMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 11),
    _Hh3cNMInterfaceIndex_Type()
)
hh3cNMInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInterfaceIndex.setStatus("current")
_Hh3cNMComponentPerformanceTask_Type = DisplayString
_Hh3cNMComponentPerformanceTask_Object = MibScalar
hh3cNMComponentPerformanceTask = _Hh3cNMComponentPerformanceTask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 1, 12),
    _Hh3cNMComponentPerformanceTask_Type()
)
hh3cNMComponentPerformanceTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMComponentPerformanceTask.setStatus("current")
_Hh3cNMPerformanceTraps_ObjectIdentity = ObjectIdentity
hh3cNMPerformanceTraps = _Hh3cNMPerformanceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 2)
)
_Hh3cNMPerformanceTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMPerformanceTrapsPrefix = _Hh3cNMPerformanceTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 2, 0)
)
_Hh3cNMDeviceConfigfileManagement_ObjectIdentity = ObjectIdentity
hh3cNMDeviceConfigfileManagement = _Hh3cNMDeviceConfigfileManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3)
)
_Hh3cNMDeviceConfigfileManagementObjects_ObjectIdentity = ObjectIdentity
hh3cNMDeviceConfigfileManagementObjects = _Hh3cNMDeviceConfigfileManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1)
)
_Hh3cNMLastBackupTime_Type = DateAndTime
_Hh3cNMLastBackupTime_Object = MibScalar
hh3cNMLastBackupTime = _Hh3cNMLastBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 2),
    _Hh3cNMLastBackupTime_Type()
)
hh3cNMLastBackupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLastBackupTime.setStatus("current")
_Hh3cNMCurrentBackupTime_Type = DateAndTime
_Hh3cNMCurrentBackupTime_Object = MibScalar
hh3cNMCurrentBackupTime = _Hh3cNMCurrentBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 3),
    _Hh3cNMCurrentBackupTime_Type()
)
hh3cNMCurrentBackupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCurrentBackupTime.setStatus("current")
_Hh3cNMCheckTaskName_Type = DisplayString
_Hh3cNMCheckTaskName_Object = MibScalar
hh3cNMCheckTaskName = _Hh3cNMCheckTaskName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 4),
    _Hh3cNMCheckTaskName_Type()
)
hh3cNMCheckTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCheckTaskName.setStatus("current")
_Hh3cNMCurrentConfigurationFileID_Type = Unsigned32
_Hh3cNMCurrentConfigurationFileID_Object = MibScalar
hh3cNMCurrentConfigurationFileID = _Hh3cNMCurrentConfigurationFileID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 5),
    _Hh3cNMCurrentConfigurationFileID_Type()
)
hh3cNMCurrentConfigurationFileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCurrentConfigurationFileID.setStatus("current")
_Hh3cNMBaselineConfigurationFileID_Type = Unsigned32
_Hh3cNMBaselineConfigurationFileID_Object = MibScalar
hh3cNMBaselineConfigurationFileID = _Hh3cNMBaselineConfigurationFileID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 6),
    _Hh3cNMBaselineConfigurationFileID_Type()
)
hh3cNMBaselineConfigurationFileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMBaselineConfigurationFileID.setStatus("current")
_Hh3cNMCurrentConfigurationFileName_Type = DisplayString
_Hh3cNMCurrentConfigurationFileName_Object = MibScalar
hh3cNMCurrentConfigurationFileName = _Hh3cNMCurrentConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 7),
    _Hh3cNMCurrentConfigurationFileName_Type()
)
hh3cNMCurrentConfigurationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCurrentConfigurationFileName.setStatus("current")
_Hh3cNMBaselineConfigurationFileName_Type = DisplayString
_Hh3cNMBaselineConfigurationFileName_Object = MibScalar
hh3cNMBaselineConfigurationFileName = _Hh3cNMBaselineConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 8),
    _Hh3cNMBaselineConfigurationFileName_Type()
)
hh3cNMBaselineConfigurationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMBaselineConfigurationFileName.setStatus("current")
_Hh3cNMLastConfigurationFileID_Type = DisplayString
_Hh3cNMLastConfigurationFileID_Object = MibScalar
hh3cNMLastConfigurationFileID = _Hh3cNMLastConfigurationFileID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 9),
    _Hh3cNMLastConfigurationFileID_Type()
)
hh3cNMLastConfigurationFileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLastConfigurationFileID.setStatus("current")
_Hh3cNMLastConfigurationFileName_Type = DisplayString
_Hh3cNMLastConfigurationFileName_Object = MibScalar
hh3cNMLastConfigurationFileName = _Hh3cNMLastConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 1, 10),
    _Hh3cNMLastConfigurationFileName_Type()
)
hh3cNMLastConfigurationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLastConfigurationFileName.setStatus("current")
_Hh3cNMDeviceConfigfileManagementTraps_ObjectIdentity = ObjectIdentity
hh3cNMDeviceConfigfileManagementTraps = _Hh3cNMDeviceConfigfileManagementTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2)
)
_Hh3cNMDeviceConfigfileManagementTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMDeviceConfigfileManagementTrapsPrefix = _Hh3cNMDeviceConfigfileManagementTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2, 0)
)
_Hh3cNMIPSMonitor_ObjectIdentity = ObjectIdentity
hh3cNMIPSMonitor = _Hh3cNMIPSMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4)
)
_Hh3cNMIPSMonitorObjects_ObjectIdentity = ObjectIdentity
hh3cNMIPSMonitorObjects = _Hh3cNMIPSMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 1)
)
_Hh3cNMIPSAlarmLevel_Type = Integer32
_Hh3cNMIPSAlarmLevel_Object = MibScalar
hh3cNMIPSAlarmLevel = _Hh3cNMIPSAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 1, 1),
    _Hh3cNMIPSAlarmLevel_Type()
)
hh3cNMIPSAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIPSAlarmLevel.setStatus("current")
_Hh3cNMIPSAlarmPeriod_Type = Integer32
_Hh3cNMIPSAlarmPeriod_Object = MibScalar
hh3cNMIPSAlarmPeriod = _Hh3cNMIPSAlarmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 1, 2),
    _Hh3cNMIPSAlarmPeriod_Type()
)
hh3cNMIPSAlarmPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIPSAlarmPeriod.setStatus("current")
_Hh3cNMIPSAlarmCount_Type = Integer32
_Hh3cNMIPSAlarmCount_Object = MibScalar
hh3cNMIPSAlarmCount = _Hh3cNMIPSAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 1, 3),
    _Hh3cNMIPSAlarmCount_Type()
)
hh3cNMIPSAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIPSAlarmCount.setStatus("current")
_Hh3cNMIPSAttackTypeInformation_Type = Unsigned32
_Hh3cNMIPSAttackTypeInformation_Object = MibScalar
hh3cNMIPSAttackTypeInformation = _Hh3cNMIPSAttackTypeInformation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 1, 4),
    _Hh3cNMIPSAttackTypeInformation_Type()
)
hh3cNMIPSAttackTypeInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIPSAttackTypeInformation.setStatus("current")
_Hh3cNMIPSAttackOriginationInformation_Type = Unsigned32
_Hh3cNMIPSAttackOriginationInformation_Object = MibScalar
hh3cNMIPSAttackOriginationInformation = _Hh3cNMIPSAttackOriginationInformation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 1, 5),
    _Hh3cNMIPSAttackOriginationInformation_Type()
)
hh3cNMIPSAttackOriginationInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIPSAttackOriginationInformation.setStatus("current")
_Hh3cNMIPSAttackDestinationInformation_Type = Unsigned32
_Hh3cNMIPSAttackDestinationInformation_Object = MibScalar
hh3cNMIPSAttackDestinationInformation = _Hh3cNMIPSAttackDestinationInformation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 1, 6),
    _Hh3cNMIPSAttackDestinationInformation_Type()
)
hh3cNMIPSAttackDestinationInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIPSAttackDestinationInformation.setStatus("current")
_Hh3cNMIPSMonitorTraps_ObjectIdentity = ObjectIdentity
hh3cNMIPSMonitorTraps = _Hh3cNMIPSMonitorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 2)
)
_Hh3cNMIPSMonitorTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMIPSMonitorTrapsPrefix = _Hh3cNMIPSMonitorTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 2, 0)
)
_Hh3cNMSysmonitor_ObjectIdentity = ObjectIdentity
hh3cNMSysmonitor = _Hh3cNMSysmonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5)
)
_Hh3cNMSysmonitorObjects_ObjectIdentity = ObjectIdentity
hh3cNMSysmonitorObjects = _Hh3cNMSysmonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1)
)
_Hh3cNMSystemMonitorDiskName_Type = DisplayString
_Hh3cNMSystemMonitorDiskName_Object = MibScalar
hh3cNMSystemMonitorDiskName = _Hh3cNMSystemMonitorDiskName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 1),
    _Hh3cNMSystemMonitorDiskName_Type()
)
hh3cNMSystemMonitorDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorDiskName.setStatus("current")
_Hh3cNMSystemMonitorDiskCurrentUsage_Type = DisplayString
_Hh3cNMSystemMonitorDiskCurrentUsage_Object = MibScalar
hh3cNMSystemMonitorDiskCurrentUsage = _Hh3cNMSystemMonitorDiskCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 2),
    _Hh3cNMSystemMonitorDiskCurrentUsage_Type()
)
hh3cNMSystemMonitorDiskCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorDiskCurrentUsage.setStatus("current")
_Hh3cNMSystemMonitorDiskLimitUsage_Type = DisplayString
_Hh3cNMSystemMonitorDiskLimitUsage_Object = MibScalar
hh3cNMSystemMonitorDiskLimitUsage = _Hh3cNMSystemMonitorDiskLimitUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 3),
    _Hh3cNMSystemMonitorDiskLimitUsage_Type()
)
hh3cNMSystemMonitorDiskLimitUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorDiskLimitUsage.setStatus("current")
_Hh3cNMSystemMonitorProcessName_Type = DisplayString
_Hh3cNMSystemMonitorProcessName_Object = MibScalar
hh3cNMSystemMonitorProcessName = _Hh3cNMSystemMonitorProcessName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 4),
    _Hh3cNMSystemMonitorProcessName_Type()
)
hh3cNMSystemMonitorProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorProcessName.setStatus("current")
_Hh3cNMSystemMonitorMemoryCurrentUsage_Type = DisplayString
_Hh3cNMSystemMonitorMemoryCurrentUsage_Object = MibScalar
hh3cNMSystemMonitorMemoryCurrentUsage = _Hh3cNMSystemMonitorMemoryCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 5),
    _Hh3cNMSystemMonitorMemoryCurrentUsage_Type()
)
hh3cNMSystemMonitorMemoryCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorMemoryCurrentUsage.setStatus("current")
_Hh3cNMSystemMonitorMemoryLimitUsage_Type = DisplayString
_Hh3cNMSystemMonitorMemoryLimitUsage_Object = MibScalar
hh3cNMSystemMonitorMemoryLimitUsage = _Hh3cNMSystemMonitorMemoryLimitUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 6),
    _Hh3cNMSystemMonitorMemoryLimitUsage_Type()
)
hh3cNMSystemMonitorMemoryLimitUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorMemoryLimitUsage.setStatus("current")
_Hh3cNMSystemMonitorCPUCurrentUsage_Type = DisplayString
_Hh3cNMSystemMonitorCPUCurrentUsage_Object = MibScalar
hh3cNMSystemMonitorCPUCurrentUsage = _Hh3cNMSystemMonitorCPUCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 7),
    _Hh3cNMSystemMonitorCPUCurrentUsage_Type()
)
hh3cNMSystemMonitorCPUCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorCPUCurrentUsage.setStatus("current")
_Hh3cNMSystemMonitorCPULimitUsage_Type = DisplayString
_Hh3cNMSystemMonitorCPULimitUsage_Object = MibScalar
hh3cNMSystemMonitorCPULimitUsage = _Hh3cNMSystemMonitorCPULimitUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 8),
    _Hh3cNMSystemMonitorCPULimitUsage_Type()
)
hh3cNMSystemMonitorCPULimitUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorCPULimitUsage.setStatus("current")
_Hh3cNMDatabaseName_Type = DisplayString
_Hh3cNMDatabaseName_Object = MibScalar
hh3cNMDatabaseName = _Hh3cNMDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 9),
    _Hh3cNMDatabaseName_Type()
)
hh3cNMDatabaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDatabaseName.setStatus("current")
_Hh3cNMCurrentSize_Type = DisplayString
_Hh3cNMCurrentSize_Object = MibScalar
hh3cNMCurrentSize = _Hh3cNMCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 10),
    _Hh3cNMCurrentSize_Type()
)
hh3cNMCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCurrentSize.setStatus("current")
_Hh3cNMLimitSize_Type = DisplayString
_Hh3cNMLimitSize_Object = MibScalar
hh3cNMLimitSize = _Hh3cNMLimitSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 11),
    _Hh3cNMLimitSize_Type()
)
hh3cNMLimitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLimitSize.setStatus("current")
_Hh3cNMSystemMonitorIP_Type = DisplayString
_Hh3cNMSystemMonitorIP_Object = MibScalar
hh3cNMSystemMonitorIP = _Hh3cNMSystemMonitorIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 12),
    _Hh3cNMSystemMonitorIP_Type()
)
hh3cNMSystemMonitorIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSystemMonitorIP.setStatus("current")
_Hh3cNMReasonofDBConnectionFailed_Type = DisplayString
_Hh3cNMReasonofDBConnectionFailed_Object = MibScalar
hh3cNMReasonofDBConnectionFailed = _Hh3cNMReasonofDBConnectionFailed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 1, 13),
    _Hh3cNMReasonofDBConnectionFailed_Type()
)
hh3cNMReasonofDBConnectionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMReasonofDBConnectionFailed.setStatus("current")
_Hh3cNMSysmonitorTraps_ObjectIdentity = ObjectIdentity
hh3cNMSysmonitorTraps = _Hh3cNMSysmonitorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2)
)
_Hh3cNMSysmonitorTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMSysmonitorTrapsPrefix = _Hh3cNMSysmonitorTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0)
)
_Hh3cNMAccessPoint_ObjectIdentity = ObjectIdentity
hh3cNMAccessPoint = _Hh3cNMAccessPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6)
)
_Hh3cNMAccessPointObjects_ObjectIdentity = ObjectIdentity
hh3cNMAccessPointObjects = _Hh3cNMAccessPointObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1)
)
_Hh3cNMDeviceID1_Type = Unsigned32
_Hh3cNMDeviceID1_Object = MibScalar
hh3cNMDeviceID1 = _Hh3cNMDeviceID1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 1),
    _Hh3cNMDeviceID1_Type()
)
hh3cNMDeviceID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceID1.setStatus("current")
_Hh3cNMAPIPAddress_Type = IpAddress
_Hh3cNMAPIPAddress_Object = MibScalar
hh3cNMAPIPAddress = _Hh3cNMAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 2),
    _Hh3cNMAPIPAddress_Type()
)
hh3cNMAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAPIPAddress.setStatus("current")
_Hh3cNMAPName_Type = DisplayString
_Hh3cNMAPName_Object = MibScalar
hh3cNMAPName = _Hh3cNMAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 3),
    _Hh3cNMAPName_Type()
)
hh3cNMAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAPName.setStatus("current")
_Hh3cNMAPID_Type = OctetString
_Hh3cNMAPID_Object = MibScalar
hh3cNMAPID = _Hh3cNMAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 4),
    _Hh3cNMAPID_Type()
)
hh3cNMAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAPID.setStatus("current")
_Hh3cNMDeviceIP_Type = IpAddress
_Hh3cNMDeviceIP_Object = MibScalar
hh3cNMDeviceIP = _Hh3cNMDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 5),
    _Hh3cNMDeviceIP_Type()
)
hh3cNMDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceIP.setStatus("current")
_Hh3cNMACDeviceName_Type = DisplayString
_Hh3cNMACDeviceName_Object = MibScalar
hh3cNMACDeviceName = _Hh3cNMACDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 6),
    _Hh3cNMACDeviceName_Type()
)
hh3cNMACDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMACDeviceName.setStatus("current")
_Hh3cNMiNodeUserName_Type = DisplayString
_Hh3cNMiNodeUserName_Object = MibScalar
hh3cNMiNodeUserName = _Hh3cNMiNodeUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 7),
    _Hh3cNMiNodeUserName_Type()
)
hh3cNMiNodeUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMiNodeUserName.setStatus("current")
_Hh3cNMiNodeUserMac_Type = OctetString
_Hh3cNMiNodeUserMac_Object = MibScalar
hh3cNMiNodeUserMac = _Hh3cNMiNodeUserMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 8),
    _Hh3cNMiNodeUserMac_Type()
)
hh3cNMiNodeUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMiNodeUserMac.setStatus("current")
_Hh3cNMRegionName1_Type = DisplayString
_Hh3cNMRegionName1_Object = MibScalar
hh3cNMRegionName1 = _Hh3cNMRegionName1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 9),
    _Hh3cNMRegionName1_Type()
)
hh3cNMRegionName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMRegionName1.setStatus("current")
_Hh3cNMPerfItem_Type = Unsigned32
_Hh3cNMPerfItem_Object = MibScalar
hh3cNMPerfItem = _Hh3cNMPerfItem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 10),
    _Hh3cNMPerfItem_Type()
)
hh3cNMPerfItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMPerfItem.setStatus("current")
_Hh3cNMCurrentValue_Type = OctetString
_Hh3cNMCurrentValue_Object = MibScalar
hh3cNMCurrentValue = _Hh3cNMCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 11),
    _Hh3cNMCurrentValue_Type()
)
hh3cNMCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCurrentValue.setStatus("current")
_Hh3cNMThresholdValue1_Type = OctetString
_Hh3cNMThresholdValue1_Object = MibScalar
hh3cNMThresholdValue1 = _Hh3cNMThresholdValue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 12),
    _Hh3cNMThresholdValue1_Type()
)
hh3cNMThresholdValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMThresholdValue1.setStatus("current")
_Hh3cNMTeamIP_Type = IpAddress
_Hh3cNMTeamIP_Object = MibScalar
hh3cNMTeamIP = _Hh3cNMTeamIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 13),
    _Hh3cNMTeamIP_Type()
)
hh3cNMTeamIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTeamIP.setStatus("current")
_Hh3cNMTeamName_Type = DisplayString
_Hh3cNMTeamName_Object = MibScalar
hh3cNMTeamName = _Hh3cNMTeamName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 14),
    _Hh3cNMTeamName_Type()
)
hh3cNMTeamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTeamName.setStatus("current")
_Hh3cNMRadioID_Type = Integer32
_Hh3cNMRadioID_Object = MibScalar
hh3cNMRadioID = _Hh3cNMRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 15),
    _Hh3cNMRadioID_Type()
)
hh3cNMRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMRadioID.setStatus("current")
_Hh3cNMStationMac_Type = OctetString
_Hh3cNMStationMac_Object = MibScalar
hh3cNMStationMac = _Hh3cNMStationMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 16),
    _Hh3cNMStationMac_Type()
)
hh3cNMStationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStationMac.setStatus("current")
_Hh3cNMRegionName_Type = DisplayString
_Hh3cNMRegionName_Object = MibScalar
hh3cNMRegionName = _Hh3cNMRegionName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 17),
    _Hh3cNMRegionName_Type()
)
hh3cNMRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMRegionName.setStatus("current")
_Hh3cNMRegionType_Type = Integer32
_Hh3cNMRegionType_Object = MibScalar
hh3cNMRegionType = _Hh3cNMRegionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 18),
    _Hh3cNMRegionType_Type()
)
hh3cNMRegionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMRegionType.setStatus("current")
_Hh3cNMStationMac1_Type = OctetString
_Hh3cNMStationMac1_Object = MibScalar
hh3cNMStationMac1 = _Hh3cNMStationMac1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 19),
    _Hh3cNMStationMac1_Type()
)
hh3cNMStationMac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStationMac1.setStatus("current")
_Hh3cNMDigitalBarrierName_Type = DisplayString
_Hh3cNMDigitalBarrierName_Object = MibScalar
hh3cNMDigitalBarrierName = _Hh3cNMDigitalBarrierName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 20),
    _Hh3cNMDigitalBarrierName_Type()
)
hh3cNMDigitalBarrierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDigitalBarrierName.setStatus("current")
_Hh3cNMStayTime_Type = DisplayString
_Hh3cNMStayTime_Object = MibScalar
hh3cNMStayTime = _Hh3cNMStayTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 21),
    _Hh3cNMStayTime_Type()
)
hh3cNMStayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStayTime.setStatus("current")
_Hh3cNMStationNum_Type = DisplayString
_Hh3cNMStationNum_Object = MibScalar
hh3cNMStationNum = _Hh3cNMStationNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 1, 22),
    _Hh3cNMStationNum_Type()
)
hh3cNMStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStationNum.setStatus("current")
_Hh3cNMAccessPointTraps_ObjectIdentity = ObjectIdentity
hh3cNMAccessPointTraps = _Hh3cNMAccessPointTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2)
)
_Hh3cNMAccessPointTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMAccessPointTrapsPrefix = _Hh3cNMAccessPointTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0)
)
_Hh3cNMFaultModel_ObjectIdentity = ObjectIdentity
hh3cNMFaultModel = _Hh3cNMFaultModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2)
)
_Hh3cNMFaultModelObjects_ObjectIdentity = ObjectIdentity
hh3cNMFaultModelObjects = _Hh3cNMFaultModelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1)
)
_Hh3cNMStartTime_Type = DisplayString
_Hh3cNMStartTime_Object = MibScalar
hh3cNMStartTime = _Hh3cNMStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 1),
    _Hh3cNMStartTime_Type()
)
hh3cNMStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStartTime.setStatus("current")
_Hh3cNMStopTime_Type = DisplayString
_Hh3cNMStopTime_Object = MibScalar
hh3cNMStopTime = _Hh3cNMStopTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 2),
    _Hh3cNMStopTime_Type()
)
hh3cNMStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStopTime.setStatus("current")
_Hh3cNMTimes_Type = Unsigned32
_Hh3cNMTimes_Object = MibScalar
hh3cNMTimes = _Hh3cNMTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 3),
    _Hh3cNMTimes_Type()
)
hh3cNMTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTimes.setStatus("current")
_Hh3cNMRepeatEventName_Type = DisplayString
_Hh3cNMRepeatEventName_Object = MibScalar
hh3cNMRepeatEventName = _Hh3cNMRepeatEventName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 4),
    _Hh3cNMRepeatEventName_Type()
)
hh3cNMRepeatEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMRepeatEventName.setStatus("current")
_Hh3cNMFlashEvent_Type = DisplayString
_Hh3cNMFlashEvent_Object = MibScalar
hh3cNMFlashEvent = _Hh3cNMFlashEvent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 5),
    _Hh3cNMFlashEvent_Type()
)
hh3cNMFlashEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMFlashEvent.setStatus("current")
_Hh3cNMFlashRelativeEvent_Type = DisplayString
_Hh3cNMFlashRelativeEvent_Object = MibScalar
hh3cNMFlashRelativeEvent = _Hh3cNMFlashRelativeEvent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 6),
    _Hh3cNMFlashRelativeEvent_Type()
)
hh3cNMFlashRelativeEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMFlashRelativeEvent.setStatus("current")
_Hh3cNMDeviceIP1_Type = OctetString
_Hh3cNMDeviceIP1_Object = MibScalar
hh3cNMDeviceIP1 = _Hh3cNMDeviceIP1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 7),
    _Hh3cNMDeviceIP1_Type()
)
hh3cNMDeviceIP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceIP1.setStatus("current")
_Hh3cNMDeviceName_Type = DisplayString
_Hh3cNMDeviceName_Object = MibScalar
hh3cNMDeviceName = _Hh3cNMDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 8),
    _Hh3cNMDeviceName_Type()
)
hh3cNMDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceName.setStatus("current")
_Hh3cNMDeviceID2_Type = Unsigned32
_Hh3cNMDeviceID2_Object = MibScalar
hh3cNMDeviceID2 = _Hh3cNMDeviceID2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 9),
    _Hh3cNMDeviceID2_Type()
)
hh3cNMDeviceID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceID2.setStatus("current")
_Hh3cNMFaultOID_Type = DisplayString
_Hh3cNMFaultOID_Object = MibScalar
hh3cNMFaultOID = _Hh3cNMFaultOID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 10),
    _Hh3cNMFaultOID_Type()
)
hh3cNMFaultOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMFaultOID.setStatus("current")
_Hh3cNMPOSInfo_Type = DisplayString
_Hh3cNMPOSInfo_Object = MibScalar
hh3cNMPOSInfo = _Hh3cNMPOSInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 11),
    _Hh3cNMPOSInfo_Type()
)
hh3cNMPOSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMPOSInfo.setStatus("current")
_Hh3cNMTrapDescription_Type = DisplayString
_Hh3cNMTrapDescription_Object = MibScalar
hh3cNMTrapDescription = _Hh3cNMTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 12),
    _Hh3cNMTrapDescription_Type()
)
hh3cNMTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTrapDescription.setStatus("current")
_Hh3cNMAlarmLevel1_Type = Unsigned32
_Hh3cNMAlarmLevel1_Object = MibScalar
hh3cNMAlarmLevel1 = _Hh3cNMAlarmLevel1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 13),
    _Hh3cNMAlarmLevel1_Type()
)
hh3cNMAlarmLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAlarmLevel1.setStatus("current")
_Hh3cNMInterfaceOperationTime_Type = Integer32
_Hh3cNMInterfaceOperationTime_Object = MibScalar
hh3cNMInterfaceOperationTime = _Hh3cNMInterfaceOperationTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 14),
    _Hh3cNMInterfaceOperationTime_Type()
)
hh3cNMInterfaceOperationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInterfaceOperationTime.setStatus("current")
_Hh3cNMVarivableOID_Type = DisplayString
_Hh3cNMVarivableOID_Object = MibScalar
hh3cNMVarivableOID = _Hh3cNMVarivableOID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 15),
    _Hh3cNMVarivableOID_Type()
)
hh3cNMVarivableOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVarivableOID.setStatus("current")
_Hh3cNMVarivableValue_Type = DisplayString
_Hh3cNMVarivableValue_Object = MibScalar
hh3cNMVarivableValue = _Hh3cNMVarivableValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 16),
    _Hh3cNMVarivableValue_Type()
)
hh3cNMVarivableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVarivableValue.setStatus("current")
_Hh3cNMPollType_Type = Integer32
_Hh3cNMPollType_Object = MibScalar
hh3cNMPollType = _Hh3cNMPollType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 1, 17),
    _Hh3cNMPollType_Type()
)
hh3cNMPollType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMPollType.setStatus("current")
_Hh3cNMFaultModelTraps_ObjectIdentity = ObjectIdentity
hh3cNMFaultModelTraps = _Hh3cNMFaultModelTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2)
)
_Hh3cNMFaultModelTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMFaultModelTrapsPrefix = _Hh3cNMFaultModelTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0)
)
_Hh3cNMFaultModelTrapsEx_ObjectIdentity = ObjectIdentity
hh3cNMFaultModelTrapsEx = _Hh3cNMFaultModelTrapsEx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6)
)
_Hh3cNMFaultModelTrapsExSub5_ObjectIdentity = ObjectIdentity
hh3cNMFaultModelTrapsExSub5 = _Hh3cNMFaultModelTrapsExSub5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6, 5)
)
_Hh3cNMSerialNumber1_Type = Unsigned32
_Hh3cNMSerialNumber1_Object = MibScalar
hh3cNMSerialNumber1 = _Hh3cNMSerialNumber1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6, 5, 1),
    _Hh3cNMSerialNumber1_Type()
)
hh3cNMSerialNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSerialNumber1.setStatus("current")
_Hh3cNMFaultModelTrapsExSub19_ObjectIdentity = ObjectIdentity
hh3cNMFaultModelTrapsExSub19 = _Hh3cNMFaultModelTrapsExSub19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6, 19)
)
_Hh3cNMSerialNumber_Type = Integer32
_Hh3cNMSerialNumber_Object = MibScalar
hh3cNMSerialNumber = _Hh3cNMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6, 19, 1),
    _Hh3cNMSerialNumber_Type()
)
hh3cNMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSerialNumber.setStatus("current")
_Hh3cNMHibIP_Type = DisplayString
_Hh3cNMHibIP_Object = MibScalar
hh3cNMHibIP = _Hh3cNMHibIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6, 19, 2),
    _Hh3cNMHibIP_Type()
)
hh3cNMHibIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMHibIP.setStatus("current")
_Hh3cNMAckUser_Type = DisplayString
_Hh3cNMAckUser_Object = MibScalar
hh3cNMAckUser = _Hh3cNMAckUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6, 19, 3),
    _Hh3cNMAckUser_Type()
)
hh3cNMAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAckUser.setStatus("current")
_Hh3cNMIsAck_Type = Integer32
_Hh3cNMIsAck_Object = MibScalar
hh3cNMIsAck = _Hh3cNMIsAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 6, 19, 4),
    _Hh3cNMIsAck_Type()
)
hh3cNMIsAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIsAck.setStatus("current")
_Hh3cNMiMCNetflowFlux_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowFlux = _Hh3cNMiMCNetflowFlux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3)
)
_Hh3cNMiMCNetflowFluxObjects_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowFluxObjects = _Hh3cNMiMCNetflowFluxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1)
)
_Hh3cNMUNBAServerName_Type = DisplayString
_Hh3cNMUNBAServerName_Object = MibScalar
hh3cNMUNBAServerName = _Hh3cNMUNBAServerName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 1),
    _Hh3cNMUNBAServerName_Type()
)
hh3cNMUNBAServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMUNBAServerName.setStatus("current")
_Hh3cNMUNBAServerIP_Type = DisplayString
_Hh3cNMUNBAServerIP_Object = MibScalar
hh3cNMUNBAServerIP = _Hh3cNMUNBAServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 2),
    _Hh3cNMUNBAServerIP_Type()
)
hh3cNMUNBAServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMUNBAServerIP.setStatus("current")
_Hh3cNMDeviceName1_Type = DisplayString
_Hh3cNMDeviceName1_Object = MibScalar
hh3cNMDeviceName1 = _Hh3cNMDeviceName1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 3),
    _Hh3cNMDeviceName1_Type()
)
hh3cNMDeviceName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDeviceName1.setStatus("current")
_Hh3cNMInterfaceDescription_Type = DisplayString
_Hh3cNMInterfaceDescription_Object = MibScalar
hh3cNMInterfaceDescription = _Hh3cNMInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 4),
    _Hh3cNMInterfaceDescription_Type()
)
hh3cNMInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInterfaceDescription.setStatus("current")
_Hh3cNMIPaddress_Type = DisplayString
_Hh3cNMIPaddress_Object = MibScalar
hh3cNMIPaddress = _Hh3cNMIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 5),
    _Hh3cNMIPaddress_Type()
)
hh3cNMIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIPaddress.setStatus("current")
_Hh3cNMApplication_Type = DisplayString
_Hh3cNMApplication_Object = MibScalar
hh3cNMApplication = _Hh3cNMApplication_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 6),
    _Hh3cNMApplication_Type()
)
hh3cNMApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMApplication.setStatus("current")
_Hh3cNMCurrentInflowSpeed_Type = OctetString
_Hh3cNMCurrentInflowSpeed_Object = MibScalar
hh3cNMCurrentInflowSpeed = _Hh3cNMCurrentInflowSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 7),
    _Hh3cNMCurrentInflowSpeed_Type()
)
hh3cNMCurrentInflowSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCurrentInflowSpeed.setStatus("current")
_Hh3cNMThresholdSpeed_Type = OctetString
_Hh3cNMThresholdSpeed_Object = MibScalar
hh3cNMThresholdSpeed = _Hh3cNMThresholdSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 8),
    _Hh3cNMThresholdSpeed_Type()
)
hh3cNMThresholdSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMThresholdSpeed.setStatus("current")
_Hh3cNMAlarmSeverity_Type = Integer32
_Hh3cNMAlarmSeverity_Object = MibScalar
hh3cNMAlarmSeverity = _Hh3cNMAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 9),
    _Hh3cNMAlarmSeverity_Type()
)
hh3cNMAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAlarmSeverity.setStatus("current")
_Hh3cNMInterval_Type = Integer32
_Hh3cNMInterval_Object = MibScalar
hh3cNMInterval = _Hh3cNMInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 10),
    _Hh3cNMInterval_Type()
)
hh3cNMInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInterval.setStatus("current")
_Hh3cNMDirection_Type = DisplayString
_Hh3cNMDirection_Object = MibScalar
hh3cNMDirection = _Hh3cNMDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 11),
    _Hh3cNMDirection_Type()
)
hh3cNMDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDirection.setStatus("current")
_Hh3cNMThresholdType_Type = Integer32
_Hh3cNMThresholdType_Object = MibScalar
hh3cNMThresholdType = _Hh3cNMThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 12),
    _Hh3cNMThresholdType_Type()
)
hh3cNMThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMThresholdType.setStatus("current")
_Hh3cNMStartTime1_Type = OctetString
_Hh3cNMStartTime1_Object = MibScalar
hh3cNMStartTime1 = _Hh3cNMStartTime1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 13),
    _Hh3cNMStartTime1_Type()
)
hh3cNMStartTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMStartTime1.setStatus("current")
_Hh3cNMEndTime_Type = OctetString
_Hh3cNMEndTime_Object = MibScalar
hh3cNMEndTime = _Hh3cNMEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 1, 14),
    _Hh3cNMEndTime_Type()
)
hh3cNMEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMEndTime.setStatus("current")
_Hh3cNMiMCNetflowFluxTraps_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowFluxTraps = _Hh3cNMiMCNetflowFluxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2)
)
_Hh3cNMiMCNetflowFluxTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowFluxTrapsPrefix = _Hh3cNMiMCNetflowFluxTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0)
)
_Hh3cNMiMCNetflowMonitor_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowMonitor = _Hh3cNMiMCNetflowMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4)
)
_Hh3cNMiMCNetflowMonitorObjects_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowMonitorObjects = _Hh3cNMiMCNetflowMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 1)
)
_Hh3cNMUNBAServerName1_Type = DisplayString
_Hh3cNMUNBAServerName1_Object = MibScalar
hh3cNMUNBAServerName1 = _Hh3cNMUNBAServerName1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 1, 1),
    _Hh3cNMUNBAServerName1_Type()
)
hh3cNMUNBAServerName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMUNBAServerName1.setStatus("current")
_Hh3cNMUNBAServerIP1_Type = DisplayString
_Hh3cNMUNBAServerIP1_Object = MibScalar
hh3cNMUNBAServerIP1 = _Hh3cNMUNBAServerIP1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 1, 2),
    _Hh3cNMUNBAServerIP1_Type()
)
hh3cNMUNBAServerIP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMUNBAServerIP1.setStatus("current")
_Hh3cNMProbeName_Type = DisplayString
_Hh3cNMProbeName_Object = MibScalar
hh3cNMProbeName = _Hh3cNMProbeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 1, 3),
    _Hh3cNMProbeName_Type()
)
hh3cNMProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMProbeName.setStatus("current")
_Hh3cNMProbeIP_Type = DisplayString
_Hh3cNMProbeIP_Object = MibScalar
hh3cNMProbeIP = _Hh3cNMProbeIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 1, 4),
    _Hh3cNMProbeIP_Type()
)
hh3cNMProbeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMProbeIP.setStatus("current")
_Hh3cNMLogFileName_Type = DisplayString
_Hh3cNMLogFileName_Object = MibScalar
hh3cNMLogFileName = _Hh3cNMLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 1, 5),
    _Hh3cNMLogFileName_Type()
)
hh3cNMLogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLogFileName.setStatus("current")
_Hh3cNMDiskLimitUsage_Type = DisplayString
_Hh3cNMDiskLimitUsage_Object = MibScalar
hh3cNMDiskLimitUsage = _Hh3cNMDiskLimitUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 1, 6),
    _Hh3cNMDiskLimitUsage_Type()
)
hh3cNMDiskLimitUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDiskLimitUsage.setStatus("current")
_Hh3cNMiMCNetflowMonitorTraps_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowMonitorTraps = _Hh3cNMiMCNetflowMonitorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2)
)
_Hh3cNMiMCNetflowMonitorTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMiMCNetflowMonitorTrapsPrefix = _Hh3cNMiMCNetflowMonitorTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0)
)
_Hh3cNMiMCSecurePolicy_ObjectIdentity = ObjectIdentity
hh3cNMiMCSecurePolicy = _Hh3cNMiMCSecurePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5)
)
_Hh3cNMiMCSecurePolicyObjects_ObjectIdentity = ObjectIdentity
hh3cNMiMCSecurePolicyObjects = _Hh3cNMiMCSecurePolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 1)
)
_Hh3cNMAccessServiceEventSeqId_Type = OctetString
_Hh3cNMAccessServiceEventSeqId_Object = MibScalar
hh3cNMAccessServiceEventSeqId = _Hh3cNMAccessServiceEventSeqId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 1, 1),
    _Hh3cNMAccessServiceEventSeqId_Type()
)
hh3cNMAccessServiceEventSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAccessServiceEventSeqId.setStatus("current")
_Hh3cNMAccessServiceUserName_Type = DisplayString
_Hh3cNMAccessServiceUserName_Object = MibScalar
hh3cNMAccessServiceUserName = _Hh3cNMAccessServiceUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 1, 2),
    _Hh3cNMAccessServiceUserName_Type()
)
hh3cNMAccessServiceUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAccessServiceUserName.setStatus("current")
_Hh3cNMAccessServiceDeviceIP_Type = OctetString
_Hh3cNMAccessServiceDeviceIP_Object = MibScalar
hh3cNMAccessServiceDeviceIP = _Hh3cNMAccessServiceDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 1, 3),
    _Hh3cNMAccessServiceDeviceIP_Type()
)
hh3cNMAccessServiceDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAccessServiceDeviceIP.setStatus("current")
_Hh3cNMAccessServiceTerminalIP_Type = OctetString
_Hh3cNMAccessServiceTerminalIP_Object = MibScalar
hh3cNMAccessServiceTerminalIP = _Hh3cNMAccessServiceTerminalIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 1, 4),
    _Hh3cNMAccessServiceTerminalIP_Type()
)
hh3cNMAccessServiceTerminalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAccessServiceTerminalIP.setStatus("current")
_Hh3cNMAccessServiceTerminalMacAddress_Type = OctetString
_Hh3cNMAccessServiceTerminalMacAddress_Object = MibScalar
hh3cNMAccessServiceTerminalMacAddress = _Hh3cNMAccessServiceTerminalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 1, 5),
    _Hh3cNMAccessServiceTerminalMacAddress_Type()
)
hh3cNMAccessServiceTerminalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAccessServiceTerminalMacAddress.setStatus("current")
_Hh3cNMAccessServiceTrapInfo_Type = DisplayString
_Hh3cNMAccessServiceTrapInfo_Object = MibScalar
hh3cNMAccessServiceTrapInfo = _Hh3cNMAccessServiceTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 1, 6),
    _Hh3cNMAccessServiceTrapInfo_Type()
)
hh3cNMAccessServiceTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAccessServiceTrapInfo.setStatus("current")
_Hh3cNMiMCSecurePolicyTraps_ObjectIdentity = ObjectIdentity
hh3cNMiMCSecurePolicyTraps = _Hh3cNMiMCSecurePolicyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 2)
)
_Hh3cNMiMCSecurePolicyTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMiMCSecurePolicyTrapsPrefix = _Hh3cNMiMCSecurePolicyTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 2, 0)
)
_Hh3cNMiMCSyslog_ObjectIdentity = ObjectIdentity
hh3cNMiMCSyslog = _Hh3cNMiMCSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8)
)
_Hh3cNMiMCSyslogObjects_ObjectIdentity = ObjectIdentity
hh3cNMiMCSyslogObjects = _Hh3cNMiMCSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1)
)
_Hh3cNMh3cyslogType_Type = OctetString
_Hh3cNMh3cyslogType_Object = MibScalar
hh3cNMh3cyslogType = _Hh3cNMh3cyslogType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 1),
    _Hh3cNMh3cyslogType_Type()
)
hh3cNMh3cyslogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogType.setStatus("current")
_Hh3cNMh3cyslogTrapDesc_Type = OctetString
_Hh3cNMh3cyslogTrapDesc_Object = MibScalar
hh3cNMh3cyslogTrapDesc = _Hh3cNMh3cyslogTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 2),
    _Hh3cNMh3cyslogTrapDesc_Type()
)
hh3cNMh3cyslogTrapDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogTrapDesc.setStatus("current")
_Hh3cNMh3cyslogDateTime_Type = OctetString
_Hh3cNMh3cyslogDateTime_Object = MibScalar
hh3cNMh3cyslogDateTime = _Hh3cNMh3cyslogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 3),
    _Hh3cNMh3cyslogDateTime_Type()
)
hh3cNMh3cyslogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogDateTime.setStatus("current")
_Hh3cNMh3cyslogDevIP_Type = OctetString
_Hh3cNMh3cyslogDevIP_Object = MibScalar
hh3cNMh3cyslogDevIP = _Hh3cNMh3cyslogDevIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 4),
    _Hh3cNMh3cyslogDevIP_Type()
)
hh3cNMh3cyslogDevIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogDevIP.setStatus("current")
_Hh3cNMh3cyslogDuplicateIP_Type = OctetString
_Hh3cNMh3cyslogDuplicateIP_Object = MibScalar
hh3cNMh3cyslogDuplicateIP = _Hh3cNMh3cyslogDuplicateIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 5),
    _Hh3cNMh3cyslogDuplicateIP_Type()
)
hh3cNMh3cyslogDuplicateIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogDuplicateIP.setStatus("current")
_Hh3cNMh3cyslogVlanID_Type = OctetString
_Hh3cNMh3cyslogVlanID_Object = MibScalar
hh3cNMh3cyslogVlanID = _Hh3cNMh3cyslogVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 6),
    _Hh3cNMh3cyslogVlanID_Type()
)
hh3cNMh3cyslogVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogVlanID.setStatus("current")
_Hh3cNMh3cyslogIfdesc_Type = OctetString
_Hh3cNMh3cyslogIfdesc_Object = MibScalar
hh3cNMh3cyslogIfdesc = _Hh3cNMh3cyslogIfdesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 7),
    _Hh3cNMh3cyslogIfdesc_Type()
)
hh3cNMh3cyslogIfdesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogIfdesc.setStatus("current")
_Hh3cNMh3cyslogUserName_Type = OctetString
_Hh3cNMh3cyslogUserName_Object = MibScalar
hh3cNMh3cyslogUserName = _Hh3cNMh3cyslogUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 8),
    _Hh3cNMh3cyslogUserName_Type()
)
hh3cNMh3cyslogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogUserName.setStatus("current")
_Hh3cNMh3cyslogSourceIP_Type = OctetString
_Hh3cNMh3cyslogSourceIP_Object = MibScalar
hh3cNMh3cyslogSourceIP = _Hh3cNMh3cyslogSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 9),
    _Hh3cNMh3cyslogSourceIP_Type()
)
hh3cNMh3cyslogSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogSourceIP.setStatus("current")
_Hh3cNMh3cyslogSourceMac_Type = OctetString
_Hh3cNMh3cyslogSourceMac_Object = MibScalar
hh3cNMh3cyslogSourceMac = _Hh3cNMh3cyslogSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 10),
    _Hh3cNMh3cyslogSourceMac_Type()
)
hh3cNMh3cyslogSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogSourceMac.setStatus("current")
_Hh3cNMh3cyslogPacketRate_Type = OctetString
_Hh3cNMh3cyslogPacketRate_Object = MibScalar
hh3cNMh3cyslogPacketRate = _Hh3cNMh3cyslogPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 12),
    _Hh3cNMh3cyslogPacketRate_Type()
)
hh3cNMh3cyslogPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogPacketRate.setStatus("current")
_Hh3cNMh3cyslogPeerMac_Type = OctetString
_Hh3cNMh3cyslogPeerMac_Object = MibScalar
hh3cNMh3cyslogPeerMac = _Hh3cNMh3cyslogPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 13),
    _Hh3cNMh3cyslogPeerMac_Type()
)
hh3cNMh3cyslogPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMh3cyslogPeerMac.setStatus("current")
_Hh3cNMRuleName_Type = DisplayString
_Hh3cNMRuleName_Object = MibScalar
hh3cNMRuleName = _Hh3cNMRuleName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 20),
    _Hh3cNMRuleName_Type()
)
hh3cNMRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMRuleName.setStatus("current")
_Hh3cNMDescription1_Type = DisplayString
_Hh3cNMDescription1_Object = MibScalar
hh3cNMDescription1 = _Hh3cNMDescription1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 21),
    _Hh3cNMDescription1_Type()
)
hh3cNMDescription1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDescription1.setStatus("current")
_Hh3cNMSyslogFacility_Type = DisplayString
_Hh3cNMSyslogFacility_Object = MibScalar
hh3cNMSyslogFacility = _Hh3cNMSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 22),
    _Hh3cNMSyslogFacility_Type()
)
hh3cNMSyslogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSyslogFacility.setStatus("current")
_Hh3cNMSyslogSeverity_Type = DisplayString
_Hh3cNMSyslogSeverity_Object = MibScalar
hh3cNMSyslogSeverity = _Hh3cNMSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 23),
    _Hh3cNMSyslogSeverity_Type()
)
hh3cNMSyslogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSyslogSeverity.setStatus("current")
_Hh3cNMParameterList_Type = DisplayString
_Hh3cNMParameterList_Object = MibScalar
hh3cNMParameterList = _Hh3cNMParameterList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 24),
    _Hh3cNMParameterList_Type()
)
hh3cNMParameterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMParameterList.setStatus("current")
_Hh3cNMTime_Type = DisplayString
_Hh3cNMTime_Object = MibScalar
hh3cNMTime = _Hh3cNMTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 25),
    _Hh3cNMTime_Type()
)
hh3cNMTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTime.setStatus("current")
_Hh3cNMReason_Type = DisplayString
_Hh3cNMReason_Object = MibScalar
hh3cNMReason = _Hh3cNMReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 26),
    _Hh3cNMReason_Type()
)
hh3cNMReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMReason.setStatus("current")
_Hh3cNMSourceIP_Type = DisplayString
_Hh3cNMSourceIP_Object = MibScalar
hh3cNMSourceIP = _Hh3cNMSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 27),
    _Hh3cNMSourceIP_Type()
)
hh3cNMSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMSourceIP.setStatus("current")
_Hh3cNMPosInfo_Type = DisplayString
_Hh3cNMPosInfo_Object = MibScalar
hh3cNMPosInfo = _Hh3cNMPosInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 28),
    _Hh3cNMPosInfo_Type()
)
hh3cNMPosInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMPosInfo.setStatus("current")
_Hh3cNMTrapLevel_Type = DisplayString
_Hh3cNMTrapLevel_Object = MibScalar
hh3cNMTrapLevel = _Hh3cNMTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 29),
    _Hh3cNMTrapLevel_Type()
)
hh3cNMTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTrapLevel.setStatus("current")
_Hh3cNMInterfaceIndex1_Type = DisplayString
_Hh3cNMInterfaceIndex1_Object = MibScalar
hh3cNMInterfaceIndex1 = _Hh3cNMInterfaceIndex1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 30),
    _Hh3cNMInterfaceIndex1_Type()
)
hh3cNMInterfaceIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInterfaceIndex1.setStatus("current")
_Hh3cwapiModeEnabled_Type = DisplayString
_Hh3cwapiModeEnabled_Object = MibScalar
hh3cwapiModeEnabled = _Hh3cwapiModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 31),
    _Hh3cwapiModeEnabled_Type()
)
hh3cwapiModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiModeEnabled.setStatus("current")
_Hh3cwapiASIPAddressType_Type = DisplayString
_Hh3cwapiASIPAddressType_Object = MibScalar
hh3cwapiASIPAddressType = _Hh3cwapiASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 32),
    _Hh3cwapiASIPAddressType_Type()
)
hh3cwapiASIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiASIPAddressType.setStatus("current")
_Hh3cwapiASIPAddress_Type = DisplayString
_Hh3cwapiASIPAddress_Object = MibScalar
hh3cwapiASIPAddress = _Hh3cwapiASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 33),
    _Hh3cwapiASIPAddress_Type()
)
hh3cwapiASIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiASIPAddress.setStatus("current")
_Hh3cwapiCertificateInstalled_Type = DisplayString
_Hh3cwapiCertificateInstalled_Object = MibScalar
hh3cwapiCertificateInstalled = _Hh3cwapiCertificateInstalled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 34),
    _Hh3cwapiCertificateInstalled_Type()
)
hh3cwapiCertificateInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiCertificateInstalled.setStatus("current")
_Hh3cNMarchivePath_Type = DisplayString
_Hh3cNMarchivePath_Object = MibScalar
hh3cNMarchivePath = _Hh3cNMarchivePath_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 35),
    _Hh3cNMarchivePath_Type()
)
hh3cNMarchivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMarchivePath.setStatus("current")
_Hh3cNMseverity_Type = DisplayString
_Hh3cNMseverity_Object = MibScalar
hh3cNMseverity = _Hh3cNMseverity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 36),
    _Hh3cNMseverity_Type()
)
hh3cNMseverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMseverity.setStatus("current")
_Hh3cNMurl_Type = DisplayString
_Hh3cNMurl_Object = MibScalar
hh3cNMurl = _Hh3cNMurl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 37),
    _Hh3cNMurl_Type()
)
hh3cNMurl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMurl.setStatus("current")
_Hh3cNMrule_Type = DisplayString
_Hh3cNMrule_Object = MibScalar
hh3cNMrule = _Hh3cNMrule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 38),
    _Hh3cNMrule_Type()
)
hh3cNMrule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMrule.setStatus("current")
_Hh3cNMeventCategory_Type = DisplayString
_Hh3cNMeventCategory_Object = MibScalar
hh3cNMeventCategory = _Hh3cNMeventCategory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 39),
    _Hh3cNMeventCategory_Type()
)
hh3cNMeventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMeventCategory.setStatus("current")
_Hh3cNMdevice_Type = DisplayString
_Hh3cNMdevice_Object = MibScalar
hh3cNMdevice = _Hh3cNMdevice_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 40),
    _Hh3cNMdevice_Type()
)
hh3cNMdevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMdevice.setStatus("current")
_Hh3cNMservice_Type = DisplayString
_Hh3cNMservice_Object = MibScalar
hh3cNMservice = _Hh3cNMservice_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 41),
    _Hh3cNMservice_Type()
)
hh3cNMservice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMservice.setStatus("current")
_Hh3cNMsourceIp_Type = DisplayString
_Hh3cNMsourceIp_Object = MibScalar
hh3cNMsourceIp = _Hh3cNMsourceIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 42),
    _Hh3cNMsourceIp_Type()
)
hh3cNMsourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMsourceIp.setStatus("current")
_Hh3cNMsourcePort_Type = DisplayString
_Hh3cNMsourcePort_Object = MibScalar
hh3cNMsourcePort = _Hh3cNMsourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 43),
    _Hh3cNMsourcePort_Type()
)
hh3cNMsourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMsourcePort.setStatus("current")
_Hh3cNMvirus_Type = DisplayString
_Hh3cNMvirus_Object = MibScalar
hh3cNMvirus = _Hh3cNMvirus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 44),
    _Hh3cNMvirus_Type()
)
hh3cNMvirus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMvirus.setStatus("current")
_Hh3cNMdestIp_Type = DisplayString
_Hh3cNMdestIp_Object = MibScalar
hh3cNMdestIp = _Hh3cNMdestIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 45),
    _Hh3cNMdestIp_Type()
)
hh3cNMdestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMdestIp.setStatus("current")
_Hh3cNMdestPort_Type = DisplayString
_Hh3cNMdestPort_Object = MibScalar
hh3cNMdestPort = _Hh3cNMdestPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 46),
    _Hh3cNMdestPort_Type()
)
hh3cNMdestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMdestPort.setStatus("current")
_Hh3cNMvpn_Type = DisplayString
_Hh3cNMvpn_Object = MibScalar
hh3cNMvpn = _Hh3cNMvpn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 47),
    _Hh3cNMvpn_Type()
)
hh3cNMvpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMvpn.setStatus("current")
_Hh3cNMeventCode_Type = DisplayString
_Hh3cNMeventCode_Object = MibScalar
hh3cNMeventCode = _Hh3cNMeventCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 48),
    _Hh3cNMeventCode_Type()
)
hh3cNMeventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMeventCode.setStatus("current")
_Hh3cNMaction_Type = DisplayString
_Hh3cNMaction_Object = MibScalar
hh3cNMaction = _Hh3cNMaction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 49),
    _Hh3cNMaction_Type()
)
hh3cNMaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMaction.setStatus("current")
_Hh3cNMinterface_Type = DisplayString
_Hh3cNMinterface_Object = MibScalar
hh3cNMinterface = _Hh3cNMinterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 50),
    _Hh3cNMinterface_Type()
)
hh3cNMinterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMinterface.setStatus("current")
_Hh3cNMdirection_Type = DisplayString
_Hh3cNMdirection_Object = MibScalar
hh3cNMdirection = _Hh3cNMdirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 51),
    _Hh3cNMdirection_Type()
)
hh3cNMdirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMdirection.setStatus("current")
_Hh3cNMeventDesc_Type = DisplayString
_Hh3cNMeventDesc_Object = MibScalar
hh3cNMeventDesc = _Hh3cNMeventDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 1, 52),
    _Hh3cNMeventDesc_Type()
)
hh3cNMeventDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMeventDesc.setStatus("current")
_Hh3cNMiMCSyslogTraps_ObjectIdentity = ObjectIdentity
hh3cNMiMCSyslogTraps = _Hh3cNMiMCSyslogTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2)
)
_Hh3cNMiMCSyslogTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMiMCSyslogTrapsPrefix = _Hh3cNMiMCSyslogTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0)
)
_Hh3cNMiMCETL_ObjectIdentity = ObjectIdentity
hh3cNMiMCETL = _Hh3cNMiMCETL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9)
)
_Hh3cNMiMCETLObjects_ObjectIdentity = ObjectIdentity
hh3cNMiMCETLObjects = _Hh3cNMiMCETLObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 1)
)
_Hh3cNMServerIp_Type = DisplayString
_Hh3cNMServerIp_Object = MibScalar
hh3cNMServerIp = _Hh3cNMServerIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 1, 1),
    _Hh3cNMServerIp_Type()
)
hh3cNMServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMServerIp.setStatus("current")
_Hh3cNMProjectId_Type = DisplayString
_Hh3cNMProjectId_Object = MibScalar
hh3cNMProjectId = _Hh3cNMProjectId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 1, 2),
    _Hh3cNMProjectId_Type()
)
hh3cNMProjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMProjectId.setStatus("current")
_Hh3cNMDescription2_Type = DisplayString
_Hh3cNMDescription2_Object = MibScalar
hh3cNMDescription2 = _Hh3cNMDescription2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 1, 3),
    _Hh3cNMDescription2_Type()
)
hh3cNMDescription2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDescription2.setStatus("current")
_Hh3cNMiMCETLTraps_ObjectIdentity = ObjectIdentity
hh3cNMiMCETLTraps = _Hh3cNMiMCETLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 2)
)
_Hh3cNMiMCETLTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMiMCETLTrapsPrefix = _Hh3cNMiMCETLTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 2, 0)
)
_Hh3cNMiMCL2TOPO_ObjectIdentity = ObjectIdentity
hh3cNMiMCL2TOPO = _Hh3cNMiMCL2TOPO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10)
)
_Hh3cNMiMCL2TOPOObjects_ObjectIdentity = ObjectIdentity
hh3cNMiMCL2TOPOObjects = _Hh3cNMiMCL2TOPOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1)
)
_Hh3cNMAlarmDeviceIP_Type = OctetString
_Hh3cNMAlarmDeviceIP_Object = MibScalar
hh3cNMAlarmDeviceIP = _Hh3cNMAlarmDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 1),
    _Hh3cNMAlarmDeviceIP_Type()
)
hh3cNMAlarmDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAlarmDeviceIP.setStatus("current")
_Hh3cNMIllegalIP_Type = OctetString
_Hh3cNMIllegalIP_Object = MibScalar
hh3cNMIllegalIP = _Hh3cNMIllegalIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 2),
    _Hh3cNMIllegalIP_Type()
)
hh3cNMIllegalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIllegalIP.setStatus("current")
_Hh3cNMBindMAC_Type = OctetString
_Hh3cNMBindMAC_Object = MibScalar
hh3cNMBindMAC = _Hh3cNMBindMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 3),
    _Hh3cNMBindMAC_Type()
)
hh3cNMBindMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMBindMAC.setStatus("current")
_Hh3cNMConflictMAC_Type = OctetString
_Hh3cNMConflictMAC_Object = MibScalar
hh3cNMConflictMAC = _Hh3cNMConflictMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 4),
    _Hh3cNMConflictMAC_Type()
)
hh3cNMConflictMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMConflictMAC.setStatus("current")
_Hh3cNMMAC_Type = OctetString
_Hh3cNMMAC_Object = MibScalar
hh3cNMMAC = _Hh3cNMMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 5),
    _Hh3cNMMAC_Type()
)
hh3cNMMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMMAC.setStatus("current")
_Hh3cNMBindIP_Type = OctetString
_Hh3cNMBindIP_Object = MibScalar
hh3cNMBindIP = _Hh3cNMBindIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 6),
    _Hh3cNMBindIP_Type()
)
hh3cNMBindIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMBindIP.setStatus("current")
_Hh3cNMConflictIP_Type = OctetString
_Hh3cNMConflictIP_Object = MibScalar
hh3cNMConflictIP = _Hh3cNMConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 7),
    _Hh3cNMConflictIP_Type()
)
hh3cNMConflictIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMConflictIP.setStatus("current")
_Hh3cNMBindInterface_Type = DisplayString
_Hh3cNMBindInterface_Object = MibScalar
hh3cNMBindInterface = _Hh3cNMBindInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 8),
    _Hh3cNMBindInterface_Type()
)
hh3cNMBindInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMBindInterface.setStatus("current")
_Hh3cNMConflictInterface_Type = DisplayString
_Hh3cNMConflictInterface_Object = MibScalar
hh3cNMConflictInterface = _Hh3cNMConflictInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 9),
    _Hh3cNMConflictInterface_Type()
)
hh3cNMConflictInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMConflictInterface.setStatus("current")
_Hh3cNMInterface_Type = DisplayString
_Hh3cNMInterface_Object = MibScalar
hh3cNMInterface = _Hh3cNMInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 10),
    _Hh3cNMInterface_Type()
)
hh3cNMInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMInterface.setStatus("current")
_Hh3cNMAlarmTime_Type = Integer32
_Hh3cNMAlarmTime_Object = MibScalar
hh3cNMAlarmTime = _Hh3cNMAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 11),
    _Hh3cNMAlarmTime_Type()
)
hh3cNMAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMAlarmTime.setStatus("current")
_Hh3cNMPollDeviceIP_Type = Integer32
_Hh3cNMPollDeviceIP_Object = MibScalar
hh3cNMPollDeviceIP = _Hh3cNMPollDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 12),
    _Hh3cNMPollDeviceIP_Type()
)
hh3cNMPollDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMPollDeviceIP.setStatus("current")
_Hh3cNMIP_Type = Integer32
_Hh3cNMIP_Object = MibScalar
hh3cNMIP = _Hh3cNMIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 1, 13),
    _Hh3cNMIP_Type()
)
hh3cNMIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMIP.setStatus("current")
_Hh3cNMiMCL2TOPOTraps_ObjectIdentity = ObjectIdentity
hh3cNMiMCL2TOPOTraps = _Hh3cNMiMCL2TOPOTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2)
)
_Hh3cNMiMCL2TOPOTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMiMCL2TOPOTrapsPrefix = _Hh3cNMiMCL2TOPOTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0)
)
_Hh3cNMVRMfault_ObjectIdentity = ObjectIdentity
hh3cNMVRMfault = _Hh3cNMVRMfault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12)
)
_Hh3cNMVRMfaultObjects_ObjectIdentity = ObjectIdentity
hh3cNMVRMfaultObjects = _Hh3cNMVRMfaultObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 1)
)
_Hh3cNMVCenterAlarmName_Type = DisplayString
_Hh3cNMVCenterAlarmName_Object = MibScalar
hh3cNMVCenterAlarmName = _Hh3cNMVCenterAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 1, 1),
    _Hh3cNMVCenterAlarmName_Type()
)
hh3cNMVCenterAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVCenterAlarmName.setStatus("current")
_Hh3cNMVCenterAlarmDescription_Type = DisplayString
_Hh3cNMVCenterAlarmDescription_Object = MibScalar
hh3cNMVCenterAlarmDescription = _Hh3cNMVCenterAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 1, 2),
    _Hh3cNMVCenterAlarmDescription_Type()
)
hh3cNMVCenterAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVCenterAlarmDescription.setStatus("current")
_Hh3cNMVCenterAlarmKey_Type = OctetString
_Hh3cNMVCenterAlarmKey_Object = MibScalar
hh3cNMVCenterAlarmKey = _Hh3cNMVCenterAlarmKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 1, 3),
    _Hh3cNMVCenterAlarmKey_Type()
)
hh3cNMVCenterAlarmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVCenterAlarmKey.setStatus("current")
_Hh3cNMVRMDeviceID_Type = Unsigned32
_Hh3cNMVRMDeviceID_Object = MibScalar
hh3cNMVRMDeviceID = _Hh3cNMVRMDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 1, 4),
    _Hh3cNMVRMDeviceID_Type()
)
hh3cNMVRMDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVRMDeviceID.setStatus("current")
_Hh3cNMVRMDeviceType_Type = OctetString
_Hh3cNMVRMDeviceType_Object = MibScalar
hh3cNMVRMDeviceType = _Hh3cNMVRMDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 1, 5),
    _Hh3cNMVRMDeviceType_Type()
)
hh3cNMVRMDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVRMDeviceType.setStatus("current")
_Hh3cNMVRMfaultTraps_ObjectIdentity = ObjectIdentity
hh3cNMVRMfaultTraps = _Hh3cNMVRMfaultTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2)
)
_Hh3cNMVRMfaultTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMVRMfaultTrapsPrefix = _Hh3cNMVRMfaultTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0)
)
_Hh3cNMDeviceCheckTaskManagement_ObjectIdentity = ObjectIdentity
hh3cNMDeviceCheckTaskManagement = _Hh3cNMDeviceCheckTaskManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 15)
)
_Hh3cNMDeviceCheckTaskManagementObjects_ObjectIdentity = ObjectIdentity
hh3cNMDeviceCheckTaskManagementObjects = _Hh3cNMDeviceCheckTaskManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 15, 1)
)
_Hh3cNMTaskId_Type = Unsigned32
_Hh3cNMTaskId_Object = MibScalar
hh3cNMTaskId = _Hh3cNMTaskId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 15, 1, 1),
    _Hh3cNMTaskId_Type()
)
hh3cNMTaskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTaskId.setStatus("current")
_Hh3cNMTaskHistoryId_Type = Unsigned32
_Hh3cNMTaskHistoryId_Object = MibScalar
hh3cNMTaskHistoryId = _Hh3cNMTaskHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 15, 1, 2),
    _Hh3cNMTaskHistoryId_Type()
)
hh3cNMTaskHistoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMTaskHistoryId.setStatus("current")
_Hh3cNMDeviceCheckTaskManagementTraps_ObjectIdentity = ObjectIdentity
hh3cNMDeviceCheckTaskManagementTraps = _Hh3cNMDeviceCheckTaskManagementTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 15, 2)
)
_Hh3cNMDeviceCheckTaskManagementTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMDeviceCheckTaskManagementTrapsPrefix = _Hh3cNMDeviceCheckTaskManagementTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 15, 2, 0)
)
_Hh3cNMDBMAN_ObjectIdentity = ObjectIdentity
hh3cNMDBMAN = _Hh3cNMDBMAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19)
)
_Hh3cNMDBMANObjects_ObjectIdentity = ObjectIdentity
hh3cNMDBMANObjects = _Hh3cNMDBMANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 1)
)
_Hh3cNMDBMANTraps_ObjectIdentity = ObjectIdentity
hh3cNMDBMANTraps = _Hh3cNMDBMANTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2)
)
_Hh3cNMDBMANTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMDBMANTrapsPrefix = _Hh3cNMDBMANTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0)
)
_Hh3cNMDBMANTrapsEx_ObjectIdentity = ObjectIdentity
hh3cNMDBMANTrapsEx = _Hh3cNMDBMANTrapsEx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6)
)
_Hh3cNMDBMANTrapsExSub1_ObjectIdentity = ObjectIdentity
hh3cNMDBMANTrapsExSub1 = _Hh3cNMDBMANTrapsExSub1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 1)
)
_Hh3cNMFileName_Type = OctetString
_Hh3cNMFileName_Object = MibScalar
hh3cNMFileName = _Hh3cNMFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 1, 1),
    _Hh3cNMFileName_Type()
)
hh3cNMFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMFileName.setStatus("current")
_Hh3cNMServerIp1_Type = OctetString
_Hh3cNMServerIp1_Object = MibScalar
hh3cNMServerIp1 = _Hh3cNMServerIp1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 1, 2),
    _Hh3cNMServerIp1_Type()
)
hh3cNMServerIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMServerIp1.setStatus("current")
_Hh3cNMDBMANTrapsExSub3_ObjectIdentity = ObjectIdentity
hh3cNMDBMANTrapsExSub3 = _Hh3cNMDBMANTrapsExSub3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 3)
)
_Hh3cNMDBaseName_Type = OctetString
_Hh3cNMDBaseName_Object = MibScalar
hh3cNMDBaseName = _Hh3cNMDBaseName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 3, 1),
    _Hh3cNMDBaseName_Type()
)
hh3cNMDBaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDBaseName.setStatus("current")
_Hh3cNMDBMANTrapsExSub7_ObjectIdentity = ObjectIdentity
hh3cNMDBMANTrapsExSub7 = _Hh3cNMDBMANTrapsExSub7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 7)
)
_Hh3cNMFileName1_Type = OctetString
_Hh3cNMFileName1_Object = MibScalar
hh3cNMFileName1 = _Hh3cNMFileName1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 7, 1),
    _Hh3cNMFileName1_Type()
)
hh3cNMFileName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMFileName1.setStatus("current")
_Hh3cNMServerIp2_Type = OctetString
_Hh3cNMServerIp2_Object = MibScalar
hh3cNMServerIp2 = _Hh3cNMServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 7, 2),
    _Hh3cNMServerIp2_Type()
)
hh3cNMServerIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMServerIp2.setStatus("current")
_Hh3cNMDBMANTrapsExSub9_ObjectIdentity = ObjectIdentity
hh3cNMDBMANTrapsExSub9 = _Hh3cNMDBMANTrapsExSub9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 9)
)
_Hh3cNMLocalDbmanVersion_Type = OctetString
_Hh3cNMLocalDbmanVersion_Object = MibScalar
hh3cNMLocalDbmanVersion = _Hh3cNMLocalDbmanVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 9, 1),
    _Hh3cNMLocalDbmanVersion_Type()
)
hh3cNMLocalDbmanVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMLocalDbmanVersion.setStatus("current")
_Hh3cNMRemoteDbmanVersion_Type = OctetString
_Hh3cNMRemoteDbmanVersion_Object = MibScalar
hh3cNMRemoteDbmanVersion = _Hh3cNMRemoteDbmanVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 6, 9, 2),
    _Hh3cNMRemoteDbmanVersion_Type()
)
hh3cNMRemoteDbmanVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMRemoteDbmanVersion.setStatus("current")
_Hh3cNMH3CCAS_ObjectIdentity = ObjectIdentity
hh3cNMH3CCAS = _Hh3cNMH3CCAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26)
)
_Hh3cNMH3CCASObjects_ObjectIdentity = ObjectIdentity
hh3cNMH3CCASObjects = _Hh3cNMH3CCASObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1)
)
_Hh3cNMHostName_Type = OctetString
_Hh3cNMHostName_Object = MibScalar
hh3cNMHostName = _Hh3cNMHostName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 1),
    _Hh3cNMHostName_Type()
)
hh3cNMHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMHostName.setStatus("current")
_Hh3cNMHostIP_Type = OctetString
_Hh3cNMHostIP_Object = MibScalar
hh3cNMHostIP = _Hh3cNMHostIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 2),
    _Hh3cNMHostIP_Type()
)
hh3cNMHostIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMHostIP.setStatus("current")
_Hh3cNMVMName1_Type = OctetString
_Hh3cNMVMName1_Object = MibScalar
hh3cNMVMName1 = _Hh3cNMVMName1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 3),
    _Hh3cNMVMName1_Type()
)
hh3cNMVMName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVMName1.setStatus("current")
_Hh3cNMVMMAC_Type = OctetString
_Hh3cNMVMMAC_Object = MibScalar
hh3cNMVMMAC = _Hh3cNMVMMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 4),
    _Hh3cNMVMMAC_Type()
)
hh3cNMVMMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVMMAC.setStatus("current")
_Hh3cNMCPUUsage_Type = Unsigned32
_Hh3cNMCPUUsage_Object = MibScalar
hh3cNMCPUUsage = _Hh3cNMCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 5),
    _Hh3cNMCPUUsage_Type()
)
hh3cNMCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCPUUsage.setStatus("current")
_Hh3cNMCpuUsageThreshold_Type = Unsigned32
_Hh3cNMCpuUsageThreshold_Object = MibScalar
hh3cNMCpuUsageThreshold = _Hh3cNMCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 6),
    _Hh3cNMCpuUsageThreshold_Type()
)
hh3cNMCpuUsageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCpuUsageThreshold.setStatus("current")
_Hh3cNMMemUsage_Type = Unsigned32
_Hh3cNMMemUsage_Object = MibScalar
hh3cNMMemUsage = _Hh3cNMMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 7),
    _Hh3cNMMemUsage_Type()
)
hh3cNMMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMMemUsage.setStatus("current")
_Hh3cNMMemUsageThreshold_Type = Unsigned32
_Hh3cNMMemUsageThreshold_Object = MibScalar
hh3cNMMemUsageThreshold = _Hh3cNMMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 8),
    _Hh3cNMMemUsageThreshold_Type()
)
hh3cNMMemUsageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMMemUsageThreshold.setStatus("current")
_Hh3cNMDiskName_Type = Unsigned32
_Hh3cNMDiskName_Object = MibScalar
hh3cNMDiskName = _Hh3cNMDiskName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 9),
    _Hh3cNMDiskName_Type()
)
hh3cNMDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDiskName.setStatus("current")
_Hh3cNMDiskUsage_Type = Unsigned32
_Hh3cNMDiskUsage_Object = MibScalar
hh3cNMDiskUsage = _Hh3cNMDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 10),
    _Hh3cNMDiskUsage_Type()
)
hh3cNMDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDiskUsage.setStatus("current")
_Hh3cNMDiskUsageThreshold_Type = Unsigned32
_Hh3cNMDiskUsageThreshold_Object = MibScalar
hh3cNMDiskUsageThreshold = _Hh3cNMDiskUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 11),
    _Hh3cNMDiskUsageThreshold_Type()
)
hh3cNMDiskUsageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMDiskUsageThreshold.setStatus("current")
_Hh3cNMVMName_Type = OctetString
_Hh3cNMVMName_Object = MibScalar
hh3cNMVMName = _Hh3cNMVMName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 20),
    _Hh3cNMVMName_Type()
)
hh3cNMVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVMName.setStatus("current")
_Hh3cNMVMIP_Type = OctetString
_Hh3cNMVMIP_Object = MibScalar
hh3cNMVMIP = _Hh3cNMVMIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 21),
    _Hh3cNMVMIP_Type()
)
hh3cNMVMIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMVMIP.setStatus("current")
_Hh3cNMClusterName_Type = OctetString
_Hh3cNMClusterName_Object = MibScalar
hh3cNMClusterName = _Hh3cNMClusterName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 31),
    _Hh3cNMClusterName_Type()
)
hh3cNMClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMClusterName.setStatus("current")
_Hh3cNMCPUUsageThreshold_Type = OctetString
_Hh3cNMCPUUsageThreshold_Object = MibScalar
hh3cNMCPUUsageThreshold = _Hh3cNMCPUUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 1, 32),
    _Hh3cNMCPUUsageThreshold_Type()
)
hh3cNMCPUUsageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNMCPUUsageThreshold.setStatus("current")
_Hh3cNMH3CCASTraps_ObjectIdentity = ObjectIdentity
hh3cNMH3CCASTraps = _Hh3cNMH3CCASTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2)
)
_Hh3cNMH3CCASTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cNMH3CCASTrapsPrefix = _Hh3cNMH3CCASTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cNMThedevicedoesnotrespondtopollpacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 1)
)
hh3cNMThedevicedoesnotrespondtopollpacket.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceOperationTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPollType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMThedevicedoesnotrespondtopollpacket.setStatus(
        "current"
    )

hh3cNMDeviceDeniedSNMPAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 2)
)
hh3cNMDeviceDeniedSNMPAccess.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceDeniedSNMPAccess.setStatus(
        "current"
    )

hh3cNMDeviceMIBAccessException = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 3)
)
hh3cNMDeviceMIBAccessException.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMErrorInformation"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceMIBAccessException.setStatus(
        "current"
    )

hh3cNMThedevicecorrectlyrespondstopollpackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 4)
)
hh3cNMThedevicecorrectlyrespondstopollpackets.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceOperationTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPollType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMThedevicecorrectlyrespondstopollpackets.setStatus(
        "current"
    )

hh3cNMDeviceModelchanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 5)
)
hh3cNMDeviceModelchanged.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastDeviceModel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentDeviceModel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceModelchanged.setStatus(
        "current"
    )

hh3cNMDeviceServiceDOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 6)
)
hh3cNMDeviceServiceDOWN.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServiceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServiceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceServiceDOWN.setStatus(
        "current"
    )

hh3cNMDeviceServiceUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 7)
)
hh3cNMDeviceServiceUP.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServiceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServiceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceServiceUP.setStatus(
        "current"
    )

hh3cNMLinkStateDOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 8)
)
hh3cNMLinkStateDOWN.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceOperationTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMLinkStateDOWN.setStatus(
        "current"
    )

hh3cNMLinkStateUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 9)
)
hh3cNMLinkStateUP.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceOperationTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMLinkStateUP.setStatus(
        "current"
    )

hh3cNMIPAddressofDeviceInterfaceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 10)
)
hh3cNMIPAddressofDeviceInterfaceChanged.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifAlias"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMIPAddressofDeviceInterfaceChanged.setStatus(
        "current"
    )

hh3cNMDiscoverIdenticalDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 11)
)
hh3cNMDiscoverIdenticalDevice.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDuplicatedDeviceList"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDiscoverIdenticalDevice.setStatus(
        "current"
    )

hh3cNMMpgroupSubinterfaceDOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 12)
)
hh3cNMMpgroupSubinterfaceDOWN.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceOperationTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMMpgroupSubinterfaceDOWN.setStatus(
        "current"
    )

hh3cNMMpgroupSubinterfaceUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 13)
)
hh3cNMMpgroupSubinterfaceUP.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceOperationTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMMpgroupSubinterfaceUP.setStatus(
        "current"
    )

hh3cNMDeviceSNMPAccessible = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 14)
)
hh3cNMDeviceSNMPAccessible.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceSNMPAccessible.setStatus(
        "current"
    )

hh3cNMIdenticalSNMPEngineID = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 16)
)
hh3cNMIdenticalSNMPEngineID.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMOtherDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMIdenticalSNMPEngineID.setStatus(
        "current"
    )

hh3cNMStackMemberofDeviceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 17)
)
hh3cNMStackMemberofDeviceDeleted.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberSerialNumber"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberParentEntityID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberParentRelPosition"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMStackMemberofDeviceDeleted.setStatus(
        "current"
    )

hh3cNMStackMemberofDeviceAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 18)
)
hh3cNMStackMemberofDeviceAdded.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberSerialNumber"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberParentEntityID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStackMemberParentRelPosition"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMStackMemberofDeviceAdded.setStatus(
        "current"
    )

hh3cNMLicenseserverexception = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 1, 2, 0, 19)
)
hh3cNMLicenseserverexception.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMLicsIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLicsPort"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"))
)
if mibBuilder.loadTexts:
    hh3cNMLicenseserverexception.setStatus(
        "current"
    )

hh3cNMPerformanceAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 2, 0, 1)
)
hh3cNMPerformanceAlert.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPerfDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTemplateName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMComponentPerformanceTask"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMPerformanceAlert.setStatus(
        "current"
    )

hh3cNMPerformanceRecoverAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 2, 0, 2)
)
hh3cNMPerformanceRecoverAlert.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPerfDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTemplateName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMComponentPerformanceTask"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMPerformanceRecoverAlert.setStatus(
        "current"
    )

hh3cNMPerformanceAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 2, 0, 3)
)
hh3cNMPerformanceAlert1.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPerfDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTemplateName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMComponentPerformanceTask"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMPerformanceAlert1.setStatus(
        "current"
    )

hh3cNMPerformanceRecoverAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 2, 2, 0, 4)
)
hh3cNMPerformanceRecoverAlert1.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPerfDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTemplateName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInstanceValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMComponentPerformanceTask"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMPerformanceRecoverAlert1.setStatus(
        "current"
    )

hh3cNMStartupConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2, 0, 1)
)
hh3cNMStartupConfigurationChanged.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastConfigurationFileID"))
)
if mibBuilder.loadTexts:
    hh3cNMStartupConfigurationChanged.setStatus(
        "current"
    )

hh3cNMRunningConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2, 0, 2)
)
hh3cNMRunningConfigurationChanged.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastConfigurationFileID"))
)
if mibBuilder.loadTexts:
    hh3cNMRunningConfigurationChanged.setStatus(
        "current"
    )

hh3cNMGettingConfigforcheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2, 0, 3)
)
hh3cNMGettingConfigforcheck.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMGettingConfigforcheck.setStatus(
        "current"
    )

hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2, 0, 4)
)
hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMCheckTaskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask.setStatus(
        "current"
    )

hh3cNMStartupConfigurationdiffersfrombaseline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2, 0, 5)
)
hh3cNMStartupConfigurationdiffersfrombaseline.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBaselineConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBaselineConfigurationFileID"))
)
if mibBuilder.loadTexts:
    hh3cNMStartupConfigurationdiffersfrombaseline.setStatus(
        "current"
    )

hh3cNMRunningConfigurationdiffersfrombaseline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 3, 2, 0, 6)
)
hh3cNMRunningConfigurationdiffersfrombaseline.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLastBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentBackupTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBaselineConfigurationFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentConfigurationFileID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBaselineConfigurationFileID"))
)
if mibBuilder.loadTexts:
    hh3cNMRunningConfigurationdiffersfrombaseline.setStatus(
        "current"
    )

hh3cNMFrequentAlertsforIDSAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 2, 0, 1)
)
hh3cNMFrequentAlertsforIDSAttack.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmPeriod"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmCount"))
)
if mibBuilder.loadTexts:
    hh3cNMFrequentAlertsforIDSAttack.setStatus(
        "current"
    )

hh3cNMFrequentAlertsforIDSSeriousAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 2, 0, 2)
)
hh3cNMFrequentAlertsforIDSSeriousAttack.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmPeriod"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmCount"))
)
if mibBuilder.loadTexts:
    hh3cNMFrequentAlertsforIDSSeriousAttack.setStatus(
        "current"
    )

hh3cNMFrequentAlertsforIDSAttackAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 2, 0, 3)
)
hh3cNMFrequentAlertsforIDSAttackAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmCount"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAttackTypeInformation"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAttackOriginationInformation"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAttackDestinationInformation"))
)
if mibBuilder.loadTexts:
    hh3cNMFrequentAlertsforIDSAttackAlarm.setStatus(
        "current"
    )

hh3cNMFrequentAlertsforIDSSeriousAttackAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 4, 2, 0, 4)
)
hh3cNMFrequentAlertsforIDSSeriousAttackAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAlarmCount"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAttackTypeInformation"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAttackOriginationInformation"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPSAttackDestinationInformation"))
)
if mibBuilder.loadTexts:
    hh3cNMFrequentAlertsforIDSSeriousAttackAlarm.setStatus(
        "current"
    )

hh3cNMUseofDiskRatioUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0, 1)
)
hh3cNMUseofDiskRatioUP.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorDiskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorDiskCurrentUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorDiskLimitUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorIP"))
)
if mibBuilder.loadTexts:
    hh3cNMUseofDiskRatioUP.setStatus(
        "current"
    )

hh3cNMUseofDiskRatioRecoverNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0, 2)
)
hh3cNMUseofDiskRatioRecoverNormal.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorDiskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorDiskCurrentUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorIP"))
)
if mibBuilder.loadTexts:
    hh3cNMUseofDiskRatioRecoverNormal.setStatus(
        "current"
    )

hh3cNMiMCProcessCoreDOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0, 3)
)
hh3cNMiMCProcessCoreDOWN.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorProcessName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorIP"))
)
if mibBuilder.loadTexts:
    hh3cNMiMCProcessCoreDOWN.setStatus(
        "current"
    )

hh3cNMUseofMemoryRatioUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0, 4)
)
hh3cNMUseofMemoryRatioUP.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorMemoryCurrentUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorMemoryLimitUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorIP"))
)
if mibBuilder.loadTexts:
    hh3cNMUseofMemoryRatioUP.setStatus(
        "current"
    )

hh3cNMUseofCPURatioUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0, 5)
)
hh3cNMUseofCPURatioUP.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorCPUCurrentUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorCPULimitUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSystemMonitorIP"))
)
if mibBuilder.loadTexts:
    hh3cNMUseofCPURatioUP.setStatus(
        "current"
    )

hh3cNMApproachthelimitofdatabase = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0, 6)
)
hh3cNMApproachthelimitofdatabase.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDatabaseName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentSize"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLimitSize"))
)
if mibBuilder.loadTexts:
    hh3cNMApproachthelimitofdatabase.setStatus(
        "current"
    )

hh3cNMDatabaseConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 5, 2, 0, 7)
)
hh3cNMDatabaseConnectionFailure.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDatabaseName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMReasonofDBConnectionFailed"))
)
if mibBuilder.loadTexts:
    hh3cNMDatabaseConnectionFailure.setStatus(
        "current"
    )

hh3cNMAPDeviceOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 1)
)
hh3cNMAPDeviceOnline.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPIPAddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPID"))
)
if mibBuilder.loadTexts:
    hh3cNMAPDeviceOnline.setStatus(
        "current"
    )

hh3cNMAPDeviceOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 2)
)
hh3cNMAPDeviceOffline.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPIPAddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPID"))
)
if mibBuilder.loadTexts:
    hh3cNMAPDeviceOffline.setStatus(
        "current"
    )

hh3cNMiNodeClientDisobeyAccessPolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 3)
)
hh3cNMiNodeClientDisobeyAccessPolicy.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMiNodeUserName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMiNodeUserMac"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMRegionName"))
)
if mibBuilder.loadTexts:
    hh3cNMiNodeClientDisobeyAccessPolicy.setStatus(
        "current"
    )

hh3cNMAPExceedsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 4)
)
hh3cNMAPExceedsThreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMRadioID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPerfItem"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"))
)
if mibBuilder.loadTexts:
    hh3cNMAPExceedsThreshold.setStatus(
        "current"
    )

hh3cNMAPRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 5)
)
hh3cNMAPRecovery.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAPID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMRadioID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPerfItem"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentValue"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"))
)
if mibBuilder.loadTexts:
    hh3cNMAPRecovery.setStatus(
        "current"
    )

hh3cNMRemoveTeamMemberDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 6)
)
hh3cNMRemoveTeamMemberDevice.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTeamIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTeamName"))
)
if mibBuilder.loadTexts:
    hh3cNMRemoveTeamMemberDevice.setStatus(
        "current"
    )

hh3cNMCannotManageTeamMemberDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 7)
)
hh3cNMCannotManageTeamMemberDevice.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTeamIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTeamName"))
)
if mibBuilder.loadTexts:
    hh3cNMCannotManageTeamMemberDevice.setStatus(
        "current"
    )

hh3cNMStationoverarea = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 8)
)
hh3cNMStationoverarea.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStationMac"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMRegionName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMRegionType"))
)
if mibBuilder.loadTexts:
    hh3cNMStationoverarea.setStatus(
        "current"
    )

hh3cNMStaEnterDigitalBarrier = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 9)
)
hh3cNMStaEnterDigitalBarrier.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStationMac"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDigitalBarrierName"))
)
if mibBuilder.loadTexts:
    hh3cNMStaEnterDigitalBarrier.setStatus(
        "current"
    )

hh3cNMStaExitDigitalBarrier = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 10)
)
hh3cNMStaExitDigitalBarrier.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStationMac"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDigitalBarrierName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStayTime"))
)
if mibBuilder.loadTexts:
    hh3cNMStaExitDigitalBarrier.setStatus(
        "current"
    )

hh3cNMStationNumberThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 11)
)
hh3cNMStationNumberThreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStationNum"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"))
)
if mibBuilder.loadTexts:
    hh3cNMStationNumberThreshold.setStatus(
        "current"
    )

hh3cNMStationNumberThreshold1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 13)
)
hh3cNMStationNumberThreshold1.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStationNum"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"))
)
if mibBuilder.loadTexts:
    hh3cNMStationNumberThreshold1.setStatus(
        "current"
    )

hh3cNMStationNumberThreshold2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 14)
)
hh3cNMStationNumberThreshold2.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStationNum"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"))
)
if mibBuilder.loadTexts:
    hh3cNMStationNumberThreshold2.setStatus(
        "current"
    )

hh3cNMStationNumberThreshold3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 1, 6, 2, 0, 15)
)
hh3cNMStationNumberThreshold3.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStationNum"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMACDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdValue"))
)
if mibBuilder.loadTexts:
    hh3cNMStationNumberThreshold3.setStatus(
        "current"
    )

hh3cNMAlarmsystemdetectedalarmsofduplicateevent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 1)
)
hh3cNMAlarmsystemdetectedalarmsofduplicateevent.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStopTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTimes"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMRepeatEventName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMAlarmsystemdetectedalarmsofduplicateevent.setStatus(
        "current"
    )

hh3cNMAlarmsystemdetectedalarmsfromunmanageddevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 2)
)
hh3cNMAlarmsystemdetectedalarmsfromunmanageddevices.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStopTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTimes"))
)
if mibBuilder.loadTexts:
    hh3cNMAlarmsystemdetectedalarmsfromunmanageddevices.setStatus(
        "current"
    )

hh3cNMAlarmsystemdetectedalarmsofunknowntraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 3)
)
hh3cNMAlarmsystemdetectedalarmsofunknowntraps.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStopTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTimes"))
)
if mibBuilder.loadTexts:
    hh3cNMAlarmsystemdetectedalarmsofunknowntraps.setStatus(
        "current"
    )

hh3cNMAlarmsystemdetectedintermittentfailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 4)
)
hh3cNMAlarmsystemdetectedintermittentfailures.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStopTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTimes"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMFlashEvent"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMFlashRelativeEvent"))
)
if mibBuilder.loadTexts:
    hh3cNMAlarmsystemdetectedintermittentfailures.setStatus(
        "current"
    )

hh3cNMLowerLevelAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 5)
)
hh3cNMLowerLevelAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMFaultOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPOSInfo"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTrapDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSerialNumber"))
)
if mibBuilder.loadTexts:
    hh3cNMLowerLevelAlarm.setStatus(
        "current"
    )

hh3cNMLowerLevelRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 6)
)
hh3cNMLowerLevelRecovery.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMFaultOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPOSInfo"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTrapDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSerialNumber"))
)
if mibBuilder.loadTexts:
    hh3cNMLowerLevelRecovery.setStatus(
        "current"
    )

hh3cNMLowerLevelSelfRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 7)
)
hh3cNMLowerLevelSelfRecovery.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMFaultOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPOSInfo"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTrapDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSerialNumber"))
)
if mibBuilder.loadTexts:
    hh3cNMLowerLevelSelfRecovery.setStatus(
        "current"
    )

hh3cNMLowerLeveltoreportvalidationtoreport1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 8)
)
if mibBuilder.loadTexts:
    hh3cNMLowerLeveltoreportvalidationtoreport1.setStatus(
        "current"
    )

hh3cNMiMCfaultmodulealarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 9)
)
hh3cNMiMCfaultmodulealarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMiMCfaultmodulealarmgroup.setStatus(
        "current"
    )

hh3cNMNTAalarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 10)
)
hh3cNMNTAalarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMNTAalarmgroup.setStatus(
        "current"
    )

hh3cNMPerformancealarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 11)
)
hh3cNMPerformancealarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMPerformancealarmgroup.setStatus(
        "current"
    )

hh3cNMConfigurationchangealarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 12)
)
hh3cNMConfigurationchangealarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMConfigurationchangealarmgroup.setStatus(
        "current"
    )

hh3cNMIPSecalarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 13)
)
hh3cNMIPSecalarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMIPSecalarmgroup.setStatus(
        "current"
    )

hh3cNMSNMPaccesserroralarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 14)
)
hh3cNMSNMPaccesserroralarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMSNMPaccesserroralarmgroup.setStatus(
        "current"
    )

hh3cNMLowerlevelalarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 15)
)
hh3cNMLowerlevelalarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMLowerlevelalarmgroup.setStatus(
        "current"
    )

hh3cNMColdstartalarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 16)
)
hh3cNMColdstartalarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMColdstartalarmgroup.setStatus(
        "current"
    )

hh3cNMSNMPrestartalarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 17)
)
hh3cNMSNMPrestartalarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMSNMPrestartalarmgroup.setStatus(
        "current"
    )

hh3cNMUseofmemoryupalarmgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 18)
)
hh3cNMUseofmemoryupalarmgroup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableOID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVarivableValue"))
)
if mibBuilder.loadTexts:
    hh3cNMUseofmemoryupalarmgroup.setStatus(
        "current"
    )

hh3cNMLowerLeveltoreportvalidationtoreport = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 2, 2, 0, 19)
)
hh3cNMLowerLeveltoreportvalidationtoreport.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMSerialNumber"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMHibIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAckUser"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIsAck"))
)
if mibBuilder.loadTexts:
    hh3cNMLowerLeveltoreportvalidationtoreport.setStatus(
        "current"
    )

hh3cNMInterfaceflowexceededthreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 1)
)
hh3cNMInterfaceflowexceededthreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMInterfaceflowexceededthreshold.setStatus(
        "current"
    )

hh3cNMInterfaceFlowrecovers = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 2)
)
hh3cNMInterfaceFlowrecovers.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMInterfaceFlowrecovers.setStatus(
        "current"
    )

hh3cNMIPflowexceededthreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 3)
)
hh3cNMIPflowexceededthreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPaddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMIPflowexceededthreshold.setStatus(
        "current"
    )

hh3cNMIPflowrecovers = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 4)
)
hh3cNMIPflowrecovers.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPaddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMIPflowrecovers.setStatus(
        "current"
    )

hh3cNMIntfappflowexceededthreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 5)
)
hh3cNMIntfappflowexceededthreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMApplication"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMIntfappflowexceededthreshold.setStatus(
        "current"
    )

hh3cNMIntfappflowrecovers = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 6)
)
hh3cNMIntfappflowrecovers.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMApplication"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMIntfappflowrecovers.setStatus(
        "current"
    )

hh3cNMAppflowexceededthreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 7)
)
hh3cNMAppflowexceededthreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMApplication"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMAppflowexceededthreshold.setStatus(
        "current"
    )

hh3cNMAppflowrecovers = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 8)
)
hh3cNMAppflowrecovers.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMApplication"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMAppflowrecovers.setStatus(
        "current"
    )

hh3cNMIpappflowexceededthreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 9)
)
hh3cNMIpappflowexceededthreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPaddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMApplication"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMIpappflowexceededthreshold.setStatus(
        "current"
    )

hh3cNMIPappflowrecovers = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 10)
)
hh3cNMIPappflowrecovers.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIPaddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMApplication"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterval"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCurrentInflowSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMThresholdSpeed"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMStartTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMEndTime"))
)
if mibBuilder.loadTexts:
    hh3cNMIPappflowrecovers.setStatus(
        "current"
    )

hh3cNMUBALicenseDetecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 15)
)
if mibBuilder.loadTexts:
    hh3cNMUBALicenseDetecting.setStatus(
        "current"
    )

hh3cNMDataTransferFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 16)
)
if mibBuilder.loadTexts:
    hh3cNMDataTransferFailed.setStatus(
        "current"
    )

hh3cNMDataFileDeleteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 17)
)
if mibBuilder.loadTexts:
    hh3cNMDataFileDeleteFailed.setStatus(
        "current"
    )

hh3cNMNTALicenseDetecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 3, 2, 0, 18)
)
if mibBuilder.loadTexts:
    hh3cNMNTALicenseDetecting.setStatus(
        "current"
    )

hh3cNMNetFolwProbePrefix = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 1)
)
hh3cNMNetFolwProbePrefix.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMProbeName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProbeIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMLogFileName"))
)
if mibBuilder.loadTexts:
    hh3cNMNetFolwProbePrefix.setStatus(
        "current"
    )

hh3cNMLoadnewconfigonprobe = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 2)
)
hh3cNMLoadnewconfigonprobe.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMProbeName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProbeIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"))
)
if mibBuilder.loadTexts:
    hh3cNMLoadnewconfigonprobe.setStatus(
        "current"
    )

hh3cNMProbeloadingconfigfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 3)
)
hh3cNMProbeloadingconfigfailed.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMProbeName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProbeIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"))
)
if mibBuilder.loadTexts:
    hh3cNMProbeloadingconfigfailed.setStatus(
        "current"
    )

hh3cNMConnectiontoDBfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 4)
)
hh3cNMConnectiontoDBfailed.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"))
)
if mibBuilder.loadTexts:
    hh3cNMConnectiontoDBfailed.setStatus(
        "current"
    )

hh3cNMReceiverloadingnewconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 5)
)
hh3cNMReceiverloadingnewconfig.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"))
)
if mibBuilder.loadTexts:
    hh3cNMReceiverloadingnewconfig.setStatus(
        "current"
    )

hh3cNMProcessorloadingnewconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 6)
)
hh3cNMProcessorloadingnewconfig.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"))
)
if mibBuilder.loadTexts:
    hh3cNMProcessorloadingnewconfig.setStatus(
        "current"
    )

hh3cNMReceiverloadingnewconfigfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 7)
)
hh3cNMReceiverloadingnewconfigfailed.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"))
)
if mibBuilder.loadTexts:
    hh3cNMReceiverloadingnewconfigfailed.setStatus(
        "current"
    )

hh3cNMProcessorloadingconfigfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 8)
)
hh3cNMProcessorloadingconfigfailed.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"))
)
if mibBuilder.loadTexts:
    hh3cNMProcessorloadingconfigfailed.setStatus(
        "current"
    )

hh3cNMReceiverstoppedprocesslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 9)
)
hh3cNMReceiverstoppedprocesslog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMReceiverstoppedprocesslog.setStatus(
        "current"
    )

hh3cNMDiskuseexceededthreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 10)
)
hh3cNMDiskuseexceededthreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMDiskuseexceededthreshold.setStatus(
        "current"
    )

hh3cNMDiskusewillreachthreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 11)
)
hh3cNMDiskusewillreachthreshold.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMDiskusewillreachthreshold.setStatus(
        "current"
    )

hh3cNMDiskusetempenough = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 12)
)
hh3cNMDiskusetempenough.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMDiskusetempenough.setStatus(
        "current"
    )

hh3cNMProcessorstoppedprocesslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 13)
)
hh3cNMProcessorstoppedprocesslog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMProcessorstoppedprocesslog.setStatus(
        "current"
    )

hh3cNMProbestoppeddatacollection = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 14)
)
hh3cNMProbestoppeddatacollection.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMProbeName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProbeIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMProbestoppeddatacollection.setStatus(
        "current"
    )

hh3cNMReceiverresumeprocessinglog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 15)
)
hh3cNMReceiverresumeprocessinglog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMReceiverresumeprocessinglog.setStatus(
        "current"
    )

hh3cNMProcessorresumeprocessinglog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 16)
)
hh3cNMProcessorresumeprocessinglog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMProcessorresumeprocessinglog.setStatus(
        "current"
    )

hh3cNMProberesumeprocessinglog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 4, 2, 0, 17)
)
hh3cNMProberesumeprocessinglog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMProbeName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProbeIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMUNBAServerIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskLimitUsage"))
)
if mibBuilder.loadTexts:
    hh3cNMProberesumeprocessinglog.setStatus(
        "current"
    )

hh3cNMFlowMonitorUnnormalinUAM = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 2, 0, 1)
)
hh3cNMFlowMonitorUnnormalinUAM.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceEventSeqId"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceUserName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceTerminalIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceTerminalMacAddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceTrapInfo"))
)
if mibBuilder.loadTexts:
    hh3cNMFlowMonitorUnnormalinUAM.setStatus(
        "current"
    )

hh3cNMFlowMonitorSeriousinUAM = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 5, 2, 0, 2)
)
hh3cNMFlowMonitorSeriousinUAM.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceEventSeqId"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceUserName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceTerminalIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceTerminalMacAddress"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAccessServiceTrapInfo"))
)
if mibBuilder.loadTexts:
    hh3cNMFlowMonitorSeriousinUAM.setStatus(
        "current"
    )

hh3cNMARPDuplicateaddressalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 1)
)
hh3cNMARPDuplicateaddressalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDuplicateIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogSourceMac"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogPeerMac"))
)
if mibBuilder.loadTexts:
    hh3cNMARPDuplicateaddressalarm.setStatus(
        "current"
    )

hh3cNMPortSecurityLogfailalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 2)
)
hh3cNMPortSecurityLogfailalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogIfdesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogSourceMac"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogUserName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogVlanID"))
)
if mibBuilder.loadTexts:
    hh3cNMPortSecurityLogfailalarm.setStatus(
        "current"
    )

hh3cNMArpOverspeedalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 3)
)
hh3cNMArpOverspeedalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogIfdesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogPacketRate"))
)
if mibBuilder.loadTexts:
    hh3cNMArpOverspeedalarm.setStatus(
        "current"
    )

hh3cNMPortAccessRejectalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 4)
)
hh3cNMPortAccessRejectalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogIfdesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogSourceIP"))
)
if mibBuilder.loadTexts:
    hh3cNMPortAccessRejectalarm.setStatus(
        "current"
    )

hh3cNMBPDUGuardalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 5)
)
hh3cNMBPDUGuardalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogIfdesc"))
)
if mibBuilder.loadTexts:
    hh3cNMBPDUGuardalarm.setStatus(
        "current"
    )

hh3cNMLOOPGUARDalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 6)
)
hh3cNMLOOPGUARDalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogIfdesc"))
)
if mibBuilder.loadTexts:
    hh3cNMLOOPGUARDalarm.setStatus(
        "current"
    )

hh3cNMDHCPServerDetectalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 7)
)
hh3cNMDHCPServerDetectalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogIfdesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogSourceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogSourceMac"))
)
if mibBuilder.loadTexts:
    hh3cNMDHCPServerDetectalarm.setStatus(
        "current"
    )

hh3cNMPortSecurityIntrusionalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 8)
)
hh3cNMPortSecurityIntrusionalarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogTrapDesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDateTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogDevIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogIfdesc"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogSourceMac"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMh3cyslogVlanID"))
)
if mibBuilder.loadTexts:
    hh3cNMPortSecurityIntrusionalarm.setStatus(
        "current"
    )

hh3cNMAttackDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 9)
)
hh3cNMAttackDetect.setObjects(
      *(("HH3C-WAPI-MIB", "hh3cwapiModeEnabled"),
        ("HH3C-WAPI-MIB", "hh3cwapiASIPAddressType"),
        ("HH3C-WAPI-MIB", "hh3cwapiASIPAddress"),
        ("HH3C-WAPI-MIB", "hh3cwapiCertificateInstalled"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMarchivePath"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMseverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMurl"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMrule"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMeventCategory"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMdevice"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMservice"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMsourceIp"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMsourcePort"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMvirus"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMdestIp"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMdestPort"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMvpn"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMeventCode"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMaction"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMinterface"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMdirection"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMeventDesc"))
)
if mibBuilder.loadTexts:
    hh3cNMAttackDetect.setStatus(
        "current"
    )

hh3cNMTrapupgradedfromsyslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 20)
)
hh3cNMTrapupgradedfromsyslog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMRuleName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogFacility"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMParameterList"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMReason"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSourceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPosInfo"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTrapLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hh3cNMTrapupgradedfromsyslog.setStatus(
        "current"
    )

hh3cNMRecovertrapupgradedfromsyslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 21)
)
hh3cNMRecovertrapupgradedfromsyslog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMRuleName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogFacility"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMParameterList"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMReason"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSourceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPosInfo"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTrapLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hh3cNMRecovertrapupgradedfromsyslog.setStatus(
        "current"
    )

hh3cNMSCCtrapupgradedfromsyslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 22)
)
hh3cNMSCCtrapupgradedfromsyslog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMRuleName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogFacility"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMParameterList"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMReason"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSourceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPosInfo"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTrapLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hh3cNMSCCtrapupgradedfromsyslog.setStatus(
        "current"
    )

hh3cNMSCCrecovertrapupgradedfromsyslog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 8, 2, 0, 23)
)
hh3cNMSCCrecovertrapupgradedfromsyslog.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMRuleName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogFacility"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSyslogSeverity"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMParameterList"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTime"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMReason"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMSourceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMPosInfo"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTrapLevel"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterfaceIndex"))
)
if mibBuilder.loadTexts:
    hh3cNMSCCrecovertrapupgradedfromsyslog.setStatus(
        "current"
    )

hh3cNMDataAnalysisTaskExecuteFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 2, 0, 1)
)
hh3cNMDataAnalysisTaskExecuteFail.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProjectId"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"))
)
if mibBuilder.loadTexts:
    hh3cNMDataAnalysisTaskExecuteFail.setStatus(
        "current"
    )

hh3cNMDataAnalysisTaskExecuteRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 2, 0, 2)
)
hh3cNMDataAnalysisTaskExecuteRecovery.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProjectId"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"))
)
if mibBuilder.loadTexts:
    hh3cNMDataAnalysisTaskExecuteRecovery.setStatus(
        "current"
    )

hh3cNMDataAnalysisSourceTableNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 9, 2, 0, 3)
)
hh3cNMDataAnalysisSourceTableNotExist.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMProjectId"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDescription"))
)
if mibBuilder.loadTexts:
    hh3cNMDataAnalysisSourceTableNotExist.setStatus(
        "current"
    )

hh3cNMIPMACBindMACConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 1)
)
hh3cNMIPMACBindMACConflictAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPollDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBindMAC"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictMAC"))
)
if mibBuilder.loadTexts:
    hh3cNMIPMACBindMACConflictAlarm.setStatus(
        "current"
    )

hh3cNMIPMACBindIPConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 2)
)
hh3cNMIPMACBindIPConflictAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPollDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMAC"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBindIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictIP"))
)
if mibBuilder.loadTexts:
    hh3cNMIPMACBindIPConflictAlarm.setStatus(
        "current"
    )

hh3cNMMACIFBindIFConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 3)
)
hh3cNMMACIFBindIFConflictAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPollDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMAC"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBindInterface"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictInterface"))
)
if mibBuilder.loadTexts:
    hh3cNMMACIFBindIFConflictAlarm.setStatus(
        "current"
    )

hh3cNMMACIFBindMACConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 4)
)
hh3cNMMACIFBindMACConflictAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPollDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterface"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBindMAC"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictMAC"))
)
if mibBuilder.loadTexts:
    hh3cNMMACIFBindMACConflictAlarm.setStatus(
        "current"
    )

hh3cNMMACInterfaceBindingInterfaceConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 5)
)
hh3cNMMACInterfaceBindingInterfaceConflictAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMAC"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBindInterface"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictInterface"))
)
if mibBuilder.loadTexts:
    hh3cNMMACInterfaceBindingInterfaceConflictAlarm.setStatus(
        "current"
    )

hh3cNMMACInterfaceBindingMACConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 6)
)
hh3cNMMACInterfaceBindingMACConflictAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterface"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMBindMAC"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictMAC"))
)
if mibBuilder.loadTexts:
    hh3cNMMACInterfaceBindingMACConflictAlarm.setStatus(
        "current"
    )

hh3cNMIllegalMACAccessingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 7)
)
hh3cNMIllegalMACAccessingAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMPollDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterface"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictMAC"))
)
if mibBuilder.loadTexts:
    hh3cNMIllegalMACAccessingAlarm.setStatus(
        "current"
    )

hh3cNMIllegalMACAccessingAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 8)
)
hh3cNMIllegalMACAccessingAlarm1.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMInterface"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMConflictMAC"))
)
if mibBuilder.loadTexts:
    hh3cNMIllegalMACAccessingAlarm1.setStatus(
        "current"
    )

hh3cNMIllegalIPAccessingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 9)
)
hh3cNMIllegalIPAccessingAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMIllegalIP"))
)
if mibBuilder.loadTexts:
    hh3cNMIllegalIPAccessingAlarm.setStatus(
        "current"
    )

hh3cNMAggregationgroupmemberportDOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 10, 2, 0, 10)
)
hh3cNMAggregationgroupmemberportDOWN.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceID"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMAlarmTime"))
)
if mibBuilder.loadTexts:
    hh3cNMAggregationgroupmemberportDOWN.setStatus(
        "current"
    )

hh3cNMVCenterMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 1)
)
hh3cNMVCenterMajorAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmKey"))
)
if mibBuilder.loadTexts:
    hh3cNMVCenterMajorAlarm.setStatus(
        "current"
    )

hh3cNMVCenterMajorAlarmRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 2)
)
hh3cNMVCenterMajorAlarmRecovery.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmKey"))
)
if mibBuilder.loadTexts:
    hh3cNMVCenterMajorAlarmRecovery.setStatus(
        "current"
    )

hh3cNMVCenterMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 3)
)
hh3cNMVCenterMinorAlarm.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmKey"))
)
if mibBuilder.loadTexts:
    hh3cNMVCenterMinorAlarm.setStatus(
        "current"
    )

hh3cNMVCenterMinorAlarmRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 4)
)
hh3cNMVCenterMinorAlarmRecovery.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmDescription"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVCenterAlarmKey"))
)
if mibBuilder.loadTexts:
    hh3cNMVCenterMinorAlarmRecovery.setStatus(
        "current"
    )

hh3cNMDeviceRoleChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 5)
)
if mibBuilder.loadTexts:
    hh3cNMDeviceRoleChanged.setStatus(
        "current"
    )

hh3cNMHostAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 6)
)
hh3cNMHostAccessFailure.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMHostAccessFailure.setStatus(
        "current"
    )

hh3cNMHostAccessSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 7)
)
hh3cNMHostAccessSuccess.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMHostAccessSuccess.setStatus(
        "current"
    )

hh3cNMVMMAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 8)
)
hh3cNMVMMAccessFailure.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMVMMAccessFailure.setStatus(
        "current"
    )

hh3cNMVMMAccessSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 9)
)
hh3cNMVMMAccessSuccess.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMVMMAccessSuccess.setStatus(
        "current"
    )

hh3cNMVCenterAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 10)
)
hh3cNMVCenterAccessFailure.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMVCenterAccessFailure.setStatus(
        "current"
    )

hh3cNMVCenterAccessSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 11)
)
hh3cNMVCenterAccessSuccess.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceID"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVRMDeviceType"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceName"))
)
if mibBuilder.loadTexts:
    hh3cNMVCenterAccessSuccess.setStatus(
        "current"
    )

hh3cNMDuplicateHostVMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 12, 2, 0, 12)
)
hh3cNMDuplicateHostVMAlarm.setObjects(
    ("HH3C-NMS-BASIC-MIB", "hh3cNMDeviceIP")
)
if mibBuilder.loadTexts:
    hh3cNMDuplicateHostVMAlarm.setStatus(
        "current"
    )

hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 15, 2, 0, 1)
)
hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask1.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMTaskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskId"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMTaskHistoryId"))
)
if mibBuilder.loadTexts:
    hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask1.setStatus(
        "current"
    )

hh3cNMDBMANfailedtouploadthebackupfiletotheFTPserver = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 1)
)
hh3cNMDBMANfailedtouploadthebackupfiletotheFTPserver.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtouploadthebackupfiletotheFTPserver.setStatus(
        "current"
    )

hh3cNMDBMANfailedtotransmitafilefromtheprimarytothebackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 2)
)
hh3cNMDBMANfailedtotransmitafilefromtheprimarytothebackup.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtotransmitafilefromtheprimarytothebackup.setStatus(
        "current"
    )

hh3cNMDBMANfailedtobackupthedatabase = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 3)
)
hh3cNMDBMANfailedtobackupthedatabase.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDBaseName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtobackupthedatabase.setStatus(
        "current"
    )

hh3cNMDBMANfailedtoexecutethescriptwhenbackingupthedatabase = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 4)
)
hh3cNMDBMANfailedtoexecutethescriptwhenbackingupthedatabase.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtoexecutethescriptwhenbackingupthedatabase.setStatus(
        "current"
    )

hh3cNMDBMANfailedtorestorethedatabase = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 5)
)
hh3cNMDBMANfailedtorestorethedatabase.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMDBaseName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtorestorethedatabase.setStatus(
        "current"
    )

hh3cNMDBMANfailedtoexecutethescriptwhenrestoringthedatabase = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 6)
)
hh3cNMDBMANfailedtoexecutethescriptwhenrestoringthedatabase.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtoexecutethescriptwhenrestoringthedatabase.setStatus(
        "current"
    )

hh3cNMDBMANfailedtorestorethedatabase1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 7)
)
hh3cNMDBMANfailedtorestorethedatabase1.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMFileName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMServerIp"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtorestorethedatabase1.setStatus(
        "current"
    )

hh3cNMDBMANfailedtocomparetheversion = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 9)
)
hh3cNMDBMANfailedtocomparetheversion.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMLocalDbmanVersion"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMRemoteDbmanVersion"))
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtocomparetheversion.setStatus(
        "current"
    )

hh3cNMDBMANfailedtorestoredatabase = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 19, 2, 0, 10)
)
if mibBuilder.loadTexts:
    hh3cNMDBMANfailedtorestoredatabase.setStatus(
        "current"
    )

hh3cNMAbnormalhoststatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 2)
)
hh3cNMAbnormalhoststatus.setObjects(
    ("HH3C-NMS-BASIC-MIB", "hh3cNMHostName")
)
if mibBuilder.loadTexts:
    hh3cNMAbnormalhoststatus.setStatus(
        "current"
    )

hh3cNMAbnormalvirtualizationmanagementsoftwareservice = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 3)
)
hh3cNMAbnormalvirtualizationmanagementsoftwareservice.setObjects(
    ("HH3C-NMS-BASIC-MIB", "hh3cNMHostName")
)
if mibBuilder.loadTexts:
    hh3cNMAbnormalvirtualizationmanagementsoftwareservice.setStatus(
        "current"
    )

hh3cNMvNICerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 5)
)
hh3cNMvNICerror.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVMName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVMMAC"))
)
if mibBuilder.loadTexts:
    hh3cNMvNICerror.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforhostCPUusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 6)
)
hh3cNMThresholdexceedalarmforhostCPUusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMHostName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMHostIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCPUUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCpuUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforhostCPUusage.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforhostmemoryusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 7)
)
hh3cNMThresholdexceedalarmforhostmemoryusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMHostName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMHostIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMemUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforhostmemoryusage.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforhostdiskusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 8)
)
hh3cNMThresholdexceedalarmforhostdiskusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMHostName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMHostIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforhostdiskusage.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforVMCPUusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 16)
)
hh3cNMThresholdexceedalarmforVMCPUusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVMName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVMIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCPUUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCpuUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforVMCPUusage.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforVMmemoryusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 17)
)
hh3cNMThresholdexceedalarmforVMmemoryusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVMName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVMIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMemUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforVMmemoryusage.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforVMdiskusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 18)
)
hh3cNMThresholdexceedalarmforVMdiskusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMVMName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMVMIP"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMDiskUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforVMdiskusage.setStatus(
        "current"
    )

hh3cNMClusterHAvalidalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 21)
)
hh3cNMClusterHAvalidalarm.setObjects(
    ("HH3C-NMS-BASIC-MIB", "hh3cNMClusterName")
)
if mibBuilder.loadTexts:
    hh3cNMClusterHAvalidalarm.setStatus(
        "current"
    )

hh3cNMAlarmforclusterhostHAheartbeattermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 22)
)
hh3cNMAlarmforclusterhostHAheartbeattermination.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMClusterName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMHostName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMHostIP"))
)
if mibBuilder.loadTexts:
    hh3cNMAlarmforclusterhostHAheartbeattermination.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforclusterCPUusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 26)
)
hh3cNMThresholdexceedalarmforclusterCPUusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMClusterName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCPUUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMCPUUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforclusterCPUusage.setStatus(
        "current"
    )

hh3cNMThresholdexceedalarmforclustermemoryusage = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 4, 2, 26, 2, 0, 27)
)
hh3cNMThresholdexceedalarmforclustermemoryusage.setObjects(
      *(("HH3C-NMS-BASIC-MIB", "hh3cNMClusterName"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMemUsage"),
        ("HH3C-NMS-BASIC-MIB", "hh3cNMMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cNMThresholdexceedalarmforclustermemoryusage.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NMS-BASIC-MIB",
    **{"hh3cNMIMCBaisic": hh3cNMIMCBaisic,
       "hh3cNMResource": hh3cNMResource,
       "hh3cNMResourceObjects": hh3cNMResourceObjects,
       "hh3cNMDeviceID": hh3cNMDeviceID,
       "hh3cNMDeviceDescription": hh3cNMDeviceDescription,
       "hh3cNMLastDeviceModel": hh3cNMLastDeviceModel,
       "hh3cNMCurrentDeviceModel": hh3cNMCurrentDeviceModel,
       "hh3cNMServiceType": hh3cNMServiceType,
       "hh3cNMServiceName": hh3cNMServiceName,
       "hh3cNMErrorInformation": hh3cNMErrorInformation,
       "hh3cNMLicsIP": hh3cNMLicsIP,
       "hh3cNMStackMemberName": hh3cNMStackMemberName,
       "hh3cNMStackMemberSerialNumber": hh3cNMStackMemberSerialNumber,
       "hh3cNMStackMemberParentEntityID": hh3cNMStackMemberParentEntityID,
       "hh3cNMStackMemberParentRelPosition": hh3cNMStackMemberParentRelPosition,
       "hh3cNMLicsPort": hh3cNMLicsPort,
       "hh3cNMDescription": hh3cNMDescription,
       "hh3cNMOtherDeviceIP": hh3cNMOtherDeviceIP,
       "hh3cNMDuplicatedDeviceList": hh3cNMDuplicatedDeviceList,
       "hh3cNMResourceTraps": hh3cNMResourceTraps,
       "hh3cNMResourceTrapsPrefix": hh3cNMResourceTrapsPrefix,
       "hh3cNMThedevicedoesnotrespondtopollpacket": hh3cNMThedevicedoesnotrespondtopollpacket,
       "hh3cNMDeviceDeniedSNMPAccess": hh3cNMDeviceDeniedSNMPAccess,
       "hh3cNMDeviceMIBAccessException": hh3cNMDeviceMIBAccessException,
       "hh3cNMThedevicecorrectlyrespondstopollpackets": hh3cNMThedevicecorrectlyrespondstopollpackets,
       "hh3cNMDeviceModelchanged": hh3cNMDeviceModelchanged,
       "hh3cNMDeviceServiceDOWN": hh3cNMDeviceServiceDOWN,
       "hh3cNMDeviceServiceUP": hh3cNMDeviceServiceUP,
       "hh3cNMLinkStateDOWN": hh3cNMLinkStateDOWN,
       "hh3cNMLinkStateUP": hh3cNMLinkStateUP,
       "hh3cNMIPAddressofDeviceInterfaceChanged": hh3cNMIPAddressofDeviceInterfaceChanged,
       "hh3cNMDiscoverIdenticalDevice": hh3cNMDiscoverIdenticalDevice,
       "hh3cNMMpgroupSubinterfaceDOWN": hh3cNMMpgroupSubinterfaceDOWN,
       "hh3cNMMpgroupSubinterfaceUP": hh3cNMMpgroupSubinterfaceUP,
       "hh3cNMDeviceSNMPAccessible": hh3cNMDeviceSNMPAccessible,
       "hh3cNMIdenticalSNMPEngineID": hh3cNMIdenticalSNMPEngineID,
       "hh3cNMStackMemberofDeviceDeleted": hh3cNMStackMemberofDeviceDeleted,
       "hh3cNMStackMemberofDeviceAdded": hh3cNMStackMemberofDeviceAdded,
       "hh3cNMLicenseserverexception": hh3cNMLicenseserverexception,
       "hh3cNMPerformance": hh3cNMPerformance,
       "hh3cNMPerformanceObjects": hh3cNMPerformanceObjects,
       "hh3cNMPerfDeviceID": hh3cNMPerfDeviceID,
       "hh3cNMTaskID": hh3cNMTaskID,
       "hh3cNMTaskName": hh3cNMTaskName,
       "hh3cNMTemplateName": hh3cNMTemplateName,
       "hh3cNMInstanceID": hh3cNMInstanceID,
       "hh3cNMInstanceOID": hh3cNMInstanceOID,
       "hh3cNMInstanceDescription": hh3cNMInstanceDescription,
       "hh3cNMInstanceValue": hh3cNMInstanceValue,
       "hh3cNMThresholdValue": hh3cNMThresholdValue,
       "hh3cNMAlarmLevel": hh3cNMAlarmLevel,
       "hh3cNMInterfaceIndex": hh3cNMInterfaceIndex,
       "hh3cNMComponentPerformanceTask": hh3cNMComponentPerformanceTask,
       "hh3cNMPerformanceTraps": hh3cNMPerformanceTraps,
       "hh3cNMPerformanceTrapsPrefix": hh3cNMPerformanceTrapsPrefix,
       "hh3cNMPerformanceAlert": hh3cNMPerformanceAlert,
       "hh3cNMPerformanceRecoverAlert": hh3cNMPerformanceRecoverAlert,
       "hh3cNMPerformanceAlert1": hh3cNMPerformanceAlert1,
       "hh3cNMPerformanceRecoverAlert1": hh3cNMPerformanceRecoverAlert1,
       "hh3cNMDeviceConfigfileManagement": hh3cNMDeviceConfigfileManagement,
       "hh3cNMDeviceConfigfileManagementObjects": hh3cNMDeviceConfigfileManagementObjects,
       "hh3cNMLastBackupTime": hh3cNMLastBackupTime,
       "hh3cNMCurrentBackupTime": hh3cNMCurrentBackupTime,
       "hh3cNMCheckTaskName": hh3cNMCheckTaskName,
       "hh3cNMCurrentConfigurationFileID": hh3cNMCurrentConfigurationFileID,
       "hh3cNMBaselineConfigurationFileID": hh3cNMBaselineConfigurationFileID,
       "hh3cNMCurrentConfigurationFileName": hh3cNMCurrentConfigurationFileName,
       "hh3cNMBaselineConfigurationFileName": hh3cNMBaselineConfigurationFileName,
       "hh3cNMLastConfigurationFileID": hh3cNMLastConfigurationFileID,
       "hh3cNMLastConfigurationFileName": hh3cNMLastConfigurationFileName,
       "hh3cNMDeviceConfigfileManagementTraps": hh3cNMDeviceConfigfileManagementTraps,
       "hh3cNMDeviceConfigfileManagementTrapsPrefix": hh3cNMDeviceConfigfileManagementTrapsPrefix,
       "hh3cNMStartupConfigurationChanged": hh3cNMStartupConfigurationChanged,
       "hh3cNMRunningConfigurationChanged": hh3cNMRunningConfigurationChanged,
       "hh3cNMGettingConfigforcheck": hh3cNMGettingConfigforcheck,
       "hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask": hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask,
       "hh3cNMStartupConfigurationdiffersfrombaseline": hh3cNMStartupConfigurationdiffersfrombaseline,
       "hh3cNMRunningConfigurationdiffersfrombaseline": hh3cNMRunningConfigurationdiffersfrombaseline,
       "hh3cNMIPSMonitor": hh3cNMIPSMonitor,
       "hh3cNMIPSMonitorObjects": hh3cNMIPSMonitorObjects,
       "hh3cNMIPSAlarmLevel": hh3cNMIPSAlarmLevel,
       "hh3cNMIPSAlarmPeriod": hh3cNMIPSAlarmPeriod,
       "hh3cNMIPSAlarmCount": hh3cNMIPSAlarmCount,
       "hh3cNMIPSAttackTypeInformation": hh3cNMIPSAttackTypeInformation,
       "hh3cNMIPSAttackOriginationInformation": hh3cNMIPSAttackOriginationInformation,
       "hh3cNMIPSAttackDestinationInformation": hh3cNMIPSAttackDestinationInformation,
       "hh3cNMIPSMonitorTraps": hh3cNMIPSMonitorTraps,
       "hh3cNMIPSMonitorTrapsPrefix": hh3cNMIPSMonitorTrapsPrefix,
       "hh3cNMFrequentAlertsforIDSAttack": hh3cNMFrequentAlertsforIDSAttack,
       "hh3cNMFrequentAlertsforIDSSeriousAttack": hh3cNMFrequentAlertsforIDSSeriousAttack,
       "hh3cNMFrequentAlertsforIDSAttackAlarm": hh3cNMFrequentAlertsforIDSAttackAlarm,
       "hh3cNMFrequentAlertsforIDSSeriousAttackAlarm": hh3cNMFrequentAlertsforIDSSeriousAttackAlarm,
       "hh3cNMSysmonitor": hh3cNMSysmonitor,
       "hh3cNMSysmonitorObjects": hh3cNMSysmonitorObjects,
       "hh3cNMSystemMonitorDiskName": hh3cNMSystemMonitorDiskName,
       "hh3cNMSystemMonitorDiskCurrentUsage": hh3cNMSystemMonitorDiskCurrentUsage,
       "hh3cNMSystemMonitorDiskLimitUsage": hh3cNMSystemMonitorDiskLimitUsage,
       "hh3cNMSystemMonitorProcessName": hh3cNMSystemMonitorProcessName,
       "hh3cNMSystemMonitorMemoryCurrentUsage": hh3cNMSystemMonitorMemoryCurrentUsage,
       "hh3cNMSystemMonitorMemoryLimitUsage": hh3cNMSystemMonitorMemoryLimitUsage,
       "hh3cNMSystemMonitorCPUCurrentUsage": hh3cNMSystemMonitorCPUCurrentUsage,
       "hh3cNMSystemMonitorCPULimitUsage": hh3cNMSystemMonitorCPULimitUsage,
       "hh3cNMDatabaseName": hh3cNMDatabaseName,
       "hh3cNMCurrentSize": hh3cNMCurrentSize,
       "hh3cNMLimitSize": hh3cNMLimitSize,
       "hh3cNMSystemMonitorIP": hh3cNMSystemMonitorIP,
       "hh3cNMReasonofDBConnectionFailed": hh3cNMReasonofDBConnectionFailed,
       "hh3cNMSysmonitorTraps": hh3cNMSysmonitorTraps,
       "hh3cNMSysmonitorTrapsPrefix": hh3cNMSysmonitorTrapsPrefix,
       "hh3cNMUseofDiskRatioUP": hh3cNMUseofDiskRatioUP,
       "hh3cNMUseofDiskRatioRecoverNormal": hh3cNMUseofDiskRatioRecoverNormal,
       "hh3cNMiMCProcessCoreDOWN": hh3cNMiMCProcessCoreDOWN,
       "hh3cNMUseofMemoryRatioUP": hh3cNMUseofMemoryRatioUP,
       "hh3cNMUseofCPURatioUP": hh3cNMUseofCPURatioUP,
       "hh3cNMApproachthelimitofdatabase": hh3cNMApproachthelimitofdatabase,
       "hh3cNMDatabaseConnectionFailure": hh3cNMDatabaseConnectionFailure,
       "hh3cNMAccessPoint": hh3cNMAccessPoint,
       "hh3cNMAccessPointObjects": hh3cNMAccessPointObjects,
       "hh3cNMDeviceID1": hh3cNMDeviceID1,
       "hh3cNMAPIPAddress": hh3cNMAPIPAddress,
       "hh3cNMAPName": hh3cNMAPName,
       "hh3cNMAPID": hh3cNMAPID,
       "hh3cNMDeviceIP": hh3cNMDeviceIP,
       "hh3cNMACDeviceName": hh3cNMACDeviceName,
       "hh3cNMiNodeUserName": hh3cNMiNodeUserName,
       "hh3cNMiNodeUserMac": hh3cNMiNodeUserMac,
       "hh3cNMRegionName1": hh3cNMRegionName1,
       "hh3cNMPerfItem": hh3cNMPerfItem,
       "hh3cNMCurrentValue": hh3cNMCurrentValue,
       "hh3cNMThresholdValue1": hh3cNMThresholdValue1,
       "hh3cNMTeamIP": hh3cNMTeamIP,
       "hh3cNMTeamName": hh3cNMTeamName,
       "hh3cNMRadioID": hh3cNMRadioID,
       "hh3cNMStationMac": hh3cNMStationMac,
       "hh3cNMRegionName": hh3cNMRegionName,
       "hh3cNMRegionType": hh3cNMRegionType,
       "hh3cNMStationMac1": hh3cNMStationMac1,
       "hh3cNMDigitalBarrierName": hh3cNMDigitalBarrierName,
       "hh3cNMStayTime": hh3cNMStayTime,
       "hh3cNMStationNum": hh3cNMStationNum,
       "hh3cNMAccessPointTraps": hh3cNMAccessPointTraps,
       "hh3cNMAccessPointTrapsPrefix": hh3cNMAccessPointTrapsPrefix,
       "hh3cNMAPDeviceOnline": hh3cNMAPDeviceOnline,
       "hh3cNMAPDeviceOffline": hh3cNMAPDeviceOffline,
       "hh3cNMiNodeClientDisobeyAccessPolicy": hh3cNMiNodeClientDisobeyAccessPolicy,
       "hh3cNMAPExceedsThreshold": hh3cNMAPExceedsThreshold,
       "hh3cNMAPRecovery": hh3cNMAPRecovery,
       "hh3cNMRemoveTeamMemberDevice": hh3cNMRemoveTeamMemberDevice,
       "hh3cNMCannotManageTeamMemberDevice": hh3cNMCannotManageTeamMemberDevice,
       "hh3cNMStationoverarea": hh3cNMStationoverarea,
       "hh3cNMStaEnterDigitalBarrier": hh3cNMStaEnterDigitalBarrier,
       "hh3cNMStaExitDigitalBarrier": hh3cNMStaExitDigitalBarrier,
       "hh3cNMStationNumberThreshold": hh3cNMStationNumberThreshold,
       "hh3cNMStationNumberThreshold1": hh3cNMStationNumberThreshold1,
       "hh3cNMStationNumberThreshold2": hh3cNMStationNumberThreshold2,
       "hh3cNMStationNumberThreshold3": hh3cNMStationNumberThreshold3,
       "hh3cNMFaultModel": hh3cNMFaultModel,
       "hh3cNMFaultModelObjects": hh3cNMFaultModelObjects,
       "hh3cNMStartTime": hh3cNMStartTime,
       "hh3cNMStopTime": hh3cNMStopTime,
       "hh3cNMTimes": hh3cNMTimes,
       "hh3cNMRepeatEventName": hh3cNMRepeatEventName,
       "hh3cNMFlashEvent": hh3cNMFlashEvent,
       "hh3cNMFlashRelativeEvent": hh3cNMFlashRelativeEvent,
       "hh3cNMDeviceIP1": hh3cNMDeviceIP1,
       "hh3cNMDeviceName": hh3cNMDeviceName,
       "hh3cNMDeviceID2": hh3cNMDeviceID2,
       "hh3cNMFaultOID": hh3cNMFaultOID,
       "hh3cNMPOSInfo": hh3cNMPOSInfo,
       "hh3cNMTrapDescription": hh3cNMTrapDescription,
       "hh3cNMAlarmLevel1": hh3cNMAlarmLevel1,
       "hh3cNMInterfaceOperationTime": hh3cNMInterfaceOperationTime,
       "hh3cNMVarivableOID": hh3cNMVarivableOID,
       "hh3cNMVarivableValue": hh3cNMVarivableValue,
       "hh3cNMPollType": hh3cNMPollType,
       "hh3cNMFaultModelTraps": hh3cNMFaultModelTraps,
       "hh3cNMFaultModelTrapsPrefix": hh3cNMFaultModelTrapsPrefix,
       "hh3cNMAlarmsystemdetectedalarmsofduplicateevent": hh3cNMAlarmsystemdetectedalarmsofduplicateevent,
       "hh3cNMAlarmsystemdetectedalarmsfromunmanageddevices": hh3cNMAlarmsystemdetectedalarmsfromunmanageddevices,
       "hh3cNMAlarmsystemdetectedalarmsofunknowntraps": hh3cNMAlarmsystemdetectedalarmsofunknowntraps,
       "hh3cNMAlarmsystemdetectedintermittentfailures": hh3cNMAlarmsystemdetectedintermittentfailures,
       "hh3cNMLowerLevelAlarm": hh3cNMLowerLevelAlarm,
       "hh3cNMLowerLevelRecovery": hh3cNMLowerLevelRecovery,
       "hh3cNMLowerLevelSelfRecovery": hh3cNMLowerLevelSelfRecovery,
       "hh3cNMLowerLeveltoreportvalidationtoreport1": hh3cNMLowerLeveltoreportvalidationtoreport1,
       "hh3cNMiMCfaultmodulealarmgroup": hh3cNMiMCfaultmodulealarmgroup,
       "hh3cNMNTAalarmgroup": hh3cNMNTAalarmgroup,
       "hh3cNMPerformancealarmgroup": hh3cNMPerformancealarmgroup,
       "hh3cNMConfigurationchangealarmgroup": hh3cNMConfigurationchangealarmgroup,
       "hh3cNMIPSecalarmgroup": hh3cNMIPSecalarmgroup,
       "hh3cNMSNMPaccesserroralarmgroup": hh3cNMSNMPaccesserroralarmgroup,
       "hh3cNMLowerlevelalarmgroup": hh3cNMLowerlevelalarmgroup,
       "hh3cNMColdstartalarmgroup": hh3cNMColdstartalarmgroup,
       "hh3cNMSNMPrestartalarmgroup": hh3cNMSNMPrestartalarmgroup,
       "hh3cNMUseofmemoryupalarmgroup": hh3cNMUseofmemoryupalarmgroup,
       "hh3cNMLowerLeveltoreportvalidationtoreport": hh3cNMLowerLeveltoreportvalidationtoreport,
       "hh3cNMFaultModelTrapsEx": hh3cNMFaultModelTrapsEx,
       "hh3cNMFaultModelTrapsExSub5": hh3cNMFaultModelTrapsExSub5,
       "hh3cNMSerialNumber1": hh3cNMSerialNumber1,
       "hh3cNMFaultModelTrapsExSub19": hh3cNMFaultModelTrapsExSub19,
       "hh3cNMSerialNumber": hh3cNMSerialNumber,
       "hh3cNMHibIP": hh3cNMHibIP,
       "hh3cNMAckUser": hh3cNMAckUser,
       "hh3cNMIsAck": hh3cNMIsAck,
       "hh3cNMiMCNetflowFlux": hh3cNMiMCNetflowFlux,
       "hh3cNMiMCNetflowFluxObjects": hh3cNMiMCNetflowFluxObjects,
       "hh3cNMUNBAServerName": hh3cNMUNBAServerName,
       "hh3cNMUNBAServerIP": hh3cNMUNBAServerIP,
       "hh3cNMDeviceName1": hh3cNMDeviceName1,
       "hh3cNMInterfaceDescription": hh3cNMInterfaceDescription,
       "hh3cNMIPaddress": hh3cNMIPaddress,
       "hh3cNMApplication": hh3cNMApplication,
       "hh3cNMCurrentInflowSpeed": hh3cNMCurrentInflowSpeed,
       "hh3cNMThresholdSpeed": hh3cNMThresholdSpeed,
       "hh3cNMAlarmSeverity": hh3cNMAlarmSeverity,
       "hh3cNMInterval": hh3cNMInterval,
       "hh3cNMDirection": hh3cNMDirection,
       "hh3cNMThresholdType": hh3cNMThresholdType,
       "hh3cNMStartTime1": hh3cNMStartTime1,
       "hh3cNMEndTime": hh3cNMEndTime,
       "hh3cNMiMCNetflowFluxTraps": hh3cNMiMCNetflowFluxTraps,
       "hh3cNMiMCNetflowFluxTrapsPrefix": hh3cNMiMCNetflowFluxTrapsPrefix,
       "hh3cNMInterfaceflowexceededthreshold": hh3cNMInterfaceflowexceededthreshold,
       "hh3cNMInterfaceFlowrecovers": hh3cNMInterfaceFlowrecovers,
       "hh3cNMIPflowexceededthreshold": hh3cNMIPflowexceededthreshold,
       "hh3cNMIPflowrecovers": hh3cNMIPflowrecovers,
       "hh3cNMIntfappflowexceededthreshold": hh3cNMIntfappflowexceededthreshold,
       "hh3cNMIntfappflowrecovers": hh3cNMIntfappflowrecovers,
       "hh3cNMAppflowexceededthreshold": hh3cNMAppflowexceededthreshold,
       "hh3cNMAppflowrecovers": hh3cNMAppflowrecovers,
       "hh3cNMIpappflowexceededthreshold": hh3cNMIpappflowexceededthreshold,
       "hh3cNMIPappflowrecovers": hh3cNMIPappflowrecovers,
       "hh3cNMUBALicenseDetecting": hh3cNMUBALicenseDetecting,
       "hh3cNMDataTransferFailed": hh3cNMDataTransferFailed,
       "hh3cNMDataFileDeleteFailed": hh3cNMDataFileDeleteFailed,
       "hh3cNMNTALicenseDetecting": hh3cNMNTALicenseDetecting,
       "hh3cNMiMCNetflowMonitor": hh3cNMiMCNetflowMonitor,
       "hh3cNMiMCNetflowMonitorObjects": hh3cNMiMCNetflowMonitorObjects,
       "hh3cNMUNBAServerName1": hh3cNMUNBAServerName1,
       "hh3cNMUNBAServerIP1": hh3cNMUNBAServerIP1,
       "hh3cNMProbeName": hh3cNMProbeName,
       "hh3cNMProbeIP": hh3cNMProbeIP,
       "hh3cNMLogFileName": hh3cNMLogFileName,
       "hh3cNMDiskLimitUsage": hh3cNMDiskLimitUsage,
       "hh3cNMiMCNetflowMonitorTraps": hh3cNMiMCNetflowMonitorTraps,
       "hh3cNMiMCNetflowMonitorTrapsPrefix": hh3cNMiMCNetflowMonitorTrapsPrefix,
       "hh3cNMNetFolwProbePrefix": hh3cNMNetFolwProbePrefix,
       "hh3cNMLoadnewconfigonprobe": hh3cNMLoadnewconfigonprobe,
       "hh3cNMProbeloadingconfigfailed": hh3cNMProbeloadingconfigfailed,
       "hh3cNMConnectiontoDBfailed": hh3cNMConnectiontoDBfailed,
       "hh3cNMReceiverloadingnewconfig": hh3cNMReceiverloadingnewconfig,
       "hh3cNMProcessorloadingnewconfig": hh3cNMProcessorloadingnewconfig,
       "hh3cNMReceiverloadingnewconfigfailed": hh3cNMReceiverloadingnewconfigfailed,
       "hh3cNMProcessorloadingconfigfailed": hh3cNMProcessorloadingconfigfailed,
       "hh3cNMReceiverstoppedprocesslog": hh3cNMReceiverstoppedprocesslog,
       "hh3cNMDiskuseexceededthreshold": hh3cNMDiskuseexceededthreshold,
       "hh3cNMDiskusewillreachthreshold": hh3cNMDiskusewillreachthreshold,
       "hh3cNMDiskusetempenough": hh3cNMDiskusetempenough,
       "hh3cNMProcessorstoppedprocesslog": hh3cNMProcessorstoppedprocesslog,
       "hh3cNMProbestoppeddatacollection": hh3cNMProbestoppeddatacollection,
       "hh3cNMReceiverresumeprocessinglog": hh3cNMReceiverresumeprocessinglog,
       "hh3cNMProcessorresumeprocessinglog": hh3cNMProcessorresumeprocessinglog,
       "hh3cNMProberesumeprocessinglog": hh3cNMProberesumeprocessinglog,
       "hh3cNMiMCSecurePolicy": hh3cNMiMCSecurePolicy,
       "hh3cNMiMCSecurePolicyObjects": hh3cNMiMCSecurePolicyObjects,
       "hh3cNMAccessServiceEventSeqId": hh3cNMAccessServiceEventSeqId,
       "hh3cNMAccessServiceUserName": hh3cNMAccessServiceUserName,
       "hh3cNMAccessServiceDeviceIP": hh3cNMAccessServiceDeviceIP,
       "hh3cNMAccessServiceTerminalIP": hh3cNMAccessServiceTerminalIP,
       "hh3cNMAccessServiceTerminalMacAddress": hh3cNMAccessServiceTerminalMacAddress,
       "hh3cNMAccessServiceTrapInfo": hh3cNMAccessServiceTrapInfo,
       "hh3cNMiMCSecurePolicyTraps": hh3cNMiMCSecurePolicyTraps,
       "hh3cNMiMCSecurePolicyTrapsPrefix": hh3cNMiMCSecurePolicyTrapsPrefix,
       "hh3cNMFlowMonitorUnnormalinUAM": hh3cNMFlowMonitorUnnormalinUAM,
       "hh3cNMFlowMonitorSeriousinUAM": hh3cNMFlowMonitorSeriousinUAM,
       "hh3cNMiMCSyslog": hh3cNMiMCSyslog,
       "hh3cNMiMCSyslogObjects": hh3cNMiMCSyslogObjects,
       "hh3cNMh3cyslogType": hh3cNMh3cyslogType,
       "hh3cNMh3cyslogTrapDesc": hh3cNMh3cyslogTrapDesc,
       "hh3cNMh3cyslogDateTime": hh3cNMh3cyslogDateTime,
       "hh3cNMh3cyslogDevIP": hh3cNMh3cyslogDevIP,
       "hh3cNMh3cyslogDuplicateIP": hh3cNMh3cyslogDuplicateIP,
       "hh3cNMh3cyslogVlanID": hh3cNMh3cyslogVlanID,
       "hh3cNMh3cyslogIfdesc": hh3cNMh3cyslogIfdesc,
       "hh3cNMh3cyslogUserName": hh3cNMh3cyslogUserName,
       "hh3cNMh3cyslogSourceIP": hh3cNMh3cyslogSourceIP,
       "hh3cNMh3cyslogSourceMac": hh3cNMh3cyslogSourceMac,
       "hh3cNMh3cyslogPacketRate": hh3cNMh3cyslogPacketRate,
       "hh3cNMh3cyslogPeerMac": hh3cNMh3cyslogPeerMac,
       "hh3cNMRuleName": hh3cNMRuleName,
       "hh3cNMDescription1": hh3cNMDescription1,
       "hh3cNMSyslogFacility": hh3cNMSyslogFacility,
       "hh3cNMSyslogSeverity": hh3cNMSyslogSeverity,
       "hh3cNMParameterList": hh3cNMParameterList,
       "hh3cNMTime": hh3cNMTime,
       "hh3cNMReason": hh3cNMReason,
       "hh3cNMSourceIP": hh3cNMSourceIP,
       "hh3cNMPosInfo": hh3cNMPosInfo,
       "hh3cNMTrapLevel": hh3cNMTrapLevel,
       "hh3cNMInterfaceIndex1": hh3cNMInterfaceIndex1,
       "hh3cwapiModeEnabled": hh3cwapiModeEnabled,
       "hh3cwapiASIPAddressType": hh3cwapiASIPAddressType,
       "hh3cwapiASIPAddress": hh3cwapiASIPAddress,
       "hh3cwapiCertificateInstalled": hh3cwapiCertificateInstalled,
       "hh3cNMarchivePath": hh3cNMarchivePath,
       "hh3cNMseverity": hh3cNMseverity,
       "hh3cNMurl": hh3cNMurl,
       "hh3cNMrule": hh3cNMrule,
       "hh3cNMeventCategory": hh3cNMeventCategory,
       "hh3cNMdevice": hh3cNMdevice,
       "hh3cNMservice": hh3cNMservice,
       "hh3cNMsourceIp": hh3cNMsourceIp,
       "hh3cNMsourcePort": hh3cNMsourcePort,
       "hh3cNMvirus": hh3cNMvirus,
       "hh3cNMdestIp": hh3cNMdestIp,
       "hh3cNMdestPort": hh3cNMdestPort,
       "hh3cNMvpn": hh3cNMvpn,
       "hh3cNMeventCode": hh3cNMeventCode,
       "hh3cNMaction": hh3cNMaction,
       "hh3cNMinterface": hh3cNMinterface,
       "hh3cNMdirection": hh3cNMdirection,
       "hh3cNMeventDesc": hh3cNMeventDesc,
       "hh3cNMiMCSyslogTraps": hh3cNMiMCSyslogTraps,
       "hh3cNMiMCSyslogTrapsPrefix": hh3cNMiMCSyslogTrapsPrefix,
       "hh3cNMARPDuplicateaddressalarm": hh3cNMARPDuplicateaddressalarm,
       "hh3cNMPortSecurityLogfailalarm": hh3cNMPortSecurityLogfailalarm,
       "hh3cNMArpOverspeedalarm": hh3cNMArpOverspeedalarm,
       "hh3cNMPortAccessRejectalarm": hh3cNMPortAccessRejectalarm,
       "hh3cNMBPDUGuardalarm": hh3cNMBPDUGuardalarm,
       "hh3cNMLOOPGUARDalarm": hh3cNMLOOPGUARDalarm,
       "hh3cNMDHCPServerDetectalarm": hh3cNMDHCPServerDetectalarm,
       "hh3cNMPortSecurityIntrusionalarm": hh3cNMPortSecurityIntrusionalarm,
       "hh3cNMAttackDetect": hh3cNMAttackDetect,
       "hh3cNMTrapupgradedfromsyslog": hh3cNMTrapupgradedfromsyslog,
       "hh3cNMRecovertrapupgradedfromsyslog": hh3cNMRecovertrapupgradedfromsyslog,
       "hh3cNMSCCtrapupgradedfromsyslog": hh3cNMSCCtrapupgradedfromsyslog,
       "hh3cNMSCCrecovertrapupgradedfromsyslog": hh3cNMSCCrecovertrapupgradedfromsyslog,
       "hh3cNMiMCETL": hh3cNMiMCETL,
       "hh3cNMiMCETLObjects": hh3cNMiMCETLObjects,
       "hh3cNMServerIp": hh3cNMServerIp,
       "hh3cNMProjectId": hh3cNMProjectId,
       "hh3cNMDescription2": hh3cNMDescription2,
       "hh3cNMiMCETLTraps": hh3cNMiMCETLTraps,
       "hh3cNMiMCETLTrapsPrefix": hh3cNMiMCETLTrapsPrefix,
       "hh3cNMDataAnalysisTaskExecuteFail": hh3cNMDataAnalysisTaskExecuteFail,
       "hh3cNMDataAnalysisTaskExecuteRecovery": hh3cNMDataAnalysisTaskExecuteRecovery,
       "hh3cNMDataAnalysisSourceTableNotExist": hh3cNMDataAnalysisSourceTableNotExist,
       "hh3cNMiMCL2TOPO": hh3cNMiMCL2TOPO,
       "hh3cNMiMCL2TOPOObjects": hh3cNMiMCL2TOPOObjects,
       "hh3cNMAlarmDeviceIP": hh3cNMAlarmDeviceIP,
       "hh3cNMIllegalIP": hh3cNMIllegalIP,
       "hh3cNMBindMAC": hh3cNMBindMAC,
       "hh3cNMConflictMAC": hh3cNMConflictMAC,
       "hh3cNMMAC": hh3cNMMAC,
       "hh3cNMBindIP": hh3cNMBindIP,
       "hh3cNMConflictIP": hh3cNMConflictIP,
       "hh3cNMBindInterface": hh3cNMBindInterface,
       "hh3cNMConflictInterface": hh3cNMConflictInterface,
       "hh3cNMInterface": hh3cNMInterface,
       "hh3cNMAlarmTime": hh3cNMAlarmTime,
       "hh3cNMPollDeviceIP": hh3cNMPollDeviceIP,
       "hh3cNMIP": hh3cNMIP,
       "hh3cNMiMCL2TOPOTraps": hh3cNMiMCL2TOPOTraps,
       "hh3cNMiMCL2TOPOTrapsPrefix": hh3cNMiMCL2TOPOTrapsPrefix,
       "hh3cNMIPMACBindMACConflictAlarm": hh3cNMIPMACBindMACConflictAlarm,
       "hh3cNMIPMACBindIPConflictAlarm": hh3cNMIPMACBindIPConflictAlarm,
       "hh3cNMMACIFBindIFConflictAlarm": hh3cNMMACIFBindIFConflictAlarm,
       "hh3cNMMACIFBindMACConflictAlarm": hh3cNMMACIFBindMACConflictAlarm,
       "hh3cNMMACInterfaceBindingInterfaceConflictAlarm": hh3cNMMACInterfaceBindingInterfaceConflictAlarm,
       "hh3cNMMACInterfaceBindingMACConflictAlarm": hh3cNMMACInterfaceBindingMACConflictAlarm,
       "hh3cNMIllegalMACAccessingAlarm": hh3cNMIllegalMACAccessingAlarm,
       "hh3cNMIllegalMACAccessingAlarm1": hh3cNMIllegalMACAccessingAlarm1,
       "hh3cNMIllegalIPAccessingAlarm": hh3cNMIllegalIPAccessingAlarm,
       "hh3cNMAggregationgroupmemberportDOWN": hh3cNMAggregationgroupmemberportDOWN,
       "hh3cNMVRMfault": hh3cNMVRMfault,
       "hh3cNMVRMfaultObjects": hh3cNMVRMfaultObjects,
       "hh3cNMVCenterAlarmName": hh3cNMVCenterAlarmName,
       "hh3cNMVCenterAlarmDescription": hh3cNMVCenterAlarmDescription,
       "hh3cNMVCenterAlarmKey": hh3cNMVCenterAlarmKey,
       "hh3cNMVRMDeviceID": hh3cNMVRMDeviceID,
       "hh3cNMVRMDeviceType": hh3cNMVRMDeviceType,
       "hh3cNMVRMfaultTraps": hh3cNMVRMfaultTraps,
       "hh3cNMVRMfaultTrapsPrefix": hh3cNMVRMfaultTrapsPrefix,
       "hh3cNMVCenterMajorAlarm": hh3cNMVCenterMajorAlarm,
       "hh3cNMVCenterMajorAlarmRecovery": hh3cNMVCenterMajorAlarmRecovery,
       "hh3cNMVCenterMinorAlarm": hh3cNMVCenterMinorAlarm,
       "hh3cNMVCenterMinorAlarmRecovery": hh3cNMVCenterMinorAlarmRecovery,
       "hh3cNMDeviceRoleChanged": hh3cNMDeviceRoleChanged,
       "hh3cNMHostAccessFailure": hh3cNMHostAccessFailure,
       "hh3cNMHostAccessSuccess": hh3cNMHostAccessSuccess,
       "hh3cNMVMMAccessFailure": hh3cNMVMMAccessFailure,
       "hh3cNMVMMAccessSuccess": hh3cNMVMMAccessSuccess,
       "hh3cNMVCenterAccessFailure": hh3cNMVCenterAccessFailure,
       "hh3cNMVCenterAccessSuccess": hh3cNMVCenterAccessSuccess,
       "hh3cNMDuplicateHostVMAlarm": hh3cNMDuplicateHostVMAlarm,
       "hh3cNMDeviceCheckTaskManagement": hh3cNMDeviceCheckTaskManagement,
       "hh3cNMDeviceCheckTaskManagementObjects": hh3cNMDeviceCheckTaskManagementObjects,
       "hh3cNMTaskId": hh3cNMTaskId,
       "hh3cNMTaskHistoryId": hh3cNMTaskHistoryId,
       "hh3cNMDeviceCheckTaskManagementTraps": hh3cNMDeviceCheckTaskManagementTraps,
       "hh3cNMDeviceCheckTaskManagementTrapsPrefix": hh3cNMDeviceCheckTaskManagementTrapsPrefix,
       "hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask1": hh3cNMDeviceconfigisnotaccordingtotherulesofchecktask1,
       "hh3cNMDBMAN": hh3cNMDBMAN,
       "hh3cNMDBMANObjects": hh3cNMDBMANObjects,
       "hh3cNMDBMANTraps": hh3cNMDBMANTraps,
       "hh3cNMDBMANTrapsPrefix": hh3cNMDBMANTrapsPrefix,
       "hh3cNMDBMANfailedtouploadthebackupfiletotheFTPserver": hh3cNMDBMANfailedtouploadthebackupfiletotheFTPserver,
       "hh3cNMDBMANfailedtotransmitafilefromtheprimarytothebackup": hh3cNMDBMANfailedtotransmitafilefromtheprimarytothebackup,
       "hh3cNMDBMANfailedtobackupthedatabase": hh3cNMDBMANfailedtobackupthedatabase,
       "hh3cNMDBMANfailedtoexecutethescriptwhenbackingupthedatabase": hh3cNMDBMANfailedtoexecutethescriptwhenbackingupthedatabase,
       "hh3cNMDBMANfailedtorestorethedatabase": hh3cNMDBMANfailedtorestorethedatabase,
       "hh3cNMDBMANfailedtoexecutethescriptwhenrestoringthedatabase": hh3cNMDBMANfailedtoexecutethescriptwhenrestoringthedatabase,
       "hh3cNMDBMANfailedtorestorethedatabase1": hh3cNMDBMANfailedtorestorethedatabase1,
       "hh3cNMDBMANfailedtocomparetheversion": hh3cNMDBMANfailedtocomparetheversion,
       "hh3cNMDBMANfailedtorestoredatabase": hh3cNMDBMANfailedtorestoredatabase,
       "hh3cNMDBMANTrapsEx": hh3cNMDBMANTrapsEx,
       "hh3cNMDBMANTrapsExSub1": hh3cNMDBMANTrapsExSub1,
       "hh3cNMFileName": hh3cNMFileName,
       "hh3cNMServerIp1": hh3cNMServerIp1,
       "hh3cNMDBMANTrapsExSub3": hh3cNMDBMANTrapsExSub3,
       "hh3cNMDBaseName": hh3cNMDBaseName,
       "hh3cNMDBMANTrapsExSub7": hh3cNMDBMANTrapsExSub7,
       "hh3cNMFileName1": hh3cNMFileName1,
       "hh3cNMServerIp2": hh3cNMServerIp2,
       "hh3cNMDBMANTrapsExSub9": hh3cNMDBMANTrapsExSub9,
       "hh3cNMLocalDbmanVersion": hh3cNMLocalDbmanVersion,
       "hh3cNMRemoteDbmanVersion": hh3cNMRemoteDbmanVersion,
       "hh3cNMH3CCAS": hh3cNMH3CCAS,
       "hh3cNMH3CCASObjects": hh3cNMH3CCASObjects,
       "hh3cNMHostName": hh3cNMHostName,
       "hh3cNMHostIP": hh3cNMHostIP,
       "hh3cNMVMName1": hh3cNMVMName1,
       "hh3cNMVMMAC": hh3cNMVMMAC,
       "hh3cNMCPUUsage": hh3cNMCPUUsage,
       "hh3cNMCpuUsageThreshold": hh3cNMCpuUsageThreshold,
       "hh3cNMMemUsage": hh3cNMMemUsage,
       "hh3cNMMemUsageThreshold": hh3cNMMemUsageThreshold,
       "hh3cNMDiskName": hh3cNMDiskName,
       "hh3cNMDiskUsage": hh3cNMDiskUsage,
       "hh3cNMDiskUsageThreshold": hh3cNMDiskUsageThreshold,
       "hh3cNMVMName": hh3cNMVMName,
       "hh3cNMVMIP": hh3cNMVMIP,
       "hh3cNMClusterName": hh3cNMClusterName,
       "hh3cNMCPUUsageThreshold": hh3cNMCPUUsageThreshold,
       "hh3cNMH3CCASTraps": hh3cNMH3CCASTraps,
       "hh3cNMH3CCASTrapsPrefix": hh3cNMH3CCASTrapsPrefix,
       "hh3cNMAbnormalhoststatus": hh3cNMAbnormalhoststatus,
       "hh3cNMAbnormalvirtualizationmanagementsoftwareservice": hh3cNMAbnormalvirtualizationmanagementsoftwareservice,
       "hh3cNMvNICerror": hh3cNMvNICerror,
       "hh3cNMThresholdexceedalarmforhostCPUusage": hh3cNMThresholdexceedalarmforhostCPUusage,
       "hh3cNMThresholdexceedalarmforhostmemoryusage": hh3cNMThresholdexceedalarmforhostmemoryusage,
       "hh3cNMThresholdexceedalarmforhostdiskusage": hh3cNMThresholdexceedalarmforhostdiskusage,
       "hh3cNMThresholdexceedalarmforVMCPUusage": hh3cNMThresholdexceedalarmforVMCPUusage,
       "hh3cNMThresholdexceedalarmforVMmemoryusage": hh3cNMThresholdexceedalarmforVMmemoryusage,
       "hh3cNMThresholdexceedalarmforVMdiskusage": hh3cNMThresholdexceedalarmforVMdiskusage,
       "hh3cNMClusterHAvalidalarm": hh3cNMClusterHAvalidalarm,
       "hh3cNMAlarmforclusterhostHAheartbeattermination": hh3cNMAlarmforclusterhostHAheartbeattermination,
       "hh3cNMThresholdexceedalarmforclusterCPUusage": hh3cNMThresholdexceedalarmforclusterCPUusage,
       "hh3cNMThresholdexceedalarmforclustermemoryusage": hh3cNMThresholdexceedalarmforclustermemoryusage}
)
