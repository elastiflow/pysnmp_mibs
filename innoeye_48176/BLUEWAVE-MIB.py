# SNMP MIB module (BLUEWAVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/innoeye_48176/BLUEWAVE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:29 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

bluewaveBaseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48176)
)
if mibBuilder.loadTexts:
    bluewaveBaseMIB.setRevisions(
        ("2016-07-08 13:09",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BluewaveBaseConformance_ObjectIdentity = ObjectIdentity
bluewaveBaseConformance = _BluewaveBaseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48176, 1)
)
_BluewaveDeviceBaseNotifications_ObjectIdentity = ObjectIdentity
bluewaveDeviceBaseNotifications = _BluewaveDeviceBaseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48176, 2)
)
_BluewaveDeviceBaseTrapPrefix_ObjectIdentity = ObjectIdentity
bluewaveDeviceBaseTrapPrefix = _BluewaveDeviceBaseTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0)
)
_BluewaveNotificationObjId_ObjectIdentity = ObjectIdentity
bluewaveNotificationObjId = _BluewaveNotificationObjId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48176, 3)
)
_DeviceMac_Type = Integer32
_DeviceMac_Object = MibScalar
deviceMac = _DeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 1),
    _DeviceMac_Type()
)
deviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMac.setStatus("current")
_DeviceRegion_Type = OctetString
_DeviceRegion_Object = MibScalar
deviceRegion = _DeviceRegion_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 2),
    _DeviceRegion_Type()
)
deviceRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRegion.setStatus("current")
_CurrentFirmwareVersion_Type = Integer32
_CurrentFirmwareVersion_Object = MibScalar
currentFirmwareVersion = _CurrentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 3),
    _CurrentFirmwareVersion_Type()
)
currentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFirmwareVersion.setStatus("current")
_DeregisterTimestamp_Type = Integer32
_DeregisterTimestamp_Object = MibScalar
deregisterTimestamp = _DeregisterTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 4),
    _DeregisterTimestamp_Type()
)
deregisterTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deregisterTimestamp.setStatus("current")
_ResourceName_Type = OctetString
_ResourceName_Object = MibScalar
resourceName = _ResourceName_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 5),
    _ResourceName_Type()
)
resourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceName.setStatus("current")
_ResourceId_Type = Integer32
_ResourceId_Object = MibScalar
resourceId = _ResourceId_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 6),
    _ResourceId_Type()
)
resourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceId.setStatus("current")
_AlarmType_Type = OctetString
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 7),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_Description_Type = OctetString
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 8),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("current")
_InitializationServerUrl_Type = OctetString
_InitializationServerUrl_Object = MibScalar
initializationServerUrl = _InitializationServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 9),
    _InitializationServerUrl_Type()
)
initializationServerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initializationServerUrl.setStatus("current")
_ProvisionServerUrl_Type = OctetString
_ProvisionServerUrl_Object = MibScalar
provisionServerUrl = _ProvisionServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 10),
    _ProvisionServerUrl_Type()
)
provisionServerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provisionServerUrl.setStatus("current")
_ProvisionTimestamp_Type = Integer32
_ProvisionTimestamp_Object = MibScalar
provisionTimestamp = _ProvisionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 11),
    _ProvisionTimestamp_Type()
)
provisionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provisionTimestamp.setStatus("current")
_InitializationTimeStamp_Type = Integer32
_InitializationTimeStamp_Object = MibScalar
initializationTimeStamp = _InitializationTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 12),
    _InitializationTimeStamp_Type()
)
initializationTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initializationTimeStamp.setStatus("current")
_TimeStamp_Type = Integer32
_TimeStamp_Object = MibScalar
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 48176, 3, 13),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeStamp.setStatus("current")

# Managed Objects groups

deviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48176, 1, 3)
)
deviceGroup.setObjects(
      *(("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "deregisterTimestamp"))
)
if mibBuilder.loadTexts:
    deviceGroup.setStatus("current")

bluewaveResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48176, 1, 4)
)
bluewaveResourceGroup.setObjects(
      *(("BLUEWAVE-MIB", "resourceName"),
        ("BLUEWAVE-MIB", "resourceId"))
)
if mibBuilder.loadTexts:
    bluewaveResourceGroup.setStatus("current")

controlTierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48176, 1, 5)
)
controlTierGroup.setObjects(
      *(("BLUEWAVE-MIB", "initializationServerUrl"),
        ("BLUEWAVE-MIB", "provisionServerUrl"),
        ("BLUEWAVE-MIB", "initializationTimeStamp"),
        ("BLUEWAVE-MIB", "provisionTimestamp"))
)
if mibBuilder.loadTexts:
    controlTierGroup.setStatus("current")

otherDetailsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48176, 1, 6)
)
otherDetailsGroup.setObjects(
      *(("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"),
        ("BLUEWAVE-MIB", "timeStamp"),
        ("BLUEWAVE-MIB", "currentFirmwareVersion"))
)
if mibBuilder.loadTexts:
    otherDetailsGroup.setStatus("current")


