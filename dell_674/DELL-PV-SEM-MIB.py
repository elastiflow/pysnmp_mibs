# SNMP MIB module (DELL-PV-SEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DELL-PV-SEM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 16:02:30 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dell = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EnterpriseSW_ObjectIdentity = ObjectIdentity
enterpriseSW = _EnterpriseSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000)
)
_StorageMgmtBranch_ObjectIdentity = ObjectIdentity
storageMgmtBranch = _StorageMgmtBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000)
)
_PvStorageMIB_ObjectIdentity = ObjectIdentity
pvStorageMIB = _PvStorageMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700)
)
_SemSNMPmib_ObjectIdentity = ObjectIdentity
semSNMPmib = _SemSNMPmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10)
)
_Variables_ObjectIdentity = ObjectIdentity
variables = _Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0)
)
_Severity_Type = OctetString
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 1),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_ObjectType_Type = OctetString
_ObjectType_Object = MibScalar
objectType = _ObjectType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 2),
    _ObjectType_Type()
)
objectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    objectType.setStatus("current")
_EventCode_Type = Integer32
_EventCode_Object = MibScalar
eventCode = _EventCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 3),
    _EventCode_Type()
)
eventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCode.setStatus("current")
_DeviceDisplayName_Type = OctetString
_DeviceDisplayName_Object = MibScalar
deviceDisplayName = _DeviceDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 4),
    _DeviceDisplayName_Type()
)
deviceDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDisplayName.setStatus("current")
_ServiceTag_Type = OctetString
_ServiceTag_Object = MibScalar
serviceTag = _ServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 5),
    _ServiceTag_Type()
)
serviceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceTag.setStatus("current")
_EventDescription_Type = OctetString
_EventDescription_Object = MibScalar
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 6),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_DeviceName_Type = OctetString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 7),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_PropertyName_Type = OctetString
_PropertyName_Object = MibScalar
propertyName = _PropertyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 8),
    _PropertyName_Type()
)
propertyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propertyName.setStatus("current")
_StatusPreviousValue_Type = OctetString
_StatusPreviousValue_Object = MibScalar
statusPreviousValue = _StatusPreviousValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 9),
    _StatusPreviousValue_Type()
)
statusPreviousValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPreviousValue.setStatus("current")
_StatusNewValue_Type = OctetString
_StatusNewValue_Object = MibScalar
statusNewValue = _StatusNewValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 10),
    _StatusNewValue_Type()
)
statusNewValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusNewValue.setStatus("current")
_EmmWWN_Type = OctetString
_EmmWWN_Object = MibScalar
emmWWN = _EmmWWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 11),
    _EmmWWN_Type()
)
emmWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emmWWN.setStatus("current")
_EmmMidplaneWWN_Type = OctetString
_EmmMidplaneWWN_Object = MibScalar
emmMidplaneWWN = _EmmMidplaneWWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 12),
    _EmmMidplaneWWN_Type()
)
emmMidplaneWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emmMidplaneWWN.setStatus("current")
_EmmSlotLocation_Type = Integer32
_EmmSlotLocation_Object = MibScalar
emmSlotLocation = _EmmSlotLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 13),
    _EmmSlotLocation_Type()
)
emmSlotLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emmSlotLocation.setStatus("current")
_DrivePortSASAddr_Type = OctetString
_DrivePortSASAddr_Object = MibScalar
drivePortSASAddr = _DrivePortSASAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 14),
    _DrivePortSASAddr_Type()
)
drivePortSASAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drivePortSASAddr.setStatus("current")
_DriveWWN_Type = OctetString
_DriveWWN_Object = MibScalar
driveWWN = _DriveWWN_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 15),
    _DriveWWN_Type()
)
driveWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveWWN.setStatus("current")
_EnclosureSlotNumber_Type = Integer32
_EnclosureSlotNumber_Object = MibScalar
enclosureSlotNumber = _EnclosureSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 16),
    _EnclosureSlotNumber_Type()
)
enclosureSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSlotNumber.setStatus("current")
_DriveNumber_Type = Integer32
_DriveNumber_Object = MibScalar
driveNumber = _DriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 17),
    _DriveNumber_Type()
)
driveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveNumber.setStatus("current")
_DrawerNumber_Type = Integer32
_DrawerNumber_Object = MibScalar
drawerNumber = _DrawerNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 18),
    _DrawerNumber_Type()
)
drawerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drawerNumber.setStatus("current")

# Managed Objects groups

variableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 0, 0)
)
variableGroup.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "eventDescription"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "propertyName"),
        ("DELL-PV-SEM-MIB", "statusPreviousValue"),
        ("DELL-PV-SEM-MIB", "statusNewValue"),
        ("DELL-PV-SEM-MIB", "emmWWN"),
        ("DELL-PV-SEM-MIB", "emmMidplaneWWN"),
        ("DELL-PV-SEM-MIB", "emmSlotLocation"),
        ("DELL-PV-SEM-MIB", "drivePortSASAddr"),
        ("DELL-PV-SEM-MIB", "driveWWN"),
        ("DELL-PV-SEM-MIB", "enclosureSlotNumber"),
        ("DELL-PV-SEM-MIB", "driveNumber"),
        ("DELL-PV-SEM-MIB", "drawerNumber"))
)
if mibBuilder.loadTexts:
    variableGroup.setStatus("current")


# Notification objects

generic = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 999)
)
generic.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"))
)
if mibBuilder.loadTexts:
    generic.setStatus(
        "current"
    )

statusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1000)
)
statusChange.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "propertyName"),
        ("DELL-PV-SEM-MIB", "statusPreviousValue"),
        ("DELL-PV-SEM-MIB", "statusNewValue"))
)
if mibBuilder.loadTexts:
    statusChange.setStatus(
        "current"
    )

propertyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1001)
)
propertyChange.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "propertyName"),
        ("DELL-PV-SEM-MIB", "statusPreviousValue"),
        ("DELL-PV-SEM-MIB", "statusNewValue"))
)
if mibBuilder.loadTexts:
    propertyChange.setStatus(
        "current"
    )

driveRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1004)
)
driveRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "drivePortSASAddr"),
        ("DELL-PV-SEM-MIB", "driveWWN"),
        ("DELL-PV-SEM-MIB", "enclosureSlotNumber"),
        ("DELL-PV-SEM-MIB", "drawerSlotNumber"),
        ("DELL-PV-SEM-MIB", "drawerNumber"))
)
if mibBuilder.loadTexts:
    driveRemoval.setStatus(
        "current"
    )

driveInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1005)
)
driveInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "drivePortSASAddr"),
        ("DELL-PV-SEM-MIB", "driveWWN"),
        ("DELL-PV-SEM-MIB", "enclosureSlotNumber"),
        ("DELL-PV-SEM-MIB", "drawerSlotNumber"),
        ("DELL-PV-SEM-MIB", "drawerNumber"))
)
if mibBuilder.loadTexts:
    driveInstall.setStatus(
        "current"
    )

drawerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1006)
)
drawerOpen.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    drawerOpen.setStatus(
        "current"
    )

drawerClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1007)
)
drawerClose.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    drawerClose.setStatus(
        "current"
    )

enclosureDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1010)
)
enclosureDiscovered.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    enclosureDiscovered.setStatus(
        "current"
    )

enclosureRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1011)
)
enclosureRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    enclosureRemoval.setStatus(
        "current"
    )

emmRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1012)
)
emmRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "emmWWN"),
        ("DELL-PV-SEM-MIB", "emmMidplaneWWN"),
        ("DELL-PV-SEM-MIB", "emmSlotLocation"))
)
if mibBuilder.loadTexts:
    emmRemoval.setStatus(
        "current"
    )

emmInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1013)
)
emmInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "emmWWN"),
        ("DELL-PV-SEM-MIB", "emmMidplaneWWN"),
        ("DELL-PV-SEM-MIB", "emmSlotLocation"))
)
if mibBuilder.loadTexts:
    emmInstall.setStatus(
        "current"
    )

powerSupplyRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1014)
)
powerSupplyRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    powerSupplyRemoval.setStatus(
        "current"
    )

powerSupplyInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1015)
)
powerSupplyInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    powerSupplyInstall.setStatus(
        "current"
    )

fanRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1016)
)
fanRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    fanRemoval.setStatus(
        "current"
    )

fanInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1017)
)
fanInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    fanInstall.setStatus(
        "current"
    )

voltageSensorRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1018)
)
voltageSensorRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    voltageSensorRemoval.setStatus(
        "current"
    )

voltageSensorInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1019)
)
voltageSensorInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    voltageSensorInstall.setStatus(
        "current"
    )

tempSensorRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1020)
)
tempSensorRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    tempSensorRemoval.setStatus(
        "current"
    )

tempSensorInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1021)
)
tempSensorInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    tempSensorInstall.setStatus(
        "current"
    )

currentSensorRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1022)
)
currentSensorRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    currentSensorRemoval.setStatus(
        "current"
    )

currentSensorInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1023)
)
currentSensorInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    currentSensorInstall.setStatus(
        "current"
    )

drawerRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1024)
)
drawerRemoval.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    drawerRemoval.setStatus(
        "current"
    )

drawerInstall = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1025)
)
drawerInstall.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"))
)
if mibBuilder.loadTexts:
    drawerInstall.setStatus(
        "current"
    )

drivePredictedFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1034)
)
drivePredictedFail.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "drivePortSASAddr"),
        ("DELL-PV-SEM-MIB", "driveWWN"),
        ("DELL-PV-SEM-MIB", "drawerSlotNumber"),
        ("DELL-PV-SEM-MIB", "drawerNumber"))
)
if mibBuilder.loadTexts:
    drivePredictedFail.setStatus(
        "current"
    )

driveFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1034)
)
driveFail.setObjects(
      *(("DELL-PV-SEM-MIB", "severity"),
        ("DELL-PV-SEM-MIB", "objectType"),
        ("DELL-PV-SEM-MIB", "eventCode"),
        ("DELL-PV-SEM-MIB", "deviceDisplayName"),
        ("DELL-PV-SEM-MIB", "serviceTag"),
        ("DELL-PV-SEM-MIB", "deviceName"),
        ("DELL-PV-SEM-MIB", "drivePortSASAddr"),
        ("DELL-PV-SEM-MIB", "driveWWN"),
        ("DELL-PV-SEM-MIB", "drawerSlotNumber"),
        ("DELL-PV-SEM-MIB", "drawerNumber"))
)
if mibBuilder.loadTexts:
    driveFail.setStatus(
        "current"
    )


# Notifications groups

eventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 674, 11000, 2000, 700, 10, 1)
)
eventGroup.setObjects(
      *(("DELL-PV-SEM-MIB", "generic"),
        ("DELL-PV-SEM-MIB", "statusChange"),
        ("DELL-PV-SEM-MIB", "propertyChange"),
        ("DELL-PV-SEM-MIB", "driveRemoval"),
        ("DELL-PV-SEM-MIB", "driveInstall"),
        ("DELL-PV-SEM-MIB", "drawerOpen"),
        ("DELL-PV-SEM-MIB", "drawerClose"),
        ("DELL-PV-SEM-MIB", "enclosureDiscovered"),
        ("DELL-PV-SEM-MIB", "enclosureRemoval"),
        ("DELL-PV-SEM-MIB", "emmRemoval"),
        ("DELL-PV-SEM-MIB", "emmInstall"),
        ("DELL-PV-SEM-MIB", "powerSupplyRemoval"),
        ("DELL-PV-SEM-MIB", "powerSupplyInstall"),
        ("DELL-PV-SEM-MIB", "fanRemoval"),
        ("DELL-PV-SEM-MIB", "fanInstall"),
        ("DELL-PV-SEM-MIB", "voltageSensorRemoval"),
        ("DELL-PV-SEM-MIB", "voltageSensorInstall"),
        ("DELL-PV-SEM-MIB", "tempSensorRemoval"),
        ("DELL-PV-SEM-MIB", "tempSensorInstall"),
        ("DELL-PV-SEM-MIB", "currentSensorRemoval"),
        ("DELL-PV-SEM-MIB", "currentSensorInstall"),
        ("DELL-PV-SEM-MIB", "drawerRemoval"),
        ("DELL-PV-SEM-MIB", "drawerInstall"),
        ("DELL-PV-SEM-MIB", "drivePredictedFail"))
)
if mibBuilder.loadTexts:
    eventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-PV-SEM-MIB",
    **{"dell": dell,
       "enterpriseSW": enterpriseSW,
       "storageMgmtBranch": storageMgmtBranch,
       "pvStorageMIB": pvStorageMIB,
       "semSNMPmib": semSNMPmib,
       "variables": variables,
       "variableGroup": variableGroup,
       "severity": severity,
       "objectType": objectType,
       "eventCode": eventCode,
       "deviceDisplayName": deviceDisplayName,
       "serviceTag": serviceTag,
       "eventDescription": eventDescription,
       "deviceName": deviceName,
       "propertyName": propertyName,
       "statusPreviousValue": statusPreviousValue,
       "statusNewValue": statusNewValue,
       "emmWWN": emmWWN,
       "emmMidplaneWWN": emmMidplaneWWN,
       "emmSlotLocation": emmSlotLocation,
       "drivePortSASAddr": drivePortSASAddr,
       "driveWWN": driveWWN,
       "enclosureSlotNumber": enclosureSlotNumber,
       "driveNumber": driveNumber,
       "drawerNumber": drawerNumber,
       "eventGroup": eventGroup,
       "generic": generic,
       "statusChange": statusChange,
       "propertyChange": propertyChange,
       "driveRemoval": driveRemoval,
       "driveInstall": driveInstall,
       "drawerOpen": drawerOpen,
       "drawerClose": drawerClose,
       "enclosureDiscovered": enclosureDiscovered,
       "enclosureRemoval": enclosureRemoval,
       "emmRemoval": emmRemoval,
       "emmInstall": emmInstall,
       "powerSupplyRemoval": powerSupplyRemoval,
       "powerSupplyInstall": powerSupplyInstall,
       "fanRemoval": fanRemoval,
       "fanInstall": fanInstall,
       "voltageSensorRemoval": voltageSensorRemoval,
       "voltageSensorInstall": voltageSensorInstall,
       "tempSensorRemoval": tempSensorRemoval,
       "tempSensorInstall": tempSensorInstall,
       "currentSensorRemoval": currentSensorRemoval,
       "currentSensorInstall": currentSensorInstall,
       "drawerRemoval": drawerRemoval,
       "drawerInstall": drawerInstall,
       "drivePredictedFail": drivePredictedFail,
       "driveFail": driveFail}
)