# Notification objects

deregisterDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0, 1)
)
deregisterDevice.setObjects(
      *(("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "deviceRegion"),
        ("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"),
        ("BLUEWAVE-MIB", "deregisterTimestamp"))
)
if mibBuilder.loadTexts:
    deregisterDevice.setStatus(
        "current"
    )

autoDerigisterDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0, 2)
)
autoDerigisterDevice.setObjects(
      *(("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "deviceRegion"),
        ("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"),
        ("BLUEWAVE-MIB", "deregisterTimestamp"))
)
if mibBuilder.loadTexts:
    autoDerigisterDevice.setStatus(
        "current"
    )

resourceStateUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0, 3)
)
resourceStateUpdate.setObjects(
      *(("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "resourceName"),
        ("BLUEWAVE-MIB", "resourceId"),
        ("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"),
        ("BLUEWAVE-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    resourceStateUpdate.setStatus(
        "current"
    )

resourceValueUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0, 4)
)
resourceValueUpdate.setObjects(
      *(("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "resourceName"),
        ("BLUEWAVE-MIB", "resourceId"),
        ("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"),
        ("BLUEWAVE-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    resourceValueUpdate.setStatus(
        "current"
    )

initializationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0, 5)
)
initializationFail.setObjects(
      *(("BLUEWAVE-MIB", "initializationServerUrl"),
        ("BLUEWAVE-MIB", "initializationTimeStamp"),
        ("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"))
)
if mibBuilder.loadTexts:
    initializationFail.setStatus(
        "current"
    )

provisionFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0, 6)
)
provisionFail.setObjects(
      *(("BLUEWAVE-MIB", "provisionServerUrl"),
        ("BLUEWAVE-MIB", "provisionTimestamp"),
        ("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"))
)
if mibBuilder.loadTexts:
    provisionFail.setStatus(
        "current"
    )

firmwareUpdateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 48176, 2, 0, 7)
)
firmwareUpdateFail.setObjects(
      *(("BLUEWAVE-MIB", "deviceMac"),
        ("BLUEWAVE-MIB", "currentFirmwareVersion"),
        ("BLUEWAVE-MIB", "alarmType"),
        ("BLUEWAVE-MIB", "description"),
        ("BLUEWAVE-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    firmwareUpdateFail.setStatus(
        "current"
    )


# Notifications groups

bluewaveNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 48176, 1, 1)
)
bluewaveNotificationGroup.setObjects(
      *(("BLUEWAVE-MIB", "initializationFail"),
        ("BLUEWAVE-MIB", "provisionFail"),
        ("BLUEWAVE-MIB", "deregisterDevice"),
        ("BLUEWAVE-MIB", "autoDerigisterDevice"),
        ("BLUEWAVE-MIB", "resourceStateUpdate"),
        ("BLUEWAVE-MIB", "resourceValueUpdate"),
        ("BLUEWAVE-MIB", "firmwareUpdateFail"))
)
if mibBuilder.loadTexts:
    bluewaveNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bluewaveBaseCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 48176, 1, 2)
)
bluewaveBaseCompliances.setObjects(
    ("BLUEWAVE-MIB", "bluewaveNotificationGroup")
)
if mibBuilder.loadTexts:
    bluewaveBaseCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUEWAVE-MIB",
    **{"bluewaveBaseMIB": bluewaveBaseMIB,
       "bluewaveBaseConformance": bluewaveBaseConformance,
       "bluewaveNotificationGroup": bluewaveNotificationGroup,
       "bluewaveBaseCompliances": bluewaveBaseCompliances,
       "deviceGroup": deviceGroup,
       "bluewaveResourceGroup": bluewaveResourceGroup,
       "controlTierGroup": controlTierGroup,
       "otherDetailsGroup": otherDetailsGroup,
       "bluewaveDeviceBaseNotifications": bluewaveDeviceBaseNotifications,
       "bluewaveDeviceBaseTrapPrefix": bluewaveDeviceBaseTrapPrefix,
       "deregisterDevice": deregisterDevice,
       "autoDerigisterDevice": autoDerigisterDevice,
       "resourceStateUpdate": resourceStateUpdate,
       "resourceValueUpdate": resourceValueUpdate,
       "initializationFail": initializationFail,
       "provisionFail": provisionFail,
       "firmwareUpdateFail": firmwareUpdateFail,
       "bluewaveNotificationObjId": bluewaveNotificationObjId,
       "deviceMac": deviceMac,
       "deviceRegion": deviceRegion,
       "currentFirmwareVersion": currentFirmwareVersion,
       "deregisterTimestamp": deregisterTimestamp,
       "resourceName": resourceName,
       "resourceId": resourceId,
       "alarmType": alarmType,
       "description": description,
       "initializationServerUrl": initializationServerUrl,
       "provisionServerUrl": provisionServerUrl,
       "provisionTimestamp": provisionTimestamp,
       "initializationTimeStamp": initializationTimeStamp,
       "timeStamp": timeStamp}
)
